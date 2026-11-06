# Xuanzang's places

**Question.** Where are the countries and sites of the *Da Tang Xiyu ji* (大唐西域記)? What have scholars proposed,
what is agreed and what is disputed? Do the Archaeological Survey's field reports and the British Indian district
gazetteers add anything to the standard identifications?

**Answer in brief.** Mizutani Shinjō's annotated translation (1971) identifies most of the 148 countries in the
text with reasonable confidence. He marks 30 of them as disputed and 21 more as uncertain or unknown, and the same
holds for 139 of the 268 sites.

Two kinds of local evidence were then set against him:
- **The Archaeological Survey's reports** (Cunningham and his assistants, 1862–87) and P. C. Mukherji's Tarai report
  (1901). This is where the identifications were argued on the ground and repeatedly revised.
- **The district gazetteers.** Six in ten of their relevant passages only repeat an authority, usually Cunningham.
  The rest add local evidence the standard books lack.

Taken together, the survey and the gazetteers:
- strengthen Mizutani's identification for 53 places, often with an inscription naming the place or an excavation;
- weaken it for 7;
- support a different site for 29;
- offer a candidate no standard authority records for 6.

The changes cluster in Magadha, the Ghazipur–Ballia stretch of the Ganges, Kuśinagara and Kapilavastu, the Salt
Range (Siṃhapura), the upper Doab, and eastern and central India. Neither source reaches juan 1 or 12 (Central Asia
and Afghanistan).

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
- **Archaeological Survey of India, Reports**, vols. I–XXIII (1871–87).
  - **Authors:** Cunningham, with volumes by J. D. Beglar, A. C. L. Carlleyle and H. B. W. Garrick.
  - **Also coded the same way:** P. C. Mukherji, *Report on a Tour of Exploration of the Antiquities in the Tarai,
    Nepal* (1901), with V. A. Smith's prefatory note.
  - **Text:** Internet Archive OCR, kept locally in `data/ref/asr/`; the identifiers are in `list.tsv`. Six volumes
    needed alternative scans because the first copies had only plates or broken text.
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
3. **Survey reports** (`data/asr_hits.tsv`, `data/coded/asr_batch*.tsv`, `data/ASR_INSTRUCTIONS.md`). Mentions of
   Xuanzang or Faxian within 1,500 characters of each other were merged into passages: 495 in all, 362 of them
   relevant.
   - **Each passage is coded for:** the author, the place, the site identified, the stance (proposes, confirms,
     revises, rejects or reports) and the field evidence.
   - **Stances:** 157 propose, 134 confirm, 39 revise, 9 reject and 23 report.
   - **Quotes:** each has a verbatim quote, checked by `scripts/check_quotes_asr.py`.
4. **Gazetteers** (`data/coded/gaz_batch*.tsv`, `data/GAZ_INSTRUCTIONS.md`). Each hit is coded for:
   - whether it is relevant;
   - which place it concerns;
   - the gazetteer's identification;
   - its stance: repeats, argues, doubts, alternative or reports;
   - the authority it cites;
   - any local evidence.

   Each coding has a verbatim quote, checked against the volume's OCR by `scripts/check_quotes_gaz.py`. Of the 1,128
   relevant passages, 674 repeat an authority, 163 argue their own case, 103 propose another site, 71 doubt the
   standard one and 117 only report views.
5. **Notes on disputed places** (`data/notes/notes_*.md`; instructions in `data/NOTES_INSTRUCTIONS.md` and
   `data/NOTES_REVISION_ASR.md`). There are 299 notes. A place gets one when any of these holds:
   - Mizutani marks it disputed, uncertain or unknown;
   - the authorities name materially different sites;
   - the survey or a gazetteer argues, doubts or proposes another site.

   Each note gives:
   - the identifications;
   - what the survey argued and found, and how its view moved from report to report;
   - what the gazetteers add (or says plainly that they add nothing);
   - a short assessment.

   The matching `data/notes/updates_*.tsv` records the proposed identification, the kind of change and a confidence.
6. **Joined table** (`data/places.tsv`, built by `scripts/build_places.py`). One row per place, with Mizutani, the
   seven authorities, the survey's identifications and field evidence, and a summary of the gazetteer evidence.

## What the survey and the gazetteers add

- **The survey's identifications moved, and the books freeze one moment of that movement.** Examples:
  - **Siṃhapura** (03.04): Cunningham placed it at Malot (1863–64), then at Ketas (1871), then at Malot again (vol. V).
    In the Jhelam gazetteer Stein argues for the plain north of Ketas.
  - **Kapilavastu** (06.02): Cunningham's Nagar, then Carlleyle's Bhuila Dih (accepted by Cunningham, vols. XII,
    XVIII), then Mukherji's excavations at Tilaurakot (1901). Smith argued that Piprahwa was Faxian's Kapilavastu.
  - **Vilaśana** (04.14): Atranji-khera, then Bilsar with the Kumāragupta pillars (vol. XI).
  - **Cīnabhukti** (04.02): Patti, then Chine/Chiniyari (vols. XIV, XXI).
  - **Jajhoti** (11.13): Khajuraho, then Chedi (vol. IX), then Bundelkhand again on the Mahoba and Madanpur
    inscriptions naming Jejākabhukti (vol. XXI).

  Gazetteers often preserve a view Cunningham had already dropped, so a district volume citing him is not always
  citing his last word.
- **Inscriptions and seals naming the place.** Examples:
  - The inscription naming Teladaka at Tillara (08.04.01, vol. VIII).
  - Inscriptions found at Nālandā that name it (09.03.01).
  - The colossal Buddha at Sahet-Mahet inscribed "Sravasti" (06.01).
  - "Kausambipura" on the Kosam pillar (05.05).
  - Gupta seals reading "Tathāgatasya Buddhasya" at Dharawat (08.04.03).
  - A monastic seal at Parbati (09.03.13).
  - From the gazetteers: the Kara inscription of 1036 naming the "Kausamba maṇḍala", copper plates naming Koṅgoda,
    the Taleshwar plates "issued from Brahmapura", and Telugu Coḷa inscriptions in Cuddapah.
- **Excavations and measured remains matched to Xuanzang's figures.** Examples:
  - The Nirvāṇa statue Carlleyle excavated at Kasia (06.04).
  - The Māyādevī temple and the split pillar at Rummindei (06.02.11–12).
  - The pillar base by the Bisari Devi mound at Sankisa (04.15.02).
  - The Rājagṛha ramparts (09.02.04).
  - The Bodh Gayā temple (08.06.04).
  - Ramparts at Śrāvastī, Sankisa, Ahicchatra, Asarur, Sugh and Multan, measured against Xuanzang's li.
- **Local names, cults and traditions** (mostly from the gazetteers). Examples:
  - The Nāga tank at Sankisa still receives milk offerings (04.15).
  - The Kesariya mound is still called "Raja Ben ka deora" (07.03.13).
  - The caste name Jijhotia survives in Bundelkhand (11.13).
- **Local route arguments.** Examples:
  - Oldham re-places the Ghazipur–Ballia sites on the ground (07.02).
  - The Hamirpur, Jhansi and Jalaun volumes argue that Eran, not Khajuraho, fits the bearings (11.13).
  - Beglar puts the Guṇamati and Śīlabhadra monasteries at Dharawat and Kauwa-dol, and Cunningham adopts both
    (08.04.03–04).

Neither source covers juan 1 and 12, and the gazetteers have little on Kashmir. The notes say so.

## Testing against the route and the texts

`route/README.md` tests the identifications against Xuanzang's own figures.

- **The li.** On 29 legs between agreed places, a li covers a median 0.239 km in a straight line, or about
  0.29–0.32 km by road. That is close to Hori's 320 m and Cunningham's 1/6 mile, well short of the 440 m Mizutani
  adopts.
- **The texts.** 262 legs were compared across T2087, 釋迦方志 (T2088) and the *Life* (T2053), with Mizutani's
  variant notes. 88 of them differ. A few variants bear on identifications:
  - Tamasavana: the *Life*'s 50 li for 500.
  - Kapilavastu: 500 li, not the *Life*'s 800.
  - The 戰主國 capital: the *Life* counts the distance to Vaiśālī from the capital, which puts it well short of
    Ghazipur.
  - Kiṭa: "three days" in all three texts, not 300 li.
  - Maheśvarapura: every bearing goes against Cunningham's Mandla.
- **Rival sites.** Candidates were scored against their neighbours' positions. This is a useful filter: it counts
  against Mizutani's Siṃhapura pair unless the text is emended. It is not proof. Kosam fails the text's 500 li and
  is still certain from its inscription and excavation.

## Main proposed revisions to Mizutani

Proposals of medium or high confidence where the evidence points away from Mizutani. The full list, including the
53 places where it supports him, is in `data/notes/updates_*.tsv`.

| Id | Place | Mizutani | Proposed | Basis |
|---|---|---|---|---|
| 05.01.09 | Navadevakula | not given | Newal near Bangarmau | ASR XI; Unao 1903 "agreed by most writers" |
| 06.01.14 | Kāśyapa's birthplace | not given | Tandwa, 9 mi W of Sahet-Mahet | stūpa 70 ft across, casing cleared (ASR XI) |
| 06.04.03a | river at Kuśinagara | Gandak = Hiraṇyavatī | Little Gandak / old channel | Cunningham; the local name "Hirana"; fits his own Kasia |
| 06.04.11 | cremation stūpa | "about 10 miles E" | Ramabhar mound E of the old channel | Gorakhpur volumes, Carlleyle; his figure looks like a slip |
| 07.01.03 | first-sermon stūpa | Dharmarājika | pillar probable, stūpa open (weakened) | Benares 1911: brick vs stone, 60 vs 70 ft |
| 07.02 | 戰主國 capital | Ghazipur | Sayyidpur or Ghazipur | Oldham's antiquities at Sayyidpur |
| 08.04.03 | Guṇamati's monastery | not given | Dharawat (Kunwa hill) | Beglar, Cunningham; Gupta seals; Gaya 1906/1957 |
| 08.04.04 | Śīlabhadra's monastery | not given | Kauwa-dol hill | Beglar, adopted by Cunningham; granite pillars |
| 09.01.03 | Kukkuṭapāda | hill N of Kurkihar | Hasra (Sobhnath) or Gurpa | Stein, Banerji; Gaya 1906 calls Stein's case "conclusive" |
| 09.02.03c | Asura's palace | not given | Rajpind cave, Chandu hill | Stein; walled road from Khiri |
| 09.03.13–14 | Kapotaka; Avalokiteśvara hill | Bihār | Parbati (Daryapur Parvati) | Cunningham's final view (ASR XV): monastic seal, terraced hill |
| 09.03.15b | 落般膩羅 | unsettled | Rajaona (Rajjana) | ASR XV; Monghyr: lake, 4 miles of mounds |
| 10.02.02a | islet east of Campā | not given | rock islets at Kahalgaon | brick temple on the summit (ASR XV); Bhagalpur 1911 |
| 10.15 | Coḷa | Nellore / Penner | Telugu Coḷa country (Renāṇḍu), Cuddapah | inscriptions (Cuddapah 1915) |

Strengthened for an undecided Mizutani: Jajhoti is Bundelkhand, on the inscriptions naming Jejākabhukti, with the
capital at Khajuraho or Eran (11.13).

Left open by the new evidence:
- **Siṃhapura's capital and its stūpas** (03.04.01a–03): three candidates. Mizutani's Kotera, Stein's plain north of
  Ketas, and Cunningham's later Malot.
- **The Manikyala body-offering site** (03.04.05). Court's inscription is read as naming the body-offering, against
  Mizutani's Banj.
- **Karṇasuvarṇa** (10.08). Rangamati is doubted by Murshidabad 1914, and Beglar's Dulmi/Sapharan rests on little.
  Later excavation, outside these sources, has favoured Rangamati.

## Limits

- **Mizutani is the 1971 state of the question.** Later work (季羨林 1985; site reports since) is not in these
  sources, and neither are the ASR *Annual Reports* (1902–38) or *Indian Archaeology – A Review*. Where a
  note-writer knew of later results, the note flags it in one clause as outside the sources.
- **OCR.** Quotes match the OCR verbatim, errors included. Middle Chinese readings in Mizutani's notes are often
  garbled and are marked "(OCR)". T2087 gaiji appear as `mNNNNN` codes in `t_route`.
- **Survey coverage.** The ASR index caught passages that name Xuanzang or Faxian. A few arguments that never name
  them were missed. One example is ASR V pp. 67–68 on the Taxila copper plate. The known gaps are listed in
  `data/FOLLOWUPS.md`.
- **Gazetteer counts include duplicate scans and editions.** Notes count volumes, not hits.
- **Coordinates** (`data/coords.tsv`) place Mizutani's identification for orientation only. Precision is
  site / town / district / country, and the basis is Mizutani's figures, a known location, or an estimate. 77 places
  are unmapped.
- **Coding corrections** made after the notes passes, and open questions in the sources, are listed in
  `data/FOLLOWUPS.md`. Among them: a CP volume in the gazetteer-vedanta selection (`in.ernet.dli.2015.281327`) is
  really Beal's *Records*, not the Chhindwara gazetteer.

## Files

- `data/places.tsv`: the joined table (start here).
- `data/places_mizutani.tsv`: the master table.
- `data/coded/`: per-juan (Mizutani), per-authority, per-batch survey (`asr_batch*`) and gazetteer (`gaz_batch*`)
  coding.
- `data/notes/`: notes and proposed updates.
- `data/asr_hits.tsv`: survey passage index.
- `data/gaz_hits.tsv`: gazetteer hit index.
- `data/coords.tsv`: coordinates.
- `map/xuanzang_places.html`: map and place dossier (published privately at
  https://claude.ai/artifact/WUH4GFEULK5rZ8oaXw8PpH), built by `map/build_page.py` from `map/template.html`.
- `route/`: route model, li calibration, candidate scores, text variants (`route/README.md`).
- `scripts/`: OCR join, quote checkers, hit indexes, merge and join.
- `data/*_INSTRUCTIONS.md`, `data/NOTES_REVISION_ASR.md`: the coding instructions.
- `PLAN.md`: the original plan.

Rebuild:

```
python3 -I scripts/merge_mizutani.py && python3 -I scripts/build_places.py && python3 -I map/build_geo.py && python3 -I map/build_page.py
```
