# Municipal sampling strategy v0.1

**Project:** Municipal AI Evidence Gaps  
**Paper:** When Transparency Is Not Enough: Evidence Gaps in Municipal AI Governance  
**Strategy version:** 0.1  
**Date:** 2026-06-08  
**Status:** Strategy complete; **no documents collected; no candidates verified**

**Related:** [`study_protocol_v0_1.md`](study_protocol_v0_1.md) · [`research_design_v0_1.md`](research_design_v0_1.md) · [`sampling_risks.md`](sampling_risks.md)

---

## 1. Sampling objective

Design a **purposive maximum-variation sample** of European municipalities for comparative public-document observability analysis—feasible for a **single-researcher** study with double-coding support on a subset.

The sample should maximise variation along five axes:

| Axis | Rationale |
|------|-----------|
| **Country** | Capture differences in national digital-government and AI policy context without making compliance claims |
| **Administrative tradition** | Compare documentation cultures (Nordic, Napoleonic, Germanic, Anglo, mixed post-communist) |
| **Municipal size** | Contrast documentation capacity of large metros, mid-size cities, and smaller municipalities |
| **AI governance visibility** | Include high-, moderate-, and emerging-visibility cases to avoid studying only frontrunners |
| **Language** | Span major European publication languages while keeping translation workload bounded |

The objective is **comparative pattern identification**, not statistical representativeness of all European municipalities. Municipalities are **not ranked**; tiers describe expected public visibility profiles for frame construction only.

---

## 2. Inclusion criteria (municipality level)

A municipality may enter the sample **only if all** conditions are met at collection verification:

1. **Public AI discourse** — the municipality has publicly discussed AI use, AI governance, AI strategy, AI guidelines, AI procurement, or AI deployment through official channels (not media alone).
2. **Public accessibility** — at least one in-scope primary document is retrievable without authentication from an official municipal domain or officially linked portal.
3. **Archival stability** — documentation is sufficiently stable to cite: persistent URL or archived snapshot; not a transient social post or broken landing page.
4. **Language feasibility** — documents are in a language the research team can analyse natively or via the agreed translation protocol (§8).
5. **Jurisdictional fit** — entity is a municipality (city, commune, gemeente, comune, etc.), not a national or regional body.
6. **Manifest registration** — inclusion recorded in `corpus_manifest_template.csv` with `inclusion_reason` and tier label.

**Verification rule:** Tier placement and candidacy are hypotheses until confirmed during collection. No municipality is in the corpus until inclusion criteria are documented.

---

## 3. Exclusion criteria

Exclude unconditionally:

| Exclusion | Examples / notes |
|-----------|------------------|
| **Purely national agencies** | National AI offices, ministries, regulators without a municipal programme document |
| **Regional governments** | Regions, länder, counties, provinces acting as primary publisher |
| **Private-sector organisations** | Vendor sites, consultancies, PPP entities without official municipal adoption |
| **Media-only visibility** | Press coverage of AI pilots with no primary municipal document trace |
| **Non-European jurisdictions** | Outside v0.1 geographic frame (EU, EEA, UK, Switzerland) |
| **Access-restricted documentation** | Intranet, login-gated, FOI-only materials |

---

## 4. Geographic and administrative frame

**Geographic scope (v0.1):** EU member states, EEA (Norway, Iceland, Liechtenstein), United Kingdom, Switzerland.

**Administrative tradition clusters** (analytic, not mutually exclusive):

| Cluster | Countries (illustrative) | Documentation culture note |
|---------|--------------------------|----------------------------|
| Nordic | DK, FI, IS, NO, SE | Strong open-government norms; advanced digital-government publication |
| Germanic | AT, CH, DE, NL (partial) | Formal administrative prose; federal complexity |
| Napoleonic | BE, ES, FR, IT, PT | Legalistic policy style; variable local autonomy |
| Anglo | IE, UK | Plain-language transparency; metropolitan structures |
| Central/Eastern | CZ, EE, LT, LV, PL, SI, etc. | Heterogeneous post-transition digital paths |
| Southern | GR, CY, MT, etc. | Smaller municipal capacity variance |

**Size bands** (using Eurostat LAU / national statistics at verification):

| Band | Population (indicative) | Target share of sample |
|------|-------------------------|------------------------|
| Large metro | > 500,000 | ~35% |
| Mid-size city | 100,000–500,000 | ~40% |
| Smaller city | 50,000–100,000 | ~25% |

Exact thresholds adjusted per country reporting; bands serve **variation**, not representativeness.

---

## 5. Candidate sampling frame (three tiers)

**Important:** The municipalities below are **proposed candidates** for the sampling frame. They are **not verified corpus members**. Inclusion requires collection-time confirmation against §2. No documents have been retrieved for this strategy document.

Tiers classify **expected AI governance visibility in public discourse** (strategies, registers, smart-city AI initiatives)—not municipal quality, readiness, or performance.

### Tier A — High visibility

Municipalities frequently referenced in European municipal digital-government and AI governance discourse; likely to publish strategies, registers, or transparency hubs (to be verified).

| Candidate | Country | Admin. tradition | Size band | Language(s) | Inclusion rationale |
|-----------|---------|------------------|-----------|-------------|---------------------|
| Amsterdam | NL | Germanic / mixed | Large metro | NL, EN | Longstanding smart-city and algorithmic transparency profile; expected high documentation visibility |
| Barcelona | ES | Napoleonic | Large metro | CA, ES | Public AI and digital rights discourse; metropolitan innovation visibility |
| Copenhagen | DK | Nordic | Large metro | DA, EN | Nordic open-government context; municipal AI policy attention |
| Helsinki | FI | Nordic | Large metro | FI, EN | National AI programme linkages; municipal digital leadership visibility |
| London (GLA / borough programme) | UK | Anglo | Large metro | EN | Algorithmic transparency tooling visibility; complex metropolitan structure—unit to be fixed at verification |
| Vienna | AT | Germanic | Large metro | DE | Public-sector innovation and city platform visibility |
| **Tier A target** | | | | | **6–8 verified municipalities** |

### Tier B — Moderate visibility

Municipalities with credible but less internationally prominent AI governance documentation profiles.

| Candidate | Country | Admin. tradition | Size band | Language(s) | Inclusion rationale |
|-----------|---------|------------------|-----------|-------------|---------------------|
| Bologna | IT | Napoleonic | Mid-size | IT | Italian municipal digital innovation; moderate international visibility |
| Gothenburg | SE | Nordic | Mid-size | SV, EN | Swedish municipal digitalisation; less global profile than Stockholm |
| Lyon | FR | Napoleonic | Large metro | FR | Major French city; AI and data policy at metropolitan scale |
| Munich | DE | Germanic | Large metro | DE | German municipal IT governance; federal context |
| Porto | PT | Napoleonic | Mid-size | PT | Portuguese smart-city activity; moderate visibility |
| Tallinn | EE | Central/Eastern | Mid-size | ET, EN | Digital-government reputation; smaller state context |
| **Tier B target** | | | | | **6–8 verified municipalities** |

### Tier C — Emerging visibility

Municipalities where AI governance documentation may be thinner or more recent—important for studying evidence gaps rather than only frontrunners.

| Candidate | Country | Admin. tradition | Size band | Language(s) | Inclusion rationale |
|-----------|---------|------------------|-----------|-------------|---------------------|
| Aarhus | DK | Nordic | Mid-size | DA | Second-city scale; potentially less documentation than capital |
| Braga | PT | Napoleonic | Smaller city | PT | Smaller Portuguese city; emerging digital programmes |
| Ghent | BE | Mixed Napoleonic/Germanic | Mid-size | NL | Belgian linguistic complexity; municipal AI visibility emerging |
| Thessaloniki | GR | Southern | Large metro | EL | Southern European capacity context; visibility to be verified |
| Trikala | GR | Southern | Smaller city | EL | Smaller Greek smart-city reference; emerging visibility |
| Zaragoza | ES | Napoleonic | Mid-size | ES | Regional city; less international visibility than Barcelona/Madrid |
| **Tier C target** | | | | | **4–6 verified municipalities** |

### Frame balance targets (post-verification)

| Dimension | Target |
|-----------|--------|
| Countries represented | ≥ 10 |
| Administrative traditions | ≥ 4 clusters |
| Tier A : B : C | roughly 35% : 40% : 25% |
| Size bands | per §4 shares ±10% |

**Replacement rule:** If a candidate fails inclusion at verification, replace with another candidate in the **same tier and similar country/tradition/size profile**, documenting the swap in manifest notes.

---

## 6. Target sample sizes

| Level | N municipalities | Rationale |
|-------|------------------|-----------|
| **Minimum sample** | **12** | Supports cross-country and cross-tier comparison across D1–D5; feasible solo coding (~60 observations per dimension at 1 doc/muni minimum) |
| **Preferred sample** | **18** | Better country and tradition coverage; allows document-type variation analysis in RQ3 |
| **Maximum feasible sample** | **24** | Upper bound for single researcher with quality control; beyond this, coding load threatens consistency without additional coders |

**Document target (guidance, not a stopping rule alone):**

| Level | Documents (total corpus) |
|-------|--------------------------|
| Minimum | 18 (≥1 primary doc per municipality) |
| Preferred | 30–45 (1–3 docs per municipality by type) |
| Maximum | 60 |

---

## 7. Stopping rules

### When is the corpus large enough?

Stop adding municipalities when **all** of the following are satisfied:

1. **Preferred sample size reached** (N = 18 verified municipalities), or maximum feasible (N = 24) if capacity allows.
2. **Variation quotas met** — country (≥10), administrative tradition (≥4 clusters), tier mix (§5), size bands (§4).
3. **Dimensional saturation (pilot check)** — after coding the first 12 municipalities, new cases yield predominantly familiar evidence-status patterns across D1–D5 (no new pattern classes in 3 consecutive municipalities). Record saturation decision in manifest notes.
4. **Document-type coverage** — corpus includes at least 4 municipalities with strategy-type docs, 4 with register/transparency-type docs, and 3 with procurement-linked docs (counts can overlap).

### When to stop adding municipalities early

Stop below preferred N only if:

- Inclusion verification failure rate exceeds 40% within a tier (frame revision required, not endless replacement).
- Translation or coding capacity bound is reached (document in `sampling_risks.md`).
- Minimum sample (N = 12) and variation quotas are already met with stable coding.

### When to continue past preferred N

Continue toward maximum (N = 24) only if:

- A specific country or tradition cluster is under-represented after quota check.
- Emerging Tier C cases are under-represented (risk of frontrunner-only bias).
- Additional coder capacity is available for reliability subsample.

**Never continue** solely to increase N without variation or saturation rationale.

---

## 8. Language strategy

### Multilingual documents

- Record `language` in corpus manifest (ISO 639-1 primary language per document).
- Municipalities publishing in multiple languages (e.g., CA/ES, NL/EN): code the **most complete governance version**; note alternate-language URLs in manifest `notes`.
- Do not merge language versions into one synthetic document; each URL is a separate manifest row if separately archived.

### Machine translation boundaries

Machine translation (MT) is permitted **only** for:

- Screening inclusion (identifying document type and AI governance relevance)
- Locating passages for `page_or_section` pointers

MT is **not sufficient alone** for fine-grained coding decisions without human verification. Final coding must be based on human-readable text (native, professionally translated excerpt, or MT + bilingual verification for short locators).

**MT-prohibited for final coding without verification:**

- Legal nuance distinctions affecting evidence-status labels
- Named-role identification (D1)
- Contract/procurement identifiers (D4)

### Coding consistency requirements

- Maintain a **translation log** in `docs/` (future): municipality, source, languages, MT tool (if any), verifier.
- Code in the **language of analysis** agreed per country cluster (typically English for cross-case synthesis; original quotes retained in `quoted_evidence` with translation note in `coder_notes`).
- Double-coding subset drawn from **native-language and MT-assisted** cases proportionally to assess label stability.

---

## 9. Archival strategy

### Source URL and access date

Every manifest row records:

| Field | Requirement |
|-------|-------------|
| `source_url` | Canonical official URL at retrieval |
| `access_date` | ISO 8601 date of first successful retrieval |
| `source_title` | As displayed on publication |
| `notes` | Redirect chains, alternate mirrors, paywall absence confirmed |

### Document versioning

1. **First retrieval** — record `access_date`; save optional WARC/PDF snapshot to `data/raw/` (gitignored; Zenodo deposit at release).
2. **Version changes** — if a document is materially updated during collection, create a **new manifest row** with new `access_date`; do not overwrite prior row.
3. **Link rot** — if URL breaks, document recovery via official archive or municipal portal search; if unrecoverable, mark source `excluded` with reason.
4. **Citation in manuscript** — cite manifest `source_url` + `access_date`; snapshot DOI from Zenodo release for long-term access.

### Archival release alignment

| Stage | Location | Git | Zenodo |
|-------|----------|-----|--------|
| Manifest metadata | `data/processed/corpus_manifest.csv` | gitignored when populated | v0.2.0+ |
| Snapshots | `data/raw/snapshots/` | gitignored | v0.2.0+ |
| Retrieval log | `data/raw/retrieval_log.csv` | gitignored | v0.2.0+ |

---

## 10. Collection workflow (planned — not executed)

```
1. Screen candidate municipality (tier hypothesis)
2. Verify inclusion criteria §2
3. Register in corpus_manifest_template.csv
4. Optional snapshot to data/raw/
5. Code D1–D5 per coding_template.csv
6. Check stopping rules §7
```

No step in this workflow has been executed for v0.1 strategy.

---

## 11. Alignment with non-claims

- Candidates are **not** scored or ranked
- Tier labels describe **expected visibility**, not municipal performance
- Verification may exclude any candidate without implication of failure
- Sampling serves Public-Document Observability comparison, not readiness scoring

See [`non_claims.md`](non_claims.md) and [`sampling_risks.md`](sampling_risks.md).

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-06-08 | Initial municipal sampling strategy; candidate frame without collection |
