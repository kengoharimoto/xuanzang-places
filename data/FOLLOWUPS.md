# Follow-ups noted during coding

- **Gaiji codes in T2087**: `data/ref/t2087_joined.txt` writes rare characters as `mNNNNN` (m03474 呾, m10370 㤄,
  m16476 殑, m20544 猱, m22129 痆, m23653 瞢, m25561 窣, m25946 笯, m27246 紇, m40981 鑊, m42434 霫, m42889 鞞…).
  `t_route` keeps them (verbatim check); a mapping table would make the routes readable.
- **Middle Chinese readings** (`mc_reading`) are often garbled by the OCR and marked "(OCR)": clean against the page
  images if the readings are wanted.
- **12.06 瞢健**: Mizutani reports Beal's view as Munjān; Beal's heading says Munjan, but his note (vol. 1 n. 144)
  puts Mung-kin around Talikan–Khanabad, i.e. agreeing with Mizutani.
- **Duplicate gazetteer scans**: several volumes exist in two scans (Jhelam 1907, Monghyr 1909/1960, Lyallpur 1905,
  Karnal 1884, Meerut 1875, Khulna, Manbhum, Midnapore…): count passages, not hits, in the report.
- **Places missing from the master table** (resolved 2026-11-06: 61 rows added in `data/places_added.tsv`, ids `.xN`; every `new` coded row mapped in `data/coded/new_resolved.tsv`) found by the gazetteer coders (`xz_id = new`): the great Brahmanical
  city on Takka's eastern border (Lahore, per the Lahore/Punjab gazetteers); the Aśoka stūpa NW of Sthāneśvara
  (Karnal 1976); the Aśoka stūpa south of Siṃhapura (Stein, Jhelam gazetteer). More in `data/coded/gaz_batch*.tsv`.
- **Mizutani's slips** noted by coders: Kashipur coordinates with N/E swapped (04.12); "Eastern Ghats" for the
  western range (pdf 355).
- **Misfiled volume in the gazetteer study**: `in.ernet.dli.2015.281327`, listed as CP10 "Chhindwara", is a reprint
  of Beal's *Buddhist Records* (vol. IV of a reprint), not a gazetteer (found while coding batch 2; all its hits coded
  `relevant=no`). The gazetteer-vedanta selection table needs fixing, and any CP10 counts there are suspect.
- **Coding corrections applied** after the notes pass: hits 917, 1013 `12.02`→`12.02a`; hit 155 `09.02.01`→`08.04.02`;
  hit 104 `new`→`07.02.04`.
- **Stance judgement calls** flagged by the notes writers (left as coded): hits 199/1723/1810 (Muchharin for 08.06.18),
  213/214 (Parbati hill for 09.03.14) and 117 (Chhathagiri) are `repeats` but name a site different from Mizutani's.
  The `gaz_argues` count for 09.03.01 (Nālandā) includes four Broadley passages that really argue about 09.03.11.
- **Atkinson ATcu3** (`cu31924023947751`, listed "unidentified 1874") is a second scan of AT11, *Himalayan Districts*
  II (1884): fix the year in the gazetteer selection metadata.
- **Possible slips in the sources**: Mizutani cites Majumdar p. 721 for the hill N of Kurkihār (09.01.03), but
  Majumdar calls Gurpa probable; Cunningham's "firm" Rohinila for 09.03.15b may only report Vivien; Dey puts the
  Mora hill NW of Bodh Gayā (all others NE).
- **02.02a Lampāka capital**: Mizutani (citing 水野清一, 『文明の十字路』 p. 134) really does print "Begram on the Logar, 10 km
  SE of Kabul" (checked on pdf 94). It sits outside Lampāka as others bound it; Vivien's Mandrawar is the only
  candidate inside. Hit 1246/1322 `new`→`03.04.02` corrected. Hit 1219 (Attock) is coded `repeats` where the same
  Cunningham passage in Rawalpindi is `argues`; hit 1903 (Thana footnote, Manikyala for 02.04.03) is coded
  `alternative` but is unargued.
- **Cunningham's ASR reports** were not coded (only *Ancient Geography*); several gazetteer passages cite them (e.g.
  Karmal for the Kunāla stūpa, ASR II). Adding ASR I–XXIII would fill gaps in the `cunningham` column.
- **Juan 6–7 fixes applied**: hits 750/778 lose 07.01.04; hit 837 `argues`→`repeats`; hits 615/659 `07.02.03b`→`07.02.02`;
  Dey's Hoey "Bul'i" row moved from 07.03.13 to 07.04 (the Monster Fish story).
- **Still open**: hits 620/621 volume "Basti District, 1801" is probably NWP Gazetteer vol. VI (1881) — fix the
  metadata; 06.01.14 `mz_other_views` credits Cunningham for Tandwa but Mizutani's quote names Beal and Legge only;
  hit 333 credits Chirand to Cunningham where Majumdar gives it to Carlleyle. Mizutani's own slips: "about ten miles E"
  for the cremation stūpa (06.04.11); Gandak = Hiraṇyavatī (06.04.03a) conflicts with his Kasia.
- **Juan 10–11 fixes applied**: hit 1528 loses 10.09/10.09.02; hit 448 loses 10.17.03. **Open**: the Chaul = Chi-mo-lo
  rows (1930/1957) are a gazetteer confusion of 枳秣羅 (another name for Malakūṭa) and inflate 10.17's count; the
  10.12.05 rows concern Faxian's monastery, linked only through Mizutani's equation; Majumdar p. 728 vs Mizutani on
  the Valabhī record of 639 and Mālava (11.05) needs checking in the text.
- **ASR coding fixes applied**: passage 361 loses 04.02.03; 151/152 `03.04.06`→`03.04.05;new`; 154 page 172; 229
  `03.04.02`→`03.04.03`. ASR V pp. 67–68 (the Taxila copper plate; Sirkap/Sirsukh; Hatial) is now coded (`asr_batch6.tsv`). **Open**: the "Madrasa" mound at Thanesar (passages 165, 370) may be one mound or two;
  passage 354 — Cunningham read 百四五十歩 as li; passage 177 evidence says 2000 li where the quote has 1,000; passage 463
  bears on 10.12 too; passage 387's `new` duplicates 386.
- **More ASR fixes**: passage 15 gains 09.03.06 (mound A, 63 ft not 53); 329 `confirms`→`revises`. **Open**: Mizutani's
  "Urel tank" for Muchalinda may be a misreading of Cunningham's plate XL (ASR XI), where Urel Tal is the Uruvilva tank
  and Muchilinda's is Teskar Tal; gazetteer hit 1762's "coincidence in position" sentence is Beglar's (ASR VIII p. 108),
  not Cunningham's. Uncoded ASR passages: vol. VIII preface p. viii (Tilaḍaka "beyond all doubt"; Son Bhandar defended),
  Beglar's Note pp. ix–x (withdrawing Bhika Pahari).
- **Annual Reports**: the IA item labelled 1928–29 (`archaeologicalsurveyofindiaannualreports192829platesmissing2749_499_b`) is
  in fact the 1929–30 report; its passages (752–778) are kept but set `relevant=no`. The 1928–29 report and 1918–20
  are still missing. Eight volumes (1903–04, 1920–22, 1925–27, 1929–30, 1935–36) were re-OCR'd with Google Vision
  because the IA text was Hindi-language OCR of English.
- **Multi-place passages in places.tsv**: a survey/AR passage coded to several ids carries one `asr_identification`,
  which `build_places.py` then shows under each id (e.g. AR passage 668: Kosam text under 04.08 and 04.08.02; 367:
  Uraśā/Hund/Taxila under 04.14). The notes are written from the passages and are right; the `asr`/`ar` columns can
  mislead for such ids. AR passage 321: the Bilsar Maitreya was bought, not excavated; Cunningham's mound 33 ft.
  Gazetteer hits 570–571 (Muttra 1911) are Vogel's AR 1906–07 text, not Führer's; hit 1792 "¼ mile" may be Sahni's ¾.
- **AR coding, open**: passage 114's single `confirms` stance shows against 02.04.16 where Spooner's Takht-i-Bahi remark
  is a rejection; 714 (Stein, Swat) also bears on 03.01.04a and 03.01.01a, uncoded; 211 bears on 02.04.06; 500 bears on
  01.38a. No Hazara gazetteer is in the gazetteer set (Hargreaves cites one for Mangali = Uraśā). AR passage 236 lost
  its stray 02.04.14.
- **EI/CII sources**: `epigraphia-indica-vol-15-vol-02.pdf` in the iCloud folder is a 1970 reprint of EI vol. II, not
  vol. XV pt 2 (its rows set `relevant=no`); `cii_3` is Bhandarkar's revised CII III (ed. Chhabra & Gai, 1981), not
  Fleet 1888. Not available as text: CII 4.2 (djvu only), EI vols 37+. Checker note: NFKC turns "…" into "...", so a
  full stop right before an ellipsis breaks a fragment.
- **EI/CII and IAR coding, open**: Taradih (Bodh Gayā) is SW of the temple in IAR 1981–87 but N in IAR 1988–89 (iar passages
  471, 492 coded to 08.06.30 on that basis); IAR 1975–76 pp. 61–62 epigraphy ("Prathamaśiva also called Pūrṇavarman") and
  the Sarai mound seasons 1976–78 are uncoded; Pūrṇavarman's copper Buddha needs its own row (iar 319 `new`, 377 under
  09.03.06); epig passage 67 misstates Bhandarkar on the old Son confluence (just below Patna); Rājagṛha IAR 1953–54
  and 1974–75 digs uncoded. IAR 1979–80 and 1985–86 were downloaded on retry and coded; IAR 1990–91 is absent from the archive.
- **From K. Harimoto's notes, to obtain or read**:
  - Mirchandani 1967 (*JIH* 45, pp. 309–c. 356; Internet Archive dli.bengal.10689.12681): coded; pp. 312–313 and
    348–349 are missing from the OCR.
  - Marquis's identifications of 提謂城 and 波利城 near Balkh (01.32.02): the slides give no names or coordinates.
  - Bakker 2014 on Śaṅkukarṇa at Banbhore, as cited in SP IV p. 55 n. 133.
  - Bakker, *The Alkhan* (2020): not open access; only a 10-page excerpt is on disk. The open-access Sourcebook
    (Balogh ed. 2020, Zenodo 7386068) is coded for 11.17, 04.01.02 and 03.06.
  - The Ajanta Cave 26 Acala inscription (Burgess and Indraji 1881): cited from general knowledge, not coded (11.03.03).
- **Coordinates not moved** for 01.38.03 (Tapa Skandar) and 01.38.03a (Khair Khana): these are alternatives; the
  map keeps the old points.
- **Stein, MASI 37 (1929)**: the Internet Archive OCR (in.ernet.dli.2015.35549) stops at about p. 64, before the Tor-dherai stūpa description and Konow's appendix on its Kharoṣṭhī inscriptions. Other scans (in.ernet.dli.2015.70429, in.gov.ignca.21977) may be complete.
- **The Life's distances and bearings** differ from the Xiyu ji in many places. The reviewers list them in `data/text/life_review_*.tsv` (`issues`) and the agents' notes are in `life_anchors_*.tsv` (`note`). Examples: Kapilavastu 800 li from Śrāvastī (Xiyu ji 500); Rāmagrāma 500 (200); Viśoka E 500 from Kauśāmbī; Karṇasuvarṇa SE 900+ from Puṇḍravardhana; Andhra SE 900+; Coḷa W 1000+. Only the Sindh stretch has been route-tested on the Life's legs (`route/chain_scores_life.tsv`).
- **04.15.02 (Sāṃkāśya's stairs)**: resolved. The Taishō (Korean base text) reads 城西二十餘里. Its apparatus (n. 0893013) gives 東 for the Song, Yuan and Ming editions and two Japanese manuscripts (【宋】【元】【明】【甲】【乙】), and the Life has 城東二十餘里. East is therefore the reading of every witness except the Korean edition. Noted in 04.15.02.
- **Sixi edition (1132)**: juans 1–8 OCR'd (`data/ref/sixi/`). It confirms the Taishō apparatus's Song readings (route/README §9). Juans 7–12 were then checked against the Jōō print of 1653 (README §9); it is not one of the Taishō witnesses, but it supports the Song-group readings at 12.09 and 12.10. The 日鈔本 manuscripts in the same IA item are not yet checked.
- **Raised by the notes on untested places (2026-11-06)**:
  - Route legs: the 09.02.03a/03b/04 legs are now anchored on the Yaṣṭivana and the great mountain
    (`segment_overrides.tsv`). Gachi (01.36) has moved to Darrah Gaz, c. 30 km S of Balkh (`coords_study.tsv`).
    Still open: 01.19 Khwarizm's leg from Vadi (the text's figure, not the site); 媲摩 → Niya (12.22.13), 200 li for
    185 km and no leg because of the variant 嫓; Kohmāri (12.22.04) long for 20 li; Mount Ilam (03.01.05) 19 km for
    400+ li; Sultanpur (04.02.03) fits neither 50 nor 500 li.
  - Text: 12.22.15's passage reads 至都邏故國. SAT's Taishō transcription has 至覩貨邏故國, so the missing 覩貨 is a slip in
    CBETA's text, not a variant (no apparatus note); the checked translation already reads Tukhāra. Resolved. 01.09a's excerpt is 01.11's 東臨葉河 sentence. 12.18.02's Life
    passage is the Cīnadevagotra story, not the peak legend.
  - places.tsv: multi-place coded passages are now split into per-place entries (`data/coded/split/`); the 16 coding
    slips found (e.g. six Rajbadidanga IAR seasons under 10.08 that concern only 10.08.02) are dropped from the
    places they don't concern. 11.12's EI passage (Sircar, EI 34) is counted but its evidence is empty.
  - Small slips: 04.01.x4's note should say three days (經三日), not two; Cunningham's "4 miles NE of Ohind" for
    02.04.19 conflicts with the text's NW; Mizutani's quotes carry OCR errors (e.g. 12.16).
- **From Ji Xianlin et al. (1985), to obtain or read** (cited by Ji, not in these sources): Srivastava,
  "Kapilavastu and its precise location", *East and West* 29 (1979) 61–74; N. Ahmed's Mahasthan report (Bhasu Vihar,
  10.04.02, raised to high on Ji's report alone); B. P. Sinha, *Archaeology and Art of India* (1979); Belenitskii et al.,
  *Srednevekovyi gorod Srednei Azii* (1973), for Khanabad (01.08), which could not be placed; Stavisky, *Kushanskaya
  Baktriya* (1977); 内田吟風 1972; 謝方, 南亞研究 1982/2; Tugusheva 1980 (Uighur *Life*); Huang Wenbi on Zanguya
  (12.22.06) and Shisbir (12.22a).
- **Ji's slips noted by the folding agents** (recorded in the notes where they matter): Benares on the left bank (07.01);
  Altekar's relic stūpa on the wrong monument (07.03.03/04); Nigali Sagar taken for Lumbinī's pillar (06.02); 黑嶺 =
  Hindu Kush against his own p. 137 (01.04a); Bunjikath = Panjikent (01.11); the eastern Ṭālaqān (01.35); Kalsi's
  coordinates for Sugh (04.09); Kashipur's lat/lon transposed (04.12); "B. C. Law wrote NE for SE" (10.12; Sirpur is
  ENE of Raipur); Jaugada on the Chilka (10.10); Cunningham credited with Jammu (11.17); Vaibhāra/Vipula
  self-contradiction (09.02.11, pp. 719/730). Coding fixes applied: 01.07.03 Klyashtornyi (not Kyzlasov); 01.38.01
  Ji names the hill, not Shotorak, as the site; 01.25 Stavisky's title.
- **07.01.02**: the note's summary of Mizutani dates the riot that destroyed the Lat Bhairon pillar to 1908; the riot was
  in 1809. Check Mizutani's own wording.
- **Resolved 2026-11-07**:
  - Foucher's Rāhula passage (01.38.02), lost in the Toyo Bunko OCR, was recovered by a Vision re-OCR of V-1 pdf 0151.
    It confirms Kâfir-Qaleh, though Foucher writes "Sud-Ouest" where the text has 東南.
  - Quality check of 30 agent-written notes (`data/notes/qc_2026-11-07.tsv`): 21 ok, 8 minor, 1 major, all fixed.
    The high ratings that name no excavation or inscription were then audited (`data/notes/high_audit_2026-11-07.tsv`).
