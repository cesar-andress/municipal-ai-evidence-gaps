#!/usr/bin/env python3
"""Export manuscript-ready tables and summary reports."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from evidence_gaps.io import CODED_CORPUS, OUTPUTS_TABLES, read_csv_if_exists
from evidence_gaps.reports import observability_summary, write_summary_report


def export(coded_path: Path, tables_dir: Path) -> int:
    """Write summary outputs when coded data exists."""
    coded = read_csv_if_exists(coded_path)
    tables_dir.mkdir(parents=True, exist_ok=True)

    summary = observability_summary(coded)
    summary_path = tables_dir / "observability_summary.csv"
    summary.to_csv(summary_path, index=False)

    report_path = write_summary_report(coded)

    if coded.empty:
        print("No coded observations yet. Wrote empty summary scaffolds:")
    else:
        print(f"Exported summaries from {len(coded)} coded rows.")

    print(f"  {summary_path}")
    print(f"  {report_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Export analysis tables and reports.")
    parser.add_argument("--coded", type=Path, default=CODED_CORPUS)
    parser.add_argument("--tables-dir", type=Path, default=OUTPUTS_TABLES)
    args = parser.parse_args()
    return export(args.coded, args.tables_dir)


if __name__ == "__main__":
    raise SystemExit(main())
