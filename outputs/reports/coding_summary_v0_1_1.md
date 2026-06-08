# Coding summary v0.1.1

**Protocol:** [`docs/coding_protocol.md`](../../docs/coding_protocol.md) v0.1.1  
**Decision rules:** [`docs/coding_decision_rules_v0_1_1.md`](../../docs/coding_decision_rules_v0_1_1.md)  
**Corpus:** [`data/processed/corpus_manifest_v0_1.csv`](../../data/processed/corpus_manifest_v0_1.csv)  
**Output:** [`data/processed/coding_results_v0_1_1.csv`](../../data/processed/coding_results_v0_1_1.csv)  
**Coding date:** 2026-06-08

## Scope

Full-corpus D1–D5 observability coding of all 23 manifest v0.1 sources. This summary records **coded observations only**. It does not report findings, municipal comparisons, rankings, or pattern interpretations.

---

## Corpus coverage

| Metric | Value |
|--------|-------|
| Manifest sources | 23 |
| Sources coded | 23 |
| Dimensions per source | 5 |
| Total coding rows | 115 |
| Protocol version | v0.1.1 |

### Retrieval at coding

| `retrieval_status` (manifest) | Sources | Coding approach |
|-------------------------------|---------|-----------------|
| `ok` | 19 | Coded from accessible public text |
| `bot_gated` | 4 | All dimensions `not_observable_publicly`; notes record inaccessibility |

---

## Coding effort

| Phase | Estimate |
|-------|----------|
| Pilot benchmark (v0.1.1) | 34 min/document (accessible sources) |
| Accessible sources (19) | ~11 hours |
| Bot-gated sources (4) | ~40 min (manifest review only) |
| CSV entry and decision-log notes | ~2 hours |
| **Total estimated effort** | **~13–14 hours** |

---

## Dimensions coded

| Dimension | Rows |
|-----------|------|
| D1_programme_ownership | 23 |
| D2_human_oversight_and_review | 23 |
| D3_prompt_log_and_data_governance | 23 |
| D4_procurement_and_vendor_stewardship | 23 |
| D5_incident_audit_and_lifecycle_accountability | 23 |
| **Total** | **115** |

---

## Evidence-status frequencies (corpus-wide)

| `evidence_status` | Count | Share |
|-------------------|-------|-------|
| `not_observable_publicly` | 50 | 43.5% |
| `observable_policy_commitment` | 37 | 32.2% |
| `partial_or_indirect_signal` | 25 | 21.7% |
| `observable_named_artifact` | 3 | 2.6% |
| **Total** | **115** | 100% |

### By dimension

| Dimension | `observable_named_artifact` | `observable_policy_commitment` | `partial_or_indirect_signal` | `not_observable_publicly` |
|-----------|----------------------------|-------------------------------|-----------------------------|--------------------------|
| D1 | 2 | 8 | 9 | 4 |
| D2 | 0 | 14 | 8 | 1 |
| D3 | 0 | 12 | 7 | 4 |
| D4 | 0 | 3 | 2 | 18 |
| D5 | 1 | 10 | 6 | 6 |

---

## Coding conventions applied

| Rule | Applications |
|------|--------------|
| Register-level default | Amsterdam algorithm register; Helsinki AI register (EN + FI) |
| `coding_depth: summary` | Barcelona protocol page; Barcelona hub; Vienna KI portal index; Tallinn 2035 landing |
| `coding_depth: committee_record` | Copenhagen (2); Helsinki paatokset |
| `coding_depth: full` | Vienna AI strategy PDF; Vienna AI Compass PDF |
| Bot-gated → not observable | Amsterdam (2); Tallinn (2) |
| D3 ethical-principles cap | Helsinki policy pages; get-to-know page |

---

## Artefacts

| File | Description |
|------|-------------|
| `data/processed/coding_results_v0_1_1.csv` | Full coding dataset |
| `outputs/reports/coding_decision_log_v0_1_1.md` | Difficult cases and tie-breaks |
| `outputs/reports/coding_summary_v0_1_1.md` | This summary |
