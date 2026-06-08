"""Coding helpers for observability annotation."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from evidence_gaps.schema import EvidenceCategory, Observability, validate_category, validate_observability


@dataclass(frozen=True)
class CodingRecord:
    """One observability annotation for a document and evidence category."""

    document_id: str
    category: EvidenceCategory
    observability: Observability
    coder: str
    coded_at: date
    evidence_excerpt: str = ""
    notes: str = ""

    def to_row(self) -> dict[str, str]:
        """Serialise to a flat dict matching coded_corpus columns."""
        return {
            "document_id": self.document_id,
            "category": self.category.value,
            "observability": self.observability.value,
            "coder": self.coder,
            "coded_at": self.coded_at.isoformat(),
            "evidence_excerpt": self.evidence_excerpt,
            "notes": self.notes,
        }


def parse_coding_row(row: dict[str, str]) -> CodingRecord:
    """Parse a CSV row into a CodingRecord."""
    return CodingRecord(
        document_id=row["document_id"],
        category=validate_category(row["category"]),
        observability=validate_observability(row["observability"]),
        coder=row["coder"],
        coded_at=date.fromisoformat(row["coded_at"]),
        evidence_excerpt=row.get("evidence_excerpt", ""),
        notes=row.get("notes", ""),
    )
