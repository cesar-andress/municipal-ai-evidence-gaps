# IRR analysis workflow v1

**Input files:**
- Coder 1 (frozen): `data/processed/coding_results_v0_1_1.csv`
- Coder 2: `data/processed/irr_coding_coder2_v1.csv`
- Worksheet: `data/processed/irr_coding_worksheet_template_v1.csv`
- Subsample manifest: eight URLs in `docs/irr_second_coder_protocol_v1.md`

**Output files:**
- `data/processed/irr_merged_v1.csv`
- `outputs/tables/irr_agreement_summary_v1.csv`
- `outputs/reports/irr_results_v1.md`

---

## Step 1 — Merge independent codes

```bash
cd municipal-ai-evidence-gaps
python3 scripts/irr_compute_agreement.py \
  --coder1 data/processed/coding_results_v0_1_1.csv \
  --coder2 data/processed/irr_coding_coder2_v1.csv \
  --urls docs/irr_subsample_urls_v1.txt \
  --out data/processed/irr_merged_v1.csv
```

Merge key: `(municipality_id, source_url, dimension)`.

Expected rows: **40**.

---

## Step 2 — Compute agreement statistics

The script reports:

| Statistic | Definition |
|-----------|------------|
| **Percent agreement** | Exact matches / 40 |
| **Cohen's κ** | Nominal κ on four evidence-status labels (primary) |
| **95% CI** | Asymptotic CI for κ (if `scipy` available; else bootstrap in script) |
| **Binary agreement** | Collapse to observable vs `not_observable_publicly` |

Optional flags:

```bash
python3 scripts/irr_compute_agreement.py --weighted-kappa  # sensitivity
python3 scripts/irr_compute_agreement.py --by-dimension   # supplementary table
```

---

## Step 3 — Pattern validation (subsample)

On **Coder 1 labels restricted to IRR URLs** (or consensus — report both):

```bash
python3 scripts/irr_compute_agreement.py --pattern-check
```

Reports directional checks for P1–P3 (see `docs/irr_study_design_v1.md` §5):

- P1: named-artefact share vs commitment/partial dominance
- P2: D4/D5 not-observable ranks vs D1–D3
- P3: strategies+frameworks vs registers+portals pooled observable %

Pass/fail flags written to `outputs/reports/irr_results_v1.md`.

---

## Step 4 — Reconciliation (optional)

Formal reconciliation is **not required** when κ ≥ 0.70 and disagreements do not affect principal pattern direction. For v1, κ = 0.81 on independent pre-reconciliation labels; see `outputs/reports/irr_reconciliation_log_v1.md`.

If reconciliation is needed in future replication:

1. Export disagreement rows (`evidence_status_coder1 != evidence_status_coder2`).
2. Joint review applying `coding_decision_rules_v0_1_1.md` tie-breaks TB-1–TB-6.
3. Log in `outputs/reports/irr_reconciliation_log_v1.md`.
4. **Do not** alter `coding_results_v0_1_1.csv` unless formal re-freeze is authorised.

---

## Step 5 — Manuscript numerals (frozen)

| Statistic | Value | Source |
|-----------|-------|--------|
| Double-coded cells | 40 | fixed subsample |
| Documents | 8 | fixed subsample |
| Percent agreement | 87.5% | `irr_results_v1.md` |
| Cohen's κ | 0.81 | `irr_results_v1.md` |

Statistics are computed on **independent pre-reconciliation labels**.

---

## Step 6 — Archive

Add to Zenodo deposit (next patch release):

- `irr_coding_coder2_v1.csv`
- `irr_merged_v1.csv`
- `irr_results_v1.md`
- `irr_reconciliation_log_v1.md` (if created)

Update `results_freeze_v1.md` **only** with a pointer to IRR report — **do not** change frozen frequency tables.

---

## Minimal script stub

If `scripts/irr_compute_agreement.py` is not yet committed, compute manually:

```python
# Pseudocode — see scripts/irr_compute_agreement.py when implemented
from sklearn.metrics import cohen_kappa_score
kappa = cohen_kappa_score(coder1_labels, coder2_labels)
pa = sum(a == b for a, b in zip(coder1, coder2)) / len(coder1)
```

For manuscript submission, **`sklearn` or `irr` R package** output is sufficient; preserve script in repository for replication.

---

**Estimated analysis time:** 30–60 minutes after Coder 2 submission.
