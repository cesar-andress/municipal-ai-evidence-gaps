"""Coding helpers for observability annotation (v0.1)."""

from __future__ import annotations

from evidence_gaps.schema import (
    NON_CLAIM_BOUNDARY_V01,
    CodingDecision,
    EvidenceObservation,
    EvidenceStatus,
    ObservabilityDimension,
    validate_dimension,
    validate_evidence_status,
)

__all__ = [
    "CodingDecision",
    "EvidenceObservation",
    "EvidenceStatus",
    "NON_CLAIM_BOUNDARY_V01",
    "ObservabilityDimension",
    "parse_coding_row",
    "validate_dimension",
    "validate_evidence_status",
]


def parse_coding_row(row: dict[str, str]) -> CodingDecision:
    """Parse a CSV row into a CodingDecision."""
    return CodingDecision.from_row(row)
