# Study protocol v0.1

**Project:** Municipal AI Evidence Gaps  
**Paper working title:** Transparency Instruments That Disclose Least: Genre Inversion in Municipal AI Governance Documentation  
**Protocol version:** 0.1  
**Date:** 2026-06-08  
**Status:** Defined; corpus collection and coding not yet started

---

## 1. Research objective

To examine what European municipal AI governance documentation makes **publicly observable** and what programme-level evidence remains **unavailable** in public sources, using a comparative documentary observability analysis.

The study tests the working claim that public municipal AI documentation is often visible at the level of **principles and commitments** but thinner at the level of **evidence needed for independent programme-level governance assessment**.

This is a **Public-Document Observability** analysis. It maintains the canonical non-claims: no readiness scoring; no municipal ranking; no legal compliance determination; no LocalGovBench validation; no inference of internal governance quality.

---

## 2. Research questions

Three research questions organise the empirical work:

**RQ1.** What governance evidence is publicly observable in municipal AI documentation?

**RQ2.** Which governance dimensions are systematically under-observable?

**RQ3.** What patterns of transparency and evidence gaps emerge across municipalities and document types?

### Operational mapping

| RQ | Coding focus |
|----|--------------|
| RQ1 | Evidence-status labels (`observable_named_artifact` through `not_observable_publicly`) across D1–D5 and document types |
| RQ2 | Dimensions with highest rates of `partial_or_indirect_signal` and `not_observable_publicly` |
| RQ3 | Cross-municipal and cross-document-type observability profiles (descriptive, not ranked) |

### Discussion implication (not an empirical RQ)

The following question is addressed interpretively in the **Discussion** section, not as a standalone empirical research question:

> What are the implications of these evidence gaps for independent governance assessment based on public documentation alone?

---

## 3. Unit of analysis

| Level | Unit | Description |
|-------|------|-------------|
| Primary | **Evidence observation** | One coded judgement per municipality × source document × observability dimension (D1–D5) |
| Secondary | **Source document** | A publicly accessible municipal AI governance artefact linked to one municipality |
| Tertiary | **Municipality** | A local government jurisdiction included in the comparative sample |

Cross-municipal comparison describes **patterns of public observability**, not municipal performance or readiness.

---

## 4. Inclusion criteria — municipalities

A municipality is eligible for v0.1 if it meets **all** of the following:

1. **European scope** — located in a European country included in the v0.1 sample frame (EU member states, EEA, UK, and Switzerland unless otherwise noted in the corpus manifest).
2. **Local government status** — city, metropolitan, or municipal authority with documented AI governance activity (strategy, register, transparency initiative, or equivalent public programme).
3. **Public documentation trace** — at least one in-scope public document (see §5) is retrievable via an official municipal domain or officially linked portal without authentication.
4. **Language accessibility** — document is in a language the coding team can analyse directly or via agreed translation protocol (recorded in manifest notes).
5. **Manifest registration** — municipality and sources are recorded in `corpus_manifest_template.csv` with `inclusion_reason`.

Pilot sampling may begin with a purposive subset before sample expansion. v0.1 does not require statistical representativeness.

---

## 5. Inclusion criteria — documents

A document is in-scope if it meets **all** of the following:

1. **Public accessibility** — available without login, FOI request, or administrative access at time of `access_date`.
2. **Official provenance** — published or linked by the municipality, a formally mandated municipal body, or an official municipal open-data portal.
3. **AI governance relevance** — addresses municipal AI use, algorithmic systems, automation, or data-driven decision support in a governance, transparency, or policy context.
4. **Document types (non-exhaustive)** — AI strategy, algorithm register entry hub, transparency/disclosure page, responsible-AI policy, relevant procurement notice or contract summary when publicly posted as governance evidence.
5. **Stable citation** — `source_url`, `source_title`, and `access_date` are recorded; optional archival snapshot noted in manifest.

---

## 6. Exclusion criteria

Exclude municipalities or documents when any of the following apply:

| Exclusion | Rationale |
|-----------|-----------|
| Non-public or access-restricted materials | Violates public-document-only boundary |
| Purely technical API docs with no governance framing | Outside AI governance observability scope |
| Vendor marketing pages not officially adopted | Weak provenance |
| News articles or secondary commentary | Not primary municipal documentation |
| Documents consisting primarily of personal data | Privacy boundary |
| National or regional documents not tied to a municipal programme | Wrong jurisdictional unit |
| Duplicate mirrors without added content | De-duplicate; retain canonical official URL |

---

## 7. Data sources

**Permitted sources (public only):**

- Official municipal websites (`*.gov`, city domains, official subdomains)
- Municipal open-data portals and transparency registers
- Officially linked PDF/HTML policy libraries
- Public procurement portals **when the notice is an official municipal publication**

**Prohibited sources:**

- Internal dashboards, intranets, leaked materials
- FOIA responses not publicly posted
- Social media posts unless formally mirrored as official publications
- Scraped personal data fields from service interfaces

**Collection protocol:**

- Manual manifest curation in v0.1; scripted helpers create scaffolds only
- Record `access_date` for every source
- Respect `robots.txt` and reasonable request rates when automated retrieval is added later

---

## 8. Coding dimensions (v0.1)

Five observability dimensions:

| ID | Dimension | Programme-level focus |
|----|-----------|----------------------|
| **D1** | Programme ownership | Named roles, offices, and accountability for municipal AI programmes |
| **D2** | Human oversight and review | Human-in-the-loop, review boards, sign-off, escalation |
| **D3** | Prompt, log, and data governance | Prompt management, logging, retention, training data boundaries |
| **D4** | Procurement and vendor stewardship | Vendor roles, contract governance, subcontracting visibility |
| **D5** | Incident, audit, and lifecycle accountability | Incidents, audits, decommissioning, change history |

See `docs/coding_protocol.md` for coding questions and examples.

---

## 9. Evidence categories and status labels

### Evidence status labels (v0.1)

| Label | Meaning |
|-------|---------|
| `observable_named_artifact` | A concrete, named governance artefact is publicly documented (role title, register, log policy, audit report, contract attachment) |
| `observable_policy_commitment` | A clear policy statement or commitment exists but lacks programme-level specificity |
| `partial_or_indirect_signal` | Indirect, implied, or fragmented mention; insufficient for independent programme assessment |
| `not_observable_publicly` | No relevant public evidence located in the coded source(s) for this dimension |

### What counts as **observable evidence**

- Named responsible office, role, or committee with AI programme remit
- Published register entry with system purpose and oversight contact
- Documented review cadence, approval workflow, or escalation path
- Stated log/retention policy tied to automated or AI-assisted systems
- Public procurement identifier linking vendor to a municipal AI system
- Published audit summary, incident report, or lifecycle/decommission notice

Evidence must be **locatable** in the source (`page_or_section`) and quotable at minimal length.

### What counts as **unobservable / unavailable**

- Categories where public documents are silent or only generically aspirational
- Practices plausibly existing internally but not disclosed (record as `not_observable_publicly`, not as failure)
- Evidence requiring non-public records, vendor NDAs, or personal data access
- Inference from software features or service behaviour without documentary support

**Unobservable ≠ non-compliant.** Absence in public documents is an analytic finding about observability, not a legal or readiness judgement.

---

## 10. Non-claims

Canonical non-claims (see [`global_editorial_style_guide.md`](global_editorial_style_guide.md)):

- no readiness scoring
- no municipal ranking
- no legal compliance determination
- no LocalGovBench validation
- no inference of internal governance quality

Extended register: model performance evaluation, personal data processing, and non-public data collection remain out of scope. See [`non_claims.md`](non_claims.md).

---

## 11. Ethical and privacy boundaries

- **Public documents only** — no administrative records or credential-gated sources
- **No personal data processing** — coders record governance categories and short locators; redact incidental identifiers
- **Provenance discipline** — official municipal publication required
- **Rate-limited retrieval** — when automation is introduced
- **Positioning** — findings describe documentation gaps, not organisational misconduct

See `docs/ethics_and_privacy.md`.

---

## 12. Planned outputs (v0.1)

| Output | Location | Description |
|--------|----------|-------------|
| Corpus manifest | `data/processed/corpus_manifest.csv` | Municipality and source inventory |
| Coding dataset | `data/processed/coding_dataset.csv` | Dimension-level evidence observations |
| Templates | `data/processed/*_template.csv` | Header schemas for manifest and coding |
| Observability summary tables | `outputs/tables/` | Cross-dimensional frequency summaries |
| Reports | `outputs/reports/` | Descriptive gap patterns |
| Protocol docs | `docs/` | Study protocol, coding protocol, non-claims |

No readiness scoring, municipal ranking, or legal compliance determination outputs will be published.

---

## 13. Versioning plan for Zenodo

| Version | Tag | Contents | Timing |
|---------|-----|----------|--------|
| **v0.1.0** | `v0.1.0` | Protocol, schema, templates, empty scaffolds, docs | Initial archival scaffold (current) |
| **v0.2.0** | `v0.2.0` | Pilot corpus manifest + coding dataset (purposive sample) | After pilot coding |
| **v1.0.0** | `v1.0.0` | Full analysis corpus, tables, manuscript-linked exports | Upon GIQ submission / acceptance |

**Zenodo metadata:** link to GitHub release, `CITATION.cff`, CC BY 4.0 license, keyword set aligned with GIQ manuscript.

**Versioning rules:**

- Protocol changes increment minor version (`v0.x.0`) and are documented in this file
- Published corpora are immutable; corrections ship as new versions with changelog
- DOI version records point to specific Git tags

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-06-08 | Initial study protocol; D1–D5 dimensions and four evidence-status labels |
| 0.1.1 | 2026-06-08 | Harmonised three core RQs; former RQ4 moved to Discussion implication |
