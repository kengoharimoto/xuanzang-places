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
behave like Tang official li on the ground. India's shorter figure fits a conversion from yojanas or from days'
marches at a fixed rate. That reading is an inference and is not tested here.

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
| Mizutani (Alor, Karachi, Lākoriān, Hyderabad, Brahmanabad, Bannu) | 0.62 | 2.69 | 41° | 1 |
| Lambrick 1964 (Banbhore, Sehwan, Badah; Mizutani elsewhere) | 0.66 | 2.32 | 36° | 1 |
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
| 11 | 0.57 (2) | Mirchandani: 0.46 (1) | 0.53 (6) |
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

