# Results consistency audit

**Audit date:** 2026-06-08  
**Auditor role:** Replication auditor (pre-manuscript freeze)  
**Canonical input:** [`data/processed/coding_results_v0_1_1.csv`](../../data/processed/coding_results_v0_1_1.csv)  
**Corpus metadata:** [`data/processed/corpus_manifest_v0_1.csv`](../../data/processed/corpus_manifest_v0_1.csv)  
**Protocol:** v0.1.1

This audit recomputes all analytical frequencies directly from the coding CSV and compares them against eight generated artefacts. It does not draft manuscript text, discussion, or conclusions.

---

## Audit method

1. Loaded 115 coding rows from `coding_results_v0_1_1.csv`.
2. Joined `source_type` and `retrieval_status` from `corpus_manifest_v0_1.csv` on `(municipality_id, source_url)` — **0 unmatched rows**.
3. Recomputed corpus-wide, dimension, municipality, and source-type frequency tables.
4. Cross-checked each table against:
   - `coding_summary_v0_1_1.md`
   - `coding_distribution_audit_v0_1_1.md`
   - `pre_analysis_validity_check.md`
   - `rq_analysis_v0_1.md`
   - `result_claims_inventory.md`
   - `findings_candidate_tables.md`
   - `findings_candidate_figures.md`
5. Flagged every cell-level mismatch.

**Recomputation script:** inline Python audit executed 2026-06-08 in repository root (no persistent script artefact).

---

## Corpus totals (recomputed)

| Metric | Recomputed | Expected |
|--------|------------|----------|
| Manifest sources | 23 | 23 |
| Municipalities | 6 | 6 |
| Dimensions per source | 5 | 5 |
| Total coding rows | 115 | 115 |
| Manifest `source_type` values present | 6 | 6 |
| Manifest join failures | 0 | 0 |

**Verdict:** Pass.

---

## Evidence-status totals (corpus-wide)

| `evidence_status` | Recomputed (n) | Recomputed (%) | Artefact agreement |
|-------------------|----------------|----------------|--------------------|
| `not_observable_publicly` | 50 | 43.5% | All reports agree |
| `observable_policy_commitment` | 37 | 32.2% | All reports agree |
| `partial_or_indirect_signal` | 25 | 21.7% | All reports agree |
| `observable_named_artifact` | 3 | 2.6% | All reports agree |
| **Observable (any non-not-observable)** | **65** | **56.5%** | `rq_analysis`, `result_claims_inventory`, `findings_candidate_figures` agree |

**Verdict:** Pass (corpus-wide).

---

## Dimension totals (D1–D5)

Recomputed dimension × `evidence_status` matrix (23 rows per dimension):

| Dimension | Named artefact | Policy commitment | Partial/indirect | Not observable |
|-----------|---------------|-------------------|------------------|----------------|
| D1 | 3 | 7 | 7 | 6 |
| D2 | 0 | 10 | 8 | 5 |
| D3 | 0 | 11 | 4 | 8 |
| D4 | 0 | 3 | 2 | 18 |
| D5 | 0 | 6 | 4 | 13 |

### Dimension observable shares

| Dimension | Observable rows | Not observable | Observable share | >50% not-observable |
|-----------|-----------------|----------------|------------------|---------------------|
| D1 | 17 | 6 | 73.9% | No (26.1%) |
| D2 | 18 | 5 | 78.3% | No (21.7%) |
| D3 | 15 | 8 | 65.2% | No (34.8%) |
| D4 | 5 | 18 | 21.7% | **Yes (78.3%)** |
| D5 | 10 | 13 | 43.5% | **Yes (56.5%)** |

### Artefact comparison

| Artefact | Dimension table | Verdict |
|----------|-----------------|---------|
| `coding_distribution_audit_v0_1_1.md` | Matches recomputed matrix | **Pass** |
| `pre_analysis_validity_check.md` | Qualitative references match (D4 78.3%; D5 56.5%; D1-only named artefacts) | **Pass** |
| `rq_analysis_v0_1.md` | Matches recomputed matrix and shares | **Pass** |
| `result_claims_inventory.md` | All frequency-based claims align | **Pass** |
| `findings_candidate_tables.md` | Table 2 and Table 4 cells match | **Pass** |
| `coding_summary_v0_1_1.md` | **Dimension table does not match** | **FAIL** — see discrepancies |

**Verdict:** Pass for downstream RQ artefacts; **fail for `coding_summary_v0_1_1.md` dimension breakdown**.

---

## Municipality totals

| `municipality_id` | Manifest sources | Coding rows | Named | Commitment | Partial | Not obs | Non-not-obs |
|-------------------|------------------|-------------|-------|------------|---------|---------|-------------|
| mun-amsterdam | 3 | 15 | 0 | 0 | 4 | 11 | 4 / 15 |
| mun-barcelona | 4 | 20 | 0 | 11 | 8 | 1 | 19 / 20 |
| mun-copenhagen | 2 | 10 | 0 | 4 | 4 | 2 | 8 / 10 |
| mun-helsinki | 5 | 25 | 0 | 9 | 4 | 12 | 13 / 25 |
| mun-vienna | 6 | 30 | 3 | 13 | 5 | 9 | 21 / 30 |
| mun-tallinn | 3 | 15 | 0 | 0 | 0 | 15 | 0 / 15 |

### Municipality × dimension `not_observable_publicly`

| Municipality | D1 | D2 | D3 | D4 | D5 |
|--------------|----|----|----|----|-----|
| Amsterdam | 2 | 2 | 2 | 3 | 2 |
| Barcelona | 0 | 0 | 0 | 0 | 1 |
| Copenhagen | 0 | 0 | 0 | 2 | 0 |
| Helsinki | 0 | 0 | 2 | 5 | 5 |
| Tallinn | 3 | 3 | 3 | 3 | 3 |
| Vienna | 1 | 0 | 1 | 5 | 2 |

| Artefact | Verdict |
|----------|---------|
| `coding_distribution_audit_v0_1_1.md` | **Pass** |
| `rq_analysis_v0_1.md` | **Pass** |
| `result_claims_inventory.md` (RQ3-C01–C05) | **Pass** |
| `coding_summary_v0_1_1.md` | No municipality table — N/A |

**Verdict:** Pass.

---

## Source-type totals

| `source_type` | Named | Commitment | Partial | Not obs | Total |
|---------------|-------|------------|---------|---------|-------|
| AI strategy | 1 | 11 | 7 | 6 | 25 |
| governance framework | 2 | 12 | 4 | 12 | 30 |
| committee record | 0 | 5 | 2 | 3 | 10 |
| algorithm register | 0 | 0 | 8 | 7 | 15 |
| AI policy | 0 | 4 | 2 | 9 | 15 |
| transparency portal | 0 | 5 | 2 | 13 | 20 |

Absent manifest types (zero rows): `procurement document`; `other official document`.

### Source type × dimension (observable cells)

| Source type | D1 | D2 | D3 | D4 | D5 |
|-------------|----|----|----|----|-----|
| AI strategy | 4 | 5 | 4 | 2 | 4 |
| governance framework | 4 | 4 | 4 | 2 | 4 |
| committee record | 2 | 2 | 2 | 0 | 1 |
| algorithm register | 3 | 3 | 1 | 0 | 1 |
| AI policy | 2 | 2 | 2 | 0 | 0 |
| transparency portal | 2 | 2 | 2 | 1 | 0 |

| Artefact | Verdict |
|----------|---------|
| `coding_distribution_audit_v0_1_1.md` | **Pass** |
| `rq_analysis_v0_1.md` | **Pass** |
| `result_claims_inventory.md` (RQ1-C06; RQ3-C06–C09) | **Pass** |

**Verdict:** Pass.

---

## `observable_named_artifact` verification

| Check | Recomputed | Report agreement |
|-------|------------|----------------|
| Corpus total | 3 (2.6%) | All reports agree |
| Dimensions with named artefacts | D1 only | All downstream reports agree |
| Municipalities with named artefacts | mun-vienna only | All downstream reports agree |
| D2–D5 named-artefact cells | 0 each | All downstream reports agree |

### Named-artefact detail (3 rows)

| # | Municipality | Dimension | `source_type` | Locator summary |
|---|--------------|-----------|---------------|-----------------|
| 1 | mun-vienna | D1 | AI strategy | MD-OS/PIKT (legal notice) |
| 2 | mun-vienna | D1 | governance framework | AI-Kompetenznetzwerk (Entstehungsgeschichte) |
| 3 | mun-vienna | D1 | governance framework | AI Competence Network / MD-OS (document header) |

| Artefact | Verdict |
|----------|---------|
| `coding_distribution_audit_v0_1_1.md` §6 | **Pass** (URLs and locators match CSV) |
| `rq_analysis_v0_1.md` | **Pass** |
| `pre_analysis_validity_check.md` | **Pass** |
| `coding_summary_v0_1_1.md` | **Partial fail** — corpus total correct; D1 shows 2 named (should be 3); D5 shows 1 named (should be 0) |

**Verdict:** Pass for CSV and downstream chain; **fail in `coding_summary` dimension cells**.

---

## Structural constraint counts

| Constraint | Recomputed | Report agreement |
|------------|------------|------------------|
| Bot-gated manifest sources | 4 | Agreed |
| Bot-gated coding rows | 20 | Agreed (`rq_analysis`, `pre_analysis_validity_check`) |
| Bot-gated share of all not-observable rows | 20/50 (40.0%) | Consistent |
| Sources with zero observable dimensions | 5 | Agreed (`rq_analysis` RQ3 list) |
| Register/portal rows (algorithm register + transparency portal) | 35 | Consistent with audit notes |

**Verdict:** Pass.

---

## Discrepancy register

| ID | Severity | Location | Issue | Canonical value |
|----|----------|----------|-------|-----------------|
| **DISC-01** | **High** | `coding_summary_v0_1_1.md` § "By dimension" | D1 dimension table incorrect across all four status columns | D1: 3 / 7 / 7 / 6 |
| **DISC-02** | **High** | `coding_summary_v0_1_1.md` § "By dimension" | D2 table incorrect | D2: 0 / 10 / 8 / 5 |
| **DISC-03** | **High** | `coding_summary_v0_1_1.md` § "By dimension" | D3 table incorrect | D3: 0 / 11 / 4 / 8 |
| **DISC-04** | **High** | `coding_summary_v0_1_1.md` § "By dimension" | D5 shows spurious `observable_named_artifact: 1` | D5 named artefact = **0** |
| **DISC-05** | **High** | `coding_summary_v0_1_1.md` § "By dimension" | D5 commitment/partial/not-obs counts wrong | D5: 0 / 6 / 4 / 13 |
| **DISC-06** | **Medium** | `coding_summary_v0_1_1.md` § "By dimension" | Internal inconsistency: dimension breakdown does not aggregate to corpus-wide totals (e.g. commitment sum across dimensions = 47 vs corpus 37) | Use recomputed dimension matrix |
| **DISC-07** | **Informational** | `coding_summary_v0_1_1.md` | Corpus-wide evidence-status table is correct despite erroneous dimension breakdown | No manuscript impact if freeze used |

### Artefacts with zero discrepancies

| Artefact | Status |
|----------|--------|
| `coding_results_v0_1_1.csv` | Canonical source (recomputation base) |
| `coding_distribution_audit_v0_1_1.md` | Consistent |
| `pre_analysis_validity_check.md` | Consistent |
| `rq_analysis_v0_1.md` | Consistent |
| `result_claims_inventory.md` | Consistent |
| `findings_candidate_tables.md` | Consistent |
| `findings_candidate_figures.md` | Consistent |

---

## Cross-report consistency summary

| Check domain | Reports checked | Discrepancies |
|--------------|-----------------|---------------|
| Corpus totals | 8 | 0 |
| Evidence-status totals | 8 | 0 (corpus-wide) |
| Dimension totals | 8 | **6 cells in 1 artefact** (`coding_summary`) |
| Municipality totals | 5 | 0 |
| Source-type totals | 5 | 0 |
| Named-artefact inventory | 6 | 2 cells in `coding_summary` dimension table |
| RQ claims vs frequencies | `result_claims_inventory` | 0 |
| Candidate table cells | `findings_candidate_tables` | 0 |

**Overall audit outcome:** **Conditional pass.** All downstream analytical artefacts (distribution audit → pre-analysis → RQ analysis → claims/tables/figures) are mutually consistent and match the CSV. One upstream summary artefact (`coding_summary_v0_1_1.md`) contains an erroneous dimension breakdown and must not be used for manuscript numbers.

---

## Canonical source of truth (recommendation)

| Priority | Artefact | Role |
|----------|----------|------|
| **1 (primary)** | `data/processed/coding_results_v0_1_1.csv` | Machine-readable ground truth; all frequencies must be recomputed from this file |
| **2 (manuscript-facing)** | `outputs/reports/results_freeze_v1.md` | Human-readable frozen snapshot derived from CSV at audit time; use for all manuscript tables and in-text numerals |
| **3 (analytic narrative)** | `outputs/reports/rq_analysis_v0_1.md` | RQ-structured descriptive analysis; consistent with CSV |
| **4 (claims gate)** | `outputs/reports/result_claims_inventory.md` | Tier A/B/C claim inventory; consistent with freeze |
| **Deprecated for numerals** | `outputs/reports/coding_summary_v0_1_1.md` | Corpus-wide counts valid; **dimension table erroneous** — correct before citation or exclude |

**Recommended remediation (post-freeze, non-blocking):** Update `coding_summary_v0_1_1.md` dimension table to match `results_freeze_v1.md` §3.

---

## Manuscript freeze readiness

| Gate | Status |
|------|--------|
| CSV complete (115/115) | Pass |
| Downstream RQ chain consistent | Pass |
| Named-artefact inventory verified | Pass |
| Claims inventory aligned | Pass |
| Freeze document issued | See `results_freeze_v1.md` |
| Known discrepancies documented | 7 flags (6 in `coding_summary` dimension table) |

**Recommendation:** Proceed to manuscript drafting using **`results_freeze_v1.md`** numerals only.

---

## Related artefacts

| File | Role |
|------|------|
| [`results_freeze_v1.md`](results_freeze_v1.md) | Definitive values for manuscript |
| [`coding_results_v0_1_1.csv`](../../data/processed/coding_results_v0_1_1.csv) | Primary data |
| [`rq_analysis_v0_1.md`](rq_analysis_v0_1.md) | RQ narrative (consistent) |

---

## Not produced

- Manuscript text
- Discussion or conclusions
- Corrective edits to `coding_summary_v0_1_1.md` (flagged only)
