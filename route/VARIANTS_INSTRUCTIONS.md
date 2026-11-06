# Comparing the route figures across the three texts (option 6)

For every route segment in your range of `route/segments.tsv` that has a distance (`li_lo`) or a bearing — i.e.
Xuanzang's statement "from A go <dir> <n> li to B" — find the same leg in:
- **T2088 釋迦方志** (Daoxuan, 650; abridges the Xiyu ji, sometimes with different figures): `data/ref/t2088_joined.txt`
- **T2053 慈恩傳** (Huili/Yancong, the *Life*; often a different route or different figures): `data/ref/t2053_joined.txt`
- **Mizutani's notes on variant readings** of T2087 itself (宋本・元本・明本・宮本・古写本・石山寺本・興聖寺本, 『方志』,
  『伝』, 他本…), in `data/mizutani/mizutani_ocr.txt` near the place's section (page markers `<<pdf NNN | p. NN>>`).

Texts carry Taishō page markers like `[T51:0953a]` inline; quote the text **without** the markers.

## Output columns (TSV, header exactly)

`id, name_zh, t2087_legs, t2088_text, t2088_legs, t2088_ref, t2053_text, t2053_legs, t2053_ref, mz_variant, mz_pdf_page, differs, note`

- `t2087_legs`: copy `legs` from `route/segments.tsv` (e.g. `西南 200+ + 東南 300+`).
- `t2088_text` / `t2053_text`: **verbatim** clause(s) giving the leg (copy; ≤ 120 chars; non-adjacent pieces joined with `…`, each ≥ 4 chars). Empty if the text has no corresponding leg.
- `t2088_legs` / `t2053_legs`: same notation as `t2087_legs`.
- `t2088_ref` / `t2053_ref`: the nearest preceding page marker (e.g. `T51:0953a`).
- `mz_variant`: Mizutani's statement of a variant reading or emendation for this leg, **verbatim** from the OCR (≤ 150 chars), else empty; `mz_pdf_page` its pdf page.
- `differs`: `none`, `li` (different distance), `bearing`, `li+bearing`, `route` (the Life goes a different way / skips or adds a place), `absent` (no corresponding leg in either), with the text(s) that differ in `note` (e.g. "2088: 五百 for 七百").
- `note`: short — what differs and whether the variant would change an identification (e.g. "the Life's 50 li fits Kosam where 500 does not").

Every segment in your range with `li_lo` gets a row, even when all agree (`differs = none`).

## Check

`python3 -I route/check_variants.py route/variants_<range>.tsv` (from `xuanzang-places/`) until bad 0. Report: rows; rows
with `differs` ≠ none (id, place, the variants, one line each); where a variant changes the fit of an identification.
