# Findings candidate tables

**Derived from:** [`rq_analysis_v0_1.md`](rq_analysis_v0_1.md)  
**Coding data:** `coding_results_v0_1_1.csv` (n = 115 rows)  
**Date:** 2026-06-08

Candidate tables for manuscript integration. Variables and rationale only — no prose results section.

---

## Table 1 — Corpus and coding overview

| Field | Value |
|-------|-------|
| **Title** | Municipal AI documentation corpus and observability coding overview (v0.1) |
| **Variables** | Municipalities (n=6); manifest sources (n=23); coding decisions (n=115); protocol version (v0.1.1); evidence-status taxonomy (4 labels); dimensions (D1–D5) |
| **Rationale** | Establishes analytic denominator and scope before presenting observability distributions; anchors non-claims (public-document observability only). |

---

## Table 2 — Evidence-status distribution (corpus-wide)

| Field | Value |
|-------|-------|
| **Title** | Distribution of evidence-status labels across all coding decisions |
| **Variables** | `evidence_status` (observable_named_artifact; observable_policy_commitment; partial_or_indirect_signal; not_observable_publicly); count; row percentage |
| **Rationale** | Primary descriptive output for RQ1; shows commitment-dominant observable profile and rarity of named artefacts. |

**Candidate cells:**

| evidence_status | n | % |
|-----------------|---|---|
| not_observable_publicly | 50 | 43.5 |
| observable_policy_commitment | 37 | 32.2 |
| partial_or_indirect_signal | 25 | 21.7 |
| observable_named_artifact | 3 | 2.6 |

---

## Table 3 — Evidence-status by observability dimension

| Field | Value |
|-------|-------|
| **Title** | Evidence-status distribution by governance dimension (D1–D5) |
| **Variables** | Dimension (D1–D5); four evidence-status counts; row total per dimension (23) |
| **Rationale** | Core table for RQ2; identifies D4/D5 under-observability and zero named-artefact cells in D2–D5. |

**Candidate structure:** 5 rows (dimensions) × 5 columns (four statuses + total).

---

## Table 4 — Dimension under-observability summary

| Field | Value |
|-------|-------|
| **Title** | Public under-observability by dimension |
| **Variables** | Dimension; `not_observable_publicly` count; share of dimension rows; under-observable flag (>50% threshold) |
| **Rationale** | Condenses RQ2 answer; highlights systematic gaps in procurement (D4) and lifecycle accountability (D5). |

**Candidate cells:**

| Dimension | not_observable | % | >50% flag |
|-----------|----------------|---|-----------|
| D4 | 18 | 78.3 | Yes |
| D5 | 13 | 56.5 | Yes |
| D3 | 8 | 34.8 | No |
| D1 | 6 | 26.1 | No |
| D2 | 5 | 21.7 | No |

---

## Table 5 — Evidence-status by source type

| Field | Value |
|-------|-------|
| **Title** | Evidence-status distribution by manifest source type |
| **Variables** | `source_type` (6 types in corpus); four evidence-status counts; source-type row totals (10–30) |
| **Rationale** | Supports RQ3 document-type patterns; shows strategy and governance-framework types carry most observable evidence. |

**Candidate structure:** 6 rows × 5 columns.

---

## Table 6 — Municipality observability profile (coded rows)

| Field | Value |
|-------|-------|
| **Title** | Evidence-status counts by municipality (coding-row basis) |
| **Variables** | `municipality_id`; manifest source count; coding-row count; four evidence-status counts |
| **Rationale** | Supports RQ3 municipality patterns without ranking; documents unequal row denominators and bot-gated retrieval effects. |

**Note for caption:** Row counts reflect manifest source multiplicity, not sampled municipal units of equal weight.

---

## Table 7 — Municipality × dimension not-observable matrix

| Field | Value |
|-------|-------|
| **Title** | Count of `not_observable_publicly` decisions by municipality and dimension |
| **Variables** | Municipality (6); dimension (D1–D5); cell = count of not-observable rows (0–3 per cell) |
| **Rationale** | Shows localized gap patterns (e.g. Helsinki D4/D5; Tallinn uniform non-observability); inputs heatmap figure. |

---

## Table 8 — Source type × dimension observability matrix

| Field | Value |
|-------|-------|
| **Title** | Observable coding decisions by source type and dimension |
| **Variables** | Source type (6); dimension (D1–D5); cell = count of non-`not_observable_publicly` rows (0–5) |
| **Rationale** | Identifies which document types contribute observable evidence to which dimensions; highlights D4 sparsity across types. |

---

## Table 9 — Transparency mechanism observability

| Field | Value |
|-------|-------|
| **Title** | Observability patterns in transparency-oriented source types |
| **Variables** | Source type (algorithm register; transparency portal); evidence-status counts; observable share |
| **Rationale** | RQ3 transparency-pattern table; separates register metadata signals from portal commitment language. |

---

## Table 10 — Corpus structural constraints

| Field | Value |
|-------|-------|
| **Title** | Manifest and retrieval constraints affecting observability distributions |
| **Variables** | Constraint type (bot-gated sources; absent source types; coding depth); affected rows; affected municipalities |
| **Rationale** | Methods-limitations table; prevents over-interpretation of non-observable counts as documentary absence. |

**Candidate rows:**

| Constraint | Rows affected |
|------------|---------------|
| Bot-gated sources (4) | 20 not-observable rows |
| No procurement document type | D4 limited to 23 non-procurement sources |
| Register index-level coding | 15 register/portal rows |

---

## Table usage map

| RQ | Primary tables |
|----|----------------|
| RQ1 | 2, 3, 5 |
| RQ2 | 3, 4 |
| RQ3 | 5, 6, 7, 8, 9, 10 |
