# Coding Mizutani's notes into the master table

Goal: one TSV row per country (国) and per locatable site in the *Da Tang Xiyu ji*, recording what **Mizutani
Shinjō** (水谷真成訳『大唐西域記』, 平凡社 中国古典文学大系 22, 1971) says about where it is. This table is the
backbone of the project; other authorities are added later. Code what Mizutani says, not what you know: if he
gives no identification, leave the field empty and say so in `mz_note`.

## Sources

- **Mizutani OCR**: `data/mizutani/mizutani_ocr.txt` (whole book; each page begins with a marker
  `<<pdf NNN | p. NN>>`) and per page `data/mizutani/vision/pNNN.txt`. pdf page = scan index; printed page =
  pdf − 18 in the body. The OCR is good but not perfect (e.g. 覩貨邏 may appear as 観貨邏/親貨邏; ruby readings
  appear as stray short kana lines, sometimes interleaved). Page images are in `data/mizutani/pages/pNNN.png`
  if you need to look at a page (use the Read tool on the PNG).
- **Taishō text** (T2087), one sentence per line: `data/ref/t2087_joined.txt`, with page markers `[T51:867b]`.
- Book structure: each juan opens with a list of its countries. Sections are numbered `N` (country) and `N・M`
  (sub-section) within the juan, e.g. `二〇・一 鉄門`, `四・三 迦膩色迦大塔`. Each section = Mizutani's
  translation, then `注` with numbered notes (`一 <lemma> <note>`). The note on the country name usually gives the
  Middle Chinese reading (e.g. `puo-tâ-lâk-ka`), the Sanskrit / original name, and the identification with
  references ([Cunningham: …], [Beal: …], [Watters: …], [足立: …], [高桑: …], [堀: …] etc.).
- Visited or hearsay: Mizutani marks hearsay countries in the notes ("伝聞国である", "(伝聞国)"). The 讃 rule: route
  sentences with 行 = visited (親践), with 至 only = hearsay (伝聞). Record both Mizutani's statement (if any) and
  what the Taishō route sentence says.

## Which rows

1. **Every country** in the juan's country list (the list at the head of the juan; check against T2087). Include
   countries "appended" (付出) and the hearsay ones. Also major regions with a 総記 (e.g. 覩貨邏国総記).
2. **Sites**: a sub-section `N・M` gets its own row when it is about a place one could locate (city, capital,
   monastery, stūpa, mountain, pass, river, lake, cave, battlefield…) *and* either Mizutani gives a location /
   identification or Xuanzang gives a distance/direction to it. Skip purely narrative sub-sections (jātaka tales,
   legends, doctrinal stories) unless the note locates the spot. Also add rows for named places inside a section
   whose notes carry an identification (e.g. a city or river with its own note), using `id` with a suffix
   (`02.04.03a`).
   Don't create rows for every stūpa mentioned in passing; prefer fewer rows with real content.

## Columns (tab-separated, UTF-8, header row exactly as below; no tabs or newlines inside fields)

| column | content |
|---|---|
| `id` | `JJ.NN` for a country, `JJ.NN.MM` for a sub-section (Arabic numerals from Mizutani's numbering: juan 2, section 4, sub 3 → `02.04.03`); suffix a letter for extra places inside one section. Preface/general sections: `01.00.01` etc. |
| `juan` | 1–12 |
| `level` | `country`, `region` (総記, 境 groupings), or `site` |
| `parent` | for a site, the `id` of its country |
| `name_zh` | name in Taishō form (traditional characters, as in T2087), e.g. 覩貨邏國. Correct OCR errors here (not in `quote`). |
| `name_ja` | Mizutani's section heading as he gives it (OCR corrected), e.g. 覩貨邏国総記 |
| `mc_reading` | Mizutani's Middle Chinese reconstruction if given (e.g. `tuo-xuâ-lâ`) |
| `original_name` | Sanskrit / Prakrit / Iranian / Turkic name(s) as Mizutani gives them (e.g. `Skt. Tukhāra`) |
| `route` | Xuanzang's itinerary into this place as Mizutani translates it, compressed: `from <prev>; <dir> <n>里` (e.g. `from 羯霜那國; SW 200余里 + SE 300余里`). Empty if none. |
| `t_route` | the Taishō route sentence copied **verbatim** from `data/ref/t2087_joined.txt` (it is checked by script), e.g. `東南山行三百餘里入鐵門。` Empty if none. |
| `t_verb` | `行` if the route sentence contains 行, `至` if only 至 (or 入/到 without 行 — then write that character), empty if none |
| `visit` | `visited`, `hearsay`, or `unclear` |
| `visit_basis` | why: `Mizutani: 伝聞国`, `t_verb 行`, `Life (慈恩伝) per Mizutani`, etc. |
| `mz_identification` | Mizutani's own identification in English/romanized, concise: modern place name(s), river, region, country, coordinates if given; e.g. `Kunduz region (Qunduz), N Afghanistan`. |
| `mz_other_views` | other identifications Mizutani reports, each with its authority: `Cunningham: X; Watters: Y; 足立: Z`. |
| `mz_refs` | the references Mizutani cites for the identification, as he cites them (e.g. `Cunningham: Anc. Geog. p.48; Watters I p.102; 高桑:研究 p.384`). |
| `mz_status` | how Mizutani presents it: `agreed` (stated as settled / no rival view), `disputed` (he reports rival views or says 諸説/異説/不明確), `uncertain` (he hedges: であろう, かと思う, 未詳 without rivals), `unknown` (未詳 / no identification) |
| `pdf_page` | pdf page of the quote (the page marker number) |
| `printed_page` | printed page number |
| `quote` | **verbatim** passage from the OCR on `pdf_page` (or running onto the next page) that supports `mz_identification` (or, if none, the note itself): copy exactly as it is in the OCR, including OCR errors; whitespace and line breaks may be dropped. Up to ~250 characters; join non-adjacent fragments with `…` (each fragment ≥ 6 characters). |
| `mz_note` | anything else useful, short: e.g. "Mizutani follows 足立; notes the river has shifted", "no identification given", "OCR doubtful: Kusāna?" |

## Checks before you finish

- Run `python3 -I scripts/check_quotes.py data/coded/<your file>.tsv` from `xuanzang-places/`, and fix every BAD row
  (usually: the quote was retyped instead of copied, or the page number is wrong). It must end with `bad 0`.
- Every country in the juan's list has a row. Report the count per juan.
- No invented content: identifications and readings come from Mizutani's text; mark doubts in `mz_note`.
