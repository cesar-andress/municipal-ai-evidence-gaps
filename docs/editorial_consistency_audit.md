# Editorial consistency audit v0.1

**Date:** 2026-06-08  
**Authority:** [`global_editorial_style_guide.md`](global_editorial_style_guide.md)  
**Scope:** `municipal-ai-evidence-gaps/` and `paper/`

## Summary

| Metric | Count |
|--------|-------|
| Files reviewed | 27 |
| Files edited | 22 |
| Issues corrected | 48 |
| Manual-review items remaining | 6 |

---

## Corrections applied

| File | Issue | Correction applied |
|------|-------|-------------------|
| `docs/global_editorial_style_guide.md` | *(new)* | Created authoritative style guide |
| `docs/editorial_consistency_audit.md` | *(new)* | Created audit log |
| `docs/non_claims.md` | Non-canonical phrasing (readiness index, maturity score, governance-capacity) | Replaced with five canonical non-claims block + extended register |
| `docs/methodology.md` | "observability"; non-goals list variants | → Public-Document Observability; canonical non-claims |
| `docs/study_protocol_v0_1.md` | Mixed non-claim verbs; readiness/maturity wording | → canonical non-claims verbatim |
| `docs/research_design_v0_1.md` | "benchmark scores", "operational maturity"; duplicate AI Act line | → canonical equivalents; deduplicated |
| `docs/coding_protocol.md` | Generic observability; prohibited-uses variants | → Public-Document Observability; canonical non-claims |
| `docs/giq_storyline.md` | readiness scores, league tables, non-compliant | → readiness scoring, municipal ranking, legal compliance determination |
| `docs/paper_blueprint.md` | benchmark validation; internal quality | → LocalGovBench validation; inference of internal governance quality |
| `docs/conceptual_model.md` | readiness scores; internal quality | → readiness scoring; inference of internal governance quality |
| `docs/sampling_risks.md` | observability ≠ internal quality | → Public-Document Observability; no inference of internal governance quality |
| `docs/journal_positioning.md` | Non-goals shorthand | → canonical non-claims list |
| `docs/municipal_sampling_strategy_v0_1.md` | "digital maturity"; readiness benchmarking | → digital-government publication; readiness scoring |
| `docs/ethics_and_privacy.md` | public documents; public observability | → public documentation; Public-Document Observability |
| `README.md` | public documents; readiness scoring variants | → public documentation; canonical non-claims; style guide link |
| `paper/docs/editorial_style_guide.md` | *(new)* | Pointer to authoritative guide |
| `paper/README.md` | No style guide link | Added editorial pointer |
| `paper/sections/00_abstract.tex` | legal compliance judgments; readiness rankings | → canonical non-claims block |
| `paper/sections/01_introduction.tex` | scoring or ranking municipalities | → readiness scoring; municipal ranking; public documentation |
| `paper/sections/02_related_work.tex` | governance-readiness (TODO) | → Programme-Level Governance Readiness |
| `paper/sections/04_method.tex` | observability; readiness scores | → Public-Document Observability; canonical non-claims |
| `paper/sections/06_discussion.tex` | evidence-gap (hyphen) | → evidence gap |
| `paper/sections/07_limitations.tex` | evaluate legal compliance; certify readiness; rank | → canonical non-claims |
| `paper/sections/08_conclusion.tex` | public documents (collective) | → public documentation |

---

## Files reviewed — no change required

| File | Reason |
|------|--------|
| `docs/research_design_v0_1.md` (RQs) | RQs already canonical verbatim |
| `docs/study_protocol_v0_1.md` (RQs) | RQs already canonical verbatim |
| `paper/sections/03_research_questions.tex` | RQs already canonical verbatim |
| `docs/data_dictionary.md` | Technical schema only; no editorial conflicts |
| `docs/tier_a_verification_protocol.md` | Screening protocol; terminology aligned |
| `outputs/reports/tier_a_verification_report.md` | Screening only; no observability findings |
| `paper/main.tex` | Title/keywords aligned |
| `paper/sections/05_results.tex` | Placeholder only |

---

## Remaining manual-review items

| File | Item | Action |
|------|------|--------|
| `docs/research_design_v0_1.md` | Contribution heading uses "Evidence-gap analysis" (hyphenated adjective) | Acceptable as section title; body uses "evidence gap" |
| `docs/giq_storyline.md` | Act heading "Evidence-gap concept" | Acceptable as narrative label; not an analytic claim |
| `docs/paper_blueprint.md` | Occasional "public documents" when referring to assessor access channel | Context-specific; distinct from collective **public documentation** |
| `docs/study_protocol_v0_1.md` | "public document" in inclusion criteria (singular unit) | Correct per style guide §1 |
| `paper/sections/04_method.tex` | "public documents" in corpus sentence (countable units) | Correct per style guide §1 |
| `CITATION.cff` / `pyproject.toml` | Author placeholders (TBD) | Update at submission—not editorial consistency |

---

## Verification

After edits:

- RQ1–RQ3 wording identical across README, protocols, storyline, blueprint, manuscript §3
- Five canonical non-claims present in `non_claims.md`, `study_protocol_v0_1.md`, `methodology.md`, manuscript abstract/method/limitations
- Government Information Quarterly capitalized consistently
- No `program-level` (US spelling) in project-authored text

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-06-08 | Initial editorial consistency audit |
