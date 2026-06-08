#!/usr/bin/env python3
"""Apply the observability coding protocol to corpus documents."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from evidence_gaps.io import CODED_CORPUS, CORPUS_INDEX, init_scaffold_files, read_csv_if_exists


def run_coding(index_path: Path, output_path: Path) -> int:
    """Initialise coded corpus scaffold; coding workflow not yet populated."""
    init_scaffold_files()
    index = read_csv_if_exists(index_path)
    coded = read_csv_if_exists(output_path)

    if index.empty:
        print(f"No corpus documents to code. Coded corpus unchanged: {output_path}")
        return 0

    print(f"Corpus index has {len(index)} rows; automated coding not yet implemented.")
    print(f"Current coded rows: {len(coded)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Code observability categories for corpus documents.")
    parser.add_argument("--index", type=Path, default=CORPUS_INDEX)
    parser.add_argument("--output", type=Path, default=CODED_CORPUS)
    args = parser.parse_args()
    return run_coding(args.index, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
