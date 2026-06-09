# Bot-gated sensitivity check v0.1

**Check date:** 2026-06-08  
**Type:** Robustness / sensitivity analysis — **does not replace frozen main results**  
**Protocol:** v0.1.1 (unchanged)  
**Frozen reference:** [`results_freeze_v1.md`](results_freeze_v1.md)  
**Primary data:** [`data/processed/coding_results_v0_1_1.csv`](../../data/processed/coding_results_v0_1_1.csv)  
**Manifest:** [`data/processed/corpus_manifest_v0_1.csv`](../../data/processed/corpus_manifest_v0_1.csv)

---

## Status and scope

| Item | Value |
|------|-------|
| **Purpose** | Test whether main observability patterns are driven by `bot_gated` manifest sources |
| **Sensitivity rule** | Exclude all manifest rows with `retrieval_status = bot_gated` |
| **Main results** | **Unchanged** — manuscript tables, figures, numerals, and `results_freeze_v1.md` remain authoritative |
| **Manuscript denominators** | **Remain 115 coding rows / 23 sources** (frozen) |

### Sensitivity datasets (derived; not frozen)

| File | Rows / sources |
|------|----------------|
| [`data/processed/corpus_manifest_v0_1_sensitivity_ok_only.csv`](../../data/processed/corpus_manifest_v0_1_sensitivity_ok_only.csv) | 19 sources |
| [`data/processed/coding_results_v0_1_1_sensitivity_ok_only.csv`](../../data/processed/coding_results_v0_1_1_sensitivity_ok_only.csv) | 95 coding rows (19 × 5) |

### Excluded `bot_gated` sources (4 sources; 20 coding rows)

| Municipality | `source_type` | URL (abbrev.) |
|--------------|---------------|---------------|
| Amsterdam | transparency portal | `amsterdam.nl/.../algoritmes-ai/` |
| Amsterdam | AI policy | `amsterdam.nl/.../amsterdamse-visie-ai/` |
| Tallinn | governance framework | `tallinn.ee/.../betti` |
| Tallinn | transparency portal | `tallinn.ee/.../tallinn-digital-twin` |

All 20 excluded coding rows are `not_observable_publicly` under protocol retrieval rules.

---

## 1. Corpus scope comparison

| Field | Frozen main | Sensitivity (ok-only) | Δ |
|-------|-------------|----------------------|---|
| Manifest sources | 23 | 19 | −4 |
| Coding decisions | 115 | 95 | −20 |
| `bot_gated` sources | 4 | 0 | −4 |
| `ok` sources | 19 | 19 | 0 |

---

## 2. Corpus-wide evidence-status distribution

| `evidence_status` | Frozen n | Frozen % (of 115) | Sensitivity n | Sensitivity % (of 95) | n Δ |
|-------------------|----------|-------------------|---------------|----------------------|-----|
| `not_observable_publicly` | 50 | 43.5% | 30 | 31.6% | −20 |
| `observable_policy_commitment` | 37 | 32.2% | 37 | 38.9% | 0 |
| `partial_or_indirect_signal` | 25 | 21.7% | 25 | 26.3% | 0 |
| `observable_named_artifact` | 3 | 2.6% | 3 | 3.2% | 0 |

| Derived metric | Frozen | Sensitivity | Stable? |
|----------------|--------|-------------|---------|
| Observable rows (non-`not_observable`) | 65 (56.5%) | 65 (68.4%) | **Counts stable; % shifts** |
| Commitment-dominant observable profile | Yes | Yes | **Yes** |

**Interpretation:** Excluding bot-gated rows removes 20 `not_observable_publicly` labels only. The commitment-heavy observable composition is **unchanged in absolute terms**.

---

## 3. D1–D5 × evidence-status (sensitivity denominators = 19 rows/dimension)

| Dimension | Metric | Frozen (23 rows) | Sensitivity (19 rows) | Change |
|-----------|--------|------------------|----------------------|--------|
| **D1** | Not obs. | 6 (26.1%) | 2 (10.5%) | ↓ pp; not systematic either way |
| **D2** | Not obs. | 5 (21.7%) | 1 (5.3%) | ↓ pp |
| **D3** | Not obs. | 8 (34.8%) | 4 (21.1%) | ↓ pp |
| **D4** | Not obs. | 18 (78.3%) | 14 (73.7%) | ↓ 4.6 pp; **still >50%** |
| **D5** | Not obs. | 13 (56.5%) | 9 (47.4%) | ↓ 9.1 pp; **falls below 50%** |

### D4 / D5 systematic under-observability (>50% not obs.)

| Dimension | Frozen | Sensitivity | Classification |
|-----------|--------|-------------|----------------|
| **D4** | **Yes** (78.3%) | **Yes** (73.7%) | **Stable** |
| **D5** | **Yes** (56.5%) | **No** (47.4%) | **Material change** |

Named-artefact rows remain 3 (all D1; all Vienna); zero in D2–D5 in both runs.

---

## 4. Municipality profiles

| Municipality | Frozen sources / rows | Sens. sources / rows | Frozen observable | Sens. observable | Qualitative shift |
|--------------|-------------------------|----------------------|-------------------|------------------|-------------------|
| Amsterdam | 3 / 15 | 1 / 5 | 4 | 4 | Share ↑; bot-gated rows removed |
| Barcelona | 4 / 20 | 4 / 20 | 19 | 19 | **Unchanged** |
| Copenhagen | 2 / 10 | 2 / 10 | 8 | 8 | **Unchanged** |
| Helsinki | 5 / 25 | 5 / 25 | 13 | 13 | **Unchanged** |
| Tallinn | 3 / 15 | 1 / 5 | 0 | 0 | Still **zero observable** on ok-only source |
| Vienna | 6 / 30 | 6 / 30 | 21 | 21 | **Unchanged** |

| Municipality | Frozen not obs. | Sens. not obs. |
|--------------|-----------------|----------------|
| Amsterdam | 11 | 1 |
| Barcelona | 1 | 1 |
| Copenhagen | 2 | 2 |
| Helsinki | 12 | 12 |
| Tallinn | 15 | 5 |
| Vienna | 9 | 9 |

**Interpretation:** Amsterdam and Tallinn profiles are **retrieval-composition sensitive**; four municipalities are **unchanged** under ok-only filtering.

---

## 5. Source-type profiles

| `source_type` | Frozen total rows | Sens. rows | Frozen obs. % | Sens. obs. % | Frozen not obs. | Sens. not obs. |
|---------------|-------------------|------------|---------------|--------------|-----------------|----------------|
| AI strategy | 25 | 25 | 76.0% | 76.0% | 6 | 6 |
| governance framework | 30 | 25 | 60.0% | 72.0% | 12 | 7 |
| committee record | 10 | 10 | 70.0% | 70.0% | 3 | 3 |
| algorithm register | 15 | 15 | 53.3% | 53.3% | 7 | 7 |
| AI policy | 15 | 10 | 40.0% | 60.0% | 9 | 4 |
| transparency portal | 20 | 10 | 35.0% | 70.0% | 13 | 3 |

**Stable (counts and obs. %):** AI strategy, committee record, algorithm register.  
**Retrieval-composition sensitive:** governance framework, AI policy, transparency portal (row totals drop because excluded sources were bot-gated and all `not_observable_publicly`).

---

## 6. Comparison summary vs `results_freeze_v1.md`

| Pattern | Frozen main result | Sensitivity (ok-only) | Verdict |
|---------|-------------------|----------------------|---------|
| Commitment-dominant observable profile | 37 commitment / 25 partial / 3 named | **Identical counts** | **Stable** |
| Corpus observable row count | 65 / 115 | 65 / 95 | **Stable count** |
| D4 systematic under-observability | Yes (78.3%) | Yes (73.7%) | **Stable** |
| D5 systematic under-observability | Yes (56.5%) | No (47.4%) | **Material change** |
| Tallinn zero-observable profile | Yes (0/15) | Yes (0/5) | **Stable** |
| Bot-gated share of not-observable rows | 20/50 (40%) | — | Confirms exclusion mechanism |

---

## 7. Effect classification

### Overall: **Minor change** (with one **material** localized exception)

| Level | Assessment |
|-------|------------|
| **Primary RQ1 pattern** (commitment-heavy observability) | **No substantive change** — absolute status counts unchanged |
| **RQ2 D4** | **No substantive change** — remains systematically under-observable |
| **RQ2 D5** | **Material change** — systematic under-observability **not** replicated under ok-only filter |
| **RQ3 municipality/source contrasts** | **Minor change** — four municipalities unchanged; Amsterdam/Tallinn and three source types shift when bot-gated rows removed |
| **Manuscript main tables/figures** | **Do not update** — frozen denominators remain 115 / 23 |

### Major issue flag

> **D5 systematic under-observability (56.5% → 47.4%) is sensitive to inclusion of bot-gated rows.**  
> Do **not** revise frozen results, Results tables, or Discussion claims without a formal re-freeze decision.  
> Report this sensitivity transparently (appendix / limitations cross-reference).

---

## 8. Proposed appendix sentence (not inserted automatically)

```text
Robustness check (ok-only sensitivity): excluding four bot-gated manifest sources (20 coding rows, all not_observable_publicly), observable evidence-status counts were unchanged (65 rows); the commitment-dominant profile and D4 systematic under-observability persisted (73.7% not observable across 19 ok-only rows per dimension); D5 not-observable share fell to 47.4%, below the study's 50% systematic threshold—indicating that bot-gated retrieval affects D5 classification but not the core commitment-heavy observable composition or D4 evidence gap.
```

---

## 9. Reproducibility

Recompute from repository root:

```bash
python3 - <<'PY'
# Uses coding_results_v0_1_1.csv + corpus_manifest_v0_1.csv
# Excludes source_url where manifest retrieval_status == bot_gated
# See data/processed/*_sensitivity_ok_only.csv for derived inputs
PY
```

Derived CSVs committed alongside this report.

---

**Check complete.** Frozen main results remain authoritative for the manuscript.
