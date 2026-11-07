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

**What they show.** 442 of the 480 places have a note (Mizutani's 419 and 61 added ones). The 38 without a note are
minor sites that have no point either. Against Mizutani's identifications, the evidence:
- supports his identification for 97 places, 56 of them with high confidence, many with an inscription or seal
  naming the place;
- weakens it for 12;
- supports a different site for 62;
- offers a candidate no standard authority records for 12.

On the map the study's confidence comes out as 105 places secure, 161 probable and 110 open. These are the ratings
after a quality check of 30 notes and an audit of every "high" rating without site evidence (both in `data/notes/`).
Another 54 minor sites are placed approximately from Xuanzang's own bearing and distance, without an identification
(`scripts/place_from_text.py`). 50 have no point.

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

The survey reports and the gazetteers do not reach juans 1 and 12 (Central Asia and Afghanistan). For the Afghan
stretch Foucher's *La vieille route* (1942–47) now fills the gap.

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
- **The *Life* (T2053), place by place.** 260 places have the Life's parallel passage, cut by agents following
  `data/LIFE_INSTRUCTIONS.md` (`data/text/life_anchors_*.tsv`, `life_passages.tsv`). Each has a DharmaMitra
  translation (`life_translation_dm.tsv`). The translations were then checked against the Chinese by agents following
  `data/LIFE_REVIEW_INSTRUCTIONS.md`, with Beal's 1911 translation as an aid only (`data/text/life_review_*.tsv`):
  187 ok, 59 corrected (minor), 14 corrected (major). The corrections include Mokṣagupta (not "Prajñāgupta"), Kharbanda
  (not Kashgar), and hearsay restored at Malakūṭa (聞).
- **Mizutani**, 『大唐西域記』 (平凡社 中国古典文学大系 22, 1971). A 488-page scan, OCR'd with Google Vision and
  kept locally because the book is in copyright. His notes are the backbone of the table.
- **Authorities.** Julien and Vivien de Saint-Martin (1857–58); Cunningham, *Ancient Geography* (1871), in Majumdar
  Sastri's edition of 1924 (`majumdar`); Beal (1884); Watters (1904–05); Dey (1927); and 季羨林 et al., *Da Tang Xiyu ji jiaozhu* 大唐西域記校注 (Beijing:
  Zhonghua, 1985; `ji`). Ji is OCR'd from the user's PDF (Google Vision, `data/ref/ji1985.txt`, blocks `=== pdf NNNN`;
  printed page = pdf − 172 in the juans), coded for 356 places in `data/coded/auth_ji_*.tsv`
  (`data/JI_INSTRUCTIONS.md`) and folded into the notes as a "Ji Xianlin et al. (1985)" paragraph
  (`data/JI_FOLD_INSTRUCTIONS.md`). It brings post-1971 work the other sources lack: Soviet excavations in Central Asia
  (Belenitskii et al. 1973, Stavisky 1977), Huang Wenbi in Xinjiang, Chinese and Japanese studies (Xiang Da, Zhang
  Guangda, Uchida 1972, 謝方 1982), Tugusheva's Uighur *Life* (1980) and Srivastava on the Piprahwa sealings (1979).
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
- **Foucher, *La vieille route de l'Inde de Bactres à Taxila*** (1942–47). The OCR comes from the Toyo Bunko Digital
  Silk Road scans (`data/ref/foucher/`). It is coded as F001–F045 in `data/coded/ar_batch12.tsv` and folded into 48 notes
  for Afghanistan and the Northwest.
- **Kuwayama Shōshin:** *Across the Hindukush of the First Millennium* (Kyoto 2002, his English papers) and his
  thesis 『カーピシー＝ガンダーラ史研究』 (1986; Kyoto University repository), a handwritten manuscript read from the page
  images: ch. 1 (罽賓, the Buddha's bowl, Nagarahāra), ch. 3 (the Sui 漕國 = Kāpiśī), ch. 4 §1 (Begram), ch. 6 §§1–3
  and 6 (the Kāpiśī holy sites, Khair Khana and Zhun, the Bāmiyān colossi). Summaries with manuscript pages and verbatim
  Japanese in `data/ref/kyoto/k1990/summary_*.md` (gitignored with the scans); folded into the Bāmiyān, Kāpiśī,
  Nagarahāra, Gandhāra and 漕矩吒 notes (`data/KUWAYAMA_FOLD_INSTRUCTIONS.md`). Also his 2020 note on 活's capital and
  Miyamoto 2015 (Kyoto repository).
- **Stein's survey memoirs:** *An Archaeological Tour in Waziristan and Northern Baluchistan* (MASI 37, 1929) and
  *An Archaeological Tour in Gedrosia* (MASI 43, 1931). They are Internet Archive OCR in `data/ref/stein/`, coded as
  S001–S020 in `data/coded/ar_batch11.tsv`.
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
   - **Added places.** 61 places that Mizutani's numbering skips or merges were added from passages the coders tagged
     `new`: 57 in the Xiyu ji and 4 found only in the Life. They have ids ending `.xN`, the status "added" on the map,
     and their own passages, translations and source coding. Seven tagged clusters turned out to belong to existing
     rows, and one (Faxian's Pūrvārāma) was dropped.
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
   The li does not behave as a fixed ground measure. In India the figures look like day stages (yojanas, which
   Xuanzang defines as 一日軍行) converted at a set rate: rough and forest legs give far fewer km per li (§10). Along modelled walking routes, walking time fits the li a
   little better than route length (about 19 li per walking hour), but neither explains the forest legs. The
   Gandhāra–Kashmir legs, short against the model, are normal along the real roads of Stein and Drew (0.175–0.30 km per li).
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
8. **Notes** (`data/notes/notes_*.md`, 442 notes). The disputed places came first (312 notes). A second pass
   (`notes_untested_*.md`, `data/NOTES_UNTESTED_INSTRUCTIONS.md`) covered the 129 places not yet assessed, with all
   the evidence then available. Each note gives the identifications, then the
   evidence in sections:
   - **Survey.**
   - **Excavations.** (Annual Reports)
   - **Inscriptions.**
   - **Later excavations.** (*Indian Archaeology*)
   - **Gazetteers.**

   Then comes a short assessment. The matching `updates_*.tsv` gives the proposed identification, the kind of change
   and a confidence.
8a. **Original names** (`data/names/`, `data/NAMES_INSTRUCTIONS.md`). The original forms of the names (Mizutani's,
   often reconstructions) were tested against Xuanzang's own transcription practice.
   - **The key** (`key.tsv`, `align.tsv`, `key_notes.md`): 262 Indic names of certain form, 138 place names and 124
     names or terms fixed by his 唐言 glosses and 舊曰…訛 corrections, aligned syllable by syllable over 238
     characters, with each character's Middle Chinese position (Qieyun, via the tshet_uinh library;
     `scripts/names_prep.py`). He marks retroflexes, voiceless aspirates and the sibilants ś/ṣ/s, but not vowel
     length, r/l, v/b/bh or voiced aspiration; clusters take -p/-t/-k characters; compounds are written member by
     member; he mostly gives Sanskrit forms, with some regional Prakrit ones.
   - **The pilot test** (`test_nw_a.tsv`, `test_nw_b.tsv`): the 47 asterisked or queried forms of India and the
     North-West, checked against the key and searched for attested forms in the Sanskrit e-text library
     (/mnt2/kengo/E-texts/1_sanskr, through a diacritic-free copy: `scripts/skt_norm.py`, `scripts/skt_search.py`), the
     inscriptions and Stein's Kashmir material. 24 forms stand; 13 better forms, 4 alternatives and 6 doubtful,
     among them Tamasāvana, Toyikā, Kheṭa(ka) for 契吒, Mūla-Sāmbapura for 茂羅三部盧, Mahāsāra, Kacaṅgalā, Lāhula and
     *Palola for Bolor (the Gilgit kings' title; Gilgit becomes an alternative to Baltistan). The key also chooses among the forms Mizutani gives for 12 more places: for 9 he lists
     the fitting form himself, usually first (vakṣu, Goviṣāṇa, Dvārapati, the vernacular Tāmalitti, …), and for 3
     his form does not fit (Uraśā only, Licchava, Lampa).
   - **Afghanistan and Central Asia** (`test_ca_a.tsv`, `test_ca_b.tsv`): the other 45 forms, mostly Iranian, Saka,
     Turkic or Gāndhārī, tested with the key's consonant mapping and searched in the *Ḥudūd al-ʿĀlam* (Minorsky
     1937), Le Strange (1905), Barthold (1928) and Marquart's *Ērānšahr* (1901) (`data/ref/iran/`, gitignored), Ji,
     Stein and Foucher. 23 stand; 13 better, 4 alternatives, 5 doubtful: Khamdādh (= Khandūd) for 昏馱多, Sutrūšna,
     Agni for 阿耆尼, Parghar, Andrāb, Xwast (Khost), *War (the base of Warwālīz, Kunduz) for 活, Kurān, Khaṣa for 佉沙;
     瞢健 is Munjān itself; 鶴悉那 hardly fits Ghazna, and 阿路猱 cannot be aruṇa (Xuanzang's own fanqie gives 猱 nau).
   - **Bactrian** (`bactrian.tsv`): the Afghan names checked against Sims-Williams, *Bactrian Documents from
     Northern Afghanistan* I (2000) and II (2007) (Internet Archive OCR, `data/ref/simswilliams/`, gitignored; the
     uploads state no licence, the uploader calls them open). 50 places: 10 confirmed, 1 better, 2 no fit. 活 = Warnu (the study's
     equation), "probably the later Warwaliz (modern Qunduz)" (II p. 242), a city with a Wakhsh cult in a contract of c. 602;
     紇露悉泯健 = Rōb + Samingān, the court of the khars of Rob in the district of Samingan (docs. N, c. 630, to Q, c. 672);
     覩貨邏 = *Tuxwār (Toxwār-, with the w that Skt. Tukhāra lacks); Tarmid, Waxš, Baxl, Gōzgān, Bamyan, Khwast
     confirmed; Sar-i Pul's Bactrian name Amber does not fit 鋭秣陀. 揭職 is not Gaz but *Garčig, Bactrian γαρσιγο
     "mountain land" (Gharchistan), the mountain zone S of Tokharistan (Yoshida 1998, "Sino-Iranica", 西南アジア研究 48;
     Sims-Williams, CRAI 2002 [2004], both in `data/ref/simswilliams/`); Yoshida also confirms 活 = war = Kunduz;
     but the capital lay on the south bank of the Oxus by the *Life* (都城在河南岸), and Kuwayama (2002, 2020) puts it,
     with the Tang seat 阿緩, at the town site N of Qal'a-ye Zāl, where the map now places it; Miyamoto (2015) puts 活路
     at Warlu in the Baghlān plain (open papers from the Kyoto repository, `data/ref/kyoto/`).
   - **The "secure" forms** (`test_sec_a/b/c.tsv`): the 267 forms that built the key, checked against it. 238 stand;
     21 better, 1 alternative, 7 doubtful: e.g. Ṭakka (磔 is retroflex), kukkuṭārāma and kukkuṭapāda (屈屈 has no r),
     telāḍhaka, śrīkṣetra, *raktamaṭṭi, oḍḍa, vakṣu, Kumēdh, Kišš for 羯霜那, Kīkān for 稽疆那, Lambura for 藍勃盧,
     Upagupta for 鄔波毱多 (Mizutani's Uruṇḍa names another object), and *Spēt- "white" for 霫蔽多 (Iranian, not
     Skt. śveta-, which weakens the Śaiva reading of 01.38.03). In all, 359 forms: 289 stand, 44 better, 9
     alternatives, 17 doubtful.
   - **In the data:** `data/names/proposed.tsv` (`scripts/names_proposed.py`) → the `name_study` columns of
     `places.tsv` and the map's place panel; "Name." paragraphs in the notes, which say where a name moves an
     identification. A name match is a lead, not site evidence: it never raises a rating to high on its own.
9. **Findings page** (`FINDINGS.html`, https://claude.ai/artifact/2H5yngbhmdj9pKEp5imP7e): a short readable summary
   of what the study found.
10. **Joined table** (`data/places.tsv`, `scripts/build_places.py`) and **map**
   (`map/xuanzang_places.html`, https://claude.ai/artifact/WUH4GFEULK5rZ8oaXw8PpH).
   - **The map shows the study's view** (`data/study_view.tsv`, `scripts/build_study_view.py`). Each place sits at the
     study's current site: its own proposed site where it settles on one (`data/coords_study.tsv`), the sources'
     point for added places, and Mizutani's point elsewhere. Colour is the study's confidence, taken from the notes'
     assessments (`updates_*.tsv`):
     - **secure:** high confidence;
     - **probable:** medium;
     - **open:** low confidence, weakened, or left open between named candidates;
     - **placed from the text:** no site identified, so the point comes from Xuanzang's own bearing and distance from
       a located place (`data/coords_text.tsv`);
     - **untested:** places without a note, where Mizutani's identification (or, for added places, the sources') has
       not been assessed.

     These classes are the study's judgements, not Mizutani's. His status is shown in each place panel, and a
     "Mizutani's points" layer draws his sites where they differ.
   - **Map filters and layers:** confidence, visit status, religious affiliation, K. Harimoto's notes, rival sites
     with their route fit, Mizutani's points, juan and level.
   - **Place panel:** the study's identification first, then Mizutani, the authorities, every source, the Xiyu ji
     and Life passages with translations, and the note.
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
  - **Proposed changes:** Lākoriān is weakened as Laṅgala's capital. The Xiyu ji's figures point to western Makran,
    the Life's to somewhere nearer Las Bela. Kachhi becomes an equal alternative for Avaṇḍa. Atyanabakela stays in lower Sindh because of 臨信度河.
- **Whole routes, juan by juan** (`route/README.md` §6). This compares each authority's set of sites with Mizutani's
  and finds the best-fitting combination of candidates.
  - **Juan 10:** the figures favour Cunningham's Deccan, against inscriptions that the study follows.
  - **Juan 9:** Magadha's short distances fit no scheme.
  - **Other juans:** 29 place notes carry a "Route test (whole juan)" line where the best fit departs from Mizutani.
  - **On the Life's figures** (§7). The Life's own figures give a different picture. They fit worse than the Xiyu
    ji's in the Northwest and Magadha (juans 2, 3, 8) and better in juans 4 and 7. In the Deccan they again favour
    Cunningham, so the conflict with the inscriptions is not an accident of one text. They pull Kapilavastu north-west.
    28 notes carry a "Route test (the Life)" line.
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

- **Later scholarship.** Mizutani is the 1971 state of the question; Ji (1985) brings it to about 1980. Work since then
  is not in these sources, and post-1971 work that Ji cites (e.g. Ahmed on Mahasthan, Belenitskii) is known only
  through him. *Indian Archaeology* is in them up to 2000–01.
- **Original names.** All 359 forms have been tested: the 92 asterisked or queried ones, and the 267 "secure" ones
  that built the key (a consistency check, so they are not independent of it). Bactrian, Khotanese and Sogdian forms known from scholarship but not in
  these files are marked "reported" and never rated above medium. Middle Chinese is itself a reconstruction, and
  two-character names match by chance easily.
- **OCR.** Quotes match the OCR verbatim, errors included.
- **Index coverage.** The indexes miss arguments that use neither the pilgrim's name, a listed site, nor a listed
  Sanskrit name. The known gaps are in `data/FOLLOWUPS.md`.
- **Places tied to several ids.** 467 coded passages concern two or more places. Each has been split into per-place
  entries (`data/coded/split/split_*.tsv`, `data/SPLIT_INSTRUCTIONS.md`), so `places.tsv` and the map show for each
  place only what bears on it: 1,022 entries apply, 124 only name the place ("named only", no evidence), and 16 were
  coding slips, now dropped. Single-place passages are as coded.
- **Translations.** They are checked and corrected but not a published translation; quote them with that caveat. The
  Life translations are checked in the same way.
- **Affiliation.** It records what the passage says, plus Mizutani's identification of sect names. The code
  `Pasupata` stands for the text's 塗灰/塗炭 ("ash-smearing") 外道; the map shows it as "ash-smearers", since
  Xuanzang never names the Pāśupatas. Legend-only
  mentions are in the notes, not coded as present practice.
- **Coordinates** (`data/coords.tsv`) are for orientation only.
- **Corrections and open questions** are in `data/FOLLOWUPS.md`.

## Files

- `data/places.tsv`: the joined table (start here).
- `data/places_mizutani.tsv`: the master table.
- `data/places_added.tsv`: 61 places missing from Mizutani's numbering (ids `.xN`), added from the sources. Mappings
  for the coded rows are in `data/coded/new_resolved.tsv`; coordinates are in `data/coords_added.tsv`.
- `data/names/`: the transcription key, the pilot tests of the original names and the study's proposed forms (method 8a).
- `data/coords_study.tsv`: coordinates for the study's own proposed sites (the map's "study's proposals" layer).
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
python3 -I scripts/merge_mizutani.py && python3 -I scripts/build_places.py && python3 -I scripts/build_study_view.py && python3 -I scripts/place_from_text.py && python3 -I scripts/build_study_view.py && python3 -I map/build_geo.py && python3 -I map/build_page.py
```
