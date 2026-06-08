# Municipal AI Evidence Gaps

Public research artifact supporting:

**When Transparency Is Not Enough: Evidence Gaps in Municipal AI Governance**  
*A Comparative Analysis of European Municipal AI Documentation*

## Purpose

This repository supports a comparative analysis of **public municipal AI documentation** in Europe. It studies what public documents make observable and what remains unavailable for governance-readiness assessment.

The project maps evidence gaps across publicly accessible strategies, registers, transparency pages, and related governance artefacts. Findings are descriptive and comparative.

## What this repository does

- Catalogues publicly accessible municipal AI governance documents
- Codes observability of governance-relevant categories in public materials
- Produces reproducible tables and reports from the documentary corpus
- Documents methodology, data definitions, and coding protocols for archival release

## What this repository does **not** do

- **Does not score municipal readiness** — no readiness index or maturity model is produced
- **Does not rank cities** — municipalities are not ordinally compared for performance
- **Does not claim legal compliance** — documentary gaps are not treated as legal findings
- **Does not use non-public data** — only publicly accessible documents are in scope

## Design for archival release

This repository is structured for release on GitHub and deposition on **Zenodo** alongside the associated GIQ manuscript. Versioning, citation metadata (`CITATION.cff`), and open licensing are included from the outset.

## Repository layout

```
municipal-ai-evidence-gaps/
├── data/
│   ├── raw/           # Source manifests and retrieval logs (no scraping yet)
│   ├── interim/       # Intermediate normalised records
│   ├── processed/     # Analysis-ready coded corpus
│   └── external/      # Third-party reference materials
├── docs/              # Methodology and protocol documentation
├── scripts/           # Collection and analysis entry points
├── src/evidence_gaps/ # Core Python package
├── notebooks/         # Exploratory analysis
├── outputs/           # Generated tables, figures, and reports
└── tests/             # Unit tests for schema and coding logic
```

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Or with `requirements.txt`:

```bash
pip install -r requirements.txt
pip install -e .
```

## Workflow (planned)

1. `scripts/collect_sources.py` — build source manifest from public URLs
2. `scripts/build_corpus_index.py` — normalise corpus metadata
3. `scripts/code_observability.py` — apply coding protocol
4. `scripts/export_tables.py` — export manuscript-ready outputs

## Status

Initial scaffold only. No real data, web scraping, or results are included yet.

## Citation

See `CITATION.cff`. A Zenodo DOI will be added upon release.

## License

See `LICENSE` (CC BY 4.0).
