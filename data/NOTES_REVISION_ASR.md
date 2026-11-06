# Revising the notes with the Archaeological Survey reports

The notes (`data/notes/notes_<range>.md`) and updates (`data/notes/updates_<range>.tsv`) were written before the ASR
reports were coded. Now `data/places.tsv` has columns `asr`, `asr_n`, `asr_evidence`, and the detail is in
`data/coded/asr_batch*.tsv` (columns: passage, file, author, relevant, xz_id, name_in_asr, asr_identification,
stance [proposes/confirms/revises/rejects/reports], evidence, page, quote, note). Volume = file (`asr01.txt` = vol. I,
1862–63 … `asr23.txt` = vol. XXIII; `mukherji1901_tarai.txt` = Mukherji's Tarai report with V. A. Smith's prefatory note).

For every place in your range with ASR passages:
1. **Existing note**: rewrite it in place as one current account (no "update" or "added" sections). Add a
   **Survey.** paragraph after **Identifications** (before **Gazetteers**): what the survey argued and found on the
   ground, by author and volume with page, with the decisive phrase quoted briefly; and **how the survey's view moved**
   (e.g. Cunningham's Siṃhapura: Malot 1863–64 → Ketas 1871 → Malot again in vol. V; Carlleyle's Kapilavastu at Bhuila
   Dih, accepted by Cunningham, later overturned by Führer/Mukherji). Gazetteer passages that only echo the ASR should
   now be described as echoing it. Revise the **Assessment** and the one-line verdict if the field evidence changes
   the picture.
2. **No note yet**: write one, in master-table order, if the survey gives a site where Mizutani has none, or a
   different site, or field evidence bearing on a disputed identification. Otherwise skip it.
3. Update `updates_<range>.tsv` to match (same columns: `id, name_zh, mizutani, proposed, change, basis,
   confidence`; add rows for new notes). Confidence may now rise (an inscription naming the place; excavation) or fall
   (the survey itself abandoned the identification).
4. Add a closing bullet list to the notes file's existing final section on places missing from the master table,
   for ASR rows coded `new` in your range (name, site, author/vol.).

Keep notes to 80–300 words. Report: notes revised, notes added, and every place whose `change` or `confidence` moved
(old → new, one line each); any coding error you notice in `asr_batch*.tsv` (don't fix it).
