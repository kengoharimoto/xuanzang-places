# Revising the notes with the ASR Annual Reports (1903–37) and Circle reports

The notes (`data/notes/notes_<range>.md`, `updates_<range>.tsv`) already include the Cunningham-series survey. Now
`data/places.tsv` has `ar`, `ar_n`, `ar_evidence`, with detail in `data/coded/ar_batch*.tsv` (same columns as the ASR
coding: passage, file, author, relevant, xz_id, name_in_asr, asr_identification, stance, evidence, page, quote, note).
Files: `arYYYY-YY.txt` = Director-General's Annual Report for that year; `ecYYYY-YY.txt` = Bengal/Eastern Circle report.

These are excavation reports, and they often **settle** what the earlier sources only argued: inscriptions and
sealings naming a place (the Haribala copper plate in the Kasia Nirvāṇa stūpa; the Govindachandra plate and the
inscribed Bodhisattva for the Jetavana at Śrāvastī; Kanishka's casket at Shah-ji-ki-Dheri; Nālandā sealings; the
Mahasthan inscription naming Pudanagara; the Kara inscription for Kauśāmbī; the Tachhasilae ladle at Taxila),
excavated plans matched to Xuanzang's description, and explicit rejections of Cunningham's sub-site identifications
(Babar-khana, Kurmal, Kachchi Kuti, Katra, Son Bhandar…).

For every place in your range with Annual Report passages:
1. **Existing note**: rewrite it in place as one current account. Add an **Excavations.** paragraph after
   **Survey.**: what was dug or found, by excavator and report year (e.g. "Vogel, AR 1907–08, p. 117"), the decisive
   phrase quoted briefly, and whether it confirms, moves or overturns the earlier identifications. Note when a find
   reversed an earlier doubt (e.g. Kasia: doubted 1905–07 on the sealings, settled 1910–11 by the copper plate).
   Revise the verdict line, **Assessment**, `proposed`, `change` and `confidence` accordingly — an inscription naming
   the place on the site normally makes confidence `high`.
2. **No note yet**: write one if the reports give a site where Mizutani has none, move or overturn an identification,
   or supply decisive evidence for a disputed one. Otherwise skip.
3. Keep `updates_<range>.tsv` in step (same columns). Add `new` places from the AR coding to the final section.

Keep notes to 80–320 words. Report: notes revised / added; every place whose `change` or `confidence` moved
(old → new, one line each); coding errors noticed in `ar_batch*.tsv` (don't fix them).
