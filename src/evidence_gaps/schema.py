"""Schema definitions for corpus manifests and coded observations."""

from __future__ import annotations

from enum import Enum


class Observability(str, Enum):
    """Whether a governance category is observable in a public document."""

    PRESENT = "present"
    PARTIAL = "partial"
    ABSENT = "absent"
    NOT_APPLICABLE = "not_applicable"


class EvidenceCategory(str, Enum):
    """Governance evidence categories for documentary coding."""

    PRINCIPLES_COMMITMENTS = "principles_and_commitments"
    SYSTEM_INVENTORY = "system_inventory"
    IMPLEMENTATION_DETAIL = "implementation_detail"
    RISK_IMPACT = "risk_and_impact"
    MONITORING_REVIEW = "monitoring_and_review"
    ACCOUNTABILITY_LINKAGES = "accountability_linkages"
    PROCUREMENT_VENDOR = "procurement_and_vendor"
    UPDATE_VERSIONING = "update_and_versioning"


source_manifest_columns: tuple[str, ...] = (
    "source_id",
    "municipality",
    "country",
    "document_type",
    "url",
    "retrieved_at",
    "language",
    "notes",
)

corpus_index_columns: tuple[str, ...] = (
    "document_id",
    "source_id",
    "title",
    "publication_year",
    "file_format",
    "inclusion_status",
)

coded_corpus_columns: tuple[str, ...] = (
    "document_id",
    "category",
    "observability",
    "coder",
    "coded_at",
    "evidence_excerpt",
    "notes",
)


def validate_observability(value: str) -> Observability:
    """Return a validated observability enum member."""
    try:
        return Observability(value)
    except ValueError as exc:
        valid = ", ".join(item.value for item in Observability)
        raise ValueError(f"Invalid observability '{value}'. Expected one of: {valid}") from exc


def validate_category(value: str) -> EvidenceCategory:
    """Return a validated evidence category enum member."""
    try:
        return EvidenceCategory(value)
    except ValueError as exc:
        valid = ", ".join(item.value for item in EvidenceCategory)
        raise ValueError(f"Invalid category '{value}'. Expected one of: {valid}") from exc
