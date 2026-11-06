# Notes on the places the study has not yet assessed

The map shows the study's view: each place's point and the study's confidence come from the notes' assessments
(`data/notes/updates_*.tsv`). Places without a note show as "untested". Your job: write a note and an updates row for
each id listed in `data/notes/untested_ids_<k>.txt`. Most are places Mizutani marks "agreed" that nobody disputes;
some are places added from the sources (`mz_status = added`, ids ending `.xN`, see `data/places_added.tsv`).

## Evidence (all in `data/`)

- `places.tsv`, one row per place. It has columns for:
  - Mizutani and the authorities;
  - the gazetteers (`gaz_*`), the ASR (`asr*`), the Annual Reports (`ar*`), *Epigraphia Indica* and CII (`epig*`)
    and *Indian Archaeology – A Review* (`iar*`), each with its evidence;
  - the Xiyu ji passage and translation (`t2087_text`, `translation`);
  - the Life passage (`life_*`);
  - religion.
- The detail behind those columns:
  - `coded/*.tsv`, with indexes `*_hits.tsv`;
  - `places_mizutani.tsv` (Mizutani's quote and other views);
  - `coded/auth_*.tsv`.
- Route tests:
  - `../route/candidate_scores.tsv` (each candidate's fit to Xuanzang's distances and bearings);
  - `../route/chain_best.tsv` and `chain_best_life.tsv` (where the best-fitting combination departs from Mizutani);
  - `../route/segment_tests.tsv`.
- For added places: their row in `places_added.tsv` (identification, sources) and `coords_added.tsv`.
- Existing notes (`notes/notes_*.md`) show the style. Read a few, including those on the place's parent country.

## Each note (Markdown, in `notes/notes_untested_<k>.md`, in master-table order)

```
### <id> <name_zh> (<original_name>) — <one-line verdict>

**Identifications.** Mizutani (or, for added places, the sources): … Authorities that say something, grouped.
**Evidence.** Only what exists: survey, excavations, inscriptions, gazetteers, the Life, route test. Cite briefly
(source, year, page / passage number).
**Assessment.** One to three sentences: is the identification secure, probable or open on this evidence?
```

Length: 40–150 words. A place with nothing beyond agreement among the authorities gets a two-line note saying so.
Keep to the evidence in these files. Later scholarship you know of may be mentioned only as "later work (not in these
sources) …", in one clause.

## Updates rows (`notes/updates_untested_<k>.tsv`)

Header exactly `id	name_zh	mizutani	proposed	change	basis	confidence`. One row per id in your list.
- `change`: `none` (Mizutani stands), `strengthened`, `weakened`, `alternative` or `new-candidate`, as in
  `data/NOTES_INSTRUCTIONS.md`. For added places use `none` when the sources' identification stands.
- `confidence`:
  - `high`: site evidence such as an excavation, an inscription naming the place, or a standing monument matching the
    description, plus agreement among the sources;
  - `medium`: the authorities agree and nothing contradicts them, but there is no site evidence;
  - `low`: little evidence, or the evidence conflicts.

Agreement alone is medium, not high.

## Finish

Report: the number of notes; the counts by confidence; every place where `change` ≠ `none`, one line each; and any
data problem you notice (do not fix coded files).
