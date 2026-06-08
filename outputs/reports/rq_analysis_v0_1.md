# RQ analysis v0.1

**Analysis date:** 2026-06-08  
**Protocol:** v0.1.1  
**Coding data:** [`data/processed/coding_results_v0_1_1.csv`](../../data/processed/coding_results_v0_1_1.csv)  
**Pre-analysis:** [`pre_analysis_validity_check.md`](pre_analysis_validity_check.md) · [`coding_distribution_audit_v0_1_1.md`](coding_distribution_audit_v0_1_1.md)

**Corpus:** 23 manifest sources · 6 municipalities · 115 coding rows

This report answers RQ1–RQ3 using descriptive coded observations only. It is not a manuscript, abstract, discussion section, or policy brief.

---

## Analytic boundaries

| In scope | Out of scope |
|----------|--------------|
| Descriptive evidence-status frequencies | Municipal ranking or readiness scoring |
| Dimension-level observability patterns | Internal governance quality inference |
| Source-type and municipality **distribution profiles** | Legal compliance determination |
| Public-document observability gaps | Normative policy recommendations |

**Weighting note:** Municipalities contribute unequal coding rows (10–30) because manifest source counts differ. Patterns below describe **coded row distributions**, not weighted municipal performance.

---

## RQ1 — What governance evidence is publicly observable in municipal AI documentation?

### Observed patterns

#### Observable evidence types (corpus-wide)

Among 115 coding rows, **65 rows (56.5%)** carry observable public evidence (any status other than `not_observable_publicly`):

| Observable `evidence_status` | Count | Share of all rows | Share of observable rows |
|------------------------------|-------|-------------------|--------------------------|
| `observable_policy_commitment` | 37 | 32.2% | 56.9% |
| `partial_or_indirect_signal` | 25 | 21.7% | 38.5% |
| `observable_named_artifact` | 3 | 2.6% | 4.6% |
| **Total observable** | **65** | **56.5%** | **100%** |

**Observable evidence types in this corpus are predominantly policy commitments and partial/indirect signals.** Named artefacts with locatable detail are rare (3 rows).

#### Dimensions where evidence appears

| Dimension | Observable rows | `not_observable_publicly` | Observable share |
|-----------|-----------------|--------------------------|------------------|
| D1 Programme ownership | 17 | 6 | 73.9% |
| D2 Human oversight and review | 18 | 5 | 78.3% |
| D3 Prompt, log, and data governance | 15 | 8 | 65.2% |
| D4 Procurement and vendor stewardship | 5 | 18 | 21.7% |
| D5 Incident, audit, and lifecycle accountability | 10 | 13 | 43.5% |

**D1, D2, and D3** show observable evidence in a majority of coded rows. **D4 and D5** show observable evidence in a minority.

#### Frequency patterns within observable evidence

| Dimension | Dominant observable label |
|-----------|---------------------------|
| D1 | Mixed: 7 commitment · 7 partial · 3 named artefact |
| D2 | `observable_policy_commitment` (10/18 observable rows) |
| D3 | `observable_policy_commitment` (11/15 observable rows) |
| D4 | `observable_policy_commitment` (3/5 observable rows) |
| D5 | `observable_policy_commitment` (6/10 observable rows) |

**Named artefacts (`observable_named_artifact`) appear only in D1** (3 rows, all Vienna sources: strategy PDF legal notice; AI Competence Network in compass documents).

#### Observable evidence by source type (pattern)

| `source_type` | Observable rows | Total rows | Observable share |
|---------------|-----------------|------------|------------------|
| AI strategy | 19 | 25 | 76.0% |
| governance framework | 18 | 30 | 60.0% |
| committee record | 7 | 10 | 70.0% |
| AI policy | 6 | 15 | 40.0% |
| algorithm register | 8 | 15 | 53.3% |
| transparency portal | 7 | 20 | 35.0% |

**No `procurement document` sources** exist in manifest v0.1.

### Interpretive implications (bounded)

- Public municipal AI documentation in this corpus most often makes **principles and commitments** observable rather than **named operational artefacts**.
- Observable evidence clusters in **strategy, governance-framework, and committee-record** source types; **transparency portals and registers** more often yield partial signals or non-observability at index level.
- **Interpretive bound:** These implications describe public-text observability in the v0.1 manifest only; they do not measure internal programme maturity.

---

## RQ2 — Which governance dimensions are systematically under-observable?

### Observed patterns

#### Systematically under-observable dimensions

Using **>50% `not_observable_publicly`** as a corpus-level under-observability threshold:

| Dimension | `not_observable_publicly` | Share | Under-observable (>50%) |
|-----------|--------------------------|-------|-------------------------|
| D4 Procurement and vendor stewardship | 18/23 | **78.3%** | **Yes** |
| D5 Incident, audit, and lifecycle accountability | 13/23 | **56.5%** | **Yes** |
| D3 Prompt, log, and data governance | 8/23 | 34.8% | No |
| D1 Programme ownership | 6/23 | 26.1% | No |
| D2 Human oversight and review | 5/23 | 21.7% | No |

**D4 and D5** are systematically under-observable in this corpus at the defined threshold.

#### Evidence-status distributions by dimension

| Dimension | Named artefact | Policy commitment | Partial/indirect | Not observable |
|-----------|-------------|-------------------|------------------|----------------|
| D1 | 3 (13.0%) | 7 (30.4%) | 7 (30.4%) | 6 (26.1%) |
| D2 | 0 (0%) | 10 (43.5%) | 8 (34.8%) | 5 (21.7%) |
| D3 | 0 (0%) | 11 (47.8%) | 4 (17.4%) | 8 (34.8%) |
| D4 | 0 (0%) | 3 (13.0%) | 2 (8.7%) | 18 (78.3%) |
| D5 | 0 (0%) | 6 (26.1%) | 4 (17.4%) | 13 (56.5%) |

#### Dimensions dominated by `not_observable_publicly`

| Dimension | Modal status | Modal share |
|-----------|--------------|-------------|
| D4 | `not_observable_publicly` | 78.3% |
| D5 | `not_observable_publicly` | 56.5% |

No other dimension has a modal share above 50% for `not_observable_publicly`.

#### Structural corpus constraints affecting D4/D5

| Constraint | Relevance |
|------------|-----------|
| Zero `procurement document` manifest rows | D4 observability limited to non-procurement source types |
| Register index-level coding | D5 lifecycle status metadata capped at partial signal |
| Committee minutes without bilag coding | D5 audit/incident artefacts may sit in unregistered attachments |

### Interpretive implications (bounded)

- **Programme-level procurement and post-deployment accountability** are the thinnest public-documentation layers in this observability frame.
- **D2 and D3** show more frequent commitment-level observability but **zero named artefacts** outside D1 — suggesting public documentation emphasises principles over operational traceability for oversight and data governance.
- **Interpretive bound:** Under-observability denotes absence from **public documents coded**, not absence of internal controls.

---

## RQ3 — What patterns of transparency and evidence gaps emerge across municipalities and document types?

### Observed patterns

#### Municipality distribution profiles (coded rows)

| Municipality | Manifest sources | Coding rows | Policy commitment | Partial/indirect | Named artefact | Not observable |
|--------------|------------------|-------------|-------------------|------------------|----------------|----------------|
| Barcelona | 4 | 20 | 11 | 8 | 0 | 1 |
| Vienna | 6 | 30 | 13 | 5 | 3 | 9 |
| Helsinki | 5 | 25 | 9 | 4 | 0 | 12 |
| Copenhagen | 2 | 10 | 4 | 4 | 0 | 2 |
| Amsterdam | 3 | 15 | 0 | 4 | 0 | 11 |
| Tallinn | 3 | 15 | 0 | 0 | 0 | 15 |

**Municipality × dimension `not_observable_publicly` counts:**

| Municipality | D1 | D2 | D3 | D4 | D5 |
|--------------|----|----|----|----|-----|
| Amsterdam | 2 | 2 | 2 | 3 | 2 |
| Barcelona | 0 | 0 | 0 | 0 | 1 |
| Copenhagen | 0 | 0 | 0 | 2 | 0 |
| Helsinki | 0 | 0 | 2 | 5 | 5 |
| Tallinn | 3 | 3 | 3 | 3 | 3 |
| Vienna | 1 | 0 | 1 | 5 | 2 |

**Profile notes (descriptive, not ranked):**

- **Tallinn:** All 15 rows `not_observable_publicly` (5 from strategy landing; 10 from bot-gated sources).
- **Amsterdam:** 11/15 `not_observable_publicly`; 10 rows from bot-gated sources; 4 partial signals from register index.
- **Barcelona:** 19/20 rows observable; single `not_observable` on hub page D5.
- **Helsinki:** D4 and D5 each show 5/5 `not_observable` on register and some policy sources; ethical-principles sources carry D1–D3 commitments.

#### Patterns by source type

| `source_type` | Not observable | Observable profile |
|---------------|----------------|-------------------|
| transparency portal | 13/20 (65.0%) | Commitments on explainer pages; hubs often thin |
| governance framework | 12/30 (40.0%) | Highest commitment count (12); 2 named artefacts (Vienna) |
| algorithm register | 7/15 (46.7%) | Partial signals only (8); no named artefacts at index level |
| AI policy | 9/15 (60.0%) | Commitments when text accessible; bot-gated rows non-observable |
| AI strategy | 6/25 (24.0%) | Highest commitment density (11) |
| committee record | 3/10 (30.0%) | Mixed commitments and partial signals |

**Source type × dimension observable-cell pattern** (count of non-`not_observable` rows per type-dimension pair, max 5):

| Source type | D1 | D2 | D3 | D4 | D5 |
|-------------|----|----|----|----|-----|
| AI strategy | 4 | 5 | 4 | 2 | 4 |
| governance framework | 4 | 4 | 4 | 2 | 4 |
| committee record | 2 | 2 | 2 | 0 | 1 |
| algorithm register | 3 | 3 | 1 | 0 | 1 |
| AI policy | 2 | 2 | 2 | 0 | 0 |
| transparency portal | 2 | 2 | 2 | 1 | 0 |

**D4 observable cells are sparse across all source types** (max 2 per type).

#### Transparency patterns

| Transparency mechanism | Observable pattern in corpus |
|------------------------|------------------------------|
| Algorithm registers (3 sources) | 8 partial signals; 7 not observable; 0 named artefacts at index level |
| Transparency portals (4 sources) | 5 commitments; 2 partial; 13 not observable (includes bot-gated hubs) |
| Public register commitments (strategy text) | Partial signals on future register creation (Barcelona ES/EN) |
| Named governance bodies in strategy text | Policy commitments (e.g. advisory council titles) |

Transparency documentation in this corpus often **describes transparency intentions** (registers, councils, scrutiny language) at commitment or partial-signal level rather than publishing operational audit or logging detail.

#### Evidence-gap patterns

| Gap type | Corpus pattern |
|----------|----------------|
| Procurement/vendor stewardship gap | D4: 78.3% not observable; no procurement document type in manifest |
| Lifecycle/accountability gap | D5: 56.5% not observable; register status metadata only partial |
| Named-artefact gap | 0 named artefacts in D2–D5; 3 total in D1 only |
| Retrieval-access gap | 20/50 not-observable rows from 4 bot-gated sources |
| Register-depth gap | 15 register/portal rows; index-level coding limits operational detail |
| Source-type gap | `procurement document` and `other official document` absent from manifest |

#### Sources with zero observable dimensions (5 sources)

| Municipality | Source type | Retrieval |
|--------------|-------------|-----------|
| Amsterdam | AI policy | bot_gated |
| Amsterdam | transparency portal | bot_gated |
| Tallinn | governance framework (BETTI) | bot_gated |
| Tallinn | transparency portal (digital twin) | bot_gated |
| Tallinn | governance framework (2035 landing) | ok (no AI-specific text coded) |

### Interpretive implications (bounded)

- **Transparency and evidence gaps co-occur:** municipalities with richer strategy/governance-framework documentation (Barcelona, Vienna) show more commitment-level observability, while **register- and portal-heavy profiles** without accessible policy PDFs show more partial or non-observable cells.
- **Document-type stratification:** AI strategies and governance frameworks carry most observable evidence; **algorithm registers at index level** contribute transparency visibility mainly as partial metadata.
- **Corpus composition effects** (bot-gating, missing procurement type, Tallinn landing depth) shape municipality profiles as much as documentary content differences.
- **Interpretive bound:** Patterns describe **v0.1 manifest observability**; cross-municipal patterns are **not** municipal quality comparisons.

---

## Cross-RQ synthesis (descriptive)

| Finding area | Core descriptive pattern |
|--------------|--------------------------|
| RQ1 | 56.5% of rows observable; commitments dominate; named artefacts rare (D1 only) |
| RQ2 | D4 and D5 systematically under-observable (>50% not observable) |
| RQ3 | Strategy/governance-framework types most observable; registers/portals mixed; Tallinn/Amsterdam bot-gated rows drive non-observability |

---

## Related artefacts

| File | Role |
|------|------|
| [`findings_candidate_tables.md`](findings_candidate_tables.md) | Candidate paper tables |
| [`findings_candidate_figures.md`](findings_candidate_figures.md) | Candidate figures |
| [`result_claims_inventory.md`](result_claims_inventory.md) | Claim-level inventory with confidence |

---

## Not produced

- Manuscript text, abstract, or discussion prose
- Policy recommendations
- Municipal rankings
- Internal governance quality assessments
