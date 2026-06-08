# Research design v0.1

**Paper working title:** When Transparency Is Not Enough: Evidence Gaps in Municipal AI Governance  
**Subtitle:** A Comparative Analysis of European Municipal AI Documentation  
**Design version:** 0.1  
**Date:** 2026-06-08  
**Status:** Design complete; empirical collection not started

**Related documents:** [`study_protocol_v0_1.md`](study_protocol_v0_1.md) · [`conceptual_model.md`](conceptual_model.md) · [`journal_positioning.md`](journal_positioning.md)

---

## 1. Research objective

To develop and apply a **public-document observability framework** for municipal AI governance, examining what programme-level evidence European municipalities make visible in official documentation and where systematic evidence gaps limit independent external assessment.

The study tests the working proposition that municipal AI documentation is frequently **transparent at the level of principles and commitments** but comparatively **thin at the level of evidence required for programme-level governance assessment**—ownership, oversight routines, data and log governance, vendor stewardship, and lifecycle accountability.

The design is **descriptive and comparative**. It does not score readiness, rank municipalities, validate benchmarking instruments, or determine legal compliance.

---

## 2. Research questions

Three research questions organise the empirical work:

### RQ1 — Observable evidence

**What governance evidence is publicly observable in municipal AI documentation?**

This question maps the presence of governance-relevant information across five observability dimensions (D1–D5) and four evidence-status labels. It asks what external reviewers can actually see—not what municipalities may do internally.

### RQ2 — Under-observable dimensions

**Which governance dimensions are systematically under-observable?**

This question identifies dimensions where public documentation most often yields `partial_or_indirect_signal` or `not_observable_publicly` rather than `observable_named_artifact`. It foregrounds structural documentation deficits rather than municipal failure.

### RQ3 — Cross-municipal patterns

**What patterns of transparency and evidence gaps emerge across municipalities?**

This question compares how observability profiles vary across municipalities and document types (strategies, registers, transparency pages, procurement disclosures). Comparison is **pattern-oriented**, not ordinal ranking.

---

## 3. Theoretical motivation

Municipal AI governance sits at the intersection of digital government, algorithmic accountability, and local administrative capacity. Three theoretical streams motivate the design:

**Transparency as necessary but insufficient.** Open-government scholarship has long treated publication as a precondition for accountability. Algorithmic transparency initiatives extend this logic to registers, impact assessments, and disclosure pages. Yet transparency research also warns that disclosure can be symbolic—making *something* visible without furnishing evidence that enables meaningful oversight (Meijer & Curtin, 2018; de Blok & Schuilenburg, 2023).

**Accountability requires traceable evidence chains.** Accountability theory distinguishes answerability, enforceability, and the availability of documentary trails that connect decisions to responsibilities (Bovens, 2007; Lindblom, 2022). Programme-level governance assessment depends on observable artefacts—named roles, review routines, logs, contracts, audit outputs—not aspirational language alone.

**Administrative burden and ceremonial compliance.** Public organisations face competing demands: publish quickly to signal responsiveness, while building the documentation infrastructure that sustained governance requires (Moynihan et al., 2018; Peeters & Schuilenburg, 2023). The result may be **ceremonial compliance**: publicly acceptable governance forms that outpace the evidentiary substance needed for independent evaluation.

This study contributes by treating **public-document observability** as a distinct analytic construct—what governance evidence is structurally available to outsiders—rather than inferring internal quality from publication presence alone.

---

## 4. Unit of analysis

| Level | Unit | Role in design |
|-------|------|----------------|
| **Primary** | Evidence observation | One coded judgement per municipality × source × dimension (D1–D5) |
| **Secondary** | Source document | Public municipal AI governance artefact (strategy, register, transparency page, etc.) |
| **Tertiary** | Municipality | Jurisdiction whose public documentation is compared descriptively |

The primary unit keeps analysis anchored in **locatable public evidence**. Municipalities enter the design as contexts for comparative pattern description, not as ranked cases.

---

## 5. Public-document observability

**Public-document observability** is the degree to which governance-relevant information about a municipal AI programme can be identified, quoted, and categorised from **publicly accessible official documentation** at a given access date.

Observability is not equivalent to:

- internal governance quality
- legal compliance
- operational maturity
- benchmark scores

It is an **epistemic boundary** concept: it marks what independent reviewers can know from the public record. Four evidence-status labels operationalise observability:

| Label | Interpretation |
|-------|----------------|
| `observable_named_artifact` | Concrete, locatable governance artefact |
| `observable_policy_commitment` | Explicit commitment without programme-level detail |
| `partial_or_indirect_signal` | Fragmentary or implied mention |
| `not_observable_publicly` | No relevant public evidence in coded sources |

See [`coding_protocol.md`](coding_protocol.md) for dimension-specific coding rules.

---

## 6. Relationship to Programme-Level Governance Readiness

**Programme-level governance readiness** refers to whether a municipal AI programme has the documented structures—ownership, oversight, data governance, vendor accountability, lifecycle controls—that would allow an external actor to assess how the programme is governed over time.

This study **does not measure readiness**. Instead, it examines the **observability conditions** under which readiness assessment from public documents alone would be possible or constrained.

| Readiness concept | This study's relationship |
|-------------------|---------------------------|
| Ownership and accountability structures | Observed via D1; gaps limit external verification |
| Oversight routines | Observed via D2; thin documentation constrains assessment |
| Traceability (logs, prompts, data) | Observed via D3; often under-documented publicly |
| Vendor governance | Observed via D4; procurement visibility varies |
| Lifecycle accountability | Observed via D5; post-deployment evidence often sparse |

The design hypothesis is that **principles and commitments are more observable than programme-level readiness evidence**—a pattern with implications for benchmarking, audit, and democratic oversight that rely on public documentation.

---

## 7. Relationship to transparency

Transparency is the **visibility mechanism** through which municipalities communicate AI governance intentions to publics, regulators, and researchers. This study treats transparency as an empirical object: what is published, in what form, with what specificity.

The design distinguishes:

- **Transparency of commitment** — strategies, ethical principles, high-level goals (often observable)
- **Transparency of operation** — logs, review cadences, vendor terms, incident routes (often under-observable)

RQ1 and RQ3 directly interrogate this distinction. The title claim—*when transparency is not enough*—refers to cases where transparency artefacts exist but do not supply programme-level evidence.

---

## 8. Relationship to accountability

Accountability requires that actors can **observe**, **question**, and **sanction** (Bovens, 2007). Public documentation is a key channel through which municipal AI programmes become answerable to councils, citizens, and oversight bodies.

Evidence gaps are **accountability limitations** for external reviewers: if ownership, oversight, or lifecycle artefacts are not publicly observable, accountability relations cannot be enacted through the public record alone. The study documents these limitations without inferring that accountability is absent internally.

---

## 9. Relationship to ceremonial compliance

**Ceremonial compliance** occurs when organisations adopt governance forms—strategies, ethics statements, register shells—that signal conformity with expectations while substantive programme evidence remains thin (Meyer & Rowan, 1977; Bromley & Powell, 2012).

In municipal AI governance, ceremonial compliance may appear as:

- published responsible-AI principles without named programme owners
- register existence without per-system oversight detail
- transparency pages that restate national frameworks without local implementation evidence

The coding protocol separates `observable_policy_commitment` from `observable_named_artifact` precisely to capture this distinction. The design does **not** label municipalities as ceremonially compliant; it maps where public documentation exhibits commitment-heavy, evidence-light patterns.

---

## 10. Relationship to administrative burden

Publishing and maintaining governance documentation imposes **administrative burden** on municipalities with limited digital governance capacity (Moynihan et al., 2018). AI governance amplifies this burden: registers, log policies, vendor disclosures, and lifecycle documentation require cross-departmental coordination.

Evidence gaps may reflect:

- capacity constraints rather than deliberate opacity
- recent programme launches before documentation matures
- reliance on vendors whose governance artefacts are not publicly mirrored

The research design records gaps descriptively and discusses burden as a **plausible explanatory context** in the discussion section—not as a measured causal variable in v0.1.

---

## 11. Expected contributions

### Contribution 1 — Public-document observability as a governance concept

The study introduces and operationalises **public-document observability** as an analytic construct for digital government research, distinguishing visibility of commitments from availability of programme-level evidence.

### Contribution 2 — Evidence-gap analysis for municipal AI governance

The study provides a comparative empirical account of **where** evidence gaps concentrate across governance dimensions and document types, advancing municipal AI governance scholarship beyond presence/absence of strategies or registers.

### Contribution 3 — Reusable coding protocol and open corpus infrastructure

The study releases a documented coding protocol (D1–D5), schema, templates, and open analysis infrastructure designed for replication, extension, and Zenodo archival—without producing readiness scores or municipal rankings.

---

## 12. Methodological overview

| Phase | Activity | Status (v0.1) |
|-------|----------|---------------|
| Design | Research design, conceptual model, journal positioning | Complete |
| Protocol | Study protocol, coding protocol, non-claims | Complete |
| Collection | Public document manifest assembly | Not started |
| Coding | D1–D5 observability coding | Not started |
| Analysis | Descriptive pattern summaries | Not started |
| Release | Zenodo v0.2+ with corpus | Planned |

Operational details: [`study_protocol_v0_1.md`](study_protocol_v0_1.md).

---

## 13. Design boundaries (non-claims summary)

- No municipal readiness scoring
- No city rankings
- No LocalGovBench validation
- No AI Act compliance determination
- No personal data processing
- No non-public data collection

Full register: [`non_claims.md`](non_claims.md).

---

## References (indicative)

- Bovens, M. (2007). Analysing and assessing accountability: A conceptual framework. *European Law Journal*.
- Bromley, P., & Powell, W. W. (2012). From smoke and mirrors to walking the talk. *Academy of Management Annals*.
- de Blok, C., & Schuilenburg, M. (2023). Algorithmic transparency in the public sector. *Government Information Quarterly*.
- Lindblom, L. (2022). AI governance in public sector institutions. *Information Polity*.
- Meijer, A., & Curtin, D. (2018). Reconciling accountability and transparency. *Perspectives on Politics*.
- Meyer, J. W., & Rowan, B. (1977). Institutionalized organizations. *American Journal of Sociology*.
- Moynihan, D. P., et al. (2018). Administrative burden. *Journal of Public Administration Research and Theory*.
- Peeters, R., & Schuilenburg, M. (2023). Algorithmic governmentality. *Philosophy & Technology*.

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-06-08 | Initial publishable research design; three RQs and three contributions |
