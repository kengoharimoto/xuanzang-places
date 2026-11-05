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
- **Places missing from the master table** found by the gazetteer coders (`xz_id = new`): the great Brahmanical
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
