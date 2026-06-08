# Coding protocol

## Purpose

Code publicly accessible municipal AI documents for **observability** of governance-relevant evidence categories.

Coding records what appears in public documentation. It does not evaluate municipal performance, legal compliance, or readiness.

## Observability values

| Value | Definition |
|-------|------------|
| `present` | Category is explicitly documented with usable detail |
| `partial` | Category is mentioned but lacks programme-level specificity |
| `absent` | Category is not observable in the public document |
| `not_applicable` | Category is not expected for this document type |

## Evidence categories (initial)

1. **Principles and commitments** — ethical statements, policy goals, public values
2. **System inventory** — named AI systems, use cases, or register entries
3. **Implementation detail** — deployment context, data sources, lifecycle information
4. **Risk and impact** — impact assessments, risk framing, affected populations
5. **Monitoring and review** — ongoing oversight, audit, or evaluation mechanisms
6. **Accountability linkages** — roles, responsibilities, complaint or redress routes
7. **Procurement and vendor** — contracting, vendor roles, or partnership disclosure
8. **Update and versioning** — revision dates, change logs, maintenance practices

Categories may be refined during pilot coding. Changes will be versioned in this document.

## Unit of coding

The default unit is one **public document** (or one register entry where registers are itemised). Multi-page transparency hubs may be coded as a bundle with a single `document_id`.

## Reliability

A subset of documents will be double-coded. Disagreements will be documented and resolved through protocol clarification, not by averaging into scores.

## Prohibited uses

- Do not convert observability counts into readiness indices
- Do not rank municipalities
- Do not treat `absent` as proof of non-compliance

## Implementation

See `src/evidence_gaps/coding.py` and `scripts/code_observability.py`.
