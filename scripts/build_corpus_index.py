#!/usr/bin/env python3
"""Build the interim corpus index from the raw source manifest."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from evidence_gaps.io import CORPUS_INDEX, SOURCE_MANIFEST, init_scaffold_files, read_csv_if_exists, write_empty_csv
from evidence_gaps.schema import corpus_index_columns


def build_index(manifest_path: Path, index_path: Path) -> int:
    """Derive a header-only or pass-through corpus index scaffold."""
    init_scaffold_files()
    manifest = read_csv_if_exists(manifest_path)
    index = read_csv_if_exists(index_path)

    if manifest.empty:
        if index.empty and not index_path.exists():
            write_empty_csv(index_path, corpus_index_columns)
            print(f"Created empty corpus index: {index_path}")
        else:
            print(f"No manifest rows to index. Corpus index unchanged: {index_path}")
        return 0

    # Future: map manifest rows to document units.
    print(f"Manifest has {len(manifest)} rows; indexing logic not yet implemented.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Build corpus index from source manifest.")
    parser.add_argument("--manifest", type=Path, default=SOURCE_MANIFEST)
    parser.add_argument("--index", type=Path, default=CORPUS_INDEX)
    args = parser.parse_args()
    return build_index(args.manifest, args.index)


if __name__ == "__main__":
    raise SystemExit(main())
