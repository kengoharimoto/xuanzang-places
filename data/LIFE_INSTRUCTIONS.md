# Marking the Life's parallel passage for each place

Goal: for every row of `data/places_mizutani.tsv` in your juan range, mark the passage of Huili and Yancong's *Life*
(大唐大慈恩寺三藏法師傳, T2053) that describes the same place, if there is one. The passages are translated
(`scripts/translate_passages.py`) and shown beside the *Xiyu ji* passage in `places.tsv` and on the map.

Source text: `data/ref/t2053_joined.txt` (CBETA/SAT text of T2053, one sentence per line, page markers `[T50:NNNNx]`,
a few gaiji codes like `&CB05882;`). The pilgrimage is in fascicles 1–5. The Life follows the journey in order,
names many of the same countries (often with the same transcriptions), and adds events (stays, teachers, debates,
dangers), sometimes with different distances or routes.

For each master id in your range, write one row to `data/text/life_anchors_<range>.tsv`, header exactly
`id	mode	anchor	end_anchor	note`:
- `excerpt` — the Life mentions or describes the place. `anchor` = the first 8–20 characters of the relevant stretch,
  copied verbatim from `t2053_joined.txt` (no page markers); `end_anchor` = the last 8–20 characters of it (inclusive).
  Take the stretch that concerns this place: its arrival sentence and description, and events there. Keep it to
  the place: if the Life spends pages on a debate at Kanauj, include the arrival and the description and stop
  before the long narrative (say so in `note`). Typical length 50–600 characters; up to ~1500 for major places.
- `none` — the Life does not mention the place (anchor and end_anchor empty). Many sites (stūpas, minor legends) and
  hearsay countries are absent from the Life; that is expected.
- `note` — anything useful: a different distance or bearing in the Life, a different name form, an event the
  *Xiyu ji* lacks, or "only named in passing".

A site that the Life mentions only inside its country's passage can share text with the country row; that is fine.
The rows must be in master-table order.

Run `XZ_TEXT=life python3 -I scripts/extract_passages.py data/text/life_anchors_<range>.tsv` and read your rows in
`data/text/life_passages_<range>.tsv`: each passage must begin and end where you intend. Fix anchors until it reports
no errors.

Report: ids with excerpts / none, total characters, and the most interesting differences between the Life and the
*Xiyu ji* in your range (distances, routes, names, events).
