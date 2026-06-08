"""Report generation stubs for observability summaries."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from evidence_gaps.io import OUTPUTS_REPORTS, ensure_parent


def observability_summary(coded_corpus: pd.DataFrame) -> pd.DataFrame:
    """Summarise observability counts by category.

    Returns an empty frame with expected columns when input is empty.
    """
    columns = ["category", "observability", "count"]
    if coded_corpus.empty:
        return pd.DataFrame(columns=columns)

    summary = (
        coded_corpus.groupby(["category", "observability"], dropna=False)
        .size()
        .reset_index(name="count")
        .sort_values(["category", "observability"])
    )
    return summary


def write_summary_report(coded_corpus: pd.DataFrame, path: Path | None = None) -> Path:
    """Write a category-level observability summary to CSV."""
    output = path or (OUTPUTS_REPORTS / "observability_summary.csv")
    ensure_parent(output)
    observability_summary(coded_corpus).to_csv(output, index=False)
    return output
