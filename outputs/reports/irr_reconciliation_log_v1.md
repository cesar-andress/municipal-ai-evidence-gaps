# IRR reconciliation log v1

**Date:** 2026-06-15  
**Protocol:** v0.1.1  
**Subsample:** 8 documents; 40 document--dimension assessments  
**Primary statistic:** Cohen's κ on **independent pre-reconciliation labels**

---

## Summary

| Field | Value |
|-------|-------|
| Disagreements | 5 / 40 cells (12.5%) |
| Percent agreement | 87.5% |
| Cohen's κ | 0.81 |
| Reconciliation required? | **No** — κ exceeds the study review threshold (0.70) |

Agreement statistics reported in the manuscript (`sections/04_method.tex`, `sections/05_results.tex`) are computed on **independent coder labels before reconciliation**, per `docs/irr_study_design_v1.md` and `outputs/reports/irr_analysis_workflow_v1.md`.

Formal consensus reconciliation was **not performed** because:

1. κ = 0.81 supports protocol consistency for submission reporting.
2. Disagreements clustered on commitment--partial and partial--non-observable boundaries (TB-2, TB-3), not on the three principal empirical patterns.
3. The frozen main corpus (`coding_results_v0_1_1.csv`) remains unchanged.

---

## Disagreement cells

| irr_id | Municipality | Source type | Dimension | Coder 1 | Coder 2 | Notes |
|--------|--------------|-------------|-----------|---------|---------|-------|
| IRR-008 | Barcelona | governance framework | D3 | partial | commitment | TB-3 boundary |
| IRR-012 | Barcelona | transparency portal | D2 | partial | not_observable | TB-2 boundary |
| IRR-018 | Copenhagen | committee record | D3 | partial | commitment | TB-3 boundary |
| IRR-027 | Helsinki | AI policy | D2 | commitment | partial | TB-1 boundary |
| IRR-035 | Vienna | governance framework | D5 | partial | not_observable | TB-2 boundary |

---

## Workflow note

If future replication requires consensus labels, apply `coding_decision_rules_v0_1_1.md` tie-breaks TB-1–TB-6 and record outcomes in an updated reconciliation log. Do **not** alter `coding_results_v0_1_1.csv` without a formal re-freeze.

**Source worksheet:** `data/processed/irr_coding_worksheet_v1.csv`  
**Merged output:** `data/processed/irr_merged_v1.csv`  
**Compute script:** `scripts/irr_compute_agreement.py`
