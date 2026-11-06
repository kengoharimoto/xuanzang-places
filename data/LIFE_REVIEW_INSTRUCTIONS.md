# Checking the Life translations against the Chinese

Inputs: `data/text/life_passages.tsv` (id, mode, t_ref, zh — the passage of the *Life*, T2053, for each place),
`data/text/life_translation_dm.tsv` (id, en — DharmaMitra machine translation), `data/places_mizutani.tsv` (names),
Beal's translation of the Life (`data/ref/beal1911_life.txt`, OCR; *The Life of Hiuen-Tsiang*, 1911) as an aid, and the
checked *Xiyu ji* translation of the same place in `data/places.tsv` (column `translation`) for consistent name forms.

**Beal has no precedence** (the user's instruction): he is an aid for spotting problems; the Chinese decides. Where
DharmaMitra is right and Beal differs, keep DharmaMitra (`ok`). Beal's Life often abridges; do not import his
omissions or paraphrases.

Write `data/text/life_review_<range>.tsv`, header exactly `id	verdict	issues	en_revised`, one row per id in your
range that has a Life passage:
- Read the Chinese, the DharmaMitra English, Beal's English for the same passage.
- `verdict`: `ok` (faithful; differences only of style), `minor` (small slips: a number, a term, a dropped clause of no
  consequence), `major` (a mistranslation that changes meaning — a wrong direction or distance, a wrong subject or
  speaker, a misread name, a clause omitted or invented, a garbled episode).
- `issues`: short list, each "phrase in DM → what the Chinese says (Beal: …)". Empty if ok.
- `en_revised`: only for `minor` and `major`: the **whole** passage's English with your corrections, otherwise keeping
  DharmaMitra's wording and conventions (Sanskrit name with the Chinese in brackets on first occurrence; li; the
  Master of the Law 法師 for Xuanzang where the text says 法師). Where the Chinese is genuinely ambiguous, keep DM's
  reading and note the alternative in `issues`.
- Gaiji codes like `&CB05882;` stand for rare characters; infer from context and say so in `issues` if it matters.
- Pay special attention to distances, bearings, numbers of days, and place names: these feed the route tests.

Check your file: every id with a Life passage in your range has one row; `en_revised` is filled for every minor/major
row and empty for ok rows; no tabs or newlines inside fields.

Report: verdict counts; every `major` (id, one line); and any distance, bearing or name where the Life differs from
the *Xiyu ji* in a way that matters for identification.
