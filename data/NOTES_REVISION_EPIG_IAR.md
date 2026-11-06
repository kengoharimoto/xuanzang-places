# Revising the notes with the inscriptions (EI, CII) and the post-1953 excavations (IAR)

The notes (`data/notes/notes_<range>.md`, `updates_<range>.tsv`) already include the Cunningham-series survey (**Survey.**)
and the Annual Reports 1903–37 (**Excavations.**). Two more sources are now coded, with columns in `data/places.tsv`:
- `epig`, `epig_n`, `epig_evidence`; detail in `data/coded/epig_batch*.tsv` (Epigraphia Indica vols 1–36 `ei_NN`, CII
  vols 1, 2.1, 2.2, 3, 5, 6 `cii_N`): inscriptions naming a Xiyu ji place, and editors' identifications.
- `iar`, `iar_n`, `iar_evidence`; detail in `data/coded/iar_batch*.tsv` (Indian Archaeology – A Review 1953–54 to
  2000–01, `iarYYYY-YY`): excavations after independence (Kosam/Ghoṣitārāma, Vaiśālī relic stūpa, Rajbadidanga
  sealings naming Raktamṛttikā, Piprahwa sealings naming Kapilavastu, Peddavegi/Veṅgī, Thanesar, Sanghol, Sirpur,
  Banavasi, Sugh "Sugha" sealing, Sahet-Mahet, Kesariya, Kolhua…).

For every place in your range with `epig_n` or `iar_n` > 0:
1. **Existing note**: rewrite it in place as one current account. Add **Inscriptions.** (after Excavations) and/or
   **Later excavations.** (1953–2001) paragraphs: what was found, by whom and when (e.g. "Srivastava, IAR 1972–73,
   p. 33"), the decisive phrase quoted briefly, and whether it confirms, moves or overturns the identification. An
   inscription or sealing that names the place on the site normally settles it (`confidence` high) — but say what it
   names (a monastery's community in the Kushan period is not the 7th-century city). Where the new evidence conflicts
   with the current `proposed` (e.g. Piprahwa sealings vs Tilaurakot), set out both cases and give the verdict the
   evidence supports, with `change` and `confidence` to match.
2. **No note yet**: write one if the new sources give a site where the table has none, move an identification, or
   settle a disputed one. Otherwise skip.
3. Keep `updates_<range>.tsv` in step. Add `new` places from these codings to the final section.

Keep notes to 80–350 words. Report: notes revised / added; every place whose `change` or `confidence` moved
(old → new, one line each); coding errors noticed in `epig_batch*.tsv` / `iar_batch*.tsv` (don't fix them).
