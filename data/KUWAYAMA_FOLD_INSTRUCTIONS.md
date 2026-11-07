# Folding Kuwayama (1990 thesis, 2002 English collection) and the secure-form name tests into the notes

## Sources

- Kuwayama Shōshin, 『カーピシー＝ガンダーラ史研究』 (thesis 1986, Kyoto repository 1990): read from the page images;
  summaries with manuscript pages and verbatim Japanese in `data/ref/kyoto/k1990/summary_ch3-4.md`, `summary_ch6a.md`,
  `summary_ch1-6b.md`. Cite as "Kuwayama 1990, p. N" (manuscript page).
- Kuwayama, *Across the Hindukush of the First Millennium* (Kyoto 2002), clean text
  `data/ref/kyoto/kuwayama2002_across_hindukush_Kuwayama_S.txt` (cite "Kuwayama 2002, p. N", printed page). Chapters:
  I Taxila/Gandhāra chronology; III the Buddha's bowl; V Shāh-jī-kī Ḍherī before Kaniṣka; VI Hadda (Tapa Shotor,
  Lalma); VII Hephthalites in Tokharistan and Gandhāra (incl. "Towns in Tokharistan"); VIII–IX Bāmiyān; X–XI Begram III;
  XII Khair Khana, Zhun, Aruṇa; XIII Napki coins; XIV–XV Turki Śāhis; XVI Yaśovarman/Huichao.
- The name tests: `data/names/test_sec_a.tsv`, `test_sec_b.tsv`, `test_sec_c.tsv` (verdicts better / alternative /
  doubtful), method in `data/NAMES_INSTRUCTIONS.md`; earlier Name paragraphs in the notes show the style
  (grep -n '^\*\*Name\.\*\*' data/notes/*.md).

## What to do, for the notes in your files only

1. **Kuwayama.** For each place he treats, add `**Kuwayama (1990, 2002).** …` before **Assessment.** (or extend an existing
   Kuwayama paragraph; the notes already cite Kuwayama 2000 and, for 活, 2002/2020): his identification, his evidence
   (texts with their Chinese wording, sites, excavations), page references, 1–4 sentences. Where he agrees and adds
   nothing, one sentence. Wrap at 118 characters.
2. **Name.** For each id in your files with a non-keep row in test_sec_*.tsv, add or extend a `**Name.**` paragraph as
   in the earlier passes, ending "(data/names/)".
3. **Assessment and updates rows** (`data/notes/updates_*.tsv`: id name_zh mizutani proposed change basis confidence;
   change ∈ none/strengthened/weakened/alternative/new-candidate): revise only where the evidence changes the picture.
   Confidence rule: high only with site evidence (excavation, inscription naming the place, matching monument); medium =
   agreement among authorities; low = little or conflicting evidence; a name match alone never gives high. Where sources
   conflict and the evidence is not decisive, leave the question open rather than decide it.
4. **Map points:** don't edit `data/coords_study.tsv` (others work in parallel); list any proposed rows in your report
   (columns id lat lon precision label note) with coordinates you are confident of.
5. Edit only your assigned note files and their updates files. Keep "ash-smearers" for 塗灰外道.

Report: notes changed (ids), every updates row changed (old → new, one-line reason), proposed map rows, and anything in
the summaries or tests you think wrong.
