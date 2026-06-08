# Municipal AI Evidence Gaps

Public research artifact supporting:

**When Transparency Is Not Enough: Evidence Gaps in Municipal AI Governance**  
*A Comparative Analysis of European Municipal AI Documentation*

## Project purpose

This repository supports a **comparative observability analysis** of public municipal AI governance documentation in Europe.

The study examines what public documents make observable and what programme-level evidence remains unavailable for independent governance assessment. The working claim under investigation:

> Public municipal AI documentation is often visible at the level of principles and commitments but thinner at the level of evidence needed for independent programme-level governance assessment.

The artifact is designed for reproducible documentary coding, descriptive reporting, and **Zenodo** archival release alongside the GIQ manuscript.

## Study boundaries

This project is **observability analysis**, not benchmark validation or compliance auditing.

| In scope | Out of scope |
|----------|--------------|
| Public municipal AI governance documents | Non-public or access-restricted records |
| Five observability dimensions (D1–D5) | Municipal readiness scoring |
| Four evidence-status labels | City rankings or league tables |
| Descriptive evidence-gap patterns | LocalGovBench validation |
| Zenodo-ready protocol and templates | AI Act compliance determinations |
| | Personal data processing |
| | Model performance evaluation |

Full boundary register: [`docs/non_claims.md`](docs/non_claims.md)  
Research design v0.1: [`docs/research_design_v0_1.md`](docs/research_design_v0_1.md)  
Study protocol v0.1: [`docs/study_protocol_v0_1.md`](docs/study_protocol_v0_1.md)  
Conceptual model: [`docs/conceptual_model.md`](docs/conceptual_model.md)  
Journal positioning: [`docs/journal_positioning.md`](docs/journal_positioning.md)  
Manuscript blueprint: [`docs/paper_blueprint.md`](docs/paper_blueprint.md)  
GIQ storyline: [`docs/giq_storyline.md`](docs/giq_storyline.md)  
Coding protocol: [`docs/coding_protocol.md`](docs/coding_protocol.md)

## Repository structure

```
municipal-ai-evidence-gaps/
├── data/
│   ├── raw/                              # Retrieval logs (future)
│   ├── interim/                          # Normalised staging (future)
│   └── processed/
│       ├── corpus_manifest_template.csv  # Manifest schema (v0.1)
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
│   ├── coding_protocol.md                # D1–D5 coding sheets
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

**Not included in v0.1:** scraped corpora, coded results, rankings, readiness scores, or compliance findings.

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
| Corpus collection | **Not started** |
| Coding (D1–D5) | **Not started** |
| Results / findings | **None available** |

No municipal documents have been collected. No websites have been scraped. No municipalities are named in the repository. The project remains at the **publishable study design** stage prior to empirical work.

## Status

**v0.1 research design and protocol complete.** Corpus collection and coding have not started. No real municipal data, scraped content, or results are included.

## License

CC BY 4.0 — see [`LICENSE`](LICENSE).
