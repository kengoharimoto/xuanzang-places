# Coding the gazetteer passages on Xuanzang's places

Input: `data/gaz_hits.tsv`: one row per mention of Xuanzang (`kind` = `xuanzang`, any old spelling: Hiuen Tsiang,
Hwen Thsang, Yuan Chwang…), of "the Chinese pilgrim" (`chinese_pilgrim`), or of Faxian (`faxian`) in the British
Indian district/provincial gazetteers (1870s–1930s, some later). Columns: `hit, identifier, vol, place, year,
series, kind, match, line, context` (context = ~1,200 characters around the match, whitespace collapsed; the full
OCR is the file `<identifier>.txt` under `../gazetteer-vedanta/*/data/ia_ocr/` or `../yoga-gazetteers/*/data/ia_ocr/`
— open it at `line` if the context is cut off).

Master table: `data/places_mizutani.tsv` (columns include `id`, `name_zh`, `original_name`, `mz_identification`,
`mz_other_views`, `mz_status`). Authorities' views: `data/coded/auth_*.tsv` if present.

Goal: for each hit, say whether it bears on **where a place in the *Xiyu ji* (or Huili's *Life*) is**, and if so
what the gazetteer says and what local evidence it adds. We want especially:
- the gazetteer's identification, and whether it simply repeats Cunningham/Beal/etc. or argues its own;
- **local evidence**: mounds, ruins, tanks, old names of villages, inscriptions, coins, finds, excavations, local
  traditions, changed river courses, measured distances;
- **local identifications** that differ from the standard ones (Mizutani's / the authorities').

## Columns (TSV, UTF-8, header exactly as below; one row per hit in your batch — every hit gets a row)

| column | content |
|---|---|
| `hit` | from `gaz_hits.tsv` |
| `identifier` | from `gaz_hits.tsv` |
| `relevant` | `yes` if the passage locates or discusses the location of a Xuanzang (or Faxian) place; `no` otherwise (biographical mentions, generic "the Chinese pilgrim found Buddhism declining", false OCR matches). Faxian-only passages: `yes` only if the place is also in the *Xiyu ji*. |
| `xz_id` | master-table `id` of the place (several separated by `;`), `new` if it is a *Xiyu ji* place missing from the table (say which in `note`), empty if `relevant=no` |
| `name_in_gaz` | how the gazetteer names the Xuanzang place (e.g. `Kie-shwang-na`, `Kapilavastu`, `Sravasti`) |
| `gaz_identification` | the site the gazetteer identifies it with (modern names, as written) |
| `stance` | `repeats` (cites/follows an authority without new argument), `argues` (gives its own reasons), `doubts` (questions the standard identification), `alternative` (proposes a different site), `reports` (lists views without deciding) |
| `authority_cited` | who the gazetteer cites: `Cunningham`, `Beal`, `Fergusson`, `Waddell`, `Führer`, `V. A. Smith`, ASI report, local officer, etc. |
| `local_evidence` | concise English summary of any local evidence (see list above); empty if none |
| `quote` | **verbatim** from the OCR (copy, don't retype), ≤ 400 chars, the sentence(s) giving the identification and evidence; join non-adjacent fragments with `…` (each ≥ 12 chars). Empty only if `relevant=no`. |
| `note` | short: disagreement with Mizutani's identification, OCR problems, cross-references to other hits |

## Checks

Run `python3 -I scripts/check_quotes_gaz.py data/coded/<your file>.tsv` from `xuanzang-places/` and fix until
`bad 0`. In your reply: number of hits coded, number relevant; a list of the passages that **argue, doubt or
propose alternatives** (hit, place, one line); and any `new` places.
