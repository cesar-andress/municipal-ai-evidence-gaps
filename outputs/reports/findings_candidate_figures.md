# Findings candidate figures

**Derived from:** [`rq_analysis_v0_1.md`](rq_analysis_v0_1.md)  
**Coding data:** `coding_results_v0_1_1.csv` (n = 115)  
**Date:** 2026-06-08

Candidate figures for manuscript integration. Specification only — no rendered graphics in this artefact.

---

## Figure 1 — Stacked bar: evidence-status by dimension

| Field | Value |
|-------|-------|
| **Title** | Evidence-status composition by observability dimension |
| **Type** | Stacked bar chart (vertical) |
| **X-axis** | D1–D5 (dimension labels) |
| **Y-axis** | Count of coding rows (max 23 per bar) |
| **Stacks** | Four `evidence_status` categories (colour-coded): observable_named_artifact; observable_policy_commitment; partial_or_indirect_signal; not_observable_publicly |
| **Data source** | Table 3 in `findings_candidate_tables.md` |
| **Rationale** | Primary visual for RQ1/RQ2; shows D4/D5 bars dominated by not-observable segment and absence of named-artefact segments in D2–D5. |

**Suggested stack order (bottom to top):** not_observable → partial → commitment → named artefact

---

## Figure 2 — Stacked bar: evidence-status by source type

| Field | Value |
|-------|-------|
| **Title** | Evidence-status composition by manifest source type |
| **Type** | Stacked bar chart (horizontal preferred for long labels) |
| **Y-axis** | Source type (6 categories) |
| **X-axis** | Coding-row count per type (10–30) |
| **Stacks** | Four evidence-status categories |
| **Data source** | Table 5 |
| **Rationale** | RQ3 document-type pattern figure; contrasts strategy/governance-framework richness with portal/register profiles. |

---

## Figure 3 — Stacked bar: evidence-status by municipality

| Field | Value |
|-------|-------|
| **Title** | Evidence-status composition by municipality (coding-row basis) |
| **Type** | Stacked bar chart (vertical) |
| **X-axis** | Six municipalities (alphabetical or manifest order) |
| **Y-axis** | Coding-row count (10–30; **not equal**) |
| **Stacks** | Four evidence-status categories |
| **Annotation** | Subtitle or note: row counts reflect manifest source multiplicity |
| **Data source** | Table 6 |
| **Rationale** | RQ3 municipality-profile figure; visualises Tallinn all-not-observable and Barcelona/Vienna observable-heavy profiles **without ranking**. |

**Caption constraint:** Do not label municipalities as "leading" or "lagging."

---

## Figure 4 — Heatmap: municipality × dimension (not-observable counts)

| Field | Value |
|-------|-------|
| **Title** | Public under-observability heatmap: municipality by dimension |
| **Type** | Heatmap (6 × 5) |
| **Rows** | Municipalities |
| **Columns** | D1–D5 |
| **Cell value** | Count of `not_observable_publicly` rows (0–3) |
| **Colour scale** | Sequential (0 = light; 3 = dark) |
| **Data source** | Table 7 |
| **Rationale** | RQ3 gap-pattern figure; highlights Helsinki D4/D5 concentration and Tallinn uniform non-observability. |

---

## Figure 5 — Heatmap: source type × dimension (observable counts)

| Field | Value |
|-------|-------|
| **Title** | Observable evidence heatmap: source type by dimension |
| **Type** | Heatmap (6 × 5) |
| **Rows** | Source types |
| **Columns** | D1–D5 |
| **Cell value** | Count of non-`not_observable_publicly` rows (0–5) |
| **Colour scale** | Sequential (0 = light; 5 = dark) |
| **Data source** | Table 8 |
| **Rationale** | Shows which document types supply observable evidence to which dimensions; D4 column expected pale across rows. |

---

## Figure 6 — Dimension × evidence-status matrix (corpus share)

| Field | Value |
|-------|-------|
| **Title** | Dimension–evidence-status matrix (row-normalised percentages) |
| **Type** | Heatmap or tile matrix |
| **Rows** | D1–D5 |
| **Columns** | Four evidence-status labels |
| **Cell value** | Percentage within dimension row (sums to 100% per row) |
| **Data source** | Table 3 (normalised) |
| **Rationale** | Complements Figure 1 with proportional view; emphasises D4 78.3% not-observable and D2/D3 commitment dominance among observable rows. |

---

## Figure 7 — Stacked bar: observable vs not-observable (corpus-wide)

| Field | Value |
|-------|-------|
| **Title** | Share of coding rows with any public observable evidence |
| **Type** | Single stacked bar or donut |
| **Segments** | Observable (65 rows; 56.5%) vs not_observable_publicly (50 rows; 43.5%) |
| **Sub-segment (optional)** | Observable split: commitment / partial / named artefact |
| **Rationale** | High-level RQ1 summary figure for introduction to results. |

---

## Figure priority for manuscript

| Priority | Figure | RQ |
|----------|--------|-----|
| 1 | Figure 1 (dimension stacked bar) | RQ1, RQ2 |
| 2 | Figure 4 (municipality × dimension heatmap) | RQ3 |
| 3 | Figure 2 (source type stacked bar) | RQ3 |
| 4 | Figure 5 (source type × dimension heatmap) | RQ3 |
| 5 | Figure 6 (dimension × status matrix) | RQ2 |
| 6 | Figure 3 (municipality stacked bar) | RQ3 |
| 7 | Figure 7 (corpus observable share) | RQ1 |

---

## Rendering notes

- Use colourblind-safe palette for four evidence-status categories
- Exclude municipality ranking annotations
- Include n=115 and v0.1.1 protocol footnote on all figures
- Mark bot-gated and absent source-type constraints in Figure 3/4 captions
