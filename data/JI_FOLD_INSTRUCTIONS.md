# Folding Ji Xianlin et al. (1985) into the place notes

Ji's commentary has been coded place by place in `data/coded/auth_ji_*.tsv`. Each row gives Ji's identification,
stance, the other views he reports, the printed page, a verbatim quote, and a note on the post-1971 evidence he
cites. The full OCR is `data/ref/ji1985.txt`. Fold it into the notes in the files assigned to you, and do not touch
any other note file.

For each place in your files that has a Ji row:

1. **Ji's paragraph.** Add `**Ji Xianlin et al. (1985).** …` before the note's **Assessment.** paragraph, wrapped at 118
   characters like the rest:
   - where Ji differs from Mizutani, or cites evidence the note does not yet have (excavations or inscriptions after
     1971, Chinese, Japanese or Russian scholarship, textual points), give his identification, his basis and the page
     in 1–4 sentences;
   - where he simply agrees with Mizutani or the study and adds nothing, write one sentence ("Ji agrees: X (p. N).").
2. **Assessment and updates.** Revise the note's **Assessment.** paragraph and its row in `data/notes/updates_*.tsv`
   only where Ji's evidence changes the picture: new site evidence, a convincing argument against the current view, or
   a different reading of the text. Keep the columns: `change` is none / strengthened / weakened / alternative /
   new-candidate.

   For confidence, use the study's rule:
   - **high:** site evidence (an excavation, an inscription naming the place, or a matching monument), or, for a major
     country, river or pass, an unbroken name, an unmistakable description and no serious rival;
   - **medium:** agreement among the authorities;
   - **low:** little or conflicting evidence.

   Ji's agreement alone does not raise a rating to high.
3. **Map point.** If Ji settles a single site different from the current map point, and the note now adopts it, do
   NOT edit `data/coords_study.tsv` (other agents run in parallel): give the row in your report instead (columns
   `id lat lon precision label note`), with approximate coordinates you are confident of. Do not move points for
   questions left open between candidates.

Places that have a Ji row but no note: list them in your report and do not create notes.

Report:
- the number of notes given a Ji paragraph;
- every assessment or updates row you changed, as old → new, with a one-line reason;
- any coordinates rows you propose (as TSV lines);
- any problem in the Ji coding rows (a wrong id or a misread quote).
