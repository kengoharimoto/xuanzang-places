# Xuanzang's places

**Question.** Where are the countries and sites of the *Da Tang Xiyu ji* (大唐西域記)? What have scholars proposed,
what is agreed and what is disputed? What do the excavations, the inscriptions and the British Indian gazetteers add
to the standard identifications?

**The standard.** There is no single agreed list, but the commentary the field cites for "where is X" is 季羨林 et al.,
*Da Tang Xiyu ji jiaozhu* 大唐西域記校注 (Zhonghua, 1985; "Ji"), which gathers the earlier authorities and the archaeology to
about 1980. Japanese scholarship cites Mizutani Shinjō's annotated translation (1971), with which Ji agrees for most
places; English-language work still goes back to Watters (1904–05) and Cunningham. The study takes Ji as the standard,
with Mizutani where Ji is silent, and its map is a visualisation of that standard wherever the evidence agrees with it.

**Against the standard** (`data/standard/compare_*.tsv`, `data/STANDARD_INSTRUCTIONS.md`): 365 of the 490 places have a
standard identification. For 262 the study agrees, and for 28 it names a more exact site within it; for 75 it departs,
putting 35 elsewhere and leaving 40 open between the standard's site and another. Among the 148 countries, 121 agree
or refine. Of the 125 places without a standard identification, mostly minor sites, the study proposes a site for 61.
Kapilavastu is not a departure: Ji already leaves it open between Piprahwa and Tilaurakot. On the map a dark ring
marks a departure, a light ring a refinement or a site where the standard has none.

**Answer in brief.** Mizutani Shinjō's annotated translation (1971), the study's working text because it covers every
place, identifies most of the 148 countries in the text with reasonable confidence. He marks 30 of them as disputed and 21 more as uncertain or unknown, and the same holds
for 139 of the 268 sites.

Five kinds of evidence were set against him:
- the Archaeological Survey's reports in Cunningham's series (1862–87), with Mukherji's Tarai report (1901);
- the Survey's *Annual Reports* (1903–37);
- *Indian Archaeology – A Review* (1953–2001);
- *Epigraphia Indica* and the *Corpus Inscriptionum Indicarum*;
- the district gazetteers.

A sixth, added in November 2026, is the scholarship since Ji (1985): 454 items listed, 103 read and coded so far, and
*Indian Archaeology – A Review* extended to 2013–14 ("Recent scholarship" below; `data/LITERATURE.md`).

**What they show.** 456 of the 490 places have a note (Mizutani's 419 and 71 added ones). The 34 without a note are
minor sites that have no point either. Taking Mizutani's identifications as the starting point (his translation covers every place), the evidence:
- supports his identification for 100 places, 59 of them with high confidence, many with an inscription or seal
  naming the place;
- weakens it for 16;
- supports a different site, or leaves the place open between his and another, for 71;
- offers a candidate no standard authority records for 25.

On the map the study's confidence comes out as 104 places secure, 155 probable and 128 open. These are the ratings
after a quality check of 30 notes and an audit of every "high" rating without site evidence, and a second check of
27 paragraphs added later (Ji, names, Bactrian, Stein/Drew, Kuwayama: 19 ok, 8 minor, all fixed; `data/notes/qc2_*.tsv`).
Another 50 minor sites are placed approximately from Xuanzang's own bearing and distance, without an identification
(`scripts/place_from_text.py`). 53 have no point.

**Settled by inscriptions or seals found on the site:**
- Kuśinagara at Kasia: the Haribala plate in the Nirvāṇa stūpa.
- Śrāvastī and the Jetavana: the Govindachandra plate, and the Bodhisattva inscribed "in the Jetavana of Śrāvastī".
- Kauśāmbī at Kosam: the Kara, Meohar and pillar inscriptions, and the Ghoṣitārāma excavation.
- Puṇḍravardhana at Mahasthan: the inscription naming Pudanagara (Puṇḍranagara).
- Nālandā: the monastery's sealings, and the Bālāditya inscription.
- Taxila: four inscriptions naming Takṣaśilā.
- Karṇasuvarṇa and the Raktamṛttikā monastery at Rajbadidanga: the monastery's own sealings.
- Srughna at Sugh: a sealing reading "Sugha".
- Ānandapura at Vadnagar.
- Kanishka's stūpa at Shah-ji-ki-Dheri.

**Moved by the new evidence:**
- **Kapilavastu** (06.02): open between Piprahwa–Ganwaria and Mizutani's Tilaurakot. The Piprahwa sealings name "the
  community of Kapilavastu monks in the Devaputra vihāra", but Falk (2017) dates them after the Kushans and takes them
  for Faxian's city; the IAR 2012–13 trenches found no habitation at Piprahwa and nothing after the Kushan period at
  Ganwaria. Tilaurakot is now dated as a walled town from the 6th century BCE (Davis et al. 2016), but nothing there
  names it, and Xuanzang's own legs split between the two.
- **Kanishka's monastery** (02.04.06): the mound beside the stūpa at Shah-ji-ki-Dheri.
- **Kosala's capital** (10.12): Śrīpura, now Sirpur.
- **Koṅgoda** (10.10): the Chilka coast, from the Śailodbhava plates.
- **Mālava** (11.05): central Gujarat, now an open alternative to Malwa (low confidence; Ji's case for Malwa
  with Dhār and the route figures both weigh against it).
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

**Public repository:** https://github.com/kengoharimoto/xuanzang-places. It leaves out two kinds of file, removed
from every commit:
- **Mizutani's notes verbatim:** `data/places_mizutani.tsv` and `data/coded/mz_*.tsv`. His translation (1971) is in
  copyright. His identifications, status and references are kept, coded in English in `data/places.tsv`. Short
  quotations used in the discussion (e.g. `route/variants_*.tsv`, `translation_issues`) are kept.
- **Long extracts from *Indian Archaeology – A Review* (1953–2001) and *Epigraphia Indica*:**
  `data/iar_hits.tsv`, `data/iar_batches/`, `data/epig_hits.tsv`, `data/epig_batches/` and the work queue
  `data/coded/split/todo_*.tsv`. The coded results (`data/coded/iar_batch*.tsv`, `epig_batch*.tsv`), with short
  quotations, are kept.

The Annual Reports, ASR and gazetteer extracts are public domain and included. Paths under `../gazetteer-vedanta/`
and `../yoga-gazetteers/` refer to https://github.com/kengoharimoto/gazetteer-studies. Licence: `LICENSE.md` (CC BY
4.0 for the study's own text and data, MIT for the scripts; the Chinese text from CBETA stays under CBETA's licence).

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
- **Recent scholarship, 1985–2026** (`data/LITERATURE.md`, `data/literature.tsv`, `data/LIT_INSTRUCTIONS.md`). A
  bibliography of 456 items built region by region in English, Japanese, Chinese and European languages; 104
  items read and coded (`data/coded/lit_batch1-18.tsv`, 246 relevant rows, quotes checked; Tsuchiya 2010 OCR'd with Google Vision), shown on the map
  as "Recent scholarship (since 1985)" and folded into the notes as **Recent scholarship.** paragraphs. Among them:
  Falk 2017 and Davis et al. 2016 (Kapilavastu, Rāmagrāma), Kuwayama's papers of 1985–99 and Miyamoto 2012–18
  (Afghanistan, Tokharistan), Naiki 2015 and 2021 (Chanaka Dheri, Taxila), Dar & Hameed 2018 (Siṃhapura), Verardi 2012
  and Filigenzi 2015 (Kashmir Smast, Swat), Shimada 2013 (Amarāvatī), Ambekar et al. 2023 (Vadnagar), Talati 2024 and
  Zhang 2016 (Khotan), the Ak-Beshim reports with Jokura et al. 2017 (the Du Huaibao stone), the ICOMOS radiocarbon dates and Tarzi 2007
  (Bamiyan), Errington 2017 (Masson's Nagarahara and Hadda), Sims-Williams 2002 (Gūzgān), Bernard et al. 2006 (Balkh), *Antiquities of Northern Pakistan* 1–3 and von
  Hinüber 2004 (Palola), *The Sacred Garden of Lumbini* (2nd ed. 2019; Tilaurakot and the Greater Lumbini sites),
  Deeg 2025 and *Early Āndhradeśa* (2025), and Deepak Anand's field reports from Magadha (a blog, cited as such and
  never the sole ground for a rating). *Indian Archaeology – A Review* 2007–08 and 2009–10 to 2013–14 (ASI
  Aurangabad Circle PDFs, text by pdftotext) were added to the IAR index, with 1990–91 and 1993–94 (missing from the study's scans) and a pass over all
  volumes for sites the index had lacked (Banavasi, Valabhī, Ujjain, Kanchipuram, the Odisha and Andhra sites, Tamluk,
  Broach): passages 729–1043, `iar_batch11-18.tsv`.
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
     rows, and one (Faxian's Pūrvārāma) was dropped. Ten more came from the recent literature's `new` rows
     (2026-11-12): Acala's monastery at Veṅgī (10.13.x1); four stūpa groups at Bodh Gayā (08.06.x5–x8), the
     Bimbisāra and Śāriputra's-disciples stūpas near Nālandā (09.03.x7–x8) and the Rāhula stūpa at Rājagṛha
     (09.02.x2), with Deepak Anand's candidates; and, from the Life, Huṣkapura (Ushkur, 03.06.x1) and the Jayendra
     monastery in Srinagar (03.06.x2). The great stūpa by the big village belongs to 09.03.15a. All are low. The
     local DharmaMitra stack was down, so their ten passages were translated by Claude and checked against the
     Chinese (model column `claude-opus-5-5 (DharmaMitra unavailable)`; the map labels them so).
2. **Authorities** (`data/coded/auth_*.tsv`).
3. **Survey, Annual Reports, *Indian Archaeology*, EI/CII.**
   - **Files:** `data/coded/asr_batch*`, `ar_batch*`, `iar_batch*`, `epig_batch*`; indexes in `data/*_hits.tsv`;
     instructions in `data/ASR_`, `AR_`, `IAR_` and `EPIG_INSTRUCTIONS.md`.
   - **How passages were found:** each source was indexed for passages naming the pilgrim, the excavated sites, or
     the Sanskrit names of disputed places.
   - **What is coded:** each passage's author, place, site, stance and evidence, with a verbatim quote checked by
     `scripts/check_quotes_asr.py`.
4. **Gazetteers** (`data/coded/gaz_batch*`). 1,188 relevant hits, of which 219 are second scans of a passage in another
   copy of the same volume (`data/gaz_duplicates.tsv`, `scripts/gaz_duplicates.py`): 969 distinct passages, each counted
   once per place.
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
   - **A third check, against Li Rongxi** (*The Great Tang Dynasty Record of the Western Regions*, BDK 1996;
     `data/LI_REVIEW_INSTRUCTIONS.md`, `review3_li_*.tsv`, quotes checked by `scripts/check_li_quotes.py`): of 484
     passages 424 stood, 57 had minor slips and 3 major errors (Suvarṇagotra's queens, 世以女稱國, read as a name;
     the Buddha at Ahicchattra preaching *to* the dragon king, read as being one), all corrected; the Chinese decides,
     Li is a reader. Where CBETA's text is corrupt and Li and Ji's text agree on another edition's reading, the English
     follows that reading and says so (中安國 for 守安國, 01.17; 增損 for 繒絹, 01.05; 如榻 for 如塔, 03.01.05: all Song,
     Yuan and Ming readings in the Taishō apparatus), and 兩三月 / 兩安居 are read 雨 ("the rains"), the text's own idiom
     (唯雨三月, 05.01), on the apparatus's Song 雨 (08.06.30, 09.02.16) and the Sixi print's 雨 (07.01.10); at 09.02.03a
     no edition is recorded with 雨. Li's own misreadings (mostly directions and
     numbers) are listed in `data/text/LI_CHECK.md`.
7. **Religious affiliation** (`data/religion/religion_*.tsv`; checked by `scripts/check_religion.py`).
   - **What is coded:** for each place, from its own passage, the monasteries and monks, the schools, the deva temples,
     the other traditions, the kind of site, and the state of Buddhism.
   - **Schools stated for countries:** Sammatīya 16, both vehicles 15, Mahāyāna 14, unspecified Hīnayāna 12,
     Sarvāstivāda 11, Mahāyāna-Sthavira 4, Sthavira 2, Mahāsāṃghika 2, Lokottaravāda 1.
   - **Other traditions, across all places:** Pāśupata 15, Śaiva 11, Jain (mostly Digambara, 露形) 12, Sūrya 2,
     Kāpālika 1.
8. **Notes** (`data/notes/notes_*.md`, 456 notes). The disputed places came first (312 notes). A second pass
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
   - **Country areas (approximate):** a layer that gives each country an extent from its own circuit figure
     (`scripts/country_areas.py`, `data/country_areas.tsv`, `map/country_areas.json`). For 134 of the 148 countries
     the text gives a circuit (國周N里; Bāmiyān and Khwārazm give breadth and length instead). The circuit is scaled
     by the straight-line km per li of its juan's route legs (`route/li_regions.tsv`), so the Deccan's inflated
     figures shrink as its distances do, and turned into an area at 0.75 of a circle's compactness. From the
     study's point for the capital, every country then grows over land at once, nearest cells first, until it
     reaches that area or 1.6 times its radius; neighbours meet half-way, and the sea stops growth. 130 are drawn:
     80 at their full area, 50 hemmed in by neighbours, the sea or the cap. Not drawn: 14 with no circuit (the six
     hearsay countries of SE Asia, Rāmagrāma and Kuśinagara, which are "deserted", Laṅgala's "several thousand li
     each way", the hearsay Fulin, the Women's country, 稽疆那, Nārikela island, Wakhan) and 4 whose capital has no
     point. Rivers the text names as a country's border are used (`data/country_borders.tsv`, ten borders of nine
     countries: Chach and Sutrushana on the Syr Darya, Kumidha and Balkh on the Oxus, Gandhāra, Siṃhapura and Ṭakka
     on the Indus, Ṭakka also on the Beas, Śatadru on the Sutlej, Srughna on the Ganges; Natural Earth 1:10m
     courses): the country may not cross the river, whose line is carried on straight beyond its ends, and grows
     more readily towards it. Phrases about the capital (國大都城西臨殑伽河) are not borders and are left out. One
     check fails: Śatadru's "great river" on the west (西臨大河) lies north and north-east of the study's point for
     its capital (Sirhind), which fits the Sanghol alternative no better; it fits a country in the Ropar–Nalagarh tract east of the
     Sutlej's southward stretch (note on 04.05). Mountains named as borders are used too
     (the same table, 13 rows): a range on one side (Kapiśa's and Lampāka's 北背雪山, Srughna's 北背大山, Khuttal's
     東接葱嶺) is a border at its crest (the highest ground within 60 km past the range's foot): the country may
     take the near slope, nothing beyond; mountains all round (山周四境 for Ferghana,
     Nagarahāra, Kulūta and Brahmapura; 四境負山 for Kashmir; 四面據山 for Agni; 山嶺周境 for Kosala; 三陲黑嶺 for
     Kapiśa and Lampāka) are read as a border at the crest: the country has the whole drainage basin above the
     gorge by which its river leaves the ring, up to the watershed, closed to its neighbours (the gorges, in
     `scripts/country_areas.py` GORGE: Tiemenguan above Korla for Agni, the Farhad narrows at Bekabad for Ferghana,
     the Panjshir's lower gorge above Naghlu for Kapiśa, the Alingar's mouth for Lampāka, Dakka for Nagarahāra,
     Baramulla for Kashmir, Larji for Kulūta, Kalagarh for Brahmapura, the Mahanadi's exit from Chhattisgarh for
     Kosala; each snapped to the grid's channel below the capital) (a basin stops at another country's capital, so Kapiśa's
     stays its own inside Nagarahāra's Kabul river), and beyond the basin it may not climb high ground. High ground is
     ground standing a set rise above the capital's valley floor (the lowest of its 3×3 cells), the rise set by
     region at roughly half the relief between the valley floors and the heights around them: 1000 m for the Tian
     Shan and Ferghana (Agni, Ferghana), 1200 m for the Oxus and Hindu Kush (Khuttal, Kapiśa, Lampāka, Nagarahāra),
     1500 m for the western Himalaya (Kashmir, Kulūta, Srughna, Brahmapura) and 250 m for central India (Kosala).
     Heights come from the open AWS terrain tiles at zoom 5 (`scripts/terrain_grid.py`, `data/ref/terrain/`,
     gitignored). Every one of the eleven meets high ground where the text puts it. The nine basins come from a
     0.01° grid of zoom-8 tiles over each country's window (`data/ref/terrain/fine_*.json`; a 0.08° cell counts when
     half of it lies in the basin), on which every channel passes within 0.6 of a 0.08° cell of its gorge; the 0.08°
     grid could not route Agni's Kaidu or Brahmapura's Ramganga. Ferghana fills its valley above Bekabad, Kashmir and
     Kulūta keep to their basins, and Kosala fills the Chhattisgarh plain up to its rim of hills. Kapiśa, at first
     drawn at 6% of its circuit because Andarab and Bamiyan took the slopes inside its ranges, now has its whole basin
     above the Panjshir's lower gorge (the Ghorband, the Panjshir, Nijrab and the Koh-daman up to the Hindu
     Kush; the Tagab joins below the gorge), 12,728 km², 15% of its circuit (about 1,300 km² of it, east of Kabul,
     is a fault of the fine grid, which closes the Kabul river's gorge below the city). Kapiśa's shortfall is not unusual: set against the perimeter of its basin,
     the circuit runs 1.8 times too long at its juan's li, Kashmir's 2.4 times (at the Gandhāra–Kashmir li of 0.15 km),
     Kulūta's 2.6 and Brahmapura's 3.5, while Ferghana's (0.8), Lampāka's (0.9) and Kosala's (1.2) fit. The Himalayan
     and Hindu Kush circuits run long, as the li do on mountain roads, or take in hill country beyond the basin. The areas show size and rough reach, not borders: the
     capital need not have been central, rivers have moved since the 7th century, the rises are a choice made by
     region, and the circuits themselves are rounded figures. The method is set out step by step, with Kapiśa worked through and its
     identification, in `map/COUNTRY_AREAS.md`.
   - **Place panel:** the study's identification first, then Mizutani, the authorities, every source, the Xiyu ji
     and Life passages with translations, and the note.
## What the recent scholarship changes

The pass over the literature since 1985 (November 2026; `data/LITERATURE.md`) changed 86 updates rows, and the 19 items downloaded on 12 November 29 more (four of them new notes for minor
Kapilavastu sites). Most add evidence or candidates; these change the picture:

- **Kapilavastu** (06.02) is open again between Piprahwa–Ganwaria and Tilaurakot (low): see above. Its dependent
  sites follow; Gotihawa stands on its own evidence as Krakucchanda's town (06.02.05, Mauryan stūpa and pillar stump in
  situ, Verardi via Falk; medium).
- **Bamiyan** (01.37.01, 01.37.01a): the ICOMOS radiocarbon dates (Petzet 2009, pp. 231–35) put the East Buddha
  at 544–595 and the West Buddha at 591–644 (2σ), so both most probably stood in c. 630; no metal was found on the
  painted clay, so 鍮石 describes a gold-painted surface (Kuwayama's reading). Tarzi 2007 dated the Eastern Monastery's
  rebuilding to the later 6th century (in use in 630) but had not found the reclining Buddha (01.37.02 stays low).
- **Gūzgān** (01.34): Sims-Williams 2002 shows Ambēr (Sar-i Pul) as the capital only in the Arab period; the
  pre-Islamic kings sat at Gurziwān/Kundarm in the mountains, so the capital of 630 is open. **Chach** (01.09): the
  chief town is open among Kanka, Mingurik and Binkath. **Nagarahara** (02.03.01a, 02.03.02): Errington 2017 shows
  Kuwayama's Shah Nasr Ghundai to be Masson's Tepe Ashrak and adds Tepe Khwaja Lahori (Mizuno) as a third candidate
  for the Dīpaṅkara stūpa. No rating changed.
- **Rāmagrāma** (06.03): the brick stūpa S of Parāsi Bazar (Ramgram, Nepal), about 46 km E of Lumbinī at the study's
  li, is a new candidate (Falk 2017; low); Dharmauli the alternative. The charcoal stūpa (06.03.04) is open between
  Lauriya-Nandangarh, Rajdhani and Falk's Rampurwa, none fitting every leg.
- **Gandhāra:** Varuṣapura (02.04.14) drops from high to medium: nothing at Shahbaz Garhi names it, and Errington's
  Shahr-i Bahlol (1993, known only through Khan Khattak 2019's quotation, where it is a premise) is a rival,
  with the Takht-i-Bāhī hill for Daṇḍaloka, which lies NNW of the town where the text has NE. The Bhīmā shrine (02.04.17) is open between Karamar, which fails
  Xuanzang's bearing, and Kashmir Smast, with an excavated Śaiva complex and reported Bhīmā inscriptions but twice
  the distance. A slab "said to come from Hund" names Udabhāṇḍa (02.04.18; Kimmet 2021).
- **Taxila:** Naiki (2021) puts the 7th-century city in Rawalpindi and the Treasure stūpa at the Dharmarājikā. His city
  fails the 70 li from the dragon pool and is kept as a rival only; the Treasure stūpa (03.03.03) is open between Baoti
  Pind and the Dharmarājikā, deserted after a massacre in the late 5th century as the text's 久絕僧徒 requires.
- **Swat:** the Uttarasena stūpa (03.01.10) is open between Shankardar and Tucci's excavated Nawe-kalai; several sites
  gain candidates reported by Bibi (2017; low).
- **Bolor** (03.02): the rock inscriptions settle the name as *Palola, the country of the Palola Ṣāhis (von Hinüber
  2004, pp. 105–106), whose dated royal inscriptions are all in the Gilgit valley (671, 687). The seat stays open
  between Baltistan (Jettmar, from 8th-century sources) and Gilgit; the one Baltistan inscription (Shigar) names
  another king and is 6th-century.
- **Kapilavastu** (06.02), from *The Sacred Garden of Lumbini* (2nd ed. 2019): Tilaurakot has a street grid of the
  Kushan period and building after it (a Gupta-style structure under Samai Mai), where Ganwaria has nothing after
  c. 300; but the excavators assume the identification and nothing names the place, so it stays open. A walled
  central complex and a monastery east of the city are candidates for 06.02.x2 and 06.02.x1 (undated, low).
- **Veṅgī** (10.13) drops from high to medium: Peddavegi is "very plausible, but we do not have any hard proof"
  (Francis 2025), since nothing on the site names it. The inscriptions naming Dhaññakaḍa (10.14) were found
  elsewhere and are of c. 300 or earlier, so Dharanikota stays medium. **Balkh** (01.32): Bernard reads the 20 li
  as a wall of c. 10 km, which suits the outer town wall better than the Bālā-Hisār; which wall Xuanzang measured
  is open.
- **Andhra:** Pūrvaśaila (10.14.02a) is weakened and open: the Amarāvatī stūpa stands on a plain (Shimada 2013), the
  text puts the convent on a mountain (據山). Vadnagar gains sealings reading "Anandpur" from the Kṣatrapa level
  (11.09; Ambekar et al. 2023).
- **Khotan:** the royal city (12.22a) drops to medium (Talati 2024: Yotkan was never excavated and may be only part of
  the city); Phema's fort (12.22.12) is probably the Kanaqin fort by Ulugh-Ziyārat, from the document equating it with
  坎城 (Zhang 2016, after Li Yinping).
- **Tokharistan:** Miyamoto's Bactrian documents give Gūzgān's seat at Sar-i Pul (01.34, perhaps the Tang 遏蜜城) and
  take Ishkashim for Wakhan's later seat, not Shighnan's (12.16a weakened, Kuwayama 1985). At Bāmiyān, Tarzi's
  excavated Eastern monastery is a candidate for the reclining Buddha (01.37.02, open).
- **Magadha:** a BHU survey (IAR 2013–14) and Anand's field reports give candidates where the study had none: Ayer
  for Buddhavana (09.02.01), Nanan for Kālapināka (09.03.10), Juafardih and Kool beside Jagdishpur for Kolika (09.03.08),
  all low. A sealing naming Śakrāditya was found 1 km N of Nālandā (IAR 2007–08). The Gurpa point was corrected.
- **Oḍra:** Puṣpagiri (10.09.02) is open between Mizutani's Udayagiri–Khandagiri, where the only excavation found a
  Jaina shrine and D. Mitra saw no other faith (IAR 1958–59), and the Assia hills N of the Mahānadī (Lalitgiri;
  Langudi claimed). The sealings of Ratnagiri and of the Jajpur Udayagiri ("Madhavapura") name other monasteries.
- **Kucha:** the Ashliji monastery (01.06.04) is open between Duldur-Aqur and the Kizilgaha caves with Bozkhana,
  10 km NW of the capital, which fit the text's bearing (Zhang and Zhu 2019).
- **Strengthened by excavation:** Ujjayinī (Garh-Kalika, 11.12) and Bharukaccha (Broach, 11.04), both occupied through
  Xuanzang's century, now high; Kāñcīpura (10.16) gains its first site evidence. Banavasi is occupied through the 7th
  century and tied by its excavators to Xuanzang's stūpas, but Koṅkaṇapura (11.02) stays open.

## Main proposed revisions to Mizutani

These are medium- or high-confidence proposals that move away from Mizutani; how each stands to Ji's standard is in
`data/standard/compare_*.tsv`. The full list is in
`data/notes/updates_*.tsv`.

| Id | Place | Mizutani | Proposed | Basis |
|---|---|---|---|---|
| 02.04.06 | Kanishka's monastery | possibly Gor Khattri | W mound beside the stūpa, Shah-ji-ki-Dheri | Spooner: casket names "the Vihāra of Kanishka" |
| 02.04.16 | Ekaśṛṅga's convent | not given | Butan, below the Shahkot Pass (Swat) | Stein AR 1911–12 |
| 03.05 | Uraśā capital | Haripur | Mangali (country confirmed as Hazara by the Bedadi ladle "Urasa-rajya") | Cunningham; Hargreaves; Konow CII 2.1 |
| 04.06 | Pāriyātra | Bairat (agreed) | Bairat, weakened | Sahni AR 1935–36 |
| 04.11 | Brahmapura | Srinagar (Garhwal) | Lakhanpur or nearby | Talesvara plates issued from Brahmapura (EI 13) |
| 05.01.09 | Navadevakula | not given | Newal near Bangarmau | ASR XI; Unao 1903 |
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

- **Later scholarship.** Mizutani is the 1971 state of the question; Ji (1985) brings it to about 1980. Of the work
  since then, 104 items have been read (`data/LITERATURE.md`); the searches ran out of budget part way, so
  coverage is uneven, and the key books and paywalled reports (Coningham et al. 2018 on Tilaurakot, Srivastava 1996,
  the Rissho reports and the full Kansai report on Maheth (only its KAKEN summary is read), Kuwayama's Rinsen volumes, Errington 1993 (Errington 2017 is read, and Errington 1993 is known through Khan Khattak 2019's quotation), Saran 2008 on Juafardih, the Telhara
  report) are listed there as wanted. Works cited at second hand are marked "not read" in the notes. *Indian
  Archaeology* is in up to 2013–14, without 2001–07 and 2008–09.
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
- `data/standard/compare_*.tsv`: each place's standard identification (Ji 1985, or Mizutani) and how the study stands to it.
- `data/literature.tsv`, `data/LITERATURE.md`: the recent-scholarship bibliography, its status and the list of PDFs wanted.
- `data/places_mizutani.tsv`: the master table.
- `data/places_added.tsv`: 71 places missing from Mizutani's numbering (ids `.xN`), added from the sources. Mappings
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
- `map/`: the map page and its builder; `map/country_areas.json` is the country-areas layer (`scripts/country_areas.py`).
- `data/country_areas.tsv`: each country's circuit as the text gives it, the km per li used, the target and drawn area,
  and the river and mountain borders with a check of each. `data/country_borders.tsv`: the rivers and mountains the
  text names as borders.
  `data/ref/ne_rivers/`: Natural Earth 1:10m river centrelines (public domain; gitignored).
- `scripts/`: OCR join, text build, extraction, translation, quote checkers, indexes, merge and join.
- `data/*INSTRUCTIONS*.md`, `data/NOTES_REVISION_*.md`: coding instructions.
- `PLAN.md`: the original plan.

Rebuild:

```
python3 -I scripts/merge_mizutani.py && python3 -I scripts/build_places.py && python3 -I scripts/build_study_view.py && python3 -I scripts/place_from_text.py && python3 -I scripts/build_study_view.py && python3 -I map/build_geo.py && python3 -I scripts/country_areas.py && python3 -I map/build_page.py
```
