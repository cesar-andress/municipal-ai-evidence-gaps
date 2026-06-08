# Non-claims register

This document states what the **municipal-ai-evidence-gaps** artifact explicitly does **not** claim or measure. It is a boundary instrument for researchers, reviewers, municipalities, and archival users.

## Analytic positioning

The artifact conducts **observability analysis** of public municipal AI documentation. It records what governance-relevant evidence appears in publicly accessible sources and what remains unavailable for independent programme-level assessment.

Observability findings are **not** proxies for organisational quality, legal status, or operational performance.

---

## This artifact does not

### Readiness and ranking

- **Measure municipal readiness** — no readiness index, maturity score, or governance-capacity metric is produced
- **Rank municipalities** — no league tables, ordinal comparisons, or "top/bottom" city lists

### Benchmark validation

- **Validate LocalGovBench** — this study does not test, confirm, or refute LocalGovBench items or scores
- **Serve as a benchmarking substitute** — observability coding is documentary, not instrument validation

### Inference beyond public evidence

- **Infer internal governance quality** — silence or thin documentation in public sources is not interpreted as poor internal practice
- **Infer undocumented practices** — coders do not speculate about non-public workflows, meetings, or controls

### Legal and compliance

- **Assess AI Act compliance** — no legal compliance determination for the EU AI Act or national transposition
- **Claim legal non-compliance** — `not_observable_publicly` is not equivalent to unlawful conduct or regulatory breach
- **Provide legal advice** — outputs are research artefacts, not counsel

### Technical evaluation

- **Evaluate model performance** — accuracy, fairness metrics, bias testing, and model benchmarks are out of scope
- **Audit live systems** — no runtime inspection, API probing, or shadow testing of municipal services

### Data ethics

- **Process personal data** — personal identifiers, citizen records, and case-level data are excluded from collection and coding
- **Collect non-public data** — administrative records, internal audits, and restricted procurement files are out of scope

---

## What the artifact does instead

| Instead of… | The artifact… |
|-------------|---------------|
| Readiness scoring | Labels evidence status per dimension in public documents |
| Ranking cities | Compares observability patterns descriptively |
| Compliance audit | Maps what is publicly documented vs. not observable |
| Benchmark validation | Documents evidence gaps relevant to governance assessment |

---

## Required coder acknowledgement

Every coding row includes `non_claim_boundary` set to the v0.1 constant defined in `src/evidence_gaps/schema.py`. This field reminds downstream users that rows are observability records bounded by this register.

---

## Version

Non-claims register v0.1 — aligned with `docs/study_protocol_v0_1.md`.
