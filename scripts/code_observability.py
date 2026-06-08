#!/usr/bin/env python3
"""Apply the observability coding protocol to corpus documents."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from evidence_gaps.io import CODING_DATASET, CORPUS_MANIFEST, init_scaffold_files, read_csv_if_exists


def run_coding(manifest_path: Path, output_path: Path) -> int:
    """Initialise coding dataset scaffold; coding workflow not yet populated."""
    init_scaffold_files()
    manifest = read_csv_if_exists(manifest_path)
    coded = read_csv_if_exists(output_path)

    if manifest.empty:
        print(f"No corpus documents to code. Coding dataset unchanged: {output_path}")
        return 0

    print(f"Corpus manifest has {len(manifest)} rows; automated coding not yet implemented.")
    print(f"Current coded rows: {len(coded)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Code D1–D5 observability dimensions for corpus documents.")
    parser.add_argument("--manifest", type=Path, default=CORPUS_MANIFEST)
    parser.add_argument("--output", type=Path, default=CODING_DATASET)
    args = parser.parse_args()
    return run_coding(args.manifest, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
