# Coding 季羨林等《大唐西域記校注》(1985) as an authority

Ji Xianlin et al., *Da Tang Xiyu ji jiaozhu* (Beijing: Zhonghua, 1985; 中外交通史籍叢刊) is the standard modern
commentary and the first post-1971 scholarship in this study. OCR: `data/ref/ji1985.txt`, in page blocks headed
`=== pdf NNNN`. The printed page number is usually on the first or last line of the block; give the printed page.
The book has a long introduction (前言), then the text juan by juan. Each passage of the text is followed by numbered
notes (〔一〕〔二〕… or ①②…) with the identifications, and the book ends with indexes. The commentators cite
Cunningham, Watters, Beal, 堀謙德, 水谷真成, Stein, Foucher, and Indian, Pakistani, Afghan and Chinese archaeology up to
c. 1980.

## Part 1. Coding → `data/coded/auth_ji_<range>.tsv`

For **every** place in your juan range (rows of `data/places_mizutani.tsv` and `data/places_added.tsv`, ids beginning
with your juans), find Ji's note(s). Header exactly:

`id	name_zh	authority	name_in_source	identification	stance	others_reported	page	source_file	quote	note`

- `authority` = `ji`;
- `source_file` = `ji1985.txt`;
- `name_in_source`: the Sanskrit or other form Ji gives;
- `identification`: Ji's own identification, in concise English;
- `stance`: `firm`, `tentative`, `rejects` or `none given`;
- `others_reported`: the views Ji reports, with names (e.g. `Cunningham: X; Mizutani: Y; Stein: Z`);
- `quote`: verbatim from the OCR, ≤ 300 chars, fragments joined with `…` (each ≥ 12 chars);
- `note`: anything after 1971 that Ji cites (excavations, inscriptions, Chinese, Japanese or Russian scholarship), and
  whether Ji differs from Mizutani.

Write no row for places Ji does not discuss. Then run
`python3 -I scripts/check_quotes_ref.py data/coded/auth_ji_<range>.tsv` and fix the quotes until it reports no bad
ones. That checker looks quotes up in `data/ref/<source_file>`.

Report: the number of rows, the places where Ji differs from Mizutani (one line each), and the post-1971 evidence Ji
cites that the study does not already have.
