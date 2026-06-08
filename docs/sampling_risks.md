# Sampling risks and mitigations v0.1

**Aligned with:** [`municipal_sampling_strategy_v0_1.md`](municipal_sampling_strategy_v0_1.md) · [`study_protocol_v0_1.md`](study_protocol_v0_1.md)

This register documents known risks in the municipal sampling design and mitigation strategies. It does not report empirical findings.

---

## 1. Selection bias

### Description
Purposive maximum-variation sampling is **not statistically representative** of all European municipalities. Frontrunners, digitally mature cities, and internationally visible cases may be over-represented in candidate frames drawn from public discourse.

### Why it matters
Patterns of observability may reflect **who publishes visibly**, not the average municipal documentation landscape. Reviewers may question generalisability.

### Mitigation
- Include **Tier C (emerging visibility)** municipalities alongside Tier A frontrunners
- Require **≥10 countries** and **≥4 administrative traditions**
- Mix **size bands** deliberately (§4 of sampling strategy)
- State **non-representativeness** explicitly in Method and Limitations
- Report sample composition table (country, tier, size, tradition) without ranking
- Use **replacement rule** within tier profiles to avoid cherry-picking only successful cases

---

## 2. Visibility bias

### Description
Municipalities with high public AI governance **visibility** (strategies, registers, conference presence) are easier to find and include than municipalities with quiet or minimal publication profiles.

### Why it matters
The study could over-sample **documentation-rich** cases, understating evidence gaps in the full municipal population—while still correctly describing gaps **within** the public record of included cases.

### Mitigation
- Tier structure forces inclusion of **moderate and emerging** visibility cases
- Inclusion criterion requires primary documents, not conference abstracts or media profiles
- Record `inclusion_reason` transparently in manifest
- Analyse **within-corpus** gap patterns; avoid population inference language
- Discussion section addresses visibility bias as boundary condition

---

## 3. Language bias

### Description
Documents in dominant European languages (EN, FR, DE, ES) are easier to code; smaller-language municipalities may be excluded or coded via machine translation with nuance loss.

### Why it matters
Observability patterns may correlate with **language accessibility** rather than documentation substance. Coders may miss indirect signals in unfamiliar languages.

### Mitigation
- Language strategy (§8 of sampling strategy): native + verified translation protocol
- Translation log for MT-assisted cases
- Proportional **double-coding** across language clusters
- Include Nordic, CEE, and Southern candidates with planned translation support
- Record `language` and translation method in manifest `notes`
- Limit MT to screening; human verification for final labels

---

## 4. Survivorship bias

### Description
Only municipalities whose documentation **survives** at access date (stable URLs, maintained registers) enter the corpus. Discontinued programmes, removed pages, and link rot exclude cases silently.

### Why it matters
Evidence gaps may appear lower than they are if failed or withdrawn documentation disappears from the public record before retrieval.

### Mitigation
- Record **failed retrieval attempts** in `data/raw/retrieval_log.csv` (planned)
- Document link rot and recovery attempts in manifest `notes`
- Archival snapshots at first retrieval (WARC/PDF) for included sources
- Version new rows on material updates; do not overwrite
- Limitations section acknowledges **snapshot temporality**

---

## 5. Documentation bias

### Description
Public documents reflect **what municipalities choose to publish**, shaped by political signalling, legal advice, vendor drafting, and administrative burden—not a neutral map of internal governance.

### Why it matters
The study observes **documentation practices**, not internal organisational reality. Thin public evidence does not prove thin internal practice.

### Mitigation
- Core non-claim: observability ≠ internal quality ([`non_claims.md`](non_claims.md))
- Evidence-status labels separate **commitments** from **named artefacts**
- Conceptual framework distinguishes transparency from programme-level evidence
- Reviewer attack map in [`paper_blueprint.md`](paper_blueprint.md)
- Avoid "governance failure" language throughout manuscript

---

## 6. Tier misclassification risk

### Description
Proposed tier labels (A/B/C) are **pre-collection hypotheses**. A Tier C candidate may prove documentation-rich; a Tier A candidate may fail inclusion.

### Mitigation
- Verify all inclusion criteria at collection; tier is annotative, not deterministic
- Allow tier relabelling post-verification in manifest `notes`
- Do not use tiers as analytic independent variables implying quality

---

## 7. Single-researcher capacity risk

### Description
Coding N municipalities × D1–D5 strains consistency and increases subjective drift over time.

### Mitigation
- Cap maximum sample at **N = 24**
- Double-code **≥15%** of observations
- Batch coding with protocol refreshes between batches
- Use structured labels (not Likert readiness scales)
- Pause collection if stopping rules met early at N = 12–18

---

## Risk summary table

| Risk | Severity | Detectability | Primary mitigation |
|------|----------|---------------|-------------------|
| Selection bias | High | Medium | Tier C + variation quotas + explicit limits |
| Visibility bias | High | Medium | Tier mix + non-population claims |
| Language bias | Medium | Medium | Translation protocol + double-coding |
| Survivorship bias | Medium | Low | Retrieval log + snapshots |
| Documentation bias | High | High | Non-claims + observability framing |
| Tier misclassification | Low | High | Verification at collection |
| Researcher capacity | Medium | Medium | Sample caps + stopping rules |

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-06-08 | Initial sampling risk register |
