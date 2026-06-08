"""Municipal AI evidence gaps — comparative documentary analysis artifact."""

__version__ = "0.1.0"

from evidence_gaps.schema import (
    NON_CLAIM_BOUNDARY_V01,
    CodingDecision,
    CorpusManifest,
    EvidenceObservation,
    EvidenceStatus,
    Municipality,
    ObservabilityDimension,
    SourceDocument,
    coding_template_columns,
    corpus_manifest_columns,
)

__all__ = [
    "CodingDecision",
    "CorpusManifest",
    "EvidenceObservation",
    "EvidenceStatus",
    "Municipality",
    "NON_CLAIM_BOUNDARY_V01",
    "ObservabilityDimension",
    "SourceDocument",
    "coding_template_columns",
    "corpus_manifest_columns",
    "__version__",
]
