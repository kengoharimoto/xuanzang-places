# Coding recent scholarship (1985–2026)

The study's sources stop at Ji (1985) for the commentary and at *Indian Archaeology – A Review* 2000–01 for
excavation. This pass adds later work: excavation and survey reports, articles and books that argue, test, confirm or
move the location of a Xiyu ji place. The bibliography is `data/literature.tsv` (one row per item, with its status);
`data/LITERATURE.md` says what has been done and which PDFs are still wanted.

## Input

- Texts: `data/ref/lit/<group>/<key>.txt` (gitignored with the rest of `data/ref/`), made from the PDF with
  `pdftotext`, or OCR'd with Google Vision where the PDF has no text layer. Groups: A juan 1 and 12, B juan 2–3,
  C juan 4–7, D juan 8–9, E juan 10–11, X general.
- The place table: `data/places.tsv`; the study's current view of each place: `data/study_view.tsv`
  (`identification`, `confidence`, `change`) and the notes in `data/notes/notes_*.md`.

## Columns (TSV, UTF-8, header exactly; `data/coded/lit_batchN.tsv`)

Same as the Survey reports (`data/ASR_INSTRUCTIONS.md`), so the build and the checker treat them alike, plus `year`:

| column | content |
|---|---|
| `passage` | `<key>:<n>`, numbering the claims within one item |
| `file` | path under `data/ref/lit/`, e.g. `A/yamauchi2020_akbeshim.txt` |
| `author` | surname(s) as in the citation (`Coningham et al.`, `Deeg`, `Kuwayama`) |
| `year` | year of publication |
| `relevant` | `yes` if the passage locates or discusses the location of a Xiyu ji place or a site Xuanzang describes in it; else `no` |
| `xz_id` | id(s) from `places.tsv`, `;`-separated; `new` for a place missing from the table (name it in `note`) |
| `name_in_asr` | the name as the source writes it |
| `asr_identification` | the site the source identifies (modern names as written; add district/province/country) |
| `stance` | `proposes` (new identification argued here), `confirms` (new evidence for an existing one), `revises` (moves an earlier one), `rejects` (only rejects one), `reports` (cites others without deciding) |
| `evidence` | in English, the evidence itself: what was dug, found, read or measured; dates; inscriptions and what they name |
| `page` | printed page if visible, else the PDF page as `pdf N` |
| `quote` | **verbatim** from the text file (copy, don't retype; any language), ≤ 400 chars, the sentence(s) stating the identification and its key evidence; join non-adjacent fragments with `…` (each ≥ 12 chars) |
| `note` | how it bears on the study's current identification (`study_view.tsv`) and on Mizutani's: agrees / adds evidence / differs (say how) |

One row per claim: an article that treats three places gets three rows. Code only what the source argues or reports
with evidence; a passing mention that repeats an old identification is `relevant=no` unless it adds something.

## Check

From `xuanzang-places/`: `python3 -I scripts/check_quotes_asr.py data/coded/lit_batchN.tsv` until `bad 0`.

## Report

Rows coded / relevant; for each place where the item **differs** from the study's identification or gives **site
evidence** (excavation, an inscription naming the place, a matching monument): id, place, one line.

# Folding into the notes

For each place with relevant rows, add or extend `**Recent scholarship.**` before **Assessment.** in its note
(`data/notes/notes_*.md`): who, when, what evidence, page; 1–4 sentences per source, wrapped at 118 characters.
Revise the Assessment and the `data/notes/updates_*.tsv` row only where the evidence changes the picture. The
confidence rule stays: high only with site evidence (excavation, an inscription naming the place, a matching
monument); medium = agreement among authorities; low = little or conflicting evidence; a name match alone never gives
high. Where the sources conflict and the evidence is not decisive, record the alternatives and leave the place open.
