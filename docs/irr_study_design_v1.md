# Inter-rater reliability study design v1

**Date:** 2026-06-15  
**Scope:** Minimum viable IRR for GIQ review — existing corpus only, protocol v0.1.1  
**Frozen main results:** unchanged (`results_freeze_v1.md`)

---

## Executive recommendation

| Decision | Recommendation |
|----------|----------------|
| **Sampling** | **33%** stratified purposive subsample |
| **Unit** | **Document–dimension assessment** (one evidence-status label per cell) |
| **Primary statistic** | **Cohen's κ** (nominal, four evidence-status labels) |
| **Secondary statistic** | **Percent agreement** (exact) |
| **Sample size** | **8 documents → 40 assessments** (from retrieved-only pool) |
| **Estimated effort** | **9–11 researcher-hours** total |

---

## 1. Sampling strategy — recommend **33%**

### Options evaluated

| Option | Documents | Cells | Verdict |
|--------|-----------|-------|---------|
| 10% | 2–3 | 10–15 | **Indefensible** — κ unstable; cannot support pattern checks |
| 20% | 5 | 25 | **Weak** — below 30-cell convention; rare labels absent |
| 25% | 6 | 30 | **Borderline** — minimum only if stratification is perfect |
| **33%** | **8** | **40** | **Recommended** — best effort/impact trade-off |
| 50% | 12 | 60 | Strong but **diminishing returns** (~15+ coder-hours) |
| Full | 23 | 115 | **Unnecessary** for GIQ; duplicates main study |

### Justification

1. **Corpus size:** With 115 assessments, reviewers expect a **double-coded subsample**, not full duplication. Thirty-three percent yields **40 cells** — meeting the common **≥30 coded units** guidance for reporting κ meaningfully in content-analysis and documentary coding papers.

2. **Stratification over randomness:** A random 33% draw risks **zero algorithm registers** or **zero named-artefact exposure** (only three exist corpus-wide). **Purposive stratification** within the subsample is standard for small-N government-information corpora and is more defensible than naive random sampling.

3. **Retrieved-only restriction:** Four **bot-gated** documents (20 cells) are coded `not_observable_publicly` by retrieval rule, not by interpretive disagreement. Including them **inflates agreement artificially** and wastes coder time. The IRR universe is therefore the **19 retrieved documents**; **8 documents = 42% of retrieved corpus**, reported honestly as approximately one-third of the manifest while excluding retrieval-blocked rows.

4. **Editorial impact:** GIQ desk and reviewer files flag **single-coder design** as a **major-revision trigger**. A transparent κ on a **genre- and dimension-balanced** subsample directly addresses the highest-frequency methodological attack without re-freezing main numerals.

---

## 2. Unit of coding — recommend **document–dimension assessment**

| Option | Fit | Problem |
|--------|-----|---------|
| Document level | Poor | One document yields **five** distinct labels; aggregating collapses the unit of analysis used in Results |
| Dimension level | Partial | Five separate κ values obscure corpus-level protocol consistency; useful as **supplementary** only |
| **Document–dimension assessment** | **Best** | Matches Methods (115 assessments); one κ over all double-coded cells |

Each cell = one `municipality × source × dimension` decision using the v0.1.1 decision tree.

---

## 3. Statistics

### Primary: **Cohen's κ** (unweighted, nominal)

- Four evidence-status categories are **operationally nominal** (decision-tree branches, not a continuous scale).
- GIQ reviewers and government-information/content-analysis norms expect **κ + interpretation** (Landis & Koch, 1977).
- Report **asymptotic 95% CI** where software permits.

**Interpretation anchor:** κ ≥ 0.61 = substantial; κ ≥ 0.41 = moderate. Target **κ ≥ 0.70** on subsample; if lower, document reconciliation and tie-break audit.

### Secondary: **Percent agreement** (exact)

- Transparent complement when **prevalence skew** (43.5% not observable; 2.6% named artefacts) depresses κ.
- Report **agreement on observable vs not observable** (binary collapse) as a one-line sensitivity if κ is debated.

### Not primary (optional sensitivity)

| Statistic | Role |
|-----------|------|
| Weighted κ | Optional if disagreements cluster on adjacent categories (partial ↔ commitment) |
| Krippendorff's α | Stronger for ordinal/multi-coder extensions; cite if reviewer requests |
| Per-dimension κ | Supplementary table only — do not replace corpus-level κ |

---

## 4. Expected sample size

### Recommended draw

| Metric | Value |
|--------|-------|
| IRR universe | 19 retrieved documents (95 assessments) |
| Double-coded documents | **8** (42% of retrieved; ~33% of full manifest) |
| Double-coded cells | **40** |
| Municipalities represented | 5 of 6 (Amsterdam, Barcelona, Copenhagen, Helsinki, Vienna) |
| Source types represented | **All 6** present in manifest |

### Stratified document list (frozen for execution)

| # | Municipality | `source_type` | Rationale |
|---|--------------|---------------|-----------|
| 1 | Amsterdam | algorithm register | Register-level ambiguity (TB-5); D4 silence |
| 2 | Barcelona | governance framework | Commitment-rich protocol; D4 language |
| 3 | Barcelona | transparency portal | Portal genre; hub-page depth |
| 4 | Copenhagen | committee record | Committee-record depth rule |
| 5 | Helsinki | algorithm register | Second register genre; bilingual context |
| 6 | Helsinki | AI policy | Principles page; D3 cap rule |
| 7 | Vienna | AI strategy (PDF) | Named-artefact exposure (D1) |
| 8 | Vienna | governance framework | Framework genre; procurement references |

**Excluded by design:** all four bot-gated URLs; Tallinn ok-only source (optional ninth doc if reviewer demands six-city coverage — adds 5 cells, +2 hours).

### Power note

Forty cells will **not** re-estimate full-corpus frequencies with precision. The IRR study tests **coding consistency**, not pattern replication at population level. Pattern checks (Section 5) are **directional** within the subsample.

---

## 5. Pattern validation (within double-coded subset)

After reconciliation, compute **subsample descriptive profiles** using **Coder 1 frozen labels** (or consensus labels — report both if they diverge materially). Compare **direction**, not point equality, to full corpus.

### P1 — Commitment-heavy / artefact-thin

**Check:** Among observable cells, commitments + partials ≫ named artefacts.

| Full corpus (115) | Expected subsample (40, Coder 1) |
|-------------------|----------------------------------|
| 65 observable; 3 named (2.6%) | ~31 observable; 1 named |
| Commitments 56.9% of observable subset | Commitments dominate observable subset |

**Pass criterion:** Named artefacts ≤10% of observable subsample cells; commitments largest single status among observables.

### P2 — Downstream concentration

**Check:** D4 and D5 show highest not-observable shares among dimensions.

| Full corpus | Subsample (8 cells per dimension) |
|-------------|-----------------------------------|
| D4 78.3% not obs.; D5 56.5% | D4 62.5% not obs.; D5 37.5% (D1–D2 0%) |

**Pass criterion:** D4 not-observable share exceeds D1–D3; D4 + D5 rank in **top two** by not-observable share.

### P3 — Genre inversion

**Check:** Combined strategies + frameworks more observable than registers + portals.

| Full corpus | Subsample |
|-------------|-----------|
| SF 67.3% vs RP 42.9% observable | SF 93.3% vs RP 66.7% (Coder 1) |

**Pass criterion:** SF pooled observable % > RP pooled observable %; algorithm-register rows still show **zero** commitment/artefact labels.

**Reporting:** One sentence in Results: patterns remain **directionally visible** in the IRR subsample; IRR does not re-freeze main numerals.

---

## 6. Manuscript integration

### Methods (~80 words)

Add to `\subsection{Coding rules and execution}` or new `\subsubsection{Inter-rater reliability}`:

- Independent second coder
- v0.1.1 manual + decision rules
- 8 documents / 40 assessments stratified subsample
- Retrieved-only; excludes bot-gated rows
- Cohen's κ + percent agreement
- Reconciliation via published tie-break rules

### Results (~60 words)

New short paragraph or footnote in `\subsection{Robustness and Sensitivity Analysis}`:

- Report κ, percent agreement, n=40
- Patterns directionally stable in subsample
- Main tables remain single-coder full corpus

### Limitations (~40 words)

Revise single-coder sentence:

- From: no IRR reported
- To: IRR on stratified 40-cell subsample; full corpus remains single-coder; subsample does not support independent pattern inference

### Conclusion / future work

Remove or soften "second-coder replication" as **future** work if IRR completed.

---

## 7. Deliverables index

| ID | File |
|----|------|
| A | [`irr_second_coder_protocol_v1.md`](irr_second_coder_protocol_v1.md) |
| B | [`../data/processed/irr_coding_worksheet_template_v1.csv`](../data/processed/irr_coding_worksheet_template_v1.csv) |
| C | [`../outputs/reports/irr_analysis_workflow_v1.md`](../outputs/reports/irr_analysis_workflow_v1.md) |
| D | Hour estimates — Section 7 of this document |

---

## 7D. Estimated hours

| Task | Owner | Hours |
|------|-------|-------|
| Protocol briefing + manual review | Coder 2 | 1.0–1.5 |
| Independent coding (8 docs × ~35 min) | Coder 2 | 4.0–5.0 |
| Adjudication session (disagreements) | Both | 1.5–2.5 |
| Tie-break documentation + worksheet merge | Coder 1 | 0.5–1.0 |
| κ / agreement calculation + subsample pattern check | Coder 1 | 0.5–1.0 |
| Manuscript Methods/Results/Limitations text | Coder 1 | 0.5 |
| **Total** | | **9–11** |

**Effort reduction options (if needed):**

- Drop to **6 documents (30 cells)** → save ~2 h; accept higher reviewer risk
- Do **not** drop below 30 cells

---

## Reviewer-facing sentence (draft)

> Inter-rater reliability was assessed on a stratified subsample of 40 document–dimension assessments (eight retrieved documents, all six source types) coded independently by a second researcher using protocol v0.1.1 (Cohen's κ = [value]; percent agreement = [value]%). Directional pattern checks on the subsample were consistent with the full-corpus profiles reported above.

---

**Status:** Design only — execution pending second coder assignment.
