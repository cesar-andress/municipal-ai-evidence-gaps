"""Filesystem helpers for corpus paths and empty scaffold files."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from evidence_gaps.schema import coded_corpus_columns, corpus_index_columns, source_manifest_columns

PACKAGE_ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = PACKAGE_ROOT / "data" / "raw"
DATA_INTERIM = PACKAGE_ROOT / "data" / "interim"
DATA_PROCESSED = PACKAGE_ROOT / "data" / "processed"
OUTPUTS_TABLES = PACKAGE_ROOT / "outputs" / "tables"
OUTPUTS_REPORTS = PACKAGE_ROOT / "outputs" / "reports"

SOURCE_MANIFEST = DATA_RAW / "source_manifest.csv"
CORPUS_INDEX = DATA_INTERIM / "corpus_index.csv"
CODED_CORPUS = DATA_PROCESSED / "coded_corpus.csv"


def ensure_parent(path: Path) -> None:
    """Create parent directories for a file path if missing."""
    path.parent.mkdir(parents=True, exist_ok=True)


def write_empty_csv(path: Path, columns: tuple[str, ...]) -> Path:
    """Write a header-only CSV scaffold."""
    ensure_parent(path)
    pd.DataFrame(columns=list(columns)).to_csv(path, index=False)
    return path


def read_csv_if_exists(path: Path) -> pd.DataFrame:
    """Read a CSV or return an empty DataFrame with expected columns."""
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path)


def scaffold_paths() -> dict[str, Path]:
    """Return canonical paths used by the analysis pipeline."""
    return {
        "source_manifest": SOURCE_MANIFEST,
        "corpus_index": CORPUS_INDEX,
        "coded_corpus": CODED_CORPUS,
        "outputs_tables": OUTPUTS_TABLES,
        "outputs_reports": OUTPUTS_REPORTS,
    }


def init_scaffold_files() -> list[Path]:
    """Create header-only CSV scaffolds when missing."""
    created: list[Path] = []
    targets = [
        (SOURCE_MANIFEST, source_manifest_columns),
        (CORPUS_INDEX, corpus_index_columns),
        (CODED_CORPUS, coded_corpus_columns),
    ]
    for path, columns in targets:
        if not path.exists():
            write_empty_csv(path, columns)
            created.append(path)
    return created
