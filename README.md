# Xuanzang's places

**Question.** Where are the countries and sites of the *Da Tang Xiyu ji* (大唐西域記)? What have scholars proposed,
what is agreed and what is disputed, and do the British Indian district gazetteers add anything to the standard
identifications?

**Answer in brief.** Mizutani Shinjō's annotated translation (1971) identifies most of the 148 countries in the
text with reasonable confidence. He marks 30 of them as disputed and 21 more as uncertain or unknown, and the same
holds for 139 of the 268 sites. The gazetteers do not touch Central Asia or Afghanistan. For India they are useful
in a narrower way than expected. Six in ten of their relevant passages only repeat an authority, usually
Cunningham. The rest carry local
evidence that the standard authorities lack: excavation reports, inscriptions naming a place, measured mounds,
place-names and living cults, and old river courses. That evidence:

- strengthens Mizutani's identification for 39 places;
- weakens it for 4;
- supports a different site for 28;
- offers a candidate no standard authority records for 8.

The changes cluster in Magadha, the Ghazipur–Ballia stretch of the Ganges, Kuśinagara, the Siṃhapura (Ketas) area,
and eastern and central India. In each of these an officer or surveyor wrote up local work in the district volume.

All assessments are provisional. Each rests on the coded quotes listed below; the user's reading of the notes is the
check.

## Sources

- **Text.** Taishō 2087 (`data/ref/t2087_joined.txt`, one sentence per line). Huili's *Life* was not used
  systematically. Mizutani cites it where the routes differ.
- **Mizutani**, 『大唐西域記』 (平凡社 中国古典文学大系 22, 1971). A 488-page scan with no text layer, OCR'd with
  Google Vision. The scan and OCR are kept locally under `data/mizutani/` and are gitignored because the book is in
  copyright. His notes are the backbone of the table: readings, Sanskrit names, identifications with references,
  and his remarks on whether Xuanzang visited a country (親践) or reports it from hearsay (伝聞).
- **Authorities.** Each was coded separately, with a verbatim quote per identification:
  - Julien (1857–58) and Vivien de Saint-Martin's *Mémoire analytique* (1858);
  - Cunningham, *Ancient Geography of India* (1871), in Majumdar Sastri's edition of 1924, whose notes are coded
    separately as `majumdar`;
  - Beal, *Si-yu-ki* (1884);
  - Watters, *On Yuan Chwang's Travels* (1904–05);
  - N. L. Dey, *Geographical Dictionary* (1927).
- **Gazetteers.** These are the 557 distinct volumes already downloaded for the gazetteer-vedanta and yoga-gazetteers
  studies. Every mention of Xuanzang in any of his old spellings (Hiuen Tsiang, Hwen Thsang, Yuan Chwang…), of "the
  Chinese pilgrim", and of Faxian was indexed. That gives 1,965 hits in 302 volumes; 1,128 of them bear on where a
  place is. Many volumes exist in two scans, so the counts include duplicates.

## Method

1. **Master table** (`data/places_mizutani.tsv`, 419 rows: 148 countries, 3 regions, 268 sites). It was coded from
   Mizutani's notes, juan by juan, following `data/CODING_INSTRUCTIONS.md`. Each row carries Mizutani's
   identification, the other views he reports, his status (agreed, disputed, uncertain or unknown), the route
   sentence from T2087, and a verbatim quote with its pdf page. The quotes are checked against the OCR by
   `scripts/check_quotes.py`.
   - **Visited or hearsay.** Mizutani applies the colophon's rule (行 = visited, 至 = hearsay) and corrects it from
     the *Life*. On this basis 108 countries are visited, 35 hearsay and 5 unclear. The 讃 itself gives 110 and 28.
2. **Authorities** (`data/coded/auth_*.tsv`, `data/AUTHORITY_INSTRUCTIONS.md`). For each place, each authority's
   identification is coded with its stance (firm, tentative, rejects, none given), the other views it reports, and a
   verbatim quote, checked by `scripts/check_quotes_ref.py`.
3. **Gazetteers** (`data/coded/gaz_batch*.tsv`, `data/GAZ_INSTRUCTIONS.md`). Each hit is coded for:
   - whether it is relevant;
   - which place it concerns;
   - the gazetteer's identification;
   - its stance: repeats, argues, doubts, alternative or reports;
   - the authority it cites;
   - any local evidence.

   Each coding has a verbatim quote, checked against the volume's OCR by `scripts/check_quotes_gaz.py`. Of the 1,128
   relevant passages, 674 repeat an authority, 163 argue their own case, 103 propose another site, 71 doubt the
   standard one and 117 only report views.
4. **Notes on disputed places** (`data/notes/notes_*.md`, `data/NOTES_INSTRUCTIONS.md`). There are 295 notes. A place
   gets one when any of these holds:
   - Mizutani marks it disputed, uncertain or unknown;
   - the authorities name materially different sites;
   - a gazetteer argues, doubts or proposes an alternative.

   Each note gives the identifications, then what the gazetteers add (or says plainly that they add nothing), then a
   short assessment. The matching `data/notes/updates_*.tsv` records the proposed identification, the kind of change
   and a confidence.
5. **Joined table** (`data/places.tsv`, built by `scripts/build_places.py`). One row per place, with Mizutani, the
   seven authorities and a summary of the gazetteer evidence.

## What the gazetteers add

The useful passages are of five kinds.

- **Excavation and survey reports** reprinted in the district volume. Examples:
  - Bloch and Vogel at Kasia support Kuśinagara (06.04), and the Gorakhpur volume answers V. A. Smith's Nepal site
    point by point.
  - Bloch at Basarh supports Vaiśālī (07.03).
  - The 1907 temple found at Mahasthan supports Puṇḍravardhana (10.04).
  - The Saugar University excavations at Sirpur support Kosala (10.12).
  - Stein's field letters on Ketas and Murti, printed in full in the Jhelam volume, move Siṃhapura's capital to the
    plain north of Ketas and its Jain stūpa to Murti (03.04.01a, 03.04.03).
- **Inscriptions and copper plates naming the place.** Examples:
  - The Kara inscription of 1036 names the "Kausamba maṇḍala" (Kauśāmbī, 05.05).
  - The Sravasti statue inscription, reported in Gonda (06.01).
  - Copper plates naming Koṅgoda, found in Khurda and Ganjam (10.10).
  - Telugu Coḷa inscriptions in Cuddapah (10.15).
  - The Taleshwar plates "issued from Brahmapura" (04.11).
- **Measured remains matched to Xuanzang's figures.** Examples:
  - Thanesar's three mounds measure about 3 miles round, against his 20 li (04.08).
  - The Bodh Gayā railing pillars stand 9 ft 10 in, against his 10-ft wall (08.06.01).
  - The Kanauj cliff above the Kālī Nadī fits Mizutani's reading of the "Ganges" (05.01).
- **Local names, cults and traditions.** Examples:
  - The Nāga tank at Sankisa still receives milk offerings, as in Faxian (04.15).
  - The Kesariya mound is still called "Raja Ben ka deora", after a wheel-turning king (07.03.13).
  - The caste name Jijhotia survives in Bundelkhand (11.13).
- **Local route arguments.** Examples:
  - Oldham re-places the Ghazipur–Ballia sites on the ground (07.02, 07.02.02).
  - The Hamirpur, Jhansi and Jalaun volumes argue from bearings that Jajhoti's capital was Eran, not Khajuraho
    (11.13).
  - The Gaya volumes place Guṇamati's and Śīlabhadra's monasteries at Dharawat and Kauwadol, where Mizutani gives
    no site (08.04.03–04).

Where the gazetteers add nothing, the notes say so. This covers all of juan 1 and 12, which have no gazetteers;
most of Kashmir; and many places where the district volume only quotes Cunningham. The gazetteers sometimes
preserve Cunningham's earlier views after he abandoned them (Atranji-khera for Vilaśana, Sanglawala Tibba for
Śākala), so a gazetteer citing Cunningham is not always citing his last word.

## Main proposed revisions to Mizutani

Medium or high confidence only. The full list, with the basis for each, is in `data/notes/updates_*.tsv`.

| Id | Place | Mizutani | Proposed | Basis |
|---|---|---|---|---|
| 03.04.01a | Siṃhapura capital | Kotera fort (Cunningham) | ruins 1–2 mi N of Ketas | Stein in Jhelam 1907; keeps the text's 40–50 li |
| 03.04.03 | stūpa SE of Siṃhapura | Ketas tanks | Murti mound | Stein's excavation, Jaina sculpture, chained distance |
| 05.01.09 | Navadevakula | not given | Nawal near Bangarmau | Unao 1903 "agreed by most writers"; Oudh 1877 |
| 06.01.14 | Kāśyapa's birthplace | not given | Tandwa, 9 mi W of Sahet-Mahet | mound and stūpa (Bahraich, Oudh) |
| 06.04.03a | river at Kuśinagara | Gandak = Hiraṇyavatī | Little Gandak / old channel | Cunningham; a local name "Hirana"; fits his own Kasia |
| 06.04.11 | cremation stūpa | "about 10 miles E" | Ramabhar mound NE of Anrudhwa | Gorakhpur volumes; his figure looks like a slip |
| 07.01.03 | first-sermon stūpa | Dharmarājika | pillar probable, stūpa open (weakened) | Benares 1911: brick vs stone, 60 vs 70 ft |
| 07.02 | 戰主國 capital | Ghazipur | Sayyidpur or Ghazipur | Oldham's antiquities at Sayyidpur |
| 08.04.03 | Guṇamati's monastery | not given | Dharawat (Kunwa hill) | Gaya 1906/1957; Cunningham's excavation |
| 08.04.04 | Śīlabhadra's monastery | not given | Kauwadol hill | Gaya; distance and the stūpa-shaped peak |
| 09.01.03 | Kukkuṭapāda | hill N of Kurkihar | Hasra (Sobhnath) or Gurpa | Stein, Banerji; Gaya 1906 calls Stein's case "conclusive" |
| 09.02.03c | Asura's palace | not given | Rajpind cave, Chandu hill | Stein; walled road from Khiri |
| 09.03.13–14 | Kapotaka; Avalokiteśvara hill | Bihār | Bihār or Dariyapur Parbati | the "pigeon" name, terraced hill; both need an emended distance |
| 09.03.15b | 落般膩羅 | unsettled | Rajaona | Monghyr: lake, 4 miles of mounds |
| 10.02.02a | islet east of Campā | not given | rock islet at Colgong | Bhagalpur 1911 and the authorities |
| 10.15 | Coḷa | Nellore / Penner | Telugu Coḷa country (Renāṇḍu), Cuddapah | inscriptions |
| 11.13 | Jajhoti | undecided (Khajuraho or Chitor) | Bundelkhand, capital probably Eran | bearings; the Jijhotia caste name |

Places where the gazetteers *weaken* Mizutani without a better site:
- Karṇasuvarṇa at Rangamati (10.08, 10.08.02): Murshidabad 1914. Later excavation, not in these sources, has since
  favoured Rangamati.
- Govisana at Kashipur (04.12): no confirmation; Atkinson's Dhikuli is the rival.
- The Sarnath first-sermon stūpa (07.01.03).

## Limits

- **Mizutani is the 1971 state of the question.** Later work (季羨林 1985; site reports since) is not in these
  sources. Where a note-writer knew of later results, the note flags it in one clause as outside the sources.
- **OCR.** Quotes match the OCR verbatim, errors included. Middle Chinese readings in Mizutani's notes are often
  garbled and are marked "(OCR)". T2087 gaiji appear as `mNNNNN` codes in `t_route`.
- **Gazetteer counts include duplicate scans and editions.** Notes count volumes, not hits.
- **Cunningham's ASR reports are not coded.** Several gazetteer passages quote them, for example Karmal for the
  Kunāla stūpa and Teliagarhi.
- **Coordinates** (`data/coords.tsv`) place Mizutani's identification for orientation only. Precision is
  site / town / district / country, and the basis is Mizutani's figures, a known location, or an estimate. 77 places
  are unmapped.
- **Coding corrections** made after the notes pass, and open questions in the sources, are listed in
  `data/FOLLOWUPS.md`. Among them: a CP volume in the gazetteer-vedanta selection (`in.ernet.dli.2015.281327`) is
  really Beal's *Records*, not the Chhindwara gazetteer.

## Files

- `data/places.tsv`: the joined table (start here).
- `data/places_mizutani.tsv`: the master table.
- `data/coded/`: the per-juan, per-authority and per-batch coding.
- `data/notes/`: notes and proposed updates.
- `data/gaz_hits.tsv`: the gazetteer hit index.
- `data/coords.tsv`: coordinates.
- `map/xuanzang_places.html`: map and place dossier (published privately at https://claude.ai/artifact/WUH4GFEULK5rZ8oaXw8PpH), built by `map/build_page.py` from `map/template.html`.
- `scripts/`: OCR join, quote checkers, hit index, merge and join.
- `data/*_INSTRUCTIONS.md`: the coding instructions.
- `PLAN.md`: the original plan.

Rebuild:

```
python3 -I scripts/merge_mizutani.py && python3 -I scripts/build_places.py && python3 -I map/build_geo.py && python3 -I map/build_page.py
```
