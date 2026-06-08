"""Tests for v0.1 schema enums, validators, and required fields."""

from datetime import date

import pytest

from evidence_gaps.schema import (
    NON_CLAIM_BOUNDARY_V01,
    CodingDecision,
    CorpusManifest,
    EvidenceObservation,
    EvidenceStatus,
    Municipality,
    ObservabilityDimension,
    SourceDocument,
    SUPPORTED_DIMENSIONS,
    SUPPORTED_EVIDENCE_STATUSES,
    coding_template_columns,
    corpus_manifest_columns,
    validate_dimension,
    validate_evidence_status,
)


def test_evidence_status_values():
    assert len(EvidenceStatus) == 4
    assert EvidenceStatus.OBSERVABLE_NAMED_ARTIFACT.value == "observable_named_artifact"
    assert EvidenceStatus.NOT_OBSERVABLE_PUBLICLY.value == "not_observable_publicly"
    assert SUPPORTED_EVIDENCE_STATUSES == {s.value for s in EvidenceStatus}


def test_observability_dimension_count():
    assert len(ObservabilityDimension) == 5
    assert ObservabilityDimension.D1_PROGRAMME_OWNERSHIP.value == "D1_programme_ownership"
    assert ObservabilityDimension.D5_INCIDENT_AUDIT_LIFECYCLE.value.startswith("D5_")


def test_validate_evidence_status_accepts_all_supported():
    for status in SUPPORTED_EVIDENCE_STATUSES:
        assert validate_evidence_status(status).value == status


def test_validate_evidence_status_rejects_invalid():
    with pytest.raises(ValueError, match="Invalid evidence_status"):
        validate_evidence_status("readiness_score")


def test_validate_dimension_accepts_all_supported():
    for dimension in SUPPORTED_DIMENSIONS:
        assert validate_dimension(dimension).value == dimension


def test_validate_dimension_rejects_unsupported_labels():
    with pytest.raises(ValueError, match="Unsupported dimension"):
        validate_dimension("D6_model_performance")
    with pytest.raises(ValueError, match="Unsupported dimension"):
        validate_dimension("principles_and_commitments")


def test_corpus_manifest_columns_match_template():
    assert corpus_manifest_columns == (
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


def test_coding_template_columns_match_schema():
    assert coding_template_columns == (
        "municipality_id",
        "source_id",
        "dimension",
        "evidence_status",
        "quoted_evidence",
        "page_or_section",
        "coder_notes",
        "non_claim_boundary",
    )


def test_municipality_requires_fields():
    with pytest.raises(ValueError, match="municipality_id"):
        Municipality(municipality_id="", municipality_name="Oslo", country="NO")


def test_source_document_requires_fields():
    with pytest.raises(ValueError, match="source_url"):
        SourceDocument(
            source_id="src-001",
            municipality_id="mun-001",
            source_url="",
            source_title="AI Strategy",
            source_type="strategy",
            access_date=date(2026, 6, 8),
        )


def test_corpus_manifest_requires_inclusion_reason():
    with pytest.raises(ValueError, match="inclusion_reason"):
        CorpusManifest(
            municipality_id="mun-001",
            municipality_name="Example City",
            country="ES",
            source_url="https://example.gov/ai",
            source_title="AI Strategy",
            source_type="strategy",
            access_date=date(2026, 6, 8),
            inclusion_reason="",
        )


def test_coding_decision_requires_non_claim_boundary():
    observation = EvidenceObservation(
        municipality_id="mun-001",
        source_id="src-001",
        dimension=ObservabilityDimension.D2_HUMAN_OVERSIGHT_REVIEW,
        evidence_status=EvidenceStatus.PARTIAL_OR_INDIRECT_SIGNAL,
    )
    with pytest.raises(ValueError, match="non_claim_boundary"):
        CodingDecision(observation=observation, non_claim_boundary="readiness_index_v1")


def test_coding_decision_round_trip():
    decision = CodingDecision(
        observation=EvidenceObservation(
            municipality_id="mun-001",
            source_id="src-001",
            dimension="D1_programme_ownership",
            evidence_status="observable_policy_commitment",
            quoted_evidence="Section 3.2",
            page_or_section="p. 12",
        ),
        coder_notes="Named digital office without AI-specific remit.",
        non_claim_boundary=NON_CLAIM_BOUNDARY_V01,
    )
    row = decision.to_row()
    parsed = CodingDecision.from_row(row)

    assert parsed.observation.dimension is ObservabilityDimension.D1_PROGRAMME_OWNERSHIP
    assert parsed.observation.evidence_status is EvidenceStatus.OBSERVABLE_POLICY_COMMITMENT
    assert parsed.non_claim_boundary == NON_CLAIM_BOUNDARY_V01
