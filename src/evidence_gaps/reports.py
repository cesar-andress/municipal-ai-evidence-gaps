"""Report generation for observability summaries (v0.1)."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from evidence_gaps.io import OUTPUTS_REPORTS, ensure_parent


def observability_summary(coding_dataset: pd.DataFrame) -> pd.DataFrame:
    """Summarise evidence-status counts by dimension.

    Returns an empty frame with expected columns when input is empty.
    """
    columns = ["dimension", "evidence_status", "count"]
    if coding_dataset.empty:
        return pd.DataFrame(columns=columns)

    summary = (
        coding_dataset.groupby(["dimension", "evidence_status"], dropna=False)
        .size()
        .reset_index(name="count")
        .sort_values(["dimension", "evidence_status"])
    )
    return summary


def write_summary_report(coding_dataset: pd.DataFrame, path: Path | None = None) -> Path:
    """Write a dimension-level observability summary to CSV."""
    output = path or (OUTPUTS_REPORTS / "observability_summary.csv")
    ensure_parent(output)
    observability_summary(coding_dataset).to_csv(output, index=False)
    return output
