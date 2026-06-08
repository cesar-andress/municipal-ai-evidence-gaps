"""Tests for coding record helpers."""

from datetime import date

from evidence_gaps.coding import CodingRecord, parse_coding_row
from evidence_gaps.schema import EvidenceCategory, Observability


def test_coding_record_round_trip():
    record = CodingRecord(
        document_id="doc-001",
        category=EvidenceCategory.PRINCIPLES_COMMITMENTS,
        observability=Observability.PARTIAL,
        coder="coder_a",
        coded_at=date(2026, 6, 8),
        evidence_excerpt="Section 2.1",
        notes="Mentions fairness principles only.",
    )
    row = record.to_row()
    parsed = parse_coding_row(row)

    assert parsed.document_id == "doc-001"
    assert parsed.category is EvidenceCategory.PRINCIPLES_COMMITMENTS
    assert parsed.observability is Observability.PARTIAL
    assert parsed.coded_at == date(2026, 6, 8)
