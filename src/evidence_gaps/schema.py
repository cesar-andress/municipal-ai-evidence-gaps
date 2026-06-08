"""Schema definitions for the v0.1 observability study protocol."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date
from enum import Enum
from typing import Any


NON_CLAIM_BOUNDARY_V01 = "observability_only_v0_1"


class EvidenceStatus(str, Enum):
    """Evidence status labels for observability coding (v0.1)."""

    OBSERVABLE_NAMED_ARTIFACT = "observable_named_artifact"
    OBSERVABLE_POLICY_COMMITMENT = "observable_policy_commitment"
    PARTIAL_OR_INDIRECT_SIGNAL = "partial_or_indirect_signal"
    NOT_OBSERVABLE_PUBLICLY = "not_observable_publicly"


class ObservabilityDimension(str, Enum):
    """Five observability dimensions (v0.1)."""

    D1_PROGRAMME_OWNERSHIP = "D1_programme_ownership"
    D2_HUMAN_OVERSIGHT_REVIEW = "D2_human_oversight_and_review"
    D3_PROMPT_LOG_DATA_GOVERNANCE = "D3_prompt_log_and_data_governance"
    D4_PROCUREMENT_VENDOR_STEWARDSHIP = "D4_procurement_and_vendor_stewardship"
    D5_INCIDENT_AUDIT_LIFECYCLE = "D5_incident_audit_and_lifecycle_accountability"


SUPPORTED_DIMENSIONS: frozenset[str] = frozenset(d.value for d in ObservabilityDimension)
SUPPORTED_EVIDENCE_STATUSES: frozenset[str] = frozenset(s.value for s in EvidenceStatus)

corpus_manifest_columns: tuple[str, ...] = (
    "municipality_id",
    "municipality_name",
    "country",
    "source_url",
    "source_title",
    "source_type",
    "access_date",
    "language",
    "inclusion_reason",
    "notes",
)

coding_template_columns: tuple[str, ...] = (
    "municipality_id",
    "source_id",
    "dimension",
    "evidence_status",
    "quoted_evidence",
    "page_or_section",
    "coder_notes",
    "non_claim_boundary",
)

# Legacy aliases used by pipeline scaffolds until scripts are migrated.
source_manifest_columns = corpus_manifest_columns
coded_corpus_columns = coding_template_columns


def _require_text(name: str, value: str | None) -> str:
    if value is None or not str(value).strip():
        raise ValueError(f"Required field '{name}' is missing or empty")
    return str(value).strip()


def validate_evidence_status(value: str) -> EvidenceStatus:
    try:
        return EvidenceStatus(value)
    except ValueError as exc:
        valid = ", ".join(sorted(SUPPORTED_EVIDENCE_STATUSES))
        raise ValueError(f"Invalid evidence_status '{value}'. Expected one of: {valid}") from exc


def validate_dimension(value: str) -> ObservabilityDimension:
    if value not in SUPPORTED_DIMENSIONS:
        valid = ", ".join(sorted(SUPPORTED_DIMENSIONS))
        raise ValueError(f"Unsupported dimension '{value}'. Expected one of: {valid}")
    try:
        return ObservabilityDimension(value)
    except ValueError as exc:
        valid = ", ".join(sorted(SUPPORTED_DIMENSIONS))
        raise ValueError(f"Unsupported dimension '{value}'. Expected one of: {valid}") from exc


@dataclass
class Municipality:
    municipality_id: str
    municipality_name: str
    country: str

    def __post_init__(self) -> None:
        self.municipality_id = _require_text("municipality_id", self.municipality_id)
        self.municipality_name = _require_text("municipality_name", self.municipality_name)
        self.country = _require_text("country", self.country)

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


@dataclass
class SourceDocument:
    source_id: str
    municipality_id: str
    source_url: str
    source_title: str
    source_type: str
    access_date: date
    language: str = ""

    def __post_init__(self) -> None:
        self.source_id = _require_text("source_id", self.source_id)
        self.municipality_id = _require_text("municipality_id", self.municipality_id)
        self.source_url = _require_text("source_url", self.source_url)
        self.source_title = _require_text("source_title", self.source_title)
        self.source_type = _require_text("source_type", self.source_type)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["access_date"] = self.access_date.isoformat()
        return data


@dataclass
class EvidenceObservation:
    municipality_id: str
    source_id: str
    dimension: ObservabilityDimension
    evidence_status: EvidenceStatus
    quoted_evidence: str = ""
    page_or_section: str = ""

    def __post_init__(self) -> None:
        self.municipality_id = _require_text("municipality_id", self.municipality_id)
        self.source_id = _require_text("source_id", self.source_id)
        if isinstance(self.dimension, str):
            self.dimension = validate_dimension(self.dimension)
        if isinstance(self.evidence_status, str):
            self.evidence_status = validate_evidence_status(self.evidence_status)

    def to_dict(self) -> dict[str, str]:
        return {
            "municipality_id": self.municipality_id,
            "source_id": self.source_id,
            "dimension": self.dimension.value,
            "evidence_status": self.evidence_status.value,
            "quoted_evidence": self.quoted_evidence,
            "page_or_section": self.page_or_section,
        }


@dataclass
class CodingDecision:
    observation: EvidenceObservation
    coder_notes: str = ""
    non_claim_boundary: str = field(default=NON_CLAIM_BOUNDARY_V01)

    def __post_init__(self) -> None:
        self.non_claim_boundary = _require_text("non_claim_boundary", self.non_claim_boundary)
        if self.non_claim_boundary != NON_CLAIM_BOUNDARY_V01:
            raise ValueError(
                f"non_claim_boundary must be '{NON_CLAIM_BOUNDARY_V01}' in protocol v0.1"
            )

    def to_row(self) -> dict[str, str]:
        row = self.observation.to_dict()
        row["coder_notes"] = self.coder_notes
        row["non_claim_boundary"] = self.non_claim_boundary
        return row

    @classmethod
    def from_row(cls, row: dict[str, str]) -> CodingDecision:
        observation = EvidenceObservation(
            municipality_id=row["municipality_id"],
            source_id=row["source_id"],
            dimension=validate_dimension(row["dimension"]),
            evidence_status=validate_evidence_status(row["evidence_status"]),
            quoted_evidence=row.get("quoted_evidence", ""),
            page_or_section=row.get("page_or_section", ""),
        )
        return cls(
            observation=observation,
            coder_notes=row.get("coder_notes", ""),
            non_claim_boundary=row.get("non_claim_boundary", NON_CLAIM_BOUNDARY_V01),
        )


@dataclass
class CorpusManifest:
    municipality_id: str
    municipality_name: str
    country: str
    source_url: str
    source_title: str
    source_type: str
    access_date: date
    language: str = ""
    inclusion_reason: str = ""
    notes: str = ""

    def __post_init__(self) -> None:
        self.municipality_id = _require_text("municipality_id", self.municipality_id)
        self.municipality_name = _require_text("municipality_name", self.municipality_name)
        self.country = _require_text("country", self.country)
        self.source_url = _require_text("source_url", self.source_url)
        self.source_title = _require_text("source_title", self.source_title)
        self.source_type = _require_text("source_type", self.source_type)
        self.inclusion_reason = _require_text("inclusion_reason", self.inclusion_reason)

    def to_row(self) -> dict[str, Any]:
        return {
            "municipality_id": self.municipality_id,
            "municipality_name": self.municipality_name,
            "country": self.country,
            "source_url": self.source_url,
            "source_title": self.source_title,
            "source_type": self.source_type,
            "access_date": self.access_date.isoformat(),
            "language": self.language,
            "inclusion_reason": self.inclusion_reason,
            "notes": self.notes,
        }

    @classmethod
    def from_row(cls, row: dict[str, str]) -> CorpusManifest:
        return cls(
            municipality_id=row["municipality_id"],
            municipality_name=row["municipality_name"],
            country=row["country"],
            source_url=row["source_url"],
            source_title=row["source_title"],
            source_type=row["source_type"],
            access_date=date.fromisoformat(row["access_date"]),
            language=row.get("language", ""),
            inclusion_reason=row.get("inclusion_reason", ""),
            notes=row.get("notes", ""),
        )
