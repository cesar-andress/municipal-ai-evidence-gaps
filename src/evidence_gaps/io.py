"""Filesystem helpers for corpus paths and scaffold files."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from evidence_gaps.schema import (
    coding_template_columns,
    corpus_manifest_columns,
)

PACKAGE_ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = PACKAGE_ROOT / "data" / "raw"
DATA_INTERIM = PACKAGE_ROOT / "data" / "interim"
DATA_PROCESSED = PACKAGE_ROOT / "data" / "processed"
OUTPUTS_TABLES = PACKAGE_ROOT / "outputs" / "tables"
OUTPUTS_REPORTS = PACKAGE_ROOT / "outputs" / "reports"

CORPUS_MANIFEST_TEMPLATE = DATA_PROCESSED / "corpus_manifest_template.csv"
CODING_TEMPLATE = DATA_PROCESSED / "coding_template.csv"
CORPUS_MANIFEST = DATA_PROCESSED / "corpus_manifest.csv"
CODING_DATASET = DATA_PROCESSED / "coding_dataset.csv"

# Legacy paths retained for scripts not yet migrated.
SOURCE_MANIFEST = DATA_RAW / "source_manifest.csv"
CORPUS_INDEX = DATA_INTERIM / "corpus_index.csv"
CODED_CORPUS = CODING_DATASET


def ensure_parent(path: Path) -> None:
    """Create parent directories for a file path if missing."""
    path.parent.mkdir(parents=True, exist_ok=True)


def write_empty_csv(path: Path, columns: tuple[str, ...]) -> Path:
    """Write a header-only CSV scaffold."""
    ensure_parent(path)
    pd.DataFrame(columns=list(columns)).to_csv(path, index=False)
    return path


def read_csv_if_exists(path: Path) -> pd.DataFrame:
    """Read a CSV or return an empty DataFrame."""
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path)


def scaffold_paths() -> dict[str, Path]:
    """Return canonical paths used by the analysis pipeline."""
    return {
        "corpus_manifest_template": CORPUS_MANIFEST_TEMPLATE,
        "coding_template": CODING_TEMPLATE,
        "corpus_manifest": CORPUS_MANIFEST,
        "coding_dataset": CODING_DATASET,
        "outputs_tables": OUTPUTS_TABLES,
        "outputs_reports": OUTPUTS_REPORTS,
    }


def init_scaffold_files() -> list[Path]:
    """Create header-only CSV scaffolds when missing (excludes versioned templates)."""
    created: list[Path] = []
    targets = [
        (CORPUS_MANIFEST, corpus_manifest_columns),
        (CODING_DATASET, coding_template_columns),
    ]
    for path, columns in targets:
        if not path.exists():
            write_empty_csv(path, columns)
            created.append(path)
    return created
