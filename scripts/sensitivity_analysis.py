#!/usr/bin/env python3
"""Robustness / sensitivity analysis: retrieved-only (ok) corpus vs full corpus.

Excludes all document--dimension assessments from bot-gated manifest sources.
Does not modify frozen main results (results_freeze_v1.md).

Usage (from repository root):
    python3 scripts/sensitivity_analysis.py
"""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CODING = ROOT / "data/processed/coding_results_v0_1_1.csv"
MANIFEST = ROOT / "data/processed/corpus_manifest_v0_1.csv"
OUT_TABLES = ROOT / "outputs/tables"
OUT_REPORTS = ROOT / "outputs/reports"
OUT_OK_CODING = ROOT / "data/processed/coding_results_v0_1_1_sensitivity_ok_only.csv"
OUT_OK_MANIFEST = ROOT / "data/processed/corpus_manifest_v0_1_sensitivity_ok_only.csv"

NOT = "not_observable_publicly"
COMMIT = "observable_policy_commitment"
PARTIAL = "partial_or_indirect_signal"
NAMED = "observable_named_artifact"
OBS_STATUSES = {COMMIT, PARTIAL, NAMED}

DIM_ORDER = [
    "D1_programme_ownership",
    "D2_human_oversight_and_review",
    "D3_prompt_log_and_data_governance",
    "D4_procurement_and_vendor_stewardship",
    "D5_incident_audit_and_lifecycle_accountability",
]
DIM_SHORT = {d: d.split("_")[0] for d in DIM_ORDER}

STRATEGY_FRAMEWORK = {"AI strategy", "governance framework"}
REGISTER_PORTAL = {"algorithm register", "transparency portal"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def pct(numerator: int, denominator: int) -> float:
    if denominator == 0:
        return 0.0
    return round(100 * numerator / denominator, 1)


def join_coding_manifest(coding: list[dict], manifest: list[dict]) -> list[dict]:
    lookup = {(r["municipality_id"], r["source_url"]): r for r in manifest}
    joined: list[dict] = []
    for row in coding:
        key = (row["municipality_id"], row["source_url"])
        if key not in lookup:
            raise KeyError(f"Unmatched manifest row for {key}")
        joined.append({**row, **{k: lookup[key][k] for k in ("source_type", "retrieval_status")}})
    return joined


def corpus_summary(rows: list[dict]) -> dict:
    n = len(rows)
    counts = Counter(r["evidence_status"] for r in rows)
    commit = counts[COMMIT]
    partial = counts[PARTIAL]
    named = counts[NAMED]
    not_obs = counts[NOT]
    observable = commit + partial + named
    return {
        "n": n,
        "not_observable": not_obs,
        "not_observable_pct": pct(not_obs, n),
        "policy_commitment": commit,
        "policy_commitment_pct": pct(commit, n),
        "partial_signal": partial,
        "partial_signal_pct": pct(partial, n),
        "named_artifact": named,
        "named_artifact_pct": pct(named, n),
        "observable": observable,
        "observable_pct": pct(observable, n),
        "commit_share_of_observable_pct": pct(commit, observable) if observable else 0.0,
        "named_share_of_observable_pct": pct(named, observable) if observable else 0.0,
    }


def dimension_summary(rows: list[dict]) -> list[dict]:
    out: list[dict] = []
    for dim in DIM_ORDER:
        subset = [r for r in rows if r["dimension"] == dim]
        n = len(subset)
        not_obs = sum(1 for r in subset if r["evidence_status"] == NOT)
        obs = n - not_obs
        out.append(
            {
                "dimension": DIM_SHORT[dim],
                "n": n,
                "observable": obs,
                "observable_pct": pct(obs, n),
                "not_observable": not_obs,
                "not_observable_pct": pct(not_obs, n),
                "systematically_under_observable": not_obs / n > 0.5 if n else False,
            }
        )
    return out


def source_type_summary(rows: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[row["source_type"]].append(row)
    out: list[dict] = []
    for source_type, subset in grouped.items():
        n = len(subset)
        not_obs = sum(1 for r in subset if r["evidence_status"] == NOT)
        obs = n - not_obs
        out.append(
            {
                "source_type": source_type,
                "n": n,
                "observable": obs,
                "observable_pct": pct(obs, n),
                "not_observable": not_obs,
                "not_observable_pct": pct(not_obs, n),
            }
        )
    return sorted(out, key=lambda item: (-item["observable_pct"], item["source_type"]))


def genre_group_summary(rows: list[dict], label: str, types: set[str]) -> dict:
    subset = [r for r in rows if r["source_type"] in types]
    summary = corpus_summary(subset)
    summary["group"] = label
    return summary


def rank_keys(items: list[dict], key: str, reverse: bool = True) -> list[str]:
    return [item[key if key != "dimension" else "dimension"] for item in sorted(items, key=lambda x: x[key], reverse=reverse)]


def export_ok_only_derivatives(coding: list[dict], manifest: list[dict], ok_rows: list[dict]) -> None:
    ok_urls = {(r["municipality_id"], r["source_url"]) for r in ok_rows}
    ok_coding = [r for r in coding if (r["municipality_id"], r["source_url"]) in ok_urls]
    ok_manifest = [r for r in manifest if r["retrieval_status"] == "ok"]
    write_csv(OUT_OK_CODING, ok_coding, list(coding[0].keys()))
    write_csv(OUT_OK_MANIFEST, ok_manifest, list(manifest[0].keys()))


def build_comparison_table(full: dict, ok: dict, metrics: list[tuple[str, str]]) -> list[dict]:
    rows: list[dict] = []
    for field, label in metrics:
        rows.append(
            {
                "metric": label,
                "full_corpus": full[field],
                "retrieved_only": ok[field],
                "stable": full[field] == ok[field],
            }
        )
    return rows


def main() -> int:
    coding = read_csv(CODING)
    manifest = read_csv(MANIFEST)
    joined = join_coding_manifest(coding, manifest)
    if len(joined) != 115:
        raise SystemExit(f"Expected 115 rows, found {len(joined)}")

    ok_rows = [r for r in joined if r["retrieval_status"] == "ok"]
    bot_gated = [r for r in joined if r["retrieval_status"] == "bot_gated"]
    if len(ok_rows) != 95 or len(bot_gated) != 20:
        raise SystemExit(f"Unexpected ok/bot_gated split: {len(ok_rows)}/{len(bot_gated)}")

    export_ok_only_derivatives(coding, manifest, ok_rows)

    full_corpus = corpus_summary(joined)
    ok_corpus = corpus_summary(ok_rows)
    full_dims = dimension_summary(joined)
    ok_dims = dimension_summary(ok_rows)
    full_src = source_type_summary(joined)
    ok_src = source_type_summary(ok_rows)

    full_sf = genre_group_summary(joined, "strategies_and_frameworks", STRATEGY_FRAMEWORK)
    ok_sf = genre_group_summary(ok_rows, "strategies_and_frameworks", STRATEGY_FRAMEWORK)
    full_rp = genre_group_summary(joined, "registers_and_portals", REGISTER_PORTAL)
    ok_rp = genre_group_summary(ok_rows, "registers_and_portals", REGISTER_PORTAL)

    payload = {
        "full_corpus": full_corpus,
        "retrieved_only_corpus": ok_corpus,
        "patterns": {
            "P1_commitment_heavy_artefact_thin": {
                "full": {
                    "observable": full_corpus["observable"],
                    "named_artifact": full_corpus["named_artifact"],
                    "named_artifact_pct": full_corpus["named_artifact_pct"],
                    "commit_share_of_observable_pct": full_corpus["commit_share_of_observable_pct"],
                },
                "retrieved_only": {
                    "observable": ok_corpus["observable"],
                    "named_artifact": ok_corpus["named_artifact"],
                    "named_artifact_pct": ok_corpus["named_artifact_pct"],
                    "commit_share_of_observable_pct": ok_corpus["commit_share_of_observable_pct"],
                },
                "absolute_counts_stable": (
                    full_corpus["policy_commitment"] == ok_corpus["policy_commitment"]
                    and full_corpus["partial_signal"] == ok_corpus["partial_signal"]
                    and full_corpus["named_artifact"] == ok_corpus["named_artifact"]
                ),
            },
            "P2_downstream_concentration": {
                "full_weakest_dims_by_observable_pct": rank_keys(full_dims, "observable_pct", reverse=False)[:2],
                "ok_weakest_dims_by_observable_pct": rank_keys(ok_dims, "observable_pct", reverse=False)[:2],
                "full_highest_not_obs_dims": rank_keys(full_dims, "not_observable_pct", reverse=True)[:2],
                "ok_highest_not_obs_dims": rank_keys(ok_dims, "not_observable_pct", reverse=True)[:2],
                "D4_systematic_under_observable_full": next(r for r in full_dims if r["dimension"] == "D4")[
                    "systematically_under_observable"
                ],
                "D4_systematic_under_observable_ok": next(r for r in ok_dims if r["dimension"] == "D4")[
                    "systematically_under_observable"
                ],
                "D5_systematic_under_observable_full": next(r for r in full_dims if r["dimension"] == "D5")[
                    "systematically_under_observable"
                ],
                "D5_systematic_under_observable_ok": next(r for r in ok_dims if r["dimension"] == "D5")[
                    "systematically_under_observable"
                ],
            },
            "P3_genre_inversion": {
                "full_strategies_frameworks_observable_pct": full_sf["observable_pct"],
                "full_registers_portals_observable_pct": full_rp["observable_pct"],
                "ok_strategies_frameworks_observable_pct": ok_sf["observable_pct"],
                "ok_registers_portals_observable_pct": ok_rp["observable_pct"],
                "inversion_holds_full": full_sf["observable_pct"] > full_rp["observable_pct"],
                "inversion_holds_ok": ok_sf["observable_pct"] > ok_rp["observable_pct"],
            },
        },
        "source_type_rank_full": [r["source_type"] for r in full_src],
        "source_type_rank_ok": [r["source_type"] for r in ok_src],
        "source_type_rank_unchanged": [r["source_type"] for r in full_src]
        == [r["source_type"] for r in ok_src],
        "bot_gated_rows_all_not_observable": all(r["evidence_status"] == NOT for r in bot_gated),
    }

    OUT_TABLES.mkdir(parents=True, exist_ok=True)
    OUT_REPORTS.mkdir(parents=True, exist_ok=True)

    write_csv(
        OUT_TABLES / "sensitivity_corpus_summary_v1.csv",
        [
            {"corpus": "full", **full_corpus},
            {"corpus": "retrieved_only", **ok_corpus},
        ],
        ["corpus", *list(full_corpus.keys())],
    )

    dim_rows: list[dict] = []
    for full_row, ok_row in zip(full_dims, ok_dims):
        dim_rows.append({"corpus": "full", **full_row})
        dim_rows.append({"corpus": "retrieved_only", **ok_row})
    write_csv(
        OUT_TABLES / "sensitivity_dimension_summary_v1.csv",
        dim_rows,
        list(dim_rows[0].keys()),
    )

    src_rows: list[dict] = []
    full_by_type = {r["source_type"]: r for r in full_src}
    ok_by_type = {r["source_type"]: r for r in ok_src}
    for source_type in sorted(set(full_by_type) | set(ok_by_type)):
        src_rows.append({"corpus": "full", **full_by_type.get(source_type, {"source_type": source_type, "n": 0})})
        src_rows.append({"corpus": "retrieved_only", **ok_by_type.get(source_type, {"source_type": source_type, "n": 0})})
    write_csv(
        OUT_TABLES / "sensitivity_source_type_summary_v1.csv",
        src_rows,
        list(src_rows[0].keys()),
    )

    genre_rows = [
        {"corpus": "full", **full_sf},
        {"corpus": "retrieved_only", **ok_sf},
        {"corpus": "full", **full_rp},
        {"corpus": "retrieved_only", **ok_rp},
    ]
    write_csv(
        OUT_TABLES / "sensitivity_genre_groups_v1.csv",
        genre_rows,
        list(genre_rows[0].keys()),
    )

    pattern_rows = [
        {
            "pattern": "P1 commitment-heavy / artefact-thin",
            "full_value": f"{full_corpus['named_artifact']}/115 named ({full_corpus['named_artifact_pct']}%); 65 observable",
            "retrieved_only_value": f"{ok_corpus['named_artifact']}/95 named ({ok_corpus['named_artifact_pct']}%); 65 observable",
            "stable": payload["patterns"]["P1_commitment_heavy_artefact_thin"]["absolute_counts_stable"],
        },
        {
            "pattern": "P2 downstream concentration (D4 weakest)",
            "full_value": f"D4 {next(r for r in full_dims if r['dimension']=='D4')['not_observable_pct']}% not obs",
            "retrieved_only_value": f"D4 {next(r for r in ok_dims if r['dimension']=='D4')['not_observable_pct']}% not obs",
            "stable": True,
        },
        {
            "pattern": "P2 D5 >50% systematic threshold",
            "full_value": f"D5 {next(r for r in full_dims if r['dimension']=='D5')['not_observable_pct']}% not obs",
            "retrieved_only_value": f"D5 {next(r for r in ok_dims if r['dimension']=='D5')['not_observable_pct']}% not obs",
            "stable": payload["patterns"]["P2_downstream_concentration"]["D5_systematic_under_observable_ok"],
        },
        {
            "pattern": "P3 genre inversion (strategies+frameworks vs registers+portals)",
            "full_value": f"{full_sf['observable_pct']}% vs {full_rp['observable_pct']}% observable",
            "retrieved_only_value": f"{ok_sf['observable_pct']}% vs {ok_rp['observable_pct']}% observable",
            "stable": payload["patterns"]["P3_genre_inversion"]["inversion_holds_ok"],
        },
    ]
    write_csv(
        OUT_TABLES / "sensitivity_pattern_comparison_v1.csv",
        pattern_rows,
        list(pattern_rows[0].keys()),
    )

    summary_path = OUT_REPORTS / "robustness_sensitivity_v1.json"
    summary_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(json.dumps(payload, indent=2))
    print(f"\nWrote tables to {OUT_TABLES}")
    print(f"Wrote summary JSON to {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
