# Non-claims register

This document states what the **municipal-ai-evidence-gaps** artifact explicitly does **not** claim or measure. It is a boundary instrument for researchers, reviewers, municipalities, and archival users.

**Editorial authority:** [`global_editorial_style_guide.md`](global_editorial_style_guide.md)

## Analytic positioning

The artifact conducts **Public-Document Observability** analysis of public municipal AI documentation. It records what governance-relevant **observable evidence** appears in publicly accessible sources and what **evidence gaps** remain unavailable for independent **Programme-Level Governance Readiness** assessment.

Observability findings are **not** proxies for organisational quality, legal status, or operational performance.

---

## Canonical non-claims

This project maintains, across all documents and outputs:

- **no readiness scoring**
- **no municipal ranking**
- **no legal compliance determination**
- **no LocalGovBench validation**
- **no inference of internal governance quality**

---

## Extended register

### Readiness and ranking

- Does not perform **readiness scoring** — no readiness index or similar metric is produced
- Does not perform **municipal ranking** — no ordinal comparisons or "top/bottom" city lists

### Benchmark validation

- Does not perform **LocalGovBench validation** — this study does not test, confirm, or refute LocalGovBench items or scores
- Does not serve as a benchmarking substitute — observability coding is documentary, not instrument validation

### Inference beyond public evidence

- Does not permit **inference of internal governance quality** — silence or thin public documentation is not interpreted as poor internal practice
- Does not infer undocumented practices — coders do not speculate about non-public workflows, meetings, or controls

### Legal and compliance

- Does not perform **legal compliance determination** — including EU AI Act or national transposition
- Does not claim legal non-compliance — `not_observable_publicly` is not equivalent to unlawful conduct or regulatory breach
- Does not provide legal advice — outputs are research artefacts, not counsel

### Technical evaluation

- Does not evaluate model performance — accuracy, fairness metrics, bias testing, and model benchmarks are out of scope
- Does not audit live systems — no runtime inspection, API probing, or shadow testing of municipal services

### Data ethics

- Does not process personal data — personal identifiers, citizen records, and case-level data are excluded from collection and coding
- Does not collect non-public data — administrative records, internal audits, and restricted procurement files are out of scope

---

## What the artifact does instead

| Instead of… | The artifact… |
|-------------|---------------|
| Readiness scoring | Labels evidence status per dimension in public documentation |
| Municipal ranking | Compares observability patterns descriptively |
| Legal compliance determination | Maps what is publicly documented vs. not observable |
| LocalGovBench validation | Documents evidence gaps relevant to governance assessment |

---

## Required coder acknowledgement

Every coding row includes `non_claim_boundary` set to the v0.1 constant defined in `src/evidence_gaps/schema.py`. This field reminds downstream users that rows are observability records bounded by this register.

---

## Version

Non-claims register v0.1.1 — aligned with [`global_editorial_style_guide.md`](global_editorial_style_guide.md).
