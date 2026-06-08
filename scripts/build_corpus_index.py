#!/usr/bin/env python3
"""Normalise corpus manifest entries from raw collection logs (v0.1)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from evidence_gaps.io import CORPUS_MANIFEST, init_scaffold_files, read_csv_if_exists


def build_index(manifest_path: Path) -> int:
    """Ensure corpus manifest scaffold exists; normalisation not yet implemented."""
    init_scaffold_files()
    manifest = read_csv_if_exists(manifest_path)

    if manifest.empty:
        print(f"No manifest rows yet. Scaffold ready: {manifest_path}")
        return 0

    print(f"Manifest has {len(manifest)} rows; normalisation logic not yet implemented.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Build corpus manifest from collected sources.")
    parser.add_argument("--manifest", type=Path, default=CORPUS_MANIFEST)
    args = parser.parse_args()
    return build_index(args.manifest)


if __name__ == "__main__":
    raise SystemExit(main())
