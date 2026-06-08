#!/usr/bin/env python3
"""Create or update the raw source manifest scaffold.

No web scraping is performed in the initial scaffold.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from evidence_gaps.io import SOURCE_MANIFEST, init_scaffold_files, read_csv_if_exists


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialise the municipal source manifest scaffold.")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=SOURCE_MANIFEST,
        help="Path to source_manifest.csv",
    )
    args = parser.parse_args()

    created = init_scaffold_files()
    manifest = read_csv_if_exists(args.manifest)

    if args.manifest in created:
        print(f"Created empty manifest: {args.manifest}")
    else:
        print(f"Manifest already exists ({len(manifest)} rows): {args.manifest}")

    print("No sources collected yet. Add entries manually or extend this script later.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
