# Municipal AI Evidence Gaps

Public research artifact supporting:

**When Transparency Is Not Enough: Evidence Gaps in Municipal AI Governance**  
*A Comparative Analysis of European Municipal AI Documentation*

## Project purpose

This repository supports a **comparative observability analysis** of public municipal AI governance documentation in Europe.

The study examines what public documentation makes observable and what programme-level evidence remains unavailable for independent governance assessment. The working claim under investigation:

> Public municipal AI documentation is often visible at the level of principles and commitments but thinner at the level of evidence needed for independent programme-level governance assessment.

The artifact is designed for reproducible documentary coding, descriptive reporting, and **Zenodo** archival release alongside the GIQ manuscript.

## Research questions

**RQ1.** What governance evidence is publicly observable in municipal AI documentation?

**RQ2.** Which governance dimensions are systematically under-observable?

**RQ3.** What patterns of transparency and evidence gaps emerge across municipalities and document types?

*Discussion implication (not an empirical RQ):* What are the implications of these evidence gaps for independent governance assessment based on public documentation alone?

## Study boundaries

This project is **Public-Document Observability** analysis. Canonical non-claims: no readiness scoring; no municipal ranking; no legal compliance determination; no LocalGovBench validation; no inference of internal governance quality.

| In scope | Out of scope |
|----------|--------------|
| Public municipal AI governance documents | Non-public or access-restricted records |
| Five observability dimensions (D1–D5) | Readiness scoring |
| Four evidence-status labels | Municipal ranking |
| Descriptive evidence gap patterns | LocalGovBench validation |
| Zenodo-ready protocol and templates | Legal compliance determination |
| | Personal data processing |
| | Model performance evaluation |

Full boundary register: [`docs/non_claims.md`](docs/non_claims.md)  
Editorial style guide: [`docs/global_editorial_style_guide.md`](docs/global_editorial_style_guide.md)  
Research design v0.1: [`docs/research_design_v0_1.md`](docs/research_design_v0_1.md)  
Study protocol v0.1: [`docs/study_protocol_v0_1.md`](docs/study_protocol_v0_1.md)  
Conceptual model: [`docs/conceptual_model.md`](docs/conceptual_model.md)  
Journal positioning: [`docs/journal_positioning.md`](docs/journal_positioning.md)  
Manuscript blueprint: [`docs/paper_blueprint.md`](docs/paper_blueprint.md)  
GIQ storyline: [`docs/giq_storyline.md`](docs/giq_storyline.md)  
Sampling strategy: [`docs/municipal_sampling_strategy_v0_1.md`](docs/municipal_sampling_strategy_v0_1.md)  
Tier A verification protocol: [`docs/tier_a_verification_protocol.md`](docs/tier_a_verification_protocol.md)  
Sampling risks: [`docs/sampling_risks.md`](docs/sampling_risks.md)  
Coding protocol: [`docs/coding_protocol.md`](docs/coding_protocol.md) (v0.1.1)  
Coding decision rules: [`docs/coding_decision_rules_v0_1_1.md`](docs/coding_decision_rules_v0_1_1.md)

## Repository structure

```
municipal-ai-evidence-gaps/
├── data/
│   ├── raw/                              # Retrieval logs (future)
│   ├── interim/                          # Normalised staging (future)
│   └── processed/
│       ├── corpus_manifest_template.csv  # Manifest schema (v0.1)
│       ├── corpus_manifest_v0_1.csv      # Initial corpus manifest (v0.1)
│       ├── corpus_manifest_quality_flags_v0_1.csv  # Pre-coding quality flags
│       ├── coding_results_v0_1_1.csv       # Full-corpus D1–D5 coding (v0.1.1)
│       ├── tier_a_verification.csv       # Tier A screening results
│       ├── coding_template.csv           # Coding schema (v0.1)
│       ├── corpus_manifest.csv           # Working manifest (gitignored)
│       └── coding_dataset.csv            # Working coding data (gitignored)
├── docs/
│   ├── research_design_v0_1.md           # Publishable study design
│   ├── study_protocol_v0_1.md            # Operational study protocol
│   ├── conceptual_model.md               # Theoretical model + diagram
│   ├── journal_positioning.md            # Target journal analysis
│   ├── paper_blueprint.md                # Full manuscript blueprint
│   ├── giq_storyline.md                  # GIQ narrative arc
│   ├── municipal_sampling_strategy_v0_1.md  # Sampling frame (v0.1)
│   ├── tier_a_verification_protocol.md   # Tier A screening protocol
│   ├── sampling_risks.md                 # Bias register and mitigations
│   ├── global_editorial_style_guide.md   # Canonical terminology and non-claims
│   ├── editorial_consistency_audit.md    # Consistency audit log
│   ├── coding_protocol.md                # D1–D5 coding sheets (v0.1.1)
│   ├── coding_decision_rules_v0_1_1.md   # Decision trees and tie-breaks
│   ├── non_claims.md                     # Boundary register
│   ├── methodology.md
│   ├── data_dictionary.md
│   └── ethics_and_privacy.md
├── scripts/
│   ├── collect_sources.py
│   ├── build_corpus_index.py
│   ├── code_observability.py
│   └── export_tables.py
├── src/evidence_gaps/                    # Schema and analysis package
├── notebooks/
├── outputs/                              # Generated tables and reports
└── tests/
```

## Observability dimensions (v0.1)

| ID | Dimension |
|----|-----------|
| D1 | Programme ownership |
| D2 | Human oversight and review |
| D3 | Prompt, log, and data governance |
| D4 | Procurement and vendor stewardship |
| D5 | Incident, audit, and lifecycle accountability |

## Evidence status labels (v0.1)

- `observable_named_artifact`
- `observable_policy_commitment`
- `partial_or_indirect_signal`
- `not_observable_publicly`

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Or:

```bash
pip install -r requirements.txt
pip install -e .
```

## Workflow

1. `scripts/collect_sources.py` — initialise corpus manifest scaffold
2. `scripts/build_corpus_index.py` — normalise manifest entries
3. `scripts/code_observability.py` — apply D1–D5 coding protocol
4. `scripts/export_tables.py` — export descriptive summary tables

Templates: copy `data/processed/*_template.csv` when starting a new coding tranche.

## Planned v0.1 release contents

Zenodo tag **`v0.1.0`** will include:

- Study protocol v0.1 (`docs/study_protocol_v0_1.md`)
- Coding protocol with D1–D5 dimension sheets
- Non-claims register
- Python schema (`src/evidence_gaps/schema.py`) and tests
- CSV templates for corpus manifest and coding
- Empty working scaffolds (no municipal data rows)
- Documentation for methodology, ethics, and data dictionary

**Not included in v0.1:** scraped corpora, coded results, municipal ranking, readiness scoring, or legal compliance determination.

## Zenodo release plan

| Version | Contents |
|---------|----------|
| `v0.1.0` | Protocol, schema, templates, documentation (current milestone) |
| `v0.2.0` | Pilot corpus manifest and coding dataset |
| `v1.0.0` | Full analysis corpus and manuscript-linked exports |

Each release receives a versioned DOI. `CITATION.cff` will be updated with the Zenodo DOI upon first deposition.

## Citation

```bibtex
@software{municipal_ai_evidence_gaps_v01,
  title  = {Municipal AI Evidence Gaps: Public Documentation Corpus and Analysis Artifact},
  author = {TBD},
  year   = {2026},
  version = {0.1.0},
  url    = {https://github.com/TBD/municipal-ai-evidence-gaps},
  note   = {Zenodo DOI pending}
}
```

See also [`CITATION.cff`](CITATION.cff).

## Research design status

| Milestone | Status |
|-----------|--------|
| Research design v0.1 | Complete |
| Study protocol v0.1 | Complete |
| Conceptual model | Complete |
| Journal positioning (GIQ primary) | Complete |
| Manuscript blueprint | Complete |
| GIQ storyline | Complete |
| Sampling strategy v0.1 | Complete |
| Tier A verification | **Complete** (6 candidates screened; 6 eligible; no coding) |
| Corpus collection | **Complete** (v0.1 manifest; 23 official sources; no scraping) |
| Corpus quality audit | **Complete** (v0.1 pre-coding audit; 28 flags; no manifest changes) |
| Pilot coding | **Complete** (3-document protocol test) |
| Coding protocol | **v0.1.1** (pilot refinements applied) |
| Full corpus coding | **Complete** (v0.1.1; 115 rows; 23 sources) |
| Results / findings | **None available** (coded observations only) |

The initial corpus manifest registers **23 official municipal source URLs** across six Tier A–verified municipalities. Full-corpus D1–D5 coding (v0.1.1) produced **115 coded observations** in [`data/processed/coding_results_v0_1_1.csv`](data/processed/coding_results_v0_1_1.csv). No paper findings or pattern analysis are included.

**Sampling strategy status:** complete  
**Tier A verification status:** complete — screening only; see [`outputs/reports/tier_a_verification_report.md`](outputs/reports/tier_a_verification_report.md)  
**Corpus inventory status:** complete — manifest only; see [`outputs/reports/corpus_inventory_report.md`](outputs/reports/corpus_inventory_report.md)  
**Corpus quality audit status:** complete — pre-coding audit; see [`outputs/reports/corpus_quality_audit_v0_1.md`](outputs/reports/corpus_quality_audit_v0_1.md)  
**Pilot coding status:** complete — protocol validation only; see [`outputs/reports/pilot_coding_protocol_test.md`](outputs/reports/pilot_coding_protocol_test.md) and [`outputs/reports/coding_protocol_refinement_log.md`](outputs/reports/coding_protocol_refinement_log.md)  
**Coding protocol version:** v0.1.1 — see [`docs/coding_protocol.md`](docs/coding_protocol.md), [`docs/coding_decision_rules_v0_1_1.md`](docs/coding_decision_rules_v0_1_1.md), [`outputs/reports/protocol_change_log_v0_1_1.md`](outputs/reports/protocol_change_log_v0_1_1.md)  
**Full corpus coding status:** complete — see [`outputs/reports/coding_summary_v0_1_1.md`](outputs/reports/coding_summary_v0_1_1.md) and [`outputs/reports/coding_decision_log_v0_1_1.md`](outputs/reports/coding_decision_log_v0_1_1.md)

## Status

**v0.1 research design, corpus manifest, pilot coding test, coding protocol v0.1.1, and full-corpus coding complete.** Coded observations only; no paper findings or municipal comparisons are included.

## License

CC BY 4.0 — see [`LICENSE`](LICENSE).
