# Tier A verification report

**Verification date:** 2026-06-08  
**Protocol:** [`docs/tier_a_verification_protocol.md`](../docs/tier_a_verification_protocol.md)  
**Data:** [`data/processed/tier_a_verification.csv`](../data/processed/tier_a_verification.csv)

## Summary

| Metric | Value |
|--------|-------|
| Candidates screened | 6 |
| Public AI documentation detected | 6 |
| Eligible at screening | 6 |
| D1–D5 coding performed | 0 |
| Corpus manifest rows created | 0 |

This report records **inclusion screening only**. It does not contain observability findings, evidence-status labels, or municipal rankings.

---

## Screening results

| Municipality | Country | Official domain | Languages | AI docs detected | Eligible |
|--------------|---------|---------------|-----------|------------------|----------|
| Amsterdam | NL | amsterdam.nl; algoritmeregister.amsterdam.nl | NL; EN | yes | yes |
| Barcelona | ES | ajuntament.barcelona.cat | CA; ES; EN | yes | yes |
| Copenhagen | DK | kk.dk | DA | yes | yes |
| Helsinki | FI | hel.fi; ai.hel.fi | FI; EN | yes | yes |
| Vienna | AT | wien.gv.at; digitales.wien.gv.at | DE; EN | yes | yes |
| Tallinn | EE | tallinn.ee; strateegia.tallinn.ee | ET; EN | yes | yes |

---

## Per-candidate notes

### Amsterdam (Gemeente Amsterdam)

- **Municipality status:** Confirmed municipal government (Netherlands).
- **Official domain:** `amsterdam.nl`; algorithm register at `algoritmeregister.amsterdam.nl`.
- **Public AI documentation (URLs only):**
  - https://algoritmeregister.amsterdam.nl/ — HTTP 200 at screening
  - https://www.amsterdam.nl/innovatie/digitalisering-technologie/algoritmes-ai/
  - https://www.amsterdam.nl/innovatie/amsterdamse-visie-ai/
- **Languages:** Dutch primary; English AI vision PDF linked from official pages.
- **Eligibility:** **yes** — official algorithm register publicly reachable; municipal AI hub and vision on official domain.

### Barcelona (Ajuntament de Barcelona)

- **Municipality status:** Confirmed municipal government (Spain).
- **Official domain:** `ajuntament.barcelona.cat`.
- **Public AI documentation (URLs only):**
  - https://ajuntament.barcelona.cat/digital/es/hagamos-accesible-la-tecnologia/uso-etico-inteligencia-artificial/uso-etico-de-la-inteligencia — HTTP 200
  - https://ajuntament.barcelona.cat/digital/en/technology-accessible-everyone/ethical-use-artificial/ethical-use-artificial-intelligence/protocol — HTTP 200
- **Languages:** Catalan, Spanish, English (Barcelona Digital City subsite).
- **Eligibility:** **yes** — municipal algorithms/data strategy and AI implementation protocol on official domain.

### Copenhagen (Københavns Kommune)

- **Municipality status:** Confirmed municipal government (Denmark).
- **Official domain:** `kk.dk`.
- **Public AI documentation (URLs only):**
  - https://www.kk.dk/nyheder/hvad-goer-robotter-ved-retssikkerheden — HTTP 200; references municipal AI code of conduct
  - https://www.kk.dk/dagsordener-og-referater/%C3%98konomiudvalget/m%C3%B8de-18022020/referat/punkt-6 — official committee record on AI code of conduct adoption
- **Languages:** Danish.
- **Eligibility:** **yes** — official municipal publication on AI governance and code of conduct.

### Helsinki (City of Helsinki)

- **Municipality status:** Confirmed municipal government (Finland).
- **Official domain:** `hel.fi`; dedicated AI register subdomain `ai.hel.fi`.
- **Public AI documentation (URLs only):**
  - https://ai.hel.fi/en/ai-register/ — HTTP 200
  - https://ai.hel.fi/en/get-to-know-ai-register/ — HTTP 200
  - https://www.hel.fi/en/news/helsinki-has-determined-ethical-principles-for-the-responsible-use-of-data-and-artificial
- **Languages:** Finnish, English.
- **Eligibility:** **yes** — official public AI register and ethical-principles publication.

### Vienna (Stadt Wien)

- **Municipality status:** Confirmed municipal government (Austria).
- **Official domain:** `wien.gv.at`; digital programme at `digitales.wien.gv.at`.
- **Public AI documentation (URLs only):**
  - https://www.wien.gv.at/spezial/ki-strategie/grundzugang/ki-als-schlusseltechnologie-fur-den-offentlichen-bereich/ — HTTP 200
  - https://digitales.wien.gv.at/wp-content/uploads/sites/47/2025/09/1065373-2025_MD-OS_PIKT_KI-Strategie_Sanjath_EN_korr-bf.pdf
- **Languages:** German; English strategy PDF on official domain.
- **Eligibility:** **yes** — official municipal AI strategy pages and published strategy document.

### Tallinn (Tallinn city government)

- **Municipality status:** Confirmed municipal government (Estonia).
- **Sampling frame note:** Classified **Tier B** in [`municipal_sampling_strategy_v0_1.md`](../docs/municipal_sampling_strategy_v0_1.md); screened in this tranche per verification task.
- **Official domain:** `tallinn.ee`; development strategy portal `strateegia.tallinn.ee`.
- **Public AI documentation (URLs only):**
  - https://www.tallinn.ee/en/internationalprojects/betti — BETTI trustworthy GenAI governance project (official municipal page)
  - https://www.tallinn.ee/en/digikaksik/tallinn-digital-twin — digital-twin / data-driven governance page
- **Languages:** Estonian, English.
- **Eligibility:** **yes** — official municipal AI-governance-related documentation detected; thinner than Tier A frontrunners (project-based rather than standalone AI strategy). Browser re-check recommended for bot-gated URLs at collection.

---

## Methodological boundaries

- **No D1–D5 coding** was performed.
- **No evidence-status labels** were assigned.
- **No findings** about observability patterns are reported.
- URLs are recorded for future manifest registration only.

---

## Bot-gating caveat

Automated HTTP requests received **403** responses from some official pages (`amsterdam.nl`, `hel.fi` news, `tallinn.ee`) while sibling official URLs on the same municipal publisher returned **200** or were confirmed via alternative official paths. Candidates remain **eligible** at screening subject to browser-confirmed `access_date` recording during collection.

---

## Recommended next steps

1. Browser re-verification of bot-gated URLs with recorded `access_date`
2. Add eligible candidates to `corpus_manifest_template.csv` (collection phase)
3. Continue Tier B/C screening before expanding corpus
4. Defer D1–D5 coding until manifest is complete

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-06-08 | Initial Tier A (plus Tallinn) screening report |
