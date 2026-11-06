# Two jobs per place: check the translation, and code religious affiliation

Inputs: `data/text/passages.tsv` (id, mode, t_ref, zh — the CBETA T2087 passage for each place), `data/text/translation_dm.tsv`
(id, en — DharmaMitra machine translation), `data/places_mizutani.tsv` (`pdf_page` = page of Mizutani's notes on the
place; his Japanese translation of the passage is on the same or the preceding pages of `data/mizutani/mizutani_ocr.txt`,
markers `<<pdf NNN | p. NN>>`), Beal (`data/ref/beal1884_vol1.txt` juan 1–5, `beal1884_vol2.txt` juan 6–12; OCR).

**Mizutani and Beal have no precedence** (the user's instruction): they are aids for spotting problems; the
Chinese decides. Where DharmaMitra is right and they differ, keep DharmaMitra (`ok`).

## A. Translation check → `data/text/review_<range>.tsv`

Header exactly: `id	verdict	issues	en_revised`
- Read the Chinese, the DharmaMitra English, Mizutani's Japanese for the same passage, and Beal's.
- `verdict`: `ok` (faithful; differences only of style), `minor` (small slips: a number, a term, a dropped clause of no
  consequence), `major` (a mistranslation that changes meaning — a wrong direction or distance, a wrong subject, a
  misread name, a clause omitted or invented, a garbled legend).
- `issues`: short list, each "phrase in DM → what the Chinese says (Mizutani: …; Beal: …)". Empty if ok.
- `en_revised`: only for `minor` and `major`: the **whole** passage's English with your corrections, otherwise keeping
  DharmaMitra's wording. Keep its conventions (Sanskrit name with Chinese in brackets on first occurrence; li; *italics*
  for terms). Do not import Mizutani's interpretations beyond what the Chinese says; where the Chinese is genuinely
  ambiguous, keep DM's reading and note the alternative in `issues`.
- Mizutani may follow a variant reading or emend the text; if so, translate the CBETA text and note the variant.

## B. Religious affiliation → `data/religion/religion_<range>.tsv`

Header exactly: `id	sangharamas	monks	schools	deva_temples	other	site_affiliation	buddhism	quote	note`
One row per id with a passage. From the passage itself (and the country description, for countries):
- `sangharamas`, `monks`: as stated (e.g. `100+`, `5000+`, `few`, `none`), empty if not stated.
- `schools`: Buddhist affiliation stated, as normalised codes separated by `;`:
  `Mahayana`, `Hinayana` (小乘 unspecified), `Sarvastivada` (說一切有部), `Sammatiya` (正量部), `Sthavira` (上座部),
  `Mahayana-Sthavira` (大乘上座部), `Mahasanghika` (大眾部), `Lokottaravada` (說出世部), `Dharmaguptaka`,
  `Mahisasaka`, `Kasyapiya`, `both` (大小二乘兼習 / 兼功習學), `other:<name>`. Use Mizutani's notes to confirm the
  Sanskrit of the school name.
- `deva_temples`: number of 天祠 as stated (e.g. `100+`, `dozens`).
- `other`: non-Buddhist traditions named, codes separated by `;`: `Jain-Digambara` (露形, 離繫, 尼乾), `Jain-Svetambara`
  (白衣), `Jain` (unspecified), `Saiva` (大自在天/Maheśvara, Śiva temples), `Pasupata` (塗灰, 灰塗), `Kapalika` (髑髏,
  skull-garlanded), `Surya` (日天, sun temple), `Devi` (大自在天妃, Bhīmā etc.), `Brahmanical` (婆羅門 learning, 外道
  unspecified), `heretics-many` (異道雜居 etc.), `other:<name>`. Only what the text says or Mizutani identifies.
- `site_affiliation` (for sites; also for a country's notable sites): `Buddhist-stupa`, `Buddhist-monastery`,
  `Buddhist-image`, `Buddhist-relic`, `Buddhist-legend`, `deva-temple`, `Jain-site`, `natural` (mountain, river, lake
  with no shrine), `city`, `other:<…>`; several allowed.
- `buddhism`: state of Buddhism the text reports for the place: `flourishing`, `mixed` (Buddhists and others),
  `declining` (ruined monasteries, few monks), `absent` (不信佛法 / 少信佛法), or empty.
- `quote`: the decisive Chinese phrase(s) verbatim from the passage (e.g. `伽藍十餘所，僧徒三千餘人，並學小乘說一切有部。天祠數十，異道雜居。`), ≤ 120 characters, fragments joined with `…`.
- `note`: e.g. Mizutani's identification of a sect name, or "露形 = Digambara Jains (Mizutani)".

## Check and report
Run `python3 -I scripts/check_religion.py data/religion/religion_<range>.tsv` (quotes must occur in the passage).
Report: verdict counts; every `major` (id, one line); affiliation counts (countries by school; places with Jain, Śaiva,
Pāśupata, Kāpālika, Sūrya); anything odd.
