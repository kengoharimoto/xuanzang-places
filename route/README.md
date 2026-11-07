# Testing identifications against Xuanzang's distances and bearings

Two checks on the identifications, using only the texts:
- a **route model**, which asks whether a proposed site sits where Xuanzang's li and bearing put it;
- a **comparison of the figures** in the *Xiyu ji* (T2087), Daoxuan's abridgement 釋迦方志 (T2088, 650) and Huili's
  *Life* 慈恩傳 (T2053), with Mizutani's notes on variant readings.

## Files

| File | What it holds |
|---|---|
| `segments.tsv` | One row per place. A row whose route sentence gives a distance has the starting place (`from_id`), the legs (bearing and li), the li range and the verb. It is built from the master table by `segments.py`. `segment_overrides.tsv` corrects six parsing errors found by the variant readers, each with a reason. |
| `model.py` → `li_calibration.txt`, `segment_tests.tsv` | Calibrates the li on agreed places, then tests every leg against Mizutani's points (`data/coords.tsv`) and flags distance and bearing misfits. |
| `candidates.tsv` | Coordinates for 231 rival sites and Mizutani's own, for 155 places. The coordinates are approximate: obscure villages are placed from the proposer's own distances, and `note` says so. |
| `candidates.py` → `candidate_scores.tsv` | Scores each candidate against its incoming and outgoing legs. |
| `chains.py` → `chain_scores.tsv` | Scores whole alternative routes, each leg measured between one scheme's own sites (§5). |
| `li_regions.py` → `li_regions.tsv`, `li_schemes.tsv` | The li by juan, visit and leg length; each scheme's best-fitting scale and the scatter left over (§8). |
| `dem_fetch.py`, `li_paths.py` → `li_paths.tsv` | Least-cost walking routes over the Copernicus GLO-90 DEM for the same legs: li against route length and walking time (§10, Test 3). |
| `li_terrain.py` → `li_terrain.tsv`, `elev_cache.json` | Each leg's km per li against its relief (SRTM) and the terrain words of its route sentence: was the li a measure of time? (§10). |
| `../data/coords_study.tsv` | Coordinates for the study's own proposed sites, scored as the scheme "Study (proposed sites)" in §6–8. |
| `apparatus_variants.py` → `apparatus_variants.tsv` | The Taishō apparatus notes of T2087, flagged where a reading touches a direction or numeral (§9). |
| `sixi_check.py` → `sixi_apparatus.tsv`, `sixi_route.tsv` | Those Song readings and the route sentences checked against the Sixi edition's scan (§9). |
| `life_segments.py` → `life_segments.tsv` | The Life's legs (from `variants_*.tsv`), in the same form as `segments.tsv` (§7). |
| `chains_all.py` → `chain_scores_all.tsv`, `chain_best.tsv` | The same for every juan: each authority's set of sites, and the best-fitting combination of candidates (§6). |
| `variants_*.tsv` | Each leg in T2087, T2088 and T2053, plus Mizutani's variant notes. Quotes are verbatim and checked by `check_variants.py`. Instructions are in `VARIANTS_INSTRUCTIONS.md`. |

## 1. How long was Xuanzang's li?

The model was calibrated on 29 legs of at least 100 li between places Mizutani treats as agreed and that are
located to site or town precision. On those legs the straight-line distance is a median **0.239 km per li**. The 10–90%
range is 0.12–0.43.

- **By region:** in Central Asia and Afghanistan (n = 6) the figure is 0.288; in India (n = 23) it is 0.231.
- **Converted to the road:** roads are commonly 1.2–1.35 times the straight line, which gives about **0.29–0.32 km per
  li travelled**.

That figure is close to Hori Kentoku's 320 m and Cunningham's working "1/6 mile" (0.27 km). It is well short of the
440 m that Mizutani adopts from Mori Shikazō's Tang small li (補注二, pdf 435).

The difference does not mean that 440 m is the wrong length for a Tang li. It means Xuanzang's stated li do not
behave like Tang official li on the ground. India's shorter figure fits a conversion from yojanas, which Xuanzang himself
defines as a day's march, at a fixed rate. §10 tests this against the terrain.

The two hearsay legs in the calibration run far shorter on the ground than stated (0.11 km per li). Hearsay figures
overstate.

## 2. The texts' figures

262 legs were compared across T2087, T2088 and T2053:
- 174 agree;
- 41 follow a different route in the *Life* (it skips or adds places, or measures from a different point);
- 21 differ in bearing and 13 in li;
- 10 have no corresponding leg.

Mizutani records a variant reading or emendation for 38 of them.

**Variants that bear on an identification:**
- **Tamasavana (04.02.03).** Every copy of T2087, and T2088, reads 500 li; the *Life* reads 50. The 50 fits a site
  near the capital, and Mizutani and the table follow it.
- **Kapilavastu (06.02).** The *Life* has 800 li from Śrāvastī where T2087 and T2088 have 500. 500 fits
  Sahet-Mahet to Tilaurakot or Piprahwa; 800 does not.
- **Rāmagrāma (06.03).** The *Life* has 500 li east from Kapilavastu where the others have 200 from Lumbinī. Mizutani
  prefers 200.
- **Kuśinagara (06.04).** Only T2088 gives a figure from Rāmagrāma: 東北 500.
- **The 戰主國 capital (07.02–07.03).** The *Life* counts the 140–150 li to Vaiśālī from the 戰主國 capital, not from
  the jar stūpa. On that reckoning the capital lies much nearer Vaiśālī than Ghazipur does. This supports the doubts
  about Ghazipur in the notes.
- **Prayāga to Kauśāmbī (05.05).** All three texts read 500 li, against about 50 km to Kosam. No variant helps. The
  *Life* gives the royal return march as "seven days".
- **Kiṭa (11.07).** All three texts read "three days". "300 li" is only the Song/Yuan/Ming reading, which Cunningham
  reread as 1,300 to reach Kaira.
- **Maheśvarapura (11.14).** All three bearings (北, or 東北 in the *Life*) support Gwalior and go against Cunningham's
  emendation to 南 for Mandla.
- **Himatala (12.11).** Mizutani follows the *Life*'s 300 li from 瞢健 over T2087's 600 by way of 訖栗瑟摩.
- **Mizutani's own emendations with no textual support.** Kapotaka (09.03.13: 150–160 li read as 50–60) and the
  large village (09.03.15a: 70 read as 170). The figures as written do not fit his sites.

## 3. Mizutani's identifications against the figures

Of the 137 legs with both ends located, 32 fall outside the calibration's distance band and 20 are more than 50° off
in bearing (`segment_tests.tsv`, column `flags`). They fall into four groups:
- **Text problems the variants explain.** Examples: Kauśāmbī, the hearsay legs in the south and the west, and
  Mathurā to Thanesar, where Mizutani himself says 東北 is wrong.
- **Disputed identifications.** Examples: Andhra to Dhānyakaṭaka, Maheśvarapura to Sindh, Avaṇḍa to Varaṇa, and the
  Kapiśa sub-sites.
- **Coarse coordinates.** These are mostly country centroids for places with no identified capital, such as Takka
  and Uḍra. Those flags say nothing.
- **Short legs within a site.** Here the coordinates cannot resolve the distances.

## 4. Rival sites

`candidate_scores.tsv` scores each candidate by how well its legs to already-located neighbours fit:
- `z`: the distance misfit in units of the calibration spread;
- `bearing`: the error in degrees.

Of the 120 places that can be scored against neighbours located to site or town precision, 18 have a rival that fits
clearly better than Mizutani's site. Most of these rest on one or two legs.

**Where the route test agrees with independent evidence in the notes:**
- **Siṃhapura (03.04, 03.04.03).** The 700 li from Taxila cannot separate Malot from Ketas: both lie about
  116 km away, against 167 predicted. The 40–50 li from the capital to the stone stūpa can.
  - Mizutani's pair, the capital at Kotera above Ketas and the stūpa at the Ketas pools, is a kilometre apart. It
    works only with Cunningham's emendation to 4–5 li.
  - Malot to Ketas (14 km) and Stein's capital north of Ketas to Murti both fit the figure as written.

  So the route test counts against Mizutani's pair, not for any one rival.
- **Mahāvana (03.01.06).** Cunningham's **Mahaban** fits, and the Shinasi stūpa does not. This rests on a single leg.
- **Hayamukha (05.03).** Cunningham's Daundia Khera fits the distances but not the bearing. Mizutani's broader area
  is about as good.
- **Coḷa (10.15).** Cunningham's **Kurnool** fits better than Nellore. The gazetteer evidence favours the Telugu Coḷa
  country (Cuddapah–Kurnool), so the two agree.

**Where it disagrees, and shows its limits:**
- **Kauśāmbī (05.05).** Rewah and Bharhut fit the 500 li. Kosam does not, yet it is confirmed by an inscription and
  by excavation. The text's figure is wrong, and the route test cannot see that.
- **Karṇasuvarṇa (10.08).** Bara Bazar fits slightly better than Rangamati. Later excavation, outside these sources,
  has favoured Rangamati.
- **Kaliṅga, Andhra and Malakūṭa (10.11, 10.13, 10.17).** Cunningham's Rajahmundry, Elgandal and Quilon fit, but these
  are mostly hearsay legs. The calibration shows hearsay figures are unreliable.

**Conclusion.** The route test is a useful filter. It confirms Malot, Mahaban and Murti, and marks places whose
figures cannot fit any proposed site. It cannot overrule an inscription or an excavation, and it is weak wherever a
neighbour's position is only approximate.

## 5. Whole routes: Sindh and Baluchistan (juan 11)

`candidates.py` scores one site at a time against Mizutani's neighbours. That penalises a scheme whose identifications
depend on each other. `chains.py` therefore scores whole routes. It covers the eight legs from Gurjara through Sindhu,
Multan, Parvata, Atyanabakela, Laṅgala, Pītaśilā and Avaṇḍa to Varṇa; Bhinmal, Multan and Harappa are held fixed.

The leg into Sindhu now starts at Gurjara (`segment_overrides.tsv`). T2087 returns to Gurjara first (從此還至瞿折羅國),
and T2088 has 從瞿折羅北野…二千里許.

| Scheme | mean \|z\| | worst \|z\| | mean bearing error | legs with \|z\| > 1.5 |
|---|---|---|---|---|
| Mirchandani 1967 (Mithankot, Gondakahar, Kasarkand, Khuzdar, Gandāva, Duki) | 0.38 | 1.11 | 18° | 0 |
| Mizutani, with Kasarkand for Laṅgala | 0.60 | 2.69 | 32° | 1 |
| Lambrick 1964 (Pano Akil–Kandhkot, Banbhore, Las Bela for Laṅgala, Sehwan, Badah, Barkhan) | 0.61 | 1.72 | 32° | 1 |
| Mizutani (Alor, Karachi, Lākoriān, Hyderabad, Brahmanabad, Bannu) | 0.62 | 2.69 | 41° | 1 |
| Cunningham's Kotesar, with Mizutani | 0.66 | 2.69 | 35° | 1 |

Mirchandani's route fits the stated li and bearings best. That holds without his emendation of 300 li to 500: the
unemended Pītaśilā–Avaṇḍa leg is z +1.1.

The study's route breaks at Avaṇḍa–Varṇa: Brahmanabad to Bannu is 810 km against about 215 predicted. Its legs into
Sindhu and into Pītaśilā are also 48° and 66° off the stated bearing.

Laṅgala is the clearest single case. Kasarkand lies due west of Karachi or Bela at the right distance. Lākoriān is 83°
off the bearing.

Two caveats:
- **Circularity.** The fit is partly circular: Mirchandani chose his sites with these distances in hand. Mizutani's
  choices rest on names and on the Arab geography.
- **The text.** Atyanabakela 臨信度河，鄰大海濱 is the main objection to Las Bela. Mirchandani reads it of the country
  ("bounded … on the east by the Indus"), but Las Bela is bounded by the Hab, not the Indus.

The Life orders the same stretch differently: Surāṣṭra → Atyanabakela → Laṅgala → north-east 700 li → Pītaśilā →
Avaṇḍa → east 700 li → Sindhu → Multan → Parvata (`variants_08-11.tsv`). Scored on the Life's legs
(`chain_scores_life.tsv`):

| Scheme | mean \|z\| | mean bearing error |
|---|---|---|
| Cunningham's Kotesar, with Mizutani | 0.64 | 57° |
| Mizutani | 0.65 | 59° |
| Lambrick 1964 | 0.71 | 39° |
| Mizutani, with Kasarkand | 0.79 | 39° |
| Mirchandani 1967 | 0.90 | 19° |

On the Life's legs the distances slightly favour Mizutani and the bearings strongly favour Mirchandani. The Life's
leg from Laṅgala north-east 700 li to Pītaśilā is too short for Kasarkand (492 km against about 167 predicted). The
Life therefore points to a Laṅgala less far west than Persian Makran. Its leg from Atyanabakela gives no figure.

## 6. Whole routes, juan by juan

`chains_all.py` repeats the test of §5 for every juan. It works in two ways:
- **Authorities' sets:** each authority's own set of sites, with Mizutani's points wherever that authority is silent.
  An authority counts only where it differs from Mizutani at two or more places in the juan.
- **Best fit:** a coordinate-descent search for the combination of candidates that best fits the figures.

Each leg scores |z| plus the bearing error divided by 45°. A "bad leg" is one with |z| > 1.5.

| Juan | Mizutani: mean \|z\| (bad legs) | Best authority's set | Best-fitting combination (places changed) |
|---|---|---|---|
| 1 | 1.17 (7) | none better | 0.83 (7) |
| 2 | 1.08 (1) | none better | 1.08 (0) |
| 3 | 1.16 (4) | Dey: 1.04 (3) | 0.96 (1) |
| 4 | 1.47 (6) | Beal: 1.28 (5) | 0.83 (6) |
| 5 | 1.1 (1) | none better | 0.64 (2) |
| 6 | 0.73 (0) | none better | 0.7 (2) |
| 7 | 0.68 (1) | none better | 0.68 (0) |
| 8 | 0.68 (0) | none better | 0.68 (0) |
| 9 | 2.42 (2) | none better | 2.29 (1) |
| 10 | 0.84 (4) | Cunningham: 0.45 (1) | 0.35 (8) |
| 11 | 0.57 (2) | Mirchandani: 0.46 (1) | 0.52 (6) |
| 12 | 0.69 (2) | none better | 0.6 (2) |

Results by juan:
- **Juan 10 (eastern India and the Deccan).** Cunningham's set fits far better than Mizutani's. The best-fitting
  combination moves eight places: Karṇasuvarṇa to Barabhum, Kaliṅga to Rajahmundry, Kosala to Chanda, Andhra to
  Elgandal, Coḷa to Kurnool and Malakūṭa to Quilon. For three of these the study has inscriptions that override the
  figures (Raktamṛttikā, Sirpur, Peddavegi). The disagreement therefore says more about Xuanzang's Deccan figures,
  most of them hearsay or reconstructed, than about the sites.
- **Juan 4.** Beal's and Cunningham's sets fit better than Mizutani's (mean |z| 1.28 and 0.97 against 1.47).
- **Juan 11.** Mirchandani's set is the best of any authority's (§5).
- **Juan 9 (Magadha).** Every scheme fits badly. The short distances between Magadha's sites do not behave like the
  li elsewhere.
- **Juans 2, 7 and 8.** Mizutani's points are already the best fit.

`chain_best.tsv` lists the 35 places where the best-fitting combination departs from Mizutani. Each of these place
notes has a "Route test (whole juan)" line pointing here. A departure is a question for the notes, not an
identification: the figures are one kind of evidence among several.

## 7. The Life's figures, juan by juan

`life_segments.py` turns the Life's legs, as recorded by the variant readers, into a segment file. It yields 123 legs,
50 of which differ from the Xiyu ji in figure, bearing or starting place. It leaves out legs with no figure, legs
counted in days or yojanas, and minor sites the Life skips. `chains_all.py route/life_segments.tsv` then repeats §6 on
these legs (`chain_scores_all_life.tsv`, `chain_best_life.tsv`).

| Juan | Xiyu ji legs: mean \|z\| (legs, bad) | Life legs: mean \|z\| (legs, bad) | Better set on the Life's legs | Life best fit (places changed) |
|---|---|---|---|---|
| 1 | 1.17 (23, 7) | 1.18 (16, 5) | Watters: 0.94 | 0.94 (5) |
| 2 | 1.08 (10, 1) | 1.97 (7, 3) | — | 1.97 (0) |
| 3 | 1.16 (15, 4) | 2.18 (9, 4) | — | 2.19 (2) |
| 4 | 1.47 (17, 6) | 0.94 (13, 3) | Beal: 0.73 | 0.62 (5) |
| 5 | 1.1 (4, 1) | 1.1 (4, 1) | — | 0.64 (2) |
| 6 | 0.73 (2, 0) | 1.04 (2, 0) | — | 0.24 (2) |
| 7 | 0.68 (3, 1) | 0.53 (2, 0) | — | 0.53 (0) |
| 8 | 0.68 (2, 0) | 1.77 (1, 1) | — | 1.77 (0) |
| 9 | 2.42 (5, 2) | — | — | — |
| 10 | 0.84 (16, 4) | 0.89 (13, 3) | Cunningham: 0.51 | 0.36 (8) |
| 11 | 0.57 (18, 2) | 0.65 (16, 3) | Mirchandani: 0.74 | 0.55 (3) |
| 12 | 0.69 (19, 2) | 0.61 (18, 1) | — | 0.5 (2) |

Results:
- **Where the Life's figures fit worse:** juans 2, 3 and 8. In the Northwest and Magadha the Xiyu ji's own figures
  are the better guide.
- **Where they fit better:** juans 4 and 7, and slightly juan 12.
- **Juan 6.** The Life's 800 li from Śrāvastī to Kapilavastu and 500 li on to Rāma pull Kapilavastu north-west, to
  Cunningham's Nagar.
- **Juan 10.** On the Life's legs Cunningham's Deccan again fits better than Mizutani's (0.51 against 0.89). Two
  independent sets of figures agree on this, so the conflict with the inscriptions (§6) is not an accident of one
  text.
- **Juan 11.** On the Life's legs the best fit takes Lambrick's Las Bela for Laṅgala and Cunningham's Kotesar for
  Atyanabakela, as in §5.

## 8. Does the li vary by region? And do the study's own proposals fit?

`li_regions.py` summarises the straight-line km per li on all legs of 100 li or more between located places
(`li_regions.tsv`):

| Group | km per li (median) | n |
|---|---|---|
| Central Asia and Afghanistan (juans 1, 2, 12) | 0.29–0.30 | 42 |
| North India (juans 4, 7, 10, 11) | 0.21–0.25 | 52 |
| Gandhāra–Kashmir and the Doab (juans 3, 5) | 0.15–0.16 | 14 |
| Hearsay destinations | 0.12 | 8 |
| Legs of 1000 li or more | 0.20 | 27 |
| Legs of 500–999 li | 0.29 | 45 |

The li is longer on the ground in Central Asia and shorter in the Punjab hills and the Doab. Hearsay distances and
very long legs are inflated.

`li_schemes.tsv` fits a separate scale to each scheme in each juan. If a scheme's sites were right and only the
figures were scaled, the scheme would show an unusual scale with little scatter. That is not what happens:
- **The Deccan (juan 10).** The scale that best fits Mizutani's sites, 0.227 km per li, is the ordinary one. The
  scatter around it stays large.
- **Where the scatter comes from.** It sits in the legs south of the Mahānadī, where the stated li run two to four
  times too long:
  - Uḍra → Koṅgoda;
  - Koṅgoda → Kaliṅga, 1400 li for 188 km;
  - Andhra → Dhānakaṭaka, 1000 li for 85 km between Peddavegi and Dharanikota, both fixed by inscriptions;
  - Coḷa → Drāviḍa, 1500 li for 206 km;
  - Drāviḍa → Malakūṭa, 3000 li for 366 km.

  The Bengal legs north of the Mahānadī fit well.
- **Conclusion.** The Deccan figures are inflated, unevenly, perhaps because they count roundabout forest routes
  (the text's 山林) or derive from days' marches. A uniform regional li does not correct them. Cunningham's sites fit
  the figures better because they were chosen to fit them. The inscription-fixed sites should not be moved on route
  grounds.

**The study's own proposals** (`data/coords_study.tsv`), scored as a scheme (§6 tables, `chain_scores_all*.tsv`):
- **Better than Mizutani** in juan 6 (Piprahwa for Kapilavastu; mean |z| 0.53 against 0.73) and juan 5 (Newal).
- **Worse** in juan 10 (Koṅgoda at the Chilka, Arang and Cuddapah lengthen the misfits, though bearings improve) and
  juan 11. There, Mālava in central Gujarat lies only 121 km from Bharukaccha for a stated 2000 li.
- **What this means.** The revisions rest on inscriptions, and the figures do not support them. In the Deccan this is
  expected, given the inflation above. For Mālava it is a real point against central Gujarat, and the 11.05 note
  should weigh it.

## 9. The Sixi edition (1132) against the Taishō apparatus

**The scan.** The Southern Song Sixi (思溪) edition is the Taishō apparatus's 【宋】. A scan of the National Diet
Library copy is in the Internet Archive item `datangxiyuji`. It has 391 pages and only juans 1–8 survive. The pages
were OCR'd with Google Vision (`data/ref/sixi/`, gitignored).

**The method.**
- `apparatus_variants.py` lists the 2,948 apparatus notes of T2087. 145 of them touch a direction or a numeral, and 49
  of those give a Song reading.
- `sixi_check.py` locates each such note in the scan by fuzzy-matching eight characters either side of it. It does the
  same for every route sentence with a distance.

**The results.**
- **The apparatus is reliable for the Song text.** Every recorded Song reading the scan reaches agrees with it: 27 by
  matching and 2 by hand (西行三百餘里 at 01.15; 西北行減二百里 at 05.01). The others fall in the lost juans 9–12 or
  where the OCR failed.
- **No unrecorded variants.** The 86 route sentences matched in juans 1–8 show no direction or numeral that differs
  from CBETA except where the apparatus already records it.
- **Vīrasana (04.14).** The Korean text (Taishō) has 東行二百六七十里，渡殑伽河，南至. The Song print has
  南行…渡殑伽河，西南至, and so does the Life. Bilsar lies due south of Ahicchatra (180°), so the Song and Life
  reading fits. The route model already uses it, because its route text follows the Song wording.
- **Kanyākubja (05.01).** The Song print and the Life read 西北 (north-west), the Korean 東南 (south-east). Kanauj lies
  east-south-east of Sankisa (116°), so here the Korean reading is right. The Song and the Life share an error.
- **Sāṃkāśya (04.15.02).** The Song print has the stairs' monastery 城東, as the apparatus says.

**The Jōō print (1653), juans 7–12.** The same Internet Archive item has the Jōō 2 (承應二年) woodblock print. Its
three volumes for juans 7–12 were OCR'd (`data/ref/joo/`) and checked the same way: `sixi_check.py "data/ref/joo/ocr0*/p-*.txt" joo`
writes `joo_apparatus.tsv` and `joo_route.tsv`.
- **Not a Taishō witness.** It agrees with 【甲】 at only 6 of the 29 notes where 【甲】 has its own reading, so it is
  none of the apparatus's Japanese witnesses. Mostly it shares the Korean reading, or the Song–Yuan–Ming group's
  where those differ.
- **Support for Song-group readings in the lost juans 9–12.** Where the Song print is lost, the Jōō print supports
  several Song-group readings. At 12.09 Kishm (訖栗瑟摩) it reads 東西千餘里, against the Korean 十餘里, which is
  implausible for a country. At 12.10 Parghar it reads 東北至, against the Korean 北至.


## 10. Was the li a measure of time?

**The question.** If Xuanzang's li were days' marches converted at a fixed rate, rather than measured distance, a li
should cover less ground where travel is slow.

**The text's own definition.** Juan 2 defines the Indian unit of distance as a day's march:

> 踰繕那者。自古聖王一日軍行也。舊傳一踰繕那四十里矣。印度國俗乃三十里。聖教所載唯十六里。

"A yojana is, since the sage kings of old, one day's march of an army. The old tradition makes a yojana 40 li; Indian
custom, 30 li; the scriptures only 16 li." So the distances given to him in India would have come as day stages, with
three rival rates of conversion. The ratio between India's li on the ground and Central Asia's (0.231 / 0.288 = 0.80,
§1) is close to what converting at the "old" 40 li, where Indian custom counted 30, would produce (0.75). This is
suggestive only, since the Central Asian li is not a true Tang li either.

**Test 1: relief.** `li_terrain.py` takes the 92 legs of 100 li or more between located places (§8's legs, hearsay
legs left out, both ends at town, site or district precision). For each it measures the relief along the straight line
from SRTM 90 m elevations (api.opentopodata.org, 40 points per leg, cached in `elev_cache.json`), and tags the
terrain from the leg's own route sentence (山 嶺 谷 磧 沙 雪 林 險 棧 崖 峻 踰 越 渉 = rough). Results
(`li_terrain.tsv`; Spearman correlation, permutation p):

| Legs | n | ρ (relief, km per li) | Flattest third | Most rugged third |
|---|---|---|---|---|
| India | 57 | −0.43 (p ≈ 0.001) | 0.239 | 0.169 |
| Central Asia and Afghanistan (juans 1, 2, 12) | 35 | −0.26 (p ≈ 0.13) | 0.277 | 0.223 |

In India the legs the text itself calls rough give 0.169 km per li against 0.233 for the rest. A li covers about 30%
less ground on rough legs. With straight-line distances this cannot separate travel time from winding roads, so
Test 3 measures the legs along modelled walking routes.

**Test 2: flat legs, where winding roads are no explanation.**
- **For time:**
  - Two of the three most inflated flat legs run through forest. Prayāga → Kauśāmbī (05.05), 入大林中…行五百餘里,
    covers about 48 km, or 0.095 km per li. The Life gives the same leg as 大林野中，行七日: 500 li for seven days, about
    70 li and 7 km a day. Into Koṅgoda (10.10), 大林中。行千二百餘里, covers about 110 km (0.091).
  - The Deccan legs found inflated two to four times in §8 are the 山林 legs.
  - In Central Asia the desert legs (磧, 沙) come out long, 0.32–0.43 km per li, as fast caravan going on flat ground
    would.
- **Against time:**
  - The high Pamir legs (12.15–12.18), surely the slowest of the journey, give an ordinary 0.29–0.36.
  - Some forest legs are normal: 11.03 大林野 gives 0.24 and 06.03 荒林 gives 0.41.
  - Some flat legs without forest are very short (Prayāga 0.116, Kapitha 0.131). These may be wrong identifications.
- **The figures themselves:** 151 of the 164 figures of 100 li or more are round hundreds, which hides any pattern of
  multiples of a 30- or 40-li stage.

**Test 3: least-cost walking routes.** `li_paths.py` routes each of the 92 legs over the Copernicus GLO-90 DEM
(`dem_fetch.py`: 463 tiles from AWS open data, kept as the 1/4 overview, about 370 m cells, in `data/ref/dem/`,
gitignored). Cost is walking time by Tobler's hiking function (6 exp(−3.5 |slope + 0.05|) km/h, 5 km/h on the flat),
on an 8-neighbour grid; sea is impassable; rivers, forest, snow and halts are not modelled. Each leg gets the route's
length and its walking time (`li_paths.tsv`). If the li measured distance, km per li along the route should be the
steadiest figure and should not depend on relief; if it measured time, hours per li should be steadier.

| Legs | n | Scatter, sd of log: straight km / li | route km / li | walking hours / li | ρ with relief: route km / li | hours / li |
|---|---|---|---|---|---|---|
| All | 92 | 0.577 | 0.565 | 0.533 | −0.19 (p ≈ 0.07) | −0.12 (p ≈ 0.24) |
| India | 57 | 0.525 | 0.513 | 0.482 | −0.39 (p ≈ 0.003) | −0.34 (p ≈ 0.01) |
| Central Asia and Afghanistan | 35 | 0.625 | 0.609 | 0.566 | −0.18 (p ≈ 0.30) | −0.08 (p ≈ 0.67) |

- **Time fits a little better than distance, everywhere.** Walking time reduces the scatter by about 6% against route
  length (bootstrap: in 98–99% of resamples, in each region), and it removes most of the relief effect in Central
  Asia. The overall rate is about 19 li per walking hour (median; 0.26 km of route per li).
- **Winding roads do not explain India's rough legs.** The terrain forces only small detours at this resolution
  (median 1.05 on flat legs, 1.13 on rugged ones), not the 1.5–2 assumed in Test 1, and the relief effect in India
  survives both route length (ρ −0.39) and walking time (ρ −0.34). The grid misses switchbacks under about 370 m, so
  real detours are larger, but not by enough to close a 30% gap.
- **Most of India's relief effect is juan 3.** Without the Gandhāra–Kashmir legs, ρ falls to −0.23 (route) and −0.20
  (time). The juan 3 legs give 0.17 km of route per li, about two-thirds of the norm, by either measure. A regional
  unit, a different informant, or doubtful sites (Mount Ilam and Mahāvana give 0.06) are as likely as slow
  going.

**Reading.** The li is not a fixed ground measure. In India especially, the figures look like day stages (yojanas)
converted at a set rate. That fits the inflated forest legs, the gap between India and Central Asia, and the Life's
seven days for 500 li. Where Xuanzang travelled himself in Central Asia, the figures behave more like distances: the
Pamir legs are not stretched as slow travel would stretch them. Modelled walking routes (Test 3) favour time over
distance only slightly, but consistently. Walking time does not explain the inflated forest legs of the Doab and the
Deccan, nor the juan 3 legs: there something other than terrain (forest, halts, a different source for the figures)
is at work.
