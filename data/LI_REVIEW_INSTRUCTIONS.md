# Checking the passage translations against Li Rongxi (1996)

The map shows an English translation of each place's Xiyu ji passage: DharmaMitra's machine translation, already
checked (and where needed corrected) against Mizutani and Beal. This pass checks it once more against Li Rongxi's
complete English translation, *The Great Tang Dynasty Record of the Western Regions* (BDK English Tripiṭaka 79, 1996),
and corrects real errors. Li is a third reader, not an authority: the Chinese decides.

## Input

- `data/text/li_input_<group>.tsv`: `id`, `name_zh`, `t2087_ref`, `zh` (the Taishō passage, CBETA), `en_current`
  (the translation now on the map).
- Li's text: `data/ref/lit/C/li1996_great_tang_record.txt` (pdftotext of the dBET PDF; running heads and page numbers
  in the text). Find the matching passage by the country/site and its neighbours; Li follows the Chinese order.

## What to check

For each row compare `en_current` with the Chinese, using Li to catch misreadings. Look for: numbers and measures
(li, paces, feet, counts of monasteries, monks, stūpas), directions and bearings, who did what (subject/object),
negations, place and person names, omitted or added clauses, and terms Li reads differently. Where `en_current` and
Li differ, decide from the Chinese which is right. Differences of style, of spelling of names, or of Li's freer
wording are not errors. Do not import Li's wording; correct `en_current` minimally in its own style.

## Output (TSV, UTF-8, header exactly; `data/text/review3_li_<group>.tsv`)

| column | content |
|---|---|
| `id` | the row's id |
| `verdict` | `ok` (no error found), `minor` (a wrong detail: a number, a direction, a name, a dropped phrase), `major` (a misreading that changes the sense of a sentence or more) |
| `issues` | for `minor`/`major`: what was wrong and why, citing the Chinese words, e.g. `東南 read as "south-east of the city" but refers to the monastery: 伽藍東南…`; empty for `ok` |
| `en_revised` | for `minor`/`major`: the whole corrected translation (`en_current` with the fixes; keep its style, italics with `*…*` as there); empty for `ok` |
| `li_quote` | for `minor`/`major`: Li's words on the point, **verbatim** from the file (copy, OCR line breaks may be joined with a space), ≤ 250 chars; may be empty if Li is wrong too or silent |
| `li_page` | the printed page number in Li near the passage, if you can see it |

Write one row for **every** input row. Check with `python3 -I scripts/check_li_quotes.py data/text/review3_li_<group>.tsv`
from `xuanzang-places/` until it reports `bad 0`. Report: rows by verdict; the `major` ones in one line each; places
where Li himself misreads the Chinese (useful to know, not to fix).
