# Testing the reconstructed original names (pilot)

Many place names in the study carry an original form that is a reconstruction (asterisked, e.g. *bāmiyana) or
queried. These forms come from Mizutani and the older authorities; the study has not tested them. Your task: test each
target form against Xuanzang's own transcription practice and look for a better form that is actually attested.

## Inputs

- `data/names/targets_<batch>.tsv`: your targets (id, name_zh, translit = the transcribed characters, original_name,
  region, identification).
- `data/names/key.tsv`, `data/names/key_notes.md`, `data/names/align.tsv`: the key to Xuanzang's transcription, built
  from the names whose form is certain. `data/names/mc.tsv`: Middle Chinese (Qieyun) positions.
- The text: `data/ref/t2087_joined.txt` (rare characters as mNNNNN, see `data/text/gaiji_map.json`). Read each
  target's passage: a 唐言 gloss gives the meaning and is a strong test of a proposed form.
- Searching attested names:
  - `python3 scripts/skt_search.py REGEX [MAX] [PATH_FILTER]` searches the Sanskrit e-text library
    (/mnt2/kengo/E-texts/1_sanskr: epics, Purāṇas with their geographical lists, kāvya incl. Harṣacarita and
    Kāvyamīmāṃsā, Buddhist texts incl. avadānas and vinaya, and inscriptions in 7_inscriptions) on a diacritic-free copy;
    write the regex without diacritics, e.g. `"\bkapis"`, `"parnots"`. Output lines are the ORIGINAL text with path:line.
  - Inscriptions and survey reports in English OCR: `data/ref/epig/` (Epigraphia Indica, CII), `data/ref/asr/`,
    `data/ref/asr_annual/`, `data/ref/iar/`; Stein's Rājataraṅgiṇī translation and Memoir (Kashmir names):
    `data/ref/stein/RajataranginiVol1.txt`, `RajataranginiVol2.txt`, `india.history.resource.41410.txt`. Use grep -i.
  - Modern name survival: the gazetteer and survey texts above; the study's existing notes in `data/notes/` (read the
    target's note first: it says what is known).

## For each target

1. **Check the current form against the key**, syllable by syllable: which characters render the form as Xuanzang
   usually does, and which do not (vowel length, retroflex/dental, aspirate, sibilant, final consonant, cluster). Say
   whether the form looks Sanskrit or vernacular (Prakrit, Gāndhārī, Iranian) and whether that fits the key.
2. **Look for attested forms** that fit the characters better: in the Sanskrit corpus (especially the geographical
   lists of peoples and countries, Rājataraṅgiṇī material for Kashmir, Buddhist texts), in inscriptions, and as modern
   names near the identified site. Try the variants the key allows. Record what you searched even when nothing fits.
3. **Weigh it**: an attested form that fits the characters and the gloss, and names a place in the right region, is a
   strong candidate; a form that fits the characters only is a weak one. Short names (two characters) match by chance
   easily: say so.

## Output

`data/names/test_<batch>.tsv`, header:

    id	name_zh	translit	current_form	key_fit	verdict	proposed_form	attestation	source_file	quote	site_lead	confidence	note

- `key_fit`: per character, e.g. `跋=ba ok; 祿=lu ok; 迦=ka ok` or with `MISMATCH (key: …)`.
- `verdict`: `keep` (the current form fits and nothing better is attested) / `doubtful` (the form breaks the key, nothing
  better found) / `better` (a better form is proposed) / `alternative` (another form is as good).
- `proposed_form`: the form you propose, IAST; asterisk if not attested.
- `attestation`: where the proposed form is attested (text and place), or empty.
- `source_file` and `quote`: path (relative to /mnt2/kengo/E-texts/1_sanskr for library hits, or to data/ref/ for the
  others) and the line, verbatim, under 300 characters. Several attestations: one row per target, the best one quoted,
  the others in `note`.
- `site_lead`: if the form points to a modern place (a surviving name near the identified area), the name and source.
- `confidence`: high / medium / low.

Then verify the quotes with a small script: each must be a substring of its file (whitespace-normalised). Keep scripts
in /home/kengo/.claude/jobs/ae7893d7/tmp/names_<batch>/. Edit no other file.

## Report

Counts by verdict; every `better` and `alternative` with its evidence in one line; site leads; and targets where you
think the identification itself should be reconsidered because of the name.
