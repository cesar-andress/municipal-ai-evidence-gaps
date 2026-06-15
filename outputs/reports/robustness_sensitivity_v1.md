# Robustness and sensitivity analysis v1

**Analysis date:** 2026-06-15  
**Type:** Robustness / sensitivity — **does not replace frozen main results**  
**Protocol:** v0.1.1 (unchanged)  
**Frozen reference:** [`results_freeze_v1.md`](results_freeze_v1.md)  
**Primary data:** [`data/processed/coding_results_v0_1_1.csv`](../../data/processed/coding_results_v0_1_1.csv)  
**Manifest:** [`data/processed/corpus_manifest_v0_1.csv`](../../data/processed/corpus_manifest_v0_1.csv)  
**Reproducibility script:** [`scripts/sensitivity_analysis.py`](../../scripts/sensitivity_analysis.py)

---

## Executive summary

| Pattern | Full corpus (115 rows) | Retrieved-only (95 rows) | Verdict |
|---------|------------------------|--------------------------|---------|
| **P1** Commitment-heavy / artefact-thin | 65 observable; 3 named artefacts (2.6%); commitments dominate observable subset (56.9%) | **Identical** observable counts (65; 37 commit / 25 partial / 3 named); named share 3.2% of 95 | **Stable** |
| **P2** Downstream concentration | D4 and D5 weakest dimensions (21.7% / 43.5% observable); D4 78.3% not obs; D5 56.5% not obs | D4 and D5 **remain weakest** (26.3% / 52.6% observable); D4 73.7% not obs (**>50% threshold**); D5 47.4% not obs (**below 50% threshold**) | **Partially stable** — gradient rank order unchanged; D5 formal classification sensitive |
| **P3** Genre inversion | Strategies + frameworks 67.3% observable (37/55); registers + portals 42.9% (15/35) | Strategies + frameworks 74.0% (37/50); registers + portals 60.0% (15/25) | **Stable** — inversion holds; gap narrows 24.4 → 14.0 pp |

**Manuscript main tables remain frozen at 115 rows / 23 sources.** This analysis supplements Limitations and optionally a short Results robustness subsection.

---

## A. Retrieved-only corpus

### Sensitivity rule

Exclude all 20 document--dimension assessments originating from four manifest sources with `retrieval_status = bot_gated`. All excluded rows are `not_observable_publicly` under protocol retrieval rules.

| Excluded source | Municipality | `source_type` |
|-----------------|--------------|---------------|
| Algoritmes en AI | Amsterdam | transparency portal |
| Amsterdamse Visie op AI | Amsterdam | AI policy |
| BETTI trustworthy GenAI | Tallinn | governance framework |
| Tallinn Digital Twin | Tallinn | transparency portal |

### Corpus scope

| Field | Full corpus | Retrieved-only | Δ |
|-------|-------------|----------------|---|
| Manifest sources | 23 | 19 | −4 |
| Doc.--dimension assessments | 115 | 95 | −20 |
| `ok` sources | 19 | 19 | 0 |
| `bot_gated` sources | 4 | 0 | −4 |

Derived files: [`coding_results_v0_1_1_sensitivity_ok_only.csv`](../../data/processed/coding_results_v0_1_1_sensitivity_ok_only.csv), [`corpus_manifest_v0_1_sensitivity_ok_only.csv`](../../data/processed/corpus_manifest_v0_1_sensitivity_ok_only.csv).

### Table A1 — Evidence-status distribution

| `evidence_status` | Full *n* | Full % | Retrieved-only *n* | Retrieved-only % | *n* Δ |
|-------------------|----------|--------|--------------------|------------------|-------|
| `not_observable_publicly` | 50 | 43.5 | 30 | 31.6 | −20 |
| `observable_policy_commitment` | 37 | 32.2 | 37 | 38.9 | 0 |
| `partial_or_indirect_signal` | 25 | 21.7 | 25 | 26.3 | 0 |
| `observable_named_artifact` | 3 | 2.6 | 3 | 3.2 | 0 |
| **Any observable** | **65** | **56.5** | **65** | **68.4** | **0** |

CSV: [`outputs/tables/sensitivity_corpus_summary_v1.csv`](../tables/sensitivity_corpus_summary_v1.csv)

### Table A2 — Dimension-level distributions

| Dimension | Full obs. % | Full not obs. % | Full >50% rule | Retr.-only obs. % | Retr.-only not obs. % | Retr.-only >50% rule | Rank (weakest obs.) |
|-----------|-------------|-----------------|----------------|-------------------|----------------------|----------------------|---------------------|
| D1 | 73.9 | 26.1 | No | 89.5 | 10.5 | No | — |
| D2 | 78.3 | 21.7 | No | 94.7 | 5.3 | No | — |
| D3 | 65.2 | 34.8 | No | 78.9 | 21.1 | No | — |
| D4 | 21.7 | 78.3 | **Yes** | 26.3 | 73.7 | **Yes** | **1st weakest (both)** |
| D5 | 43.5 | 56.5 | **Yes** | 52.6 | 47.4 | No | **2nd weakest (both)** |

**Rank orderings (observable %, ascending = weakest first):**  
- Full: D4 → D5 → D3 → D1 → D2 — **unchanged** in retrieved-only: D4 → D5 → D3 → D1 → D2  
- Not-observable % (descending): D4 → D5 → D3 → D1 → D2 — **unchanged**

CSV: [`outputs/tables/sensitivity_dimension_summary_v1.csv`](../tables/sensitivity_dimension_summary_v1.csv)

### Table A3 — Document-type distributions

| `source_type` | Full rows | Full obs. % | Retr.-only rows | Retr.-only obs. % | Rank change |
|---------------|-----------|-------------|-----------------|-------------------|-------------|
| AI strategy | 25 | 76.0 | 25 | 76.0 | No |
| committee record | 10 | 70.0 | 10 | 70.0 | No |
| governance framework | 30 | 60.0 | 25 | 72.0 | % shifts; rows −5 |
| algorithm register | 15 | 53.3 | 15 | 53.3 | No |
| AI policy | 15 | 40.0 | 10 | 60.0 | % shifts; rows −5 |
| transparency portal | 20 | 35.0 | 10 | 70.0 | % shifts; rows −10 |

**Source-type rank by observable % (full):** AI strategy → committee record → governance framework → algorithm register → AI policy → transparency portal  

**Source-type rank (retrieved-only):** AI strategy → governance framework → transparency portal → committee record → AI policy → algorithm register  

**Rank order changes** for middle tiers because excluded bot-gated rows were exclusively `not_observable_publicly` for governance framework (−5), AI policy (−5), and transparency portal (−10). **Algorithm register rank relative to normative genres is unchanged** (still below AI strategy and governance framework).

CSV: [`outputs/tables/sensitivity_source_type_summary_v1.csv`](../tables/sensitivity_source_type_summary_v1.csv)

---

## B. Bot-gated exclusion — pattern comparison

CSV: [`outputs/tables/sensitivity_pattern_comparison_v1.csv`](../tables/sensitivity_pattern_comparison_v1.csv)

### P1 — Commitment-heavy / artefact-thin profile

| Metric | Full corpus | Retrieved-only | Interpretation |
|--------|-------------|----------------|----------------|
| Observable assessments | 65 / 115 (56.5%) | 65 / 95 (68.4%) | Count **stable**; share rises because only non-observable rows removed |
| Policy commitments | 37 (32.2%) | 37 (38.9%) | **Stable** |
| Partial signals | 25 (21.7%) | 25 (26.3%) | **Stable** |
| Named artefacts | 3 (2.6%) | 3 (3.2%) | **Stable** — all D1 / Vienna |
| Commitments as % of observable subset | 56.9% | 56.9% | **Stable** |
| Named as % of observable subset | 4.6% | 4.6% | **Stable** |

**Substantive interpretation:** P1 is **not driven by bot-gated retrieval**. Excluding contaminating cases removes silence labels only; the commitment-heavy, artefact-thin epistemic profile persists in absolute terms.

### P2 — Downstream concentration pattern

| Metric | Full corpus | Retrieved-only | Interpretation |
|--------|-------------|----------------|----------------|
| Weakest dimensions (observable %) | D4 (21.7%), D5 (43.5%) | D4 (26.3%), D5 (52.6%) | **Rank order stable** |
| Highest not-observable dimensions | D4 (78.3%), D5 (56.5%) | D4 (73.7%), D5 (47.4%) | **Rank order stable** |
| D4 >50% systematic threshold | Yes | Yes | **Stable** |
| D5 >50% systematic threshold | Yes | No | **Threshold-sensitive** |

**Substantive interpretation:** The **downstream gradient** (D4 and D5 concentrate the thinnest evidence) **persists** after exclusion. D4 procurement stewardship remains systematically under-observable under the study's majority rule. D5 lifecycle accountability **remains the second-weakest dimension** but its 56.5% not-observable share **falls to 47.4%** when bot-gated rows are removed—because 20% of all not-observable rows (4/20 per dimension across bot-gated sources) were retrieval-conditioned rather than content-coded silence on retrieved text.

### P3 — Genre inversion pattern

| Group | Full observable % (*n*) | Retrieved-only observable % (*n*) | Gap (pp) |
|-------|---------------------------|-----------------------------------|----------|
| AI strategies + governance frameworks | 67.3% (37/55) | 74.0% (37/50) | — |
| Algorithm registers + transparency portals | 42.9% (15/35) | 60.0% (15/25) | — |
| **Inversion (SF minus RP)** | **+24.4 pp** | **+14.0 pp** | Narrower but **positive** |

| Detail | Full | Retrieved-only |
|--------|------|----------------|
| Registers: commitment / named rows | 0 / 0 (15 rows) | 0 / 0 (15 rows) | **Stable** |
| Portals: commitment rows | 5 | 5 | **Stable** |

CSV: [`outputs/tables/sensitivity_genre_groups_v1.csv`](../tables/sensitivity_genre_groups_v1.csv)

**Substantive interpretation:** Purpose-built transparency instruments **continue to supply thinner verifiable governance evidence** than normative strategies and frameworks after excluding bot-gated cases. The inversion **strengthens in relative terms** for excluded portal/framework rows that were purely retrieval failures, but **algorithm registers remain at 53.3%** observable with **zero** commitment- or artefact-classified evidence in both runs.

---

## C. Genre inversion robustness (registers + portals vs strategies + frameworks)

**Test:** Is combined observable share for registers + portals **lower** than for strategies + frameworks?

| Corpus | Strategies + frameworks | Registers + portals | Inversion holds? |
|--------|---------------------------|---------------------|------------------|
| Full (115) | 67.3% (37/55) | 42.9% (15/35) | **Yes** (−24.4 pp) |
| Retrieved-only (95) | 74.0% (37/50) | 60.0% (15/25) | **Yes** (−14.0 pp) |

Individual-type floor after exclusion: **algorithm register 53.3%** ≤ **AI strategy 76.0%** and **governance framework 72.0%**; **transparency portal** rises to 70.0% in retrieved-only but **combined register + portal pool (60.0%)** remains below **combined strategy + framework pool (74.0%)**.

---

## D. Downstream gradient robustness

**Test:** Do D4 and D5 remain the two weakest dimensions after exclusion?

| Test | Full corpus | Retrieved-only | Stable? |
|------|-------------|----------------|---------|
| Lowest observable % dimensions | D4, D5 | D4, D5 | **Yes** |
| Highest not-observable % dimensions | D4, D5 | D4, D5 | **Yes** |
| D4 systematically under-observable (>50%) | Yes (78.3%) | Yes (73.7%) | **Yes** |
| D5 systematically under-observable (>50%) | Yes (56.5%) | No (47.4%) | **No** (formal flag only) |
| D5 still second-weakest dimension | Yes | Yes | **Yes** |

---

## Deliverable 2 — Manuscript-ready text

### Results subsection (recommended: new §5.4 or paragraph before §5.3 synthesis)

```latex
\subsection{Robustness: retrieved-only sensitivity}
\label{subsec:results-robustness}

Four manifest sources (20 document--dimension assessments) could not be retrieved automatically at collection and were coded \texttt{not\_observable\_publicly} under published retrieval rules.
To test whether the three empirical patterns depend on these potentially contaminating cases, all assessments from \texttt{bot\_gated} sources were excluded and distributions were recomputed on the retrieved-only corpus (19 sources; 95 assessments).

The commitment-heavy, artefact-thin profile was unchanged in absolute terms: 65 assessments still recorded policy commitments or partial signals and only three (3.2\%) named a governance artefact---the same status counts as in the full 115-assessment corpus (Table~\ref{tab:evidence-status}).
Downstream concentration persisted in rank order: procurement stewardship (D4) and lifecycle accountability (D5) remained the two weakest dimensions (26.3\% and 52.6\% observable, respectively), and D4 still exceeded the study's majority under-observability threshold (73.7\% without qualifying public evidence).
Lifecycle accountability fell to 47.4\% not observable---below the 50\% systematic threshold---indicating that part of the full-corpus D5 gap reflects retrieval-composition rather than evidence visible in successfully retrieved text.
Genre inversion also persisted: AI strategies and governance frameworks jointly supplied 74.0\% observable assessments (37/50), whereas algorithm registers and transparency portals jointly supplied 60.0\% (15/25); algorithm-register rows still recorded zero commitment- or artefact-classified evidence.
Individual source-type rank order shifted for retrieval-conditioned genres, but the aggregated normative-versus-transparency-instrument asymmetry did not reverse.
```

### Methods paragraph (recommended: end of §Analytical Procedure)

```latex
As a robustness check, the analysis was repeated on a retrieved-only subset that excluded all document--dimension assessments originating from manifest sources with \texttt{retrieval\_status = bot\_gated} (four sources; 20 assessments, all coded \texttt{not\_observable\_publicly}).
This sensitivity run tests pattern stability without altering the frozen main corpus (115 assessments) reported in Results tables.
No causal inference, hypothesis testing, or inferential statistics were applied in either run; comparisons use the same evidence-status labels and majority threshold as the primary analysis.
```

### Limitations paragraph (recommended: §Documentary and Observability Limitations)

```latex
Bot-gated retrieval affects composition-sensitive shares but not the core pattern structure.
Sensitivity analysis excluding four \texttt{bot\_gated} sources (20 assessments) left observable evidence-status counts unchanged (65 rows) and preserved the commitment-heavy, artefact-thin profile, D4 systematic under-observability (73.7\%), and genre inversion between combined strategies or frameworks (74.0\% observable) and combined registers or portals (60.0\%).
Lifecycle accountability's full-corpus systematic under-observability (56.5\%) did not replicate under retrieved-only filtering (47.4\%), so downstream-gap claims for D5 should be read as gradient concentration rather than as a retrieval-invariant majority rule.
Amsterdam and Tallinn municipality profiles are the most retrieval-composition-sensitive; Barcelona, Copenhagen, Helsinki, and Vienna were unchanged under ok-only filtering.
```

---

## Deliverable 3–5 — Recommended placement

| Content | Section | Location |
|---------|---------|----------|
| Sensitivity rule + retrieved-only *n* | **Methods** | `\subsection{Analytical Procedure}` — final paragraph before reproducibility note |
| Pattern stability summary + Table (A1–A3 condensed) | **Results** | New `\subsection{Robustness: retrieved-only sensitivity}` after `\ref{subsec:results-rq3}` and **before** the three-pattern synthesis paragraph |
| D5 threshold sensitivity + Amsterdam/Tallinn caveat | **Limitations** | `\subsection{Documentary and Observability Limitations}` — after bot-gating sentence |
| Optional appendix table | **Supplementary** | Full Tables A1–A3 if word limit tight |

---

## Deliverable 6 — Exact numerals for manuscript insertion

### Corpus scope
- Bot-gated sources excluded: **4**
- Assessments excluded: **20** (all `not_observable_publicly`)
- Retrieved-only corpus: **19 sources**, **95 assessments**
- Bot-gated share of all not-observable rows: **20/50 (40.0%)** — unchanged from freeze

### P1 — Commitment-heavy / artefact-thin
| Numeral | Full (115) | Retrieved-only (95) |
|---------|------------|---------------------|
| Observable assessments | 65 (56.5%) | 65 (68.4%) |
| Policy commitments | 37 (32.2%) | 37 (38.9%) |
| Partial signals | 25 (21.7%) | 25 (26.3%) |
| Named artefacts | 3 (2.6%) | 3 (3.2%) |
| Commitments / observable subset | 37/65 (56.9%) | 37/65 (56.9%) |
| Named / observable subset | 3/65 (4.6%) | 3/65 (4.6%) |

### P2 — Downstream concentration
| Dimension | Full not obs. | Full obs. | Retr.-only not obs. | Retr.-only obs. | >50% full | >50% retr.-only |
|-----------|---------------|-----------|---------------------|-----------------|-----------|-----------------|
| D4 | 18/23 (78.3%) | 5/23 (21.7%) | 14/19 (73.7%) | 5/19 (26.3%) | Yes | Yes |
| D5 | 13/23 (56.5%) | 10/23 (43.5%) | 9/19 (47.4%) | 10/19 (52.6%) | Yes | **No** |

Weakest-dimension rank (observable %): **D4, D5** — stable both runs.

### P3 — Genre inversion
| Group | Full observable | Retrieved-only observable | Gap (full) | Gap (retr.-only) |
|-------|-----------------|---------------------------|------------|------------------|
| Strategies + frameworks | 37/55 (**67.3%**) | 37/50 (**74.0%**) | +24.4 pp | +14.0 pp |
| Registers + portals | 15/35 (**42.9%**) | 15/25 (**60.0%**) | | |
| Algorithm register only | 8/15 (53.3%) | 8/15 (53.3%) | 0 commit; 0 named | 0 commit; 0 named |

### Municipality sensitivity (qualitative numerals)
| Municipality | Full obs. / rows | Retr.-only obs. / rows | Changed? |
|--------------|------------------|------------------------|----------|
| Amsterdam | 4/15 | 4/5 | Share only |
| Barcelona | 19/20 | 19/20 | No |
| Copenhagen | 8/10 | 8/10 | No |
| Helsinki | 13/25 | 13/25 | No |
| Tallinn | 0/15 | 0/5 | No (still zero) |
| Vienna | 21/30 | 21/30 | No |

---

## LaTeX table — condensed sensitivity (optional Table 6)

```latex
\begin{table}[htbp]
  \centering
  \caption{Retrieved-only robustness check (full corpus vs.\ exclusion of four \texttt{bot\_gated} sources).}
  \label{tab:robustness-retrieved-only}
  \footnotesize
  \setlength{\tabcolsep}{4pt}
  \begin{tabular}{lrrrr}
    \toprule
    Pattern / metric & Full & Retrieved-only & Stable? \\
    \midrule
    Observable assessments & 65/115 (56.5\%) & 65/95 (68.4\%) & Count yes \\
    Named artefacts & 3 (2.6\%) & 3 (3.2\%) & Yes \\
    D4 not observable & 78.3\% & 73.7\% & Yes ($>$50\%) \\
    D5 not observable & 56.5\% & 47.4\% & Threshold no \\
    Strategies + frameworks obs.\ \% & 67.3\% & 74.0\% & Inversion yes \\
    Registers + portals obs.\ \% & 42.9\% & 60.0\% & Inversion yes \\
    \bottomrule
  \end{tabular}
\end{table}
```

---

## Reproducibility

```bash
cd municipal-ai-evidence-gaps
python3 scripts/sensitivity_analysis.py
```

Outputs:
- `outputs/tables/sensitivity_*.csv`
- `outputs/reports/robustness_sensitivity_v1.json`
- `data/processed/*_sensitivity_ok_only.csv`

**Frozen main results (`results_freeze_v1.md`, manuscript Tables 1–5) remain authoritative.**

---

## Relation to prior check

This report supersedes and extends [`bot_gated_sensitivity_check_v0_1.md`](bot_gated_sensitivity_check_v0_1.md) with explicit P1–P3 framing, genre-group aggregation, rank-order comparison, CSV exports, and manuscript insertion text.
