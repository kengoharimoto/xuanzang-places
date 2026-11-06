# Xuanzang's places

**Question.** Where are the countries and sites of the *Da Tang Xiyu ji* (大唐西域記)? What have scholars proposed,
what is agreed and what is disputed? What do the excavations, the inscriptions and the British Indian gazetteers add
to the standard identifications?

**Answer in brief.** Mizutani Shinjō's annotated translation (1971) identifies most of the 148 countries in the text
with reasonable confidence. He marks 30 of them as disputed and 21 more as uncertain or unknown, and the same holds
for 139 of the 268 sites.

Five kinds of evidence were set against him:
- the Archaeological Survey's reports in Cunningham's series (1862–87), with Mukherji's Tarai report (1901);
- the Survey's *Annual Reports* (1903–37);
- *Indian Archaeology – A Review* (1953–2001);
- *Epigraphia Indica* and the *Corpus Inscriptionum Indicarum*;
- the district gazetteers.

**What they show.** 312 places have notes. Against Mizutani's identifications, the evidence:
- supports his identification for 78 places, 48 of them with high confidence, many with an inscription or seal
  naming the place;
- weakens it for 6;
- supports a different site for 37;
- offers a candidate no standard authority records for 9.

**Settled by inscriptions or seals found on the site:**
- Kuśinagara at Kasia: the Haribala plate in the Nirvāṇa stūpa.
- Śrāvastī and the Jetavana: the Govindachandra plate, and the Bodhisattva inscribed "in the Jetavana of Śrāvastī".
- Kauśāmbī at Kosam: the Kara, Meohar and pillar inscriptions, and the Ghoṣitārāma excavation.
- Puṇḍravardhana at Mahasthan: the inscription naming Pundranagara.
- Nālandā: the monastery's sealings, and the Bālāditya inscription.
- Taxila: four inscriptions naming Takṣaśilā.
- Karṇasuvarṇa and the Raktamṛttikā monastery at Rajbadidanga: the monastery's own sealings.
- Srughna at Sugh: a sealing reading "Sugha".
- Ānandapura at Vadnagar.
- Kanishka's stūpa at Shah-ji-ki-Dheri.

**Moved by the new evidence:**
- **Kapilavastu** (06.02): now Piprahwa–Ganwaria, against Mizutani's Tilaurakot. The Piprahwa sealings name "the
  community of Kapilavastu monks in the Devaputra vihāra". They are Kushan, about four centuries before Xuanzang,
  so Tilaurakot remains the rival for the city he saw.
- **Kanishka's monastery** (02.04.06): the mound beside the stūpa at Shah-ji-ki-Dheri.
- **Kosala's capital** (10.12): Śrīpura, now Sirpur.
- **Koṅgoda** (10.10): the Chilka coast, from the Śailodbhava plates.
- **Mālava** (11.05): central Gujarat.
- **Kukkuṭapāda** (09.01.03): Gurpa, the "Gurupāda" of an inscription.

Neither the survey nor the gazetteers reach juan 1 or 12 (Central Asia and Afghanistan).

**Every place now also has:**
- its passage of the Chinese text, with the text's own interlinear notes;
- an English translation, made by DharmaMitra's API and checked against the Chinese, with Mizutani and Beal as aids;
- its religious affiliation as the text reports it: the Buddhist school, numbers of monasteries and monks, deva
  temples, and Jain, Śaiva, Pāśupata, Kāpālika and Sūrya worship.

All assessments are provisional. Each rests on the coded quotes listed below; the user's reading of the notes is the
check.

## Sources

- **Text.** T2087, from the CBETA TEI XML (`scripts/build_t2087_xml.py`, `data/ref/t2087_cb_joined.txt`): the printed
  Taishō readings, with the 355 interlinear notes in （…） and the rare characters resolved. For the route figures,
  Daoxuan's 釋迦方志 (T2088) and Huili's *Life* (T2053) were also used (`route/`).
- **Mizutani**, 『大唐西域記』 (平凡社 中国古典文学大系 22, 1971). A 488-page scan, OCR'd with Google Vision and
  kept locally because the book is in copyright. His notes are the backbone of the table.
- **Authorities.** Julien and Vivien de Saint-Martin (1857–58); Cunningham, *Ancient Geography* (1871), in Majumdar
  Sastri's edition of 1924 (`majumdar`); Beal (1884); Watters (1904–05); Dey (1927).
- **Archaeological Survey of India, *Reports*,** vols. I–XXIII (1871–87). The volumes are by Cunningham, Beglar,
  Carlleyle and Garrick. Mukherji's Tarai report (1901) is coded the same way.
- **ASI *Annual Reports*** (1903–37) and the Bengal/Eastern Circle reports. Eight volumes whose Internet Archive text
  was unusable were re-OCR'd with Google Vision. 1918–20 and 1928–29 are missing.
- ***Indian Archaeology – A Review*** (1953–54 to 2000–01).
  - **OCR:** the Internet Archive's OCR of this series is unusable (Hindi-language OCR of English), so it was
    re-OCR'd here with Surya, run on a local vLLM server.
  - **Gaps:** 1973–74 is the archive's own English OCR of another copy. 1979–80 and 1985–86 needed several download
    retries; 1990–91 is not on the archive.
- ***Epigraphia Indica*** vols. 1–36 and **CII** vols. 1, 2.1, 2.2, 3 (in Bhandarkar's revised edition), 5 and 6.
  These are the user's own copies, from their text extracts.
- **Gazetteers.** The 557 volumes of the gazetteer-vedanta and yoga-gazetteers studies.
- **Baluchistan District Gazetteers** (1906–08) and the *Imperial Gazetteer* Baluchistan volume (1908). These are
  Internet Archive OCR, in `data/ref/baluch/` (gitignored). The identifiers are listed in
  `../yoga-gazetteers/regions/data/selection.tsv` (BAL*). They are coded as B001–B055 in `data/coded/gaz_batch10.tsv`.
- **K. Harimoto's notes** (`data/Archive/`). Earlier working notes:
  - a country-by-country extraction of what the text says about non-Buddhists, with letter codes;
  - notes on Songyun's 善特山, on Faxian's 波羅越 against Bhramaragiri, on Mahārāṣṭra and on Pāṇini;
  - two sketches of the route through Kapiśa.

  They are entered as a register (`data/user_obs/observations.tsv`, one row per observation, with an assessment) and
  as a paragraph in the relevant notes. Their proposals were tested against Kuwayama 2000 and 1972, Beal 1869/1884,
  Sachau's al-Bīrūnī, Lambrick's *Sind*, the Skandapurāṇa vol. IV, Kafle's Niśvāsamukha, Cecil 2020, Nagasawa's 法顕伝・宋雲行紀 (OCR'd here with Google Vision), Bakker's 2016 Gonda Lecture, Mirchandani's
  articles of 1967 and 1969 (JIH) and 1976 (ABORI), the open-access Hunnic Peoples sourcebook (Balogh ed. 2020),
  and Marquis's 2020 slides on Afghanistan
  (`data/user_obs/obs_*.tsv`, quotes checked with `scripts/check_quotes_obs.py`).

## Method

1. **Master table** (`data/places_mizutani.tsv`, 419 rows: 148 countries, 3 regions, 268 sites). It was coded from
   Mizutani's notes, with verbatim quotes checked by `scripts/check_quotes.py`. Mizutani's visited/hearsay marking
   gives 108 countries visited, 35 hearsay and 5 unclear.
2. **Authorities** (`data/coded/auth_*.tsv`).
3. **Survey, Annual Reports, *Indian Archaeology*, EI/CII.**
   - **Files:** `data/coded/asr_batch*`, `ar_batch*`, `iar_batch*`, `epig_batch*`; indexes in `data/*_hits.tsv`;
     instructions in `data/ASR_`, `AR_`, `IAR_` and `EPIG_INSTRUCTIONS.md`.
   - **How passages were found:** each source was indexed for passages naming the pilgrim, the excavated sites, or
     the Sanskrit names of disputed places.
   - **What is coded:** each passage's author, place, site, stance and evidence, with a verbatim quote checked by
     `scripts/check_quotes_asr.py`.
4. **Gazetteers** (`data/coded/gaz_batch*`). 1,128 relevant passages.
5. **Route tests** (`route/README.md`). The li is calibrated at about 0.24 km in a straight line, or 0.29–0.32 km by
   road. Every leg is tested, rival sites are scored, and the figures are compared across T2087, T2088 and the *Life*.
6. **Text and translation** (`data/text/`).
   - **The passages:** T2087 is cut into one passage per place (`anchors_*.tsv`, `scripts/extract_passages.py`;
     country passages open with the arrival sentence).
   - **The translation:** each passage was translated by DharmaMitra's public cat-translate API
     (`translation_dm.tsv`, `scripts/translate_passages.py`). It was then checked against the Chinese, with Mizutani
     and Beal as aids only (`review_*.tsv`, `review2_*.tsv`; `data/REVIEW_RELIGION_INSTRUCTIONS.md`).
   - **The results:** 248 passages were fine as translated; 147 had minor slips and 24 major errors, all corrected in
     the published English.
   - **Recurring errors:** invented glosses (such as "mūla-gandha-kuṭī" for 精舍, "Pravaragiri" for any great
     mountain), misread names, and reversed roles in the legends.
7. **Religious affiliation** (`data/religion/religion_*.tsv`; checked by `scripts/check_religion.py`).
   - **What is coded:** for each place, from its own passage, the monasteries and monks, the schools, the deva temples,
     the other traditions, the kind of site, and the state of Buddhism.
   - **Schools stated for countries:** Sammatīya 16, both vehicles 15, Mahāyāna 14, unspecified Hīnayāna 12,
     Sarvāstivāda 11, Mahāyāna-Sthavira 4, Sthavira 2, Mahāsāṃghika 2, Lokottaravāda 1.
   - **Other traditions, across all places:** Pāśupata 15, Śaiva 11, Jain (mostly Digambara, 露形) 12, Sūrya 2,
     Kāpālika 1.
8. **Notes on disputed places** (`data/notes/notes_*.md`, 312 notes). Each note gives the identifications, then the
   evidence in sections:
   - **Survey.**
   - **Excavations.** (Annual Reports)
   - **Inscriptions.**
   - **Later excavations.** (*Indian Archaeology*)
   - **Gazetteers.**

   Then comes a short assessment. The matching `updates_*.tsv` gives the proposed identification, the kind of change
   and a confidence.
9. **Joined table** (`data/places.tsv`, `scripts/build_places.py`) and **map**
   (`map/xuanzang_places.html`, https://claude.ai/artifact/WUH4GFEULK5rZ8oaXw8PpH).
   - **Map filters:** Mizutani's status, the visit status, religious affiliation, K. Harimoto's notes, juan and level.
   - **Place panel:** every source, the notes, and the Chinese text with its translation.

## Main proposed revisions to Mizutani

These are medium- or high-confidence proposals that move away from Mizutani. The full list is in
`data/notes/updates_*.tsv`.

| Id | Place | Mizutani | Proposed | Basis |
|---|---|---|---|---|
| 02.04.06 | Kanishka's monastery | possibly Gor Khattri | W mound beside the stūpa, Shah-ji-ki-Dheri | Spooner: casket names "the Vihāra of Kanishka" |
| 02.04.16 | Ekaśṛṅga's convent | not given | Butan, below the Shahkot Pass (Swat) | Stein AR 1911–12 |
| 03.05 | Uraśā capital | Haripur | Mangali (country confirmed as Hazara by the Bedadi ladle "Urasa-rajya") | Cunningham; Hargreaves; Konow CII 2.1 |
| 04.06 | Pāriyātra | Bairat (agreed) | Bairat, weakened | Sahni AR 1935–36 |
| 04.11 | Brahmapura | Srinagar (Garhwal) | Lakhanpur or nearby | Talesvara plates issued from Brahmapura (EI 13) |
| 05.01.09 | Navadevakula | not given | Newal near Bangarmau | ASR XI; Unao 1903 |
| 06.02 | Kapilavastu | Tilaurakot | Piprahwa–Ganwaria (Tilaurakot the rival) | Srivastava IAR 1972–73: sealings naming the Kapilavastu saṅgha (Kushan) |
| 06.01.14 | Kāśyapa's birthplace | not given | Tandwa (Bhitti the rival) | ASR XI; Marshall AR 1910–11 |
| 06.04.03a, 06.04.11 | Kuśinagara river, cremation stūpa | Gandak; "10 miles E" | Little Gandak; Ramabhar | Cunningham; AR 1910–11 |
| 07.02 | 戰主國 capital | Ghazipur | Sayyidpur or Ghazipur | Oldham; the *Life*'s distance |
| 08.02.05, 08.06.01 | Pāṭaliputra pillar; Bodhi-tree enclosure | Kumrahar; stone railing | unlocated; brick wall (weakened) | Spooner AR 1912–13; Bloch AR 1908–09 |
| 08.04.03, 08.04.04 | Guṇamati's and Śīlabhadra's monasteries | not given | Dharawat; Kauwa-dol | Beglar, Cunningham; Gupta seals |
| 09.01.03 | Kukkuṭapāda | hill N of Kurkihar | Gurpa (Gurupāda); Hasra second | Silao pedestal (Chhabra, EI 25); Stein; Banerji |
| 09.02.03c | Asura's palace | not given | Rajpind cave | Stein |
| 09.03.13–14 | Kapotaka; its hill | Bihār | Parbati | ASR XV |
| 09.03.15b | 落般膩羅 | unsettled | Rajaona | ASR XV |
| 10.02.02a | islet east of Campā | not given | rock islets at Kahalgaon | ASR XV |
| 10.10 | Koṅgoda | Jaugada | Koṅgoda-maṇḍala, Mahānadī to north Ganjam; capital on the Sālimā near the Chilka | Śailodbhava plates (EI) |
| 10.15 | Coḷa | Nellore | Telugu Coḷa country, Cuddapah–Kurnool | Venkayya; Cuddapah 1915 |
| 11.05 | Mālava | Malwa or Gujarat | central Gujarat, SE of the Mahī | Bhandarkar (CII 3), Sircar (EI 34) |

**From K. Harimoto's notes and the sources they led to:**
- **Kapiśa** (01.38.02–03a). Kuwayama 2000 confirms the Rāhula monastery as the Borj-e Kafir stūpa SE of Begram;
  Mes Aynak is too far for 30 li. He reads 霫蔽多伐剌祠 as Śvetāśvatara, as the notes do, and places it at Tapa
  Skandar (Umā-Maheśvara). Aruṇa is the Sūrya temple of Khair Khana. Both are alternatives, long for the text's li.
- **Laṅgala's capital** (11.19). 窣菟黎濕伐羅 = Sthūleśvara by name. Mirchandani (1969) proposed it from the Devī
  Bhāgavata alone and placed it at Kasarkand; the Skandapurāṇa puts that liṅga at the Indus mouth, so the site is open.
- **Sindh and Baluchistan** (11.15–11.23). Mirchandani's Baluchistan route of 1967 has these sites: Sindhu in the
  Derajat, Atyanabakela = Las Bela, Laṅgala = Makran with Kasarkand, Pītaśilā = Khuzdar, Avaṇḍa = Kachhi/Gandāva and
  Varṇa near Duki.
  - **Route test:** it fits Xuanzang's distances and bearings better as a whole than Mizutani's (mean |z| 0.38 against
    0.62; `route/README.md` §5).
  - **Baluchistan District Gazetteers** (1906–08): they support Kachhi with Kandabil = Gandāva, tributary to Sind
    c. 635, and Buddhist sealings of the 8th–9th century.
  - **Proposed changes:** Laṅgala's capital moves west (Lākoriān weakened), and Kachhi becomes an equal alternative for
    Avaṇḍa. Atyanabakela stays in lower Sindh because of 臨信度河.
- **Parvata** (11.17). Bakker (2020) links it with Toramāṇa's Parvatikā near Akhnūr/Sialkot; the distance from Multan
  is too short for that.
- **Atyanabakela's capital** (11.18). Banbhore (Debal) is added to Karachi and Koṭeśvara.
- **Songyun's 濕婆仙** (02.04.15). A Śiva shrine inside the Daṇḍaloka monastery c. 520. Beal missed it; Nagasawa
  had already read it as Śiva, with ash-smearers.
- **Religion coding.** Compared with the notes' letter codes: Vipula hill (09.02.11) is now tagged Jain.
  Mayūrapura's 大天祠 also carries the "Mahādeva temple" reading.

**Still open:**
- **Siṃhapura's capital** (03.04.01a): Kotera, Stein's plain north of Ketas, or Malot.
- **Bhramaragiri** (10.12.05): Arang's Bhaṅgara-pavata, or Nāgārjunakoṇḍa's Siripavata.
- **Kaliṅga's capital** (10.11): Kalingapatnam or Mukhalingam.
- **Koṅkaṇapura** (11.02): Annagundi or Banavasi.
- **Jajhoti's capital** (11.13): Khajuraho or Eran.
- **Śatadru** (04.05): Sanghol proposed for Sarhind, without an inscription.

## Limits

- **Later scholarship.** Mizutani is the 1971 state of the question. Later scholarship, such as 季羨林's 1985
  commentary, is not in these sources. *Indian Archaeology* is in them up to 2000–01.
- **OCR.** Quotes match the OCR verbatim, errors included.
- **Index coverage.** The indexes miss arguments that use neither the pilgrim's name, a listed site, nor a listed
  Sanskrit name. The known gaps are in `data/FOLLOWUPS.md`.
- **Places tied to several ids.** A passage coded to several places shows its one identification under each in
  `places.tsv`. The notes are the reliable reading.
- **Translations.** They are checked and corrected but not a published translation; quote them with that caveat.
- **Affiliation.** It records what the passage says, plus Mizutani's identification of sect names. The code
  `Pasupata` stands for the text's 塗灰/塗炭 ("ash-smearing") 外道; the map shows it as "ash-smearers", since
  Xuanzang never names the Pāśupatas. Legend-only
  mentions are in the notes, not coded as present practice.
- **Coordinates** (`data/coords.tsv`) are for orientation only.
- **Corrections and open questions** are in `data/FOLLOWUPS.md`.

## Files

- `data/places.tsv`: the joined table (start here).
- `data/places_mizutani.tsv`: the master table.
- `data/coded/`: coding by source (`mz_juan*`, `auth_*`, `asr_batch*`, `ar_batch*`, `iar_batch*`, `epig_batch*`,
  `gaz_batch*`).
- `data/notes/`: notes and proposed updates.
- `data/text/`: passages, anchors, translations, translation reviews.
- `data/religion/`: affiliation coding (`religion_zz_user.tsv`: corrections from the comparison with K. Harimoto's codes).
- `data/user_obs/`: K. Harimoto's observations (`observations.tsv`), the letter codes of the 外道 note (`religion_codes.tsv`), and the source checks (`obs_*.tsv`).
- `data/*_hits.tsv`: indexes.
- `data/coords.tsv`: coordinates.
- `route/`: route tests.
- `map/`: the map page and its builder.
- `scripts/`: OCR join, text build, extraction, translation, quote checkers, indexes, merge and join.
- `data/*INSTRUCTIONS*.md`, `data/NOTES_REVISION_*.md`: coding instructions.
- `PLAN.md`: the original plan.

Rebuild:

```
python3 -I scripts/merge_mizutani.py && python3 -I scripts/build_places.py && python3 -I map/build_geo.py && python3 -I map/build_page.py
```
