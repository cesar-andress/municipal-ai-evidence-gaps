# Release notes — v1.0.4

**Date:** 2026-06-15  
**DOI:** [10.5281/zenodo.20603415](https://doi.org/10.5281/zenodo.20603415)  
**GitHub tag:** [v1.0.4](https://github.com/cesar-andress/municipal-ai-evidence-gaps/tree/v1.0.4)  
**Manuscript:** *Transparency Instruments That Disclose Least: Genre Inversion in Municipal AI Governance Documentation* (GIQ submission)

## Summary

Release **v1.0.4** is the **final manuscript-linked artifact release** for GIQ submission. It aligns repository metadata, citation files, and documentation with the genre-inversion contribution hierarchy and manuscript title. **Frozen full-corpus numerals, coding results, tables, figures, protocol v0.1.1, sensitivity outputs, and IRR statistics are unchanged** from v1.0.2/v1.0.3.

## Changed in v1.0.4 (metadata and documentation only)

- `CITATION.cff`, `pyproject.toml`, and `README.md` — version **1.0.4**, final manuscript title, contribution hierarchy (genre inversion primary)
- Linked documentation (`docs/giq_storyline.md`, `docs/research_design_v0_1.md`, etc.) — title and framing alignment
- Manuscript availability statements and Method §4.5 — cite Zenodo/GitHub **v1.0.4**
- Manuscript Discussion §6.1 — construct-validity clarification (genre-neutral coding rules; no scientific or numeric changes)

## Unchanged scientific content

- `data/processed/coding_results_v0_1_1.csv` (115 rows)
- `outputs/reports/results_freeze_v1.md`
- Protocol v0.1.1 and coding decision rules
- Retrieved-only sensitivity reports and IRR materials (κ = 0.81; 40 cells)

## Reproduce

```bash
git checkout v1.0.4
pip install -e ".[dev]"
python3 scripts/sensitivity_analysis.py
python3 scripts/irr_compute_agreement.py --worksheet data/processed/irr_coding_worksheet_v1.csv
```

## Supersedes

- [RELEASE_NOTES_v1.0.2.md](RELEASE_NOTES_v1.0.2.md) — obsolete; retained for history only
