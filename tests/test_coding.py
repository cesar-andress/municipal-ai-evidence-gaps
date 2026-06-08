"""Tests for coding helpers."""

from evidence_gaps.coding import parse_coding_row
from evidence_gaps.schema import (
    NON_CLAIM_BOUNDARY_V01,
    EvidenceStatus,
    ObservabilityDimension,
)


def test_parse_coding_row():
    row = {
        "municipality_id": "mun-001",
        "source_id": "src-001",
        "dimension": "D3_prompt_log_and_data_governance",
        "evidence_status": "not_observable_publicly",
        "quoted_evidence": "",
        "page_or_section": "",
        "coder_notes": "No log retention detail in transparency page.",
        "non_claim_boundary": NON_CLAIM_BOUNDARY_V01,
    }
    decision = parse_coding_row(row)

    assert decision.observation.dimension is ObservabilityDimension.D3_PROMPT_LOG_DATA_GOVERNANCE
    assert decision.observation.evidence_status is EvidenceStatus.NOT_OBSERVABLE_PUBLICLY
