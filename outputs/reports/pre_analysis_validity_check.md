# Pre-analysis validity check

**Audit date:** 2026-06-08  
**Coding data:** [`data/processed/coding_results_v0_1_1.csv`](../../data/processed/coding_results_v0_1_1.csv)  
**Distribution audit:** [`coding_distribution_audit_v0_1_1.md`](coding_distribution_audit_v0_1_1.md)  
**Protocol:** v0.1.1

Validity review before RQ1–RQ3 analysis. This document assesses whether the coded observation set is structurally fit for descriptive research-question work. It does not answer the research questions or produce substantive findings.

---

## Recommendation

### **Proceed to RQ analysis**

Proceed with descriptive RQ analysis using the current `coding_results_v0_1_1.csv`, subject to the caveats documented below. Targeted recoding or protocol review is **not required** as a blocking step.

| Option | Assessment |
|--------|------------|
| **Proceed to RQ analysis** | **Selected** — coding is complete, protocol-consistent, and distribution patterns are structurally explainable |
| Perform targeted recoding | Optional future enhancement (register entry-level; committee bilag URLs); not blocking |
| Perform protocol review | Not indicated; v0.1.1 rules appear applied consistently |

---

## 1. Coding balance

| Check | Status | Notes |
|-------|--------|-------|
| Row completeness | Pass | 115/115 expected rows (23 sources × 5 dimensions) |
| Label validity | Pass | All labels in v0.1.1 four-status taxonomy |
| Dimension coverage | Pass | D1–D5 each have 23 rows |
| Municipality coverage | Pass | All six manifest municipalities represented |
| Status distribution usable | Pass with caveats | Heavy `not_observable_publicly` (43.5%) and sparse `observable_named_artifact` (2.6%) |

### Balance observations (descriptive, not findings)

- **D4** is structurally sparse: 78.3% `not_observable_publicly`, consistent with zero procurement documents in manifest v0.1.
- **mun-tallinn** contributes 15 rows all `not_observable_publicly` — manifest and retrieval constraint, not label imbalance across coders.
- **mun-vienna** contributes all three `observable_named_artifact` rows — reflects richer full-document sources (PDF legal notices, competence network naming).
- Non-`not_observable` rates vary by municipality row count and bot-gated share; RQ analysis should treat manifest source counts as descriptive denominators, not equal weights.

---

## 2. Category health

| Category type | Health | Detail |
|---------------|--------|--------|
| `observable_policy_commitment` | Healthy | 37 rows (32.2%); present across D1–D5 |
| `partial_or_indirect_signal` | Healthy | 25 rows (21.7%) |
| `not_observable_publicly` | Healthy but dominant | 50 rows (43.5%); expected for public-document observability study |
| `observable_named_artifact` | **Sparse but valid** | 3 rows (2.6%); D1-only; Vienna-only |
| D2–D5 × `observable_named_artifact` | **Empty** | Zero cells; see protocol-drift section |
| `procurement document` source type | **Absent** | Manifest gap; D4 analysis limited to non-procurement source types |

### Empty and near-empty flags

| Flag | Severity | Action for RQ phase |
|------|----------|---------------------|
| Zero `observable_named_artifact` in D2–D5 | Informational | Report as structural observability pattern; do not treat as coding error |
| Zero procurement source type | Informational | Scope D4 claims to available source types |
| mun-tallinn all `not_observable_publicly` | Informational | Document corpus retrieval/manifest limitation in methods |

---

## 3. Protocol drift risks

| Risk | Detected? | Evidence |
|------|-----------|----------|
| Inflation of `observable_named_artifact` | No | Only 3 rows; all have named unit + locator |
| Deflation via excessive `not_observable_publicly` on accessible text | Low | Barcelona/Vienna/Helsinki policy pages carry commitment labels |
| Register index rule over-applied | **Moderate** | 15 register rows, 0 named artifacts; entry-level coding not applied |
| Summary-page under-depth | **Moderate** | Barcelona protocol, Vienna portal, Tallinn landing coded at summary depth per rules |
| Bot-gated rows inflating `not_observable_publicly` | **Expected** | 20/50 not-observable rows from 4 bot-gated sources |
| D3 cap misapplied | Low | Principles pages capped at `observable_policy_commitment` consistently |
| Tie-break inconsistency | Low | Documented in `coding_decision_log_v0_1_1.md` |

**Overall drift risk:** Low-to-moderate. Patterns align with v0.1.1 conservative rules and manifest composition rather than systematic label misuse.

---

## 4. Readiness for RQ analysis

| Prerequisite | Ready? |
|--------------|--------|
| Complete coding matrix | Yes |
| Valid evidence-status taxonomy | Yes |
| Documented coding decisions | Yes (`coding_decision_log_v0_1_1.md`) |
| Distribution audit | Yes (this tranche) |
| Non-claims boundary preserved | Yes — audit contains no ranking or governance-quality inference |
| Known corpus constraints documented | Yes — bot-gated sources, missing procurement type, Tallinn sparsity |

### Caveats to carry into RQ analysis

1. **Do not treat municipality row counts as equal weights** — sources per municipality range from 2 to 6.
2. **Interpret D4 through manifest scope** — no procurement documents registered.
3. **`observable_named_artifact` is D1-concentrated** — cross-dimension named-artefact comparisons are structurally limited.
4. **Bot-gated and summary-depth rows** — document as observability boundary conditions, not missing data errors.
5. **Optional sensitivity work later** — entry-level register recoding or bilag retrieval would be a separate tranche, not a prerequisite.

---

## 5. `observable_named_artifact` validity summary

| Question | Audit answer |
|----------|--------------|
| Is 3/115 plausibly rare? | **Yes** — under register-level defaults, D3 cap, and absent procurement sources |
| Is under-assignment likely? | **Partial** — register entry pages and committee bilags may contain additional locatable artefacts, but current assignments follow v0.1.1 hierarchy rules |
| Does sparsity block RQ work? | **No** — RQ1–RQ3 concern observability and evidence gaps; sparse named artefacts are themselves a descriptive pattern |

---

## Artefacts

| File | Role |
|------|------|
| `outputs/reports/coding_distribution_audit_v0_1_1.md` | Full distribution tables |
| `outputs/reports/pre_analysis_validity_check.md` | This validity check |

---

## Not performed

- RQ1–RQ3 analysis
- Municipal ranking
- Paper text generation
- Recoding or protocol modification
