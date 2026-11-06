# Cutting the Xiyu ji into one passage per place

Goal: for every row of `data/places_mizutani.tsv` in your juan range, mark the passage of the *Da Tang Xiyu ji*
(T2087) that describes that place. The passages are then translated by DharmaMitra (`scripts/translate_passages.py`)
and shown with the translation in `places.tsv` and the map.

Source text: `data/ref/t2087_cb_joined.txt` — CBETA's T2087 with real characters (no gaiji codes), CBETA punctuation,
one sentence per line, page markers `[T51:NNNNx]`. Mizutani's section numbering (the master `id`) follows the text's
order. (The master table's `t_route` comes from a different edition with gaiji codes and other punctuation; use it only
to find the place, not as an anchor.)

Write `data/text/anchors_<range>.tsv`, header exactly `id	mode	anchor	end_anchor	note`, one row per master id in your
range, in master-table order:
- `segment` — the place has its own stretch of text (a country, or a site with its own description). `anchor` = the
  first 8–20 characters of that stretch, copied verbatim from `t2087_cb_joined.txt` (no page markers; punctuation as
  in that file). The passage runs to the next segment's anchor; so give **sub-sites their own anchors** where the
  text moves on to them, and let the country row cover the country's general description up to its first site.
  For the **last segment of each juan**, give `end_anchor` = the last characters of that juan's text (before the next
  `卷第…`), so it does not run on.
- `excerpt` — the place is only mentioned inside another place's passage (a capital, a river, a neighbouring hearsay
  country named in passing). `anchor` = start and `end_anchor` = end of the sentence(s) mentioning it.
- `note` — anything odd ("no separate section; excerpt from the country description").

Narrative between places (legends, jātakas) belongs to the preceding place's passage; that is intended.

Run `python3 -I scripts/extract_passages.py data/text/anchors_<range>.tsv` and read your ids' rows in
`data/text/passages_<range>.tsv`: each passage must begin and end where you intend, with nothing in your juans left out.
Fix anchors until it reports no errors for your ids.

Report: ids covered (segment / excerpt / none, with reasons for none), total characters, and anything odd.
