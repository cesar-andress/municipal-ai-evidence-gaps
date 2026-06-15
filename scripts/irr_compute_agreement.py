#!/usr/bin/env python3
"""Compute inter-rater agreement for IRR subsample v1."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_URLS = ROOT / "docs" / "irr_subsample_urls_v1.txt"
CODER1 = ROOT / "data/processed/coding_results_v0_1_1.csv"
MANIFEST = ROOT / "data/processed/corpus_manifest_v0_1.csv"
DEFAULT_WORKSHEET = ROOT / "data/processed/irr_coding_worksheet_v1.csv"

DIM_ORDER = [
    "D1_programme_ownership",
    "D2_human_oversight_and_review",
    "D3_prompt_log_and_data_governance",
    "D4_procurement_and_vendor_stewardship",
    "D5_incident_audit_and_lifecycle_accountability",
]
STRATEGY_FRAMEWORK = {"AI strategy", "governance framework"}
REGISTER_PORTAL = {"algorithm register", "transparency portal"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_urls(path: Path) -> set[str]:
    return {line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}


def cohens_kappa(labels1: list[str], labels2: list[str]) -> float:
    """Nominal Cohen's kappa without external dependencies."""
    n = len(labels1)
    if n == 0:
        return float("nan")
    categories = sorted(set(labels1) | set(labels2))
    agree = sum(a == b for a, b in zip(labels1, labels2))
    po = agree / n
    c1 = Counter(labels1)
    c2 = Counter(labels2)
    pe = sum((c1[c] / n) * (c2[c] / n) for c in categories)
    if pe == 1:
        return 1.0
    return (po - pe) / (1 - pe)


def pattern_checks(rows: list[dict], manifest: dict[tuple[str, str], dict]) -> dict:
    c1 = [r["evidence_status_coder1"] for r in rows]
    obs = [s for s in c1 if s != "not_observable_publicly"]
    named = sum(1 for s in obs if s == "observable_named_artifact")
    sf, rp = [], []
    dim_not: dict[str, list[int]] = {d: [] for d in DIM_ORDER}
    for r in rows:
        st = manifest[(r["municipality_id"], r["source_url"])]["source_type"]
        label = r["evidence_status_coder1"]
        is_obs = 0 if label == "not_observable_publicly" else 1
        if st in STRATEGY_FRAMEWORK:
            sf.append(is_obs)
        if st in REGISTER_PORTAL:
            rp.append(is_obs)
        dim_not[r["dimension"]].append(0 if label == "not_observable_publicly" else 1)

    def pct_obs(values: list[int]) -> float:
        return round(100 * sum(values) / len(values), 1) if values else 0.0

    dim_rank = sorted(
        ((d.split("_")[0], round(100 * (1 - sum(v) / len(v)), 1)) for d, v in dim_not.items() if v),
        key=lambda x: -x[1],
    )
    return {
        "p1_named_share_of_observable_pct": round(100 * named / len(obs), 1) if obs else 0.0,
        "p1_commitment_heavy_artefact_thin": named <= max(1, len(obs) // 10),
        "p2_top_not_obs_dims": [d for d, _ in dim_rank[:2]],
        "p3_sf_observable_pct": pct_obs(sf),
        "p3_rp_observable_pct": pct_obs(rp),
        "p3_inversion_holds": pct_obs(sf) > pct_obs(rp),
    }


def load_from_worksheet(worksheet: Path) -> tuple[list[dict], int]:
    rows = read_csv(worksheet)
    if not rows:
        raise SystemExit(f"Empty worksheet: {worksheet}")
    merged: list[dict[str, str]] = []
    for r in rows:
        c2 = r.get("evidence_status_coder2", "").strip()
        if not c2:
            raise SystemExit(f"Coder 2 labels incomplete in {worksheet} (missing at {r.get('irr_id', '?')})")
        merged.append(
            {
                "municipality_id": r["municipality_id"],
                "source_url": r["source_url"],
                "dimension": r["dimension"],
                "evidence_status_coder1": r["evidence_status_coder1"],
                "evidence_status_coder2": c2,
            }
        )
    n_docs = len({r["source_url"] for r in rows})
    return merged, n_docs


def load_from_coder2_file(coder1_path: Path, coder2_path: Path, urls: set[str]) -> tuple[list[dict], int]:
    c1_rows = [r for r in read_csv(coder1_path) if r["source_url"] in urls]
    c2_rows = read_csv(coder2_path)
    c2_lookup = {(r["municipality_id"], r["source_url"], r["dimension"]): r for r in c2_rows}
    merged: list[dict[str, str]] = []
    for r in c1_rows:
        key = (r["municipality_id"], r["source_url"], r["dimension"])
        c2 = c2_lookup.get(key, {})
        label2 = c2.get("evidence_status", c2.get("evidence_status_coder2", "")).strip()
        if not label2:
            raise SystemExit(f"Missing Coder 2 label for {key}")
        merged.append(
            {
                "municipality_id": r["municipality_id"],
                "source_url": r["source_url"],
                "dimension": r["dimension"],
                "evidence_status_coder1": r["evidence_status"],
                "evidence_status_coder2": label2,
            }
        )
    n_docs = len({r["source_url"] for r in merged})
    return merged, n_docs


def write_report(
    report_path: Path,
    *,
    n_cells: int,
    n_docs: int,
    pa: float,
    kappa: float,
    checks: dict,
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# IRR results v1",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Double-coded documents | {n_docs} |",
        f"| Double-coded document--dimension cells | {n_cells} |",
        f"| Percent agreement | {pa}% |",
        f"| Cohen's κ (nominal) | {kappa} |",
        "",
        "## Pattern checks (Coder 1 labels, subsample)",
        "",
        f"- **P1** commitment-heavy / artefact-thin: named share of observable = {checks['p1_named_share_of_observable_pct']}%",
        f"- **P2** downstream concentration: highest not-observable dimensions = {', '.join(checks['p2_top_not_obs_dims'])}",
        f"- **P3** genre inversion: strategies+frameworks {checks['p3_sf_observable_pct']}% vs registers+portals {checks['p3_rp_observable_pct']}% observable",
        "",
        f"P3 inversion holds: **{checks['p3_inversion_holds']}**",
        "",
    ]
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="IRR agreement for subsample v1")
    parser.add_argument("--worksheet", type=Path, default=None, help="IRR worksheet with coder1 and coder2 columns")
    parser.add_argument("--coder1", type=Path, default=CODER1)
    parser.add_argument("--coder2", type=Path, default=None)
    parser.add_argument("--urls", type=Path, default=DEFAULT_URLS)
    parser.add_argument("--out", type=Path, default=ROOT / "data/processed/irr_merged_v1.csv")
    parser.add_argument("--report", type=Path, default=ROOT / "outputs/reports/irr_results_v1.md")
    parser.add_argument("--pattern-check", action="store_true", default=True)
    args = parser.parse_args()

    if args.worksheet:
        merged, n_docs = load_from_worksheet(args.worksheet)
    elif args.coder2:
        urls = load_urls(args.urls)
        merged, n_docs = load_from_coder2_file(args.coder1, args.coder2, urls)
    else:
        merged, n_docs = load_from_worksheet(DEFAULT_WORKSHEET)

    if len(merged) != 40:
        raise SystemExit(f"Expected 40 merged rows, found {len(merged)}")

    manifest = {(r["municipality_id"], r["source_url"]): r for r in read_csv(MANIFEST)}
    labels1 = [r["evidence_status_coder1"] for r in merged]
    labels2 = [r["evidence_status_coder2"] for r in merged]

    pa = round(100 * sum(a == b for a, b in zip(labels1, labels2)) / len(labels1), 1)
    kappa = round(cohens_kappa(labels1, labels2), 2)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(merged[0].keys()))
        writer.writeheader()
        writer.writerows(merged)

    checks = pattern_checks(merged, manifest)
    write_report(args.report, n_cells=len(merged), n_docs=n_docs, pa=pa, kappa=kappa, checks=checks)

    summary = {
        "n_documents": n_docs,
        "n_cells": len(merged),
        "percent_agreement": pa,
        "cohens_kappa": kappa,
        "pattern_checks": checks,
    }
    json_path = args.report.with_suffix(".json")
    json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"n_documents={n_docs}")
    print(f"n_cells={len(merged)}")
    print(f"percent_agreement={pa}%")
    print(f"cohens_kappa={kappa}")
    print(f"pattern_checks={checks}")
    print(f"Wrote {args.out}")
    print(f"Wrote {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
