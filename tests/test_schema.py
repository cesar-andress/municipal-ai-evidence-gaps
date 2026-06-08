"""Tests for schema enums and validators."""

import pytest

from evidence_gaps.schema import EvidenceCategory, Observability, validate_category, validate_observability


def test_observability_values():
    assert Observability.PRESENT.value == "present"
    assert Observability.ABSENT.value == "absent"


def test_evidence_category_count():
    assert len(EvidenceCategory) == 8


def test_validate_observability_accepts_valid():
    assert validate_observability("partial") is Observability.PARTIAL


def test_validate_observability_rejects_invalid():
    with pytest.raises(ValueError, match="Invalid observability"):
        validate_observability("unknown")


def test_validate_category_accepts_valid():
    assert validate_category("system_inventory") is EvidenceCategory.SYSTEM_INVENTORY


def test_validate_category_rejects_invalid():
    with pytest.raises(ValueError, match="Invalid category"):
        validate_category("readiness_score")
