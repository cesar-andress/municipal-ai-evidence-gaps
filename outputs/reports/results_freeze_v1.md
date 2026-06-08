# Results freeze v1

**Freeze date:** 2026-06-08  
**Protocol:** v0.1.1  
**Audit:** [`results_consistency_audit.md`](results_consistency_audit.md)  
**Primary data:** [`data/processed/coding_results_v0_1_1.csv`](../../data/processed/coding_results_v0_1_1.csv)  
**Corpus manifest:** [`data/processed/corpus_manifest_v0_1.csv`](../../data/processed/corpus_manifest_v0_1.csv)

**Status:** Frozen — all manuscript numerals, tables, and figures must cite values from this document unless a future re-freeze supersedes it.

This document records definitive descriptive frequencies only. It does not contain manuscript prose, discussion, or conclusions.

---

## 1. Corpus scope (frozen)

| Field | Value |
|-------|-------|
| Municipalities | 6 (Amsterdam, Barcelona, Copenhagen, Helsinki, Vienna, Tallinn) |
| Manifest sources | 23 |
| Coding decisions | 115 (23 sources × 5 dimensions) |
| Protocol version | v0.1.1 |
| Evidence-status labels | 4 |
| Dimensions | D1–D5 |
| Manifest `source_type` categories present | 6 |
| Manifest `source_type` categories absent | `procurement document`; `other official document` |

### Manifest sources per municipality

| `municipality_id` | Sources | Coding rows |
|-------------------|---------|-------------|
| mun-amsterdam | 3 | 15 |
| mun-barcelona | 4 | 20 |
| mun-copenhagen | 2 | 10 |
| mun-helsinki | 5 | 25 |
| mun-tallinn | 3 | 15 |
| mun-vienna | 6 | 30 |

### Retrieval at coding

| `retrieval_status` | Sources | Coding rows |
|--------------------|---------|-------------|
| `ok` | 19 | 95 |
| `bot_gated` | 4 | 20 |

---

## 2. Corpus-wide evidence-status distribution (frozen)

| `evidence_status` | n | % of 115 rows |
|-------------------|---|---------------|
| `not_observable_publicly` | 50 | 43.5% |
| `observable_policy_commitment` | 37 | 32.2% |
| `partial_or_indirect_signal` | 25 | 21.7% |
| `observable_named_artifact` | 3 | 2.6% |

| Derived metric | n | % |
|----------------|---|-----|
| Any observable evidence (non-`not_observable`) | 65 | 56.5% |
| Not observable | 50 | 43.5% |

### Observable subset composition

| `evidence_status` | n | % of 65 observable rows |
|-------------------|---|-------------------------|
| `observable_policy_commitment` | 37 | 56.9% |
| `partial_or_indirect_signal` | 25 | 38.5% |
| `observable_named_artifact` | 3 | 4.6% |

---

## 3. Dimension distribution (frozen)

### D1–D5 × evidence-status counts

| Dimension | Named artefact | Policy commitment | Partial/indirect | Not observable | Total |
|-----------|---------------|-------------------|------------------|----------------|-------|
| D1 Programme ownership | 3 | 7 | 7 | 6 | 23 |
| D2 Human oversight and review | 0 | 10 | 8 | 5 | 23 |
| D3 Prompt, log, and data governance | 0 | 11 | 4 | 8 | 23 |
| D4 Procurement and vendor stewardship | 0 | 3 | 2 | 18 | 23 |
| D5 Incident, audit, and lifecycle accountability | 0 | 6 | 4 | 13 | 23 |

### D1–D5 × evidence-status row percentages

| Dimension | Named % | Commitment % | Partial % | Not obs % |
|-----------|---------|--------------|-----------|-----------|
| D1 | 13.0% | 30.4% | 30.4% | 26.1% |
| D2 | 0.0% | 43.5% | 34.8% | 21.7% |
| D3 | 0.0% | 47.8% | 17.4% | 34.8% |
| D4 | 0.0% | 13.0% | 8.7% | 78.3% |
| D5 | 0.0% | 26.1% | 17.4% | 56.5% |

### Dimension observable summary

| Dimension | Observable n | Not observable n | Observable % | Systematically under-observable (>50% not obs) |
|-----------|--------------|------------------|--------------|-----------------------------------------------|
| D1 | 17 | 6 | 73.9% | No |
| D2 | 18 | 5 | 78.3% | No |
| D3 | 15 | 8 | 65.2% | No |
| D4 | 5 | 18 | 21.7% | **Yes** |
| D5 | 10 | 13 | 43.5% | **Yes** |

### Modal dimension status

| Dimension | Modal `evidence_status` | Modal share |
|-----------|-------------------------|-------------|
| D1 | Mixed (no status >60%) | — |
| D2 | `observable_policy_commitment` | 43.5% |
| D3 | `observable_policy_commitment` | 47.8% |
| D4 | `not_observable_publicly` | 78.3% |
| D5 | `not_observable_publicly` | 56.5% |

---

## 4. Municipality profiles (frozen)

### Evidence-status by municipality

| Municipality | Sources | Rows | Named | Commitment | Partial | Not obs | Observable rows |
|--------------|---------|------|-------|------------|---------|---------|-----------------|
| Amsterdam | 3 | 15 | 0 | 0 | 4 | 11 | 4 |
| Barcelona | 4 | 20 | 0 | 11 | 8 | 1 | 19 |
| Copenhagen | 2 | 10 | 0 | 4 | 4 | 2 | 8 |
| Helsinki | 5 | 25 | 0 | 9 | 4 | 12 | 13 |
| Tallinn | 3 | 15 | 0 | 0 | 0 | 15 | 0 |
| Vienna | 6 | 30 | 3 | 13 | 5 | 9 | 21 |

### Municipality × dimension `not_observable_publicly` counts

| Municipality | D1 | D2 | D3 | D4 | D5 |
|--------------|----|----|----|----|-----|
| Amsterdam | 2 | 2 | 2 | 3 | 2 |
| Barcelona | 0 | 0 | 0 | 0 | 1 |
| Copenhagen | 0 | 0 | 0 | 2 | 0 |
| Helsinki | 0 | 0 | 2 | 5 | 5 |
| Tallinn | 3 | 3 | 3 | 3 | 3 |
| Vienna | 1 | 0 | 1 | 5 | 2 |

---

## 5. Source-type profiles (frozen)

### Evidence-status by `source_type`

| `source_type` | Named | Commitment | Partial | Not obs | Total |
|---------------|-------|------------|---------|---------|-------|
| AI strategy | 1 | 11 | 7 | 6 | 25 |
| governance framework | 2 | 12 | 4 | 12 | 30 |
| committee record | 0 | 5 | 2 | 3 | 10 |
| algorithm register | 0 | 0 | 8 | 7 | 15 |
| AI policy | 0 | 4 | 2 | 9 | 15 |
| transparency portal | 0 | 5 | 2 | 13 | 20 |

### Source-type observable shares

| `source_type` | Observable n | Not obs n | Observable % | Not obs % |
|---------------|--------------|-----------|--------------|-----------|
| AI strategy | 19 | 6 | 76.0% | 24.0% |
| governance framework | 18 | 12 | 60.0% | 40.0% |
| committee record | 7 | 3 | 70.0% | 30.0% |
| algorithm register | 8 | 7 | 53.3% | 46.7% |
| AI policy | 6 | 9 | 40.0% | 60.0% |
| transparency portal | 7 | 13 | 35.0% | 65.0% |

### Source type × dimension observable cells

| `source_type` | D1 | D2 | D3 | D4 | D5 |
|---------------|----|----|----|----|-----|
| AI strategy | 4 | 5 | 4 | 2 | 4 |
| governance framework | 4 | 4 | 4 | 2 | 4 |
| committee record | 2 | 2 | 2 | 0 | 1 |
| algorithm register | 3 | 3 | 1 | 0 | 1 |
| AI policy | 2 | 2 | 2 | 0 | 0 |
| transparency portal | 2 | 2 | 2 | 1 | 0 |

**D4 observable maximum per source type:** 2 rows.

---

## 6. `observable_named_artifact` inventory (frozen)

| Metric | Value |
|--------|-------|
| Total named-artefact rows | 3 |
| Share of corpus | 2.6% |
| Dimensions | D1 only |
| Municipalities | mun-vienna only |
| Source types | AI strategy (1); governance framework (2) |

| # | Municipality | Dimension | `source_type` | `quoted_evidence` | `page_or_section` |
|---|--------------|-----------|---------------|-------------------|-------------------|
| 1 | mun-vienna | D1 | AI strategy | ICT Strategy and Process Management Group (MD-OS/PIKT) | Legal notice |
| 2 | mun-vienna | D1 | governance framework | AI-Kompetenznetzwerk, bestehend aus Vertreter*innen der Magistratsdirektion | Entstehungsgeschichte |
| 3 | mun-vienna | D1 | governance framework | AI Competence Network (headed by the Executive Group for Organisation and Security (MD-OS)) | Document header |

**Empty cells (frozen):** D2–D5 × `observable_named_artifact` = 0 for all dimensions.

---

## 7. Structural constraints (frozen)

| Constraint | Value |
|------------|-------|
| Bot-gated manifest sources | 4 |
| Bot-gated coding rows | 20 |
| Bot-gated rows as share of all not-observable | 20/50 (40.0%) |
| Sources with zero observable dimensions | 5 |
| Register + transparency portal coding rows | 35 |
| Procurement document sources in manifest | 0 |

### Five zero-observable sources

| Municipality | `source_type` | `retrieval_status` |
|--------------|---------------|-------------------|
| Amsterdam | AI policy | bot_gated |
| Amsterdam | transparency portal | bot_gated |
| Tallinn | governance framework (BETTI) | bot_gated |
| Tallinn | transparency portal (digital twin) | bot_gated |
| Tallinn | governance framework (2035 landing) | ok |

---

## 8. RQ summary numerals (frozen)

Use these values for results-section numerals and Tier A claims.

| RQ | Frozen statement (numeral only) |
|----|--------------------------------|
| RQ1 | 65/115 rows (56.5%) observable; 37 commitments; 25 partial; 3 named artefacts |
| RQ1 | D1 73.9%, D2 78.3%, D3 65.2% observable; named artefacts D1-only (3 rows) |
| RQ2 | D4 18/23 not observable (78.3%); D5 13/23 (56.5%); both >50% threshold |
| RQ2 | D2 5/23 (21.7%); D3 8/23 (34.8%) — not systematically under-observable |
| RQ3 | Tallinn 15/15 not observable; Amsterdam 11/15 not observable (10 bot-gated rows) |
| RQ3 | Barcelona 19/20 observable; Vienna only municipality with named artefacts |
| RQ3 | Transparency portal 13/20 not observable (65.0%) |

---

## 9. Manuscript table bindings (frozen)

| Manuscript table | Freeze section |
|------------------|----------------|
| Corpus overview | §1 |
| Evidence-status distribution | §2 |
| Dimension × status | §3 |
| Under-observability summary | §3 (observable summary) |
| Source-type distribution | §5 |
| Municipality profile | §4 |
| Municipality × dimension heatmap | §4 (matrix) |
| Source type × dimension heatmap | §5 (observable cells) |
| Named-artefact inventory | §6 |
| Structural constraints | §7 |

Candidate table specs: [`findings_candidate_tables.md`](findings_candidate_tables.md)  
Tier A claims: [`result_claims_inventory.md`](result_claims_inventory.md)

---

## 10. Provenance and supersession

| Field | Value |
|-------|-------|
| Derived from | `coding_results_v0_1_1.csv` (115 rows) + `corpus_manifest_v0_1.csv` join |
| Validated by | `results_consistency_audit.md` |
| Supersedes | Informal conversation summaries; `coding_summary_v0_1_1.md` dimension table (erroneous) |
| Next version trigger | Protocol change, recoding, or manifest revision |

**Canonical hierarchy:** `coding_results_v0_1_1.csv` → `results_freeze_v1.md` → manuscript.
