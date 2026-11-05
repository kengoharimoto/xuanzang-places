# Coding the standard authorities' identifications

The master table (`data/places_mizutani.tsv`, built from `data/coded/mz_juan*.tsv`) has one row per country/site
with Mizutani's identification. This step adds, for each row, what **one authority** says. One agent per
authority; one output file per authority: `data/coded/auth_<authority>.tsv`.

## Reference texts (all in `data/ref/`; OCR, so expect errors and no page markers except printed page numbers
embedded in the running text)

| authority key | file | notes |
|---|---|---|
| `cunningham` | `cunningham1871_agi.txt` | Majumdar Sastri's 1924 edition of *Ancient Geography of India* (1871). Majumdar's own notes add later identifications: code them as authority `majumdar` in the same file, rows separate from Cunningham's. |
| `watters` | `watters1904_vol1.txt`, `watters1905_vol2.txt` | Watters discusses earlier identifications critically; record his own view and those he reports. |
| `beal` | `beal1884_vol1.txt`, `beal1884_vol2.txt` | Identifications are mostly in the footnotes. |
| `vivien` | `julien1858_vol2_with_vivien.txt` | Vivien de Saint-Martin, "Mémoire analytique sur la carte de l'Asie centrale et de l'Inde" at the end of Julien vol. 2 (French). Also the `julien` key for Julien's own Sanskrit restitutions/notes if they include a location. |
| `dey` | `dey1927.txt` | N. L. Dey, *Geographical Dictionary* (1927): alphabetical by Sanskrit name; entries often cite Xuanzang (as Hiuen Tsiang) and give modern sites. |

## Rows

For **every** row of `data/places_mizutani.tsv` (countries and sites), search your authority's text for the place
(Sanskrit name in its old spellings — Kapisa/Kia-pi-shi/Kapiśa…, the Chinese transcription in Wade/old French
romanisation, Beal's/Julien's forms, the modern candidate names in `mz_identification` and `mz_other_views`).
Write one row per place for which the authority gives a location or identification. If the authority discusses
the place but gives no location, write a row with `identification` = `none given`. If the place is not discussed,
write no row (the merge will show it as blank).

## Columns (TSV, UTF-8, header exactly as below; no tabs/newlines inside fields)

| column | content |
|---|---|
| `id` | the master table `id` |
| `name_zh` | from the master table (for readability) |
| `authority` | the key above |
| `name_in_source` | the place name as this authority writes it (e.g. `Kia-pi-shi`, `Kapiśa`) |
| `identification` | the authority's own identification, concise English: modern place / ruin / region (and coordinates or distances if given) |
| `stance` | `firm`, `tentative` (probably, perhaps, may be), `rejects` (only rejects others' views), `none given` |
| `others_reported` | other identifications the authority reports, with names: `Cunningham: X; Saint-Martin: Y` |
| `page` | printed page number if you can find it in the OCR near the passage (running heads / page numbers), else empty |
| `source_file` | file name in `data/ref/` |
| `quote` | **verbatim** from the file (copy, don't retype; OCR errors included), ≤ 300 chars; join non-adjacent fragments with `…` (each ≥ 12 chars) |
| `note` | short: disagreement with Mizutani, OCR doubts, etc. |

## Checks

Run `python3 -I scripts/check_quotes_ref.py data/coded/auth_<authority>.tsv` from `xuanzang-places/` and fix rows
until `bad 0`. Report: rows written; master rows you could not find in the source; the places where your
authority's identification differs from Mizutani's (`id`, both views, one line each).
