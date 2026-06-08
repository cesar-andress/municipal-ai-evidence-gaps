# Result claims inventory

**Derived from:** [`rq_analysis_v0_1.md`](rq_analysis_v0_1.md)  
**Date:** 2026-06-08  
**Corpus:** 115 coding rows · 23 sources · 6 municipalities · protocol v0.1.1

Candidate result claims with evidence pointers and confidence levels. Claims are descriptive observability statements only.

**Confidence key:** high = direct frequency in coding data; moderate = pattern across multiple cells with corpus constraints noted; low = bounded implication requiring cautious wording.

**Exceeds-data flag:** ⚠️ = claim must not be stated without qualification or falls outside non-claims.

---

## RQ1 claims

| ID | Claim text | Evidence | Confidence | Exceeds data? |
|----|------------|----------|------------|---------------|
| RQ1-C01 | 65 of 115 coding rows (56.5%) record some form of publicly observable governance evidence. | `coding_results_v0_1_1.csv`: 37 commitment + 25 partial + 3 named artefact | **high** | No |
| RQ1-C02 | Observable public evidence is predominantly coded as `observable_policy_commitment` (37 rows; 56.9% of observable rows). | Status frequency table | **high** | No |
| RQ1-C03 | `observable_named_artifact` is rare in the corpus (3 rows; 2.6% of all rows). | 3 D1 Vienna rows only | **high** | No |
| RQ1-C04 | Named artefacts with locatable detail appear only for D1 programme ownership, not D2–D5. | Zero named artefacts in D2–D5 | **high** | No |
| RQ1-C05 | D1, D2, and D3 each show observable evidence in more than 60% of dimension rows. | D1 73.9%; D2 78.3%; D3 65.2% observable share | **high** | No |
| RQ1-C06 | AI strategy and governance-framework source types account for the largest shares of observable policy commitments. | 11 + 12 commitment rows respectively | **high** | No |
| RQ1-C07 | Public municipal AI documentation in this corpus makes principles and commitments more observable than operational named artefacts. | Commitment 37 vs named artefact 3 | **moderate** | No |
| RQ1-C08 | Municipalities with richer strategy and governance-framework documentation show higher observable row counts in this manifest. | Barcelona 19/20; Vienna 21/30 observable rows | **moderate** | ⚠️ Do not phrase as municipal quality or ranking |
| RQ1-C09 | All municipalities publish equally observable AI governance documentation. | Variable observable profiles; Tallinn 0/15 | **—** | ⚠️ **EXCEEDS DATA** if stated affirmatively |

---

## RQ2 claims

| ID | Claim text | Evidence | Confidence | Exceeds data? |
|----|------------|----------|------------|---------------|
| RQ2-C01 | D4 (procurement and vendor stewardship) is the most under-observable dimension: 18/23 rows (78.3%) are `not_observable_publicly`. | Dimension × status table | **high** | No |
| RQ2-C02 | D5 (incident, audit, and lifecycle accountability) is systematically under-observable: 13/23 rows (56.5%) are `not_observable_publicly`. | >50% threshold | **high** | No |
| RQ2-C03 | No `observable_named_artifact` rows occur in D2, D3, D4, or D5. | Empty dimension × status cells | **high** | No |
| RQ2-C04 | D2 and D3 are not systematically under-observable by the >50% not-observable threshold (21.7% and 34.8% respectively). | RQ2 threshold table | **high** | No |
| RQ2-C05 | Where D4 evidence is observable, it appears as policy commitment (3 rows) or partial signal (2 rows), never as named artefact. | D4 status distribution | **high** | No |
| RQ2-C06 | The manifest contains no `procurement document` source type, constraining D4 observability to non-procurement texts. | `corpus_manifest_v0_1.csv` | **high** | No |
| RQ2-C07 | Public documentation under-observability in D4/D5 indicates weak internal procurement and lifecycle governance. | — | **—** | ⚠️ **EXCEEDS DATA** — non-claim violation |
| RQ2-C08 | European municipalities systematically fail to publish procurement governance for AI. | n=6 purposive sample; no procurement docs | **—** | ⚠️ **EXCEEDS DATA** — generalisation beyond sample |

---

## RQ3 claims

| ID | Claim text | Evidence | Confidence | Exceeds data? |
|----|------------|----------|------------|---------------|
| RQ3-C01 | All 15 Tallinn coding rows are `not_observable_publicly`. | mun-tallinn status counts | **high** | No |
| RQ3-C02 | Ten of Amsterdam's 15 coding rows are `not_observable_publicly`, associated with bot-gated manifest sources. | 2 bot-gated sources × 5 dimensions | **high** | No |
| RQ3-C03 | Barcelona's coded rows are predominantly observable (19/20), with a single `not_observable_publicly` cell (hub page D5). | Municipality profile | **high** | No |
| RQ3-C04 | Helsinki register sources (EN + FI) contribute 10 `not_observable_publicly` rows concentrated in D3–D5. | Register row pattern | **high** | No |
| RQ3-C05 | Vienna is the only municipality with `observable_named_artifact` rows (3; all D1). | Named artefact inventory | **high** | No |
| RQ3-C06 | Transparency portal source types show 65% `not_observable_publicly` (13/20 rows). | Source-type distribution | **high** | No |
| RQ3-C07 | Algorithm register source types yield partial signals (8 rows) but no named artefacts at register-index coding depth. | Register coding notes | **high** | No |
| RQ3-C08 | AI strategy and governance-framework types show the highest observable-cell counts across D1–D3. | Source type × dimension matrix | **moderate** | No |
| RQ3-C09 | D4 observable evidence appears in at most 2 rows per source type. | Source type × dimension matrix | **high** | No |
| RQ3-C10 | Five manifest sources produce zero observable dimensions (2 Amsterdam bot-gated; 2 Tallinn bot-gated; 1 Tallinn landing). | Zero-observable source list | **high** | No |
| RQ3-C11 | Transparency documentation often states commitments to registers and scrutiny without publishing operational audit or logging detail. | Strategy partial signals + portal commitments + D5 gap | **moderate** | No |
| RQ3-C12 | Evidence-gap patterns are shaped by manifest composition and retrieval constraints as well as documentary content. | Pre-analysis validity; bot-gated 20 rows | **moderate** | No |
| RQ3-C13 | Barcelona is the best-governed municipality in the sample. | — | **—** | ⚠️ **EXCEEDS DATA** — ranking/non-claim violation |
| RQ3-C14 | Tallinn lacks AI governance altogether. | 15 not-observable rows; bot-gating | **—** | ⚠️ **EXCEEDS DATA** — infers internal quality from public silence |
| RQ3-C15 | Publishing an algorithm register ensures procurement observability. | Registers show D4 0 observable cells at index level | **—** | ⚠️ **EXCEEDS DATA** — causal claim beyond cross-sectional coding |

---

## Cross-cutting claims

| ID | Claim text | Evidence | Confidence | Exceeds data? |
|----|------------|----------|------------|---------------|
| XC-C01 | The v0.1 corpus exhibits a commitment-heavy, artefact-thin public observability profile. | 37 commitments vs 3 named artefacts | **high** | No |
| XC-C02 | Programme-level procurement and post-deployment accountability are the least publicly documented governance dimensions in this sample. | D4 78.3%; D5 56.5% not observable | **high** | No |
| XC-C03 | Findings describe public-document observability in six purposive municipalities and do not support statistical generalisation to all European municipalities. | Sampling strategy v0.1 | **high** | No |
| XC-C04 | Non-observable coding labels indicate absence from coded public sources, not confirmed absence of internal controls. | Protocol non-claims | **high** | No |

---

## Claims summary

| Confidence | Count | Exceeds-data flags |
|------------|-------|-------------------|
| High | 24 | 0 |
| Moderate | 6 | 1 (RQ1-C08 wording) |
| Exceeds data (do not publish) | 6 | RQ1-C09; RQ2-C07; RQ2-C08; RQ3-C13; RQ3-C14; RQ3-C15 |

---

## Recommended claim tiers for manuscript

| Tier | Claim IDs | Use |
|------|-----------|-----|
| **Tier A (results-ready)** | RQ1-C01–C06; RQ2-C01–C06; RQ3-C01–C10; XC-C01–C04 | Direct frequency statements |
| **Tier B (discussion-pending)** | RQ1-C07–C08; RQ3-C11–C12 | Bounded implications; require methods caveats |
| **Tier C (prohibited)** | RQ1-C09; RQ2-C07–C08; RQ3-C13–C15 | Violate non-claims or exceed data |
