# Xuanzang's places

**Question.** Where are the countries and sites of the *Da Tang Xiyu ji* (大唐西域記)? What have scholars proposed,
what is agreed and what is disputed? Do the Archaeological Survey's reports and the British Indian district
gazetteers add anything to the standard identifications?

**Answer in brief.** Mizutani Shinjō's annotated translation (1971) identifies most of the 148 countries in the text
with reasonable confidence. He marks 30 of them as disputed and 21 more as uncertain or unknown, and the same holds
for 139 of the 268 sites.

Three kinds of local evidence were set against him:
- **The Survey's reports in Cunningham's series** (1862–87), with Mukherji's Tarai report (1901). This is where the
  identifications were argued on the ground and repeatedly revised.
- **The Survey's Annual Reports** (1903–37) and Circle reports. These are the excavations: they settled several
  questions with inscriptions naming the place.
- **The district gazetteers.** Six in ten of their relevant passages only repeat an authority, usually Cunningham.
  The rest add local evidence the standard books lack.

Together they:
- strengthen Mizutani's identification for 66 places, 40 of them with high confidence;
- weaken it for 6;
- support a different site for 33;
- offer a candidate no standard authority records for 7.

Several of the hardest questions turn out to be settled by inscriptions found on the site:
- Kuśinagara at Kasia: the Haribala copper plate in the Nirvāṇa stūpa (1910–11).
- Śrāvastī and the Jetavana at Sahet-Mahet: the Govindachandra plate, and a Bodhisattva inscribed "in the Jetavana
  of Śrāvastī".
- Kauśāmbī at Kosam: the Kara and Meohar inscriptions.
- Puṇḍravardhana at Mahasthan: the 1931 inscription naming Pudanagara.
- Kanishka's stūpa at Shah-ji-ki-Dheri: the inscribed casket.
- Nālandā: the monastery's own sealings.
- Taxila: three inscriptions naming Takṣaśilā.

The remaining revisions cluster in Magadha, the Ghazipur–Ballia stretch of the Ganges, the Salt Range (Siṃhapura),
Gandhāra and Swat, and eastern and central India. Neither survey nor gazetteers reach juan 1 or 12 (Central Asia
and Afghanistan).

All assessments are provisional. Each rests on the coded quotes listed below; the user's reading of the notes is the
check.

## Sources

- **Texts.** Taishō 2087 (`data/ref/t2087_joined.txt`, one sentence per line). Daoxuan's 釋迦方志 (T2088) and Huili's
  *Life* (T2053) were used for the route figures (`route/`).
- **Mizutani**, 『大唐西域記』 (平凡社 中国古典文学大系 22, 1971). A 488-page scan with no text layer, OCR'd with
  Google Vision. The scan and OCR are kept locally under `data/mizutani/` and are gitignored because the book is in
  copyright. His notes are the backbone of the table: readings, Sanskrit names, identifications with references,
  variant readings, and his remarks on whether Xuanzang visited a country (親践) or reports it from hearsay (伝聞).
- **Authorities.** Each was coded separately, with a verbatim quote per identification:
  - Julien (1857–58) and Vivien de Saint-Martin's *Mémoire analytique* (1858);
  - Cunningham, *Ancient Geography of India* (1871), in Majumdar Sastri's edition of 1924, whose notes are coded
    separately as `majumdar`;
  - Beal, *Si-yu-ki* (1884);
  - Watters, *On Yuan Chwang's Travels* (1904–05);
  - N. L. Dey, *Geographical Dictionary* (1927).
- **Archaeological Survey of India, Reports**, vols. I–XXIII (1871–87).
  - **Authors:** Cunningham, with volumes by Beglar, Carlleyle and Garrick.
  - **Also coded the same way:** P. C. Mukherji's *Report on a Tour of Exploration of the Antiquities in the Tarai,
    Nepal* (1901), with V. A. Smith's prefatory note.
  - **Text:** Internet Archive OCR, in `data/ref/asr/`.
- **Archaeological Survey of India, Annual Reports**, 1903–04 to 1936–37, and the Bengal/Eastern Circle reports
  (1903–05, 1913–21).
  - **Missing:** 1918–20 and 1928–29.
  - **OCR:** the Internet Archive's text for eight volumes was Hindi-language OCR of English, so those were
    re-OCR'd with Google Vision from the scans.
  - **Text:** in `data/ref/asr_annual/`, with identifiers in `got.tsv` and `pdfs.tsv`.
- **Gazetteers.** These are the 557 distinct volumes already downloaded for the gazetteer-vedanta and yoga-gazetteers
  studies. Every mention of Xuanzang in any of his old spellings, of "the Chinese pilgrim", and of Faxian was
  indexed. That gives 1,965 hits in 302 volumes; 1,128 of them bear on where a place is.

## Method

1. **Master table** (`data/places_mizutani.tsv`, 419 rows: 148 countries, 3 regions, 268 sites). It was coded from
   Mizutani's notes following `data/CODING_INSTRUCTIONS.md`. Each row carries Mizutani's identification, the other
   views he reports, his status, the T2087 route sentence, and a verbatim quote with its pdf page, checked by
   `scripts/check_quotes.py`.
   - **Visited or hearsay:** 108 countries are visited, 35 hearsay and 5 unclear, by Mizutani's application of the
     colophon's rule (行 = visited, 至 = hearsay).
2. **Authorities** (`data/coded/auth_*.tsv`; checked by `scripts/check_quotes_ref.py`).
3. **Survey reports.**
   - **Cunningham series:** `data/asr_hits.tsv`, `data/coded/asr_batch*.tsv`, `data/ASR_INSTRUCTIONS.md`. 495
     passages, 362 relevant.
   - **Annual Reports:** `data/ar_hits.tsv`, `data/coded/ar_batch*.tsv`, `data/AR_INSTRUCTIONS.md`. 830 passages,
     122 relevant.

   For the Annual Reports, the index takes passages naming the pilgrim, and also passages naming one of about 70
   excavated sites alongside excavation or identification words. Excavation reports often never name Xuanzang.

   Each passage is coded for the author, the place, the site, the stance (proposes, confirms, revises, rejects or
   reports) and the field evidence, with a verbatim quote checked by `scripts/check_quotes_asr.py`.
4. **Gazetteers** (`data/coded/gaz_batch*.tsv`, `data/GAZ_INSTRUCTIONS.md`). Of the 1,128 relevant passages:

   | Stance | Passages |
   |---|---|
   | Repeat an authority | 674 |
   | Argue their own case | 163 |
   | Propose another site | 103 |
   | Doubt the standard one | 71 |
   | Report views only | 117 |
5. **Route tests** (`route/`, see `route/README.md`).
   - **The li:** calibrated on legs between agreed places.
   - **Legs:** every leg is tested against Mizutani's points, and rival sites are scored.
   - **Texts:** the figures are compared across T2087, T2088 and the *Life*.
6. **Notes on disputed places** (`data/notes/notes_*.md`). There are 307 notes. Instructions are in
   `data/NOTES_INSTRUCTIONS.md`, `NOTES_REVISION_ASR.md` and `NOTES_REVISION_AR.md`.

   Each note covers:
   - the identifications;
   - what the survey argued (**Survey.**);
   - what was dug and found (**Excavations.**);
   - what the gazetteers add;
   - a short assessment.

   The matching `updates_*.tsv` gives the proposed identification, the kind of change and a confidence.
7. **Joined table** (`data/places.tsv`, built by `scripts/build_places.py`). One row per place.

## What the sources add

- **Inscriptions and sealings naming the place, found on the site.** These are the strongest evidence, and the
  Annual Reports supply most of them. Examples:
  - Kasia's Haribala plate "in the Nirvāṇa-caitya" and its Mahāparinirvāṇa sealings (06.04).
  - The Govindachandra plate naming "the great convent of the holy Jetavana" (06.01.04).
  - Kanishka's casket naming "the Vihāra of Kanishka" (02.04.03, 02.04.06).
  - "Śrī-Nālandā-mahāvihāra" sealings (09.03.01).
  - The Mahasthan inscription naming Pudanagara (10.04).
  - The Kara inscription "in the kingdom of Kausambi" and the Meohar inscription (05.05).
  - Bloch's Vaiśālī seals (07.03).
  - The Tachhasilae ladle and the Dharmarājikā scroll at Taxila (03.03).
  - Teladaka at Tillara (08.04.01).
  - The Jejākabhukti inscriptions in Bundelkhand (11.13).
  - Gupta seals at Dharawat (08.04.03).
- **The survey's moving identifications.** Examples:
  - Siṃhapura: Malot, then Ketas, then Malot.
  - Kapilavastu: Nagar, then Bhuila Dih, then Tilaurakot.
  - Vilaśana: Atranji, then Bilsar.
  - Kasia: doubted in 1905–07 on the sealings, settled in 1910–11 by the plate.

  The gazetteers often preserve a stage Cunningham had already left.
- **Excavated plans and measurements.** Examples:
  - Marshall's Rājagṛha walls, which fit the text's 150 li and make Cunningham's emendation to 50 unnecessary
    (09.02.04).
  - Gṛdhrakūṭa at Chhatha-giri, with Bimbisāra's road and its two stūpas (09.02.09).
  - Thanesar's mounds against the 20 li (04.08).
  - The Kunāla stūpa on the Hathial ridge (03.03.06), and the Sirsukh walls (03.03.01a).
  - The 1935–36 dig at Bairat, which found no support for Pāriyātra (04.06).
- **Local names, cults and route arguments** from the gazetteers. Examples:
  - The Nāga tank at Sankisa still receives milk offerings.
  - The Kesariya mound is still called "Raja Ben ka deora".
  - The caste name Jijhotia survives in Bundelkhand.
  - Oldham's Ghazipur sites.
  - The Gaya volumes' monastery sites.
- **The text's own figures** (`route/README.md`).
  - **The li:** Xuanzang's li works out at about 0.24 km in a straight line, or 0.29–0.32 km by road, against the
    440 m Mizutani adopts.
  - **Variants:** a few variant readings bear on identifications: Tamasavana, Kapilavastu, the 戰主國 capital, Kiṭa
    and Maheśvarapura.
  - **Limits:** the route test counts against Mizutani's Siṃhapura pair unless the text is emended. It cannot
    overrule an inscription: Kosam fails the text's 500 li.

## Main proposed revisions to Mizutani

These are medium- or high-confidence proposals that move away from Mizutani. The full list, including the 66 places
where the evidence supports him, is in `data/notes/updates_*.tsv`.

| Id | Place | Mizutani | Proposed | Basis |
|---|---|---|---|---|
| 02.04.06 | Kanishka's monastery | possibly Gor Khattri | W mound beside the stūpa, Shah-ji-ki-Dheri | Spooner AR 1908–09: casket names "the Vihāra of Kanishka" |
| 02.04.16 | Ekaśṛṅga's convent | not given | Butan, below the Shahkot Pass (Swat) | Stein AR 1911–12; Sahri-Bahlol abandoned before the 7th c. |
| 03.05 | Uraśā capital | Haripur | Mangali on the Mangal stream | Cunningham; Hargreaves's visit, AR 1923–24 |
| 04.06 | Pāriyātra | Bairat (agreed) | Bairat, weakened | Sahni AR 1935–36: one monastery, nothing after the 2nd c. |
| 05.01.09 | Navadevakula | not given | Newal near Bangarmau | ASR XI; Unao 1903 |
| 06.01.14 | Kāśyapa's birthplace | not given | Tandwa (Bhitti the rival) | ASR XI; Marshall AR 1910–11 |
| 06.04.03a | river at Kuśinagara | Gandak | Little Gandak / old channel | Cunningham; local name "Hirana" |
| 06.04.11 | cremation stūpa | "about 10 miles E" | Ramabhar stūpa (Mauryan), near Kasia | AR 1910–11 excavation; Gorakhpur volumes |
| 07.02 | 戰主國 capital | Ghazipur | Sayyidpur or Ghazipur | Oldham; the *Life*'s distance to Vaiśālī |
| 08.02.05 | Aśoka pillar, Pāṭaliputra | Kumrahar | unlocated (weakened) | Spooner AR 1912–13: the fragments are columns of the Mauryan hall |
| 08.04.03 | Guṇamati's monastery | not given | Dharawat (Kunwa hill) | Beglar, Cunningham; Gupta seals |
| 08.04.04 | Śīlabhadra's monastery | not given | Kauwa-dol hill | Beglar, adopted by Cunningham |
| 08.06.01 | Bodhi-tree enclosure | stone railing | brick wall, untraced (weakened) | Bloch AR 1908–09: the railing is Śuṅga |
| 09.01.03 | Kukkuṭapāda | hill N of Kurkihar | Hasra (Sobhnath) or Gurpa | Stein, Banerji; Gaya 1906 |
| 09.02.03c | Asura's palace | not given | Rajpind cave, Chandu hill | Stein; walled road from Khiri |
| 09.03.13–14 | Kapotaka; its hill | Bihār | Parbati (Daryapur Parvati) | ASR XV: monastic seal, terraced hill |
| 09.03.15b | 落般膩羅 | unsettled | Rajaona (Rajjana) | ASR XV; Monghyr volumes |
| 10.02.02a | islet east of Campā | not given | rock islets at Kahalgaon | ASR XV; Bhagalpur 1911 |
| 10.15 | Coḷa | Nellore | Telugu Coḷa country, Cuddapah–Kurnool | Venkayya AR 1905–06; Cuddapah 1915 |

**Left open:**
- **Siṃhapura's capital and stūpas** (03.04.01a–03): Kotera, Stein's plain north of Ketas, or Malot.
- **Rangamati for Karṇasuvarṇa** (10.08): occupied in Xuanzang's time, but "the capital … a matter of doubt" in
  1920–21.
- **Jajhoti's capital** (11.13): Khajuraho or Eran.
- **Saptaparṇī** (09.02.16): Marshall's levelled spur, not the Son Bhandar.

## Limits

- **Mizutani is the 1971 state of the question.** Later work (季羨林 1985; *Indian Archaeology – A Review*; site
  reports since 1947) is not in these sources. A note flags later results only in one clause.
- **OCR.** Quotes match the OCR verbatim, errors included.
- **Index coverage.** The survey and Annual Report indexes miss arguments that use neither the pilgrim's name nor a
  listed site. The known gaps are in `data/FOLLOWUPS.md`.
- **Places tied to several ids.** A passage coded to several places shows its one identification under each in
  `places.tsv`. The notes, written from the passages, are the reliable reading.
- **Gazetteer counts include duplicate scans and editions.** Notes count volumes, not hits.
- **Coordinates** (`data/coords.tsv`) are for orientation only. 77 places are unmapped.
- **Corrections and open questions** are in `data/FOLLOWUPS.md`. One concerns another study: a CP volume in the
  gazetteer-vedanta selection (`in.ernet.dli.2015.281327`) is really Beal's *Records*.

## Files

- `data/places.tsv`: the joined table (start here).
- `data/places_mizutani.tsv`: the master table.
- `data/coded/`: Mizutani (`mz_juan*`), authorities (`auth_*`), Cunningham-series survey (`asr_batch*`), Annual Reports
  (`ar_batch*`), gazetteers (`gaz_batch*`).
- `data/notes/`: notes and proposed updates.
- `data/*_hits.tsv`: passage and hit indexes.
- `data/coords.tsv`: coordinates.
- `data/text/`: the T2087 passage for each place (CBETA text, cut by `anchors_*.tsv` with `scripts/extract_passages.py`;
  `passages.tsv`) and its English machine translation by DharmaMitra's public cat-translate API
  (`translation_dm.tsv`, `scripts/translate_passages.py`). Both are in `places.tsv` and the map's place panel. The
  translation is unrevised: check it against Mizutani or Beal before quoting.
- `route/`: route model, li calibration, candidate scores, text variants (`route/README.md`).
- `map/xuanzang_places.html`: map and place dossier (published privately at
  https://claude.ai/artifact/WUH4GFEULK5rZ8oaXw8PpH), built by `map/build_page.py` from `map/template.html`.
- `scripts/`: OCR join, quote checkers, indexes, merge and join.
- `data/*_INSTRUCTIONS.md`, `data/NOTES_REVISION_*.md`: coding instructions.
- `PLAN.md`: the original plan.

Rebuild:

```
python3 -I scripts/merge_mizutani.py && python3 -I scripts/build_places.py && python3 -I map/build_geo.py && python3 -I map/build_page.py
```
