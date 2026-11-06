# Coding Epigraphia Indica and the Corpus Inscriptionum Indicarum

Follow `data/ASR_INSTRUCTIONS.md` (same columns, same stances, same quote rules; checker:
`python3 -I scripts/check_quotes_asr.py data/coded/epig_batchN.tsv`), with these differences:

- Input: `data/epig_batches/epig_batchN.tsv` (rows of `data/epig_hits.tsv`, with extra columns `pilgrim` (a mention of
  Xuanzang/Faxian), `names` (the Sanskrit place-names that triggered the passage) and `candidate_ids` (master ids those
  names belong to — a hint, not a coding). Full texts: `data/ref/epig/<file>` (`ei_NN` = Epigraphia Indica vol. NN;
  `cii_N` = CII vol. N: 1 Aśoka (Hultzsch 1925), 2.1 Kharoṣṭhī (Konow), 2.2 Bharhut, 3 Early Guptas (Fleet 1888),
  5 Vākāṭakas, 6 Śilāhāras).
- `author`: the editor of the inscription or article (Hultzsch, Kielhorn, Fleet, Konow, Bühler, Sircar, Chhabra…).
- What matters here: (1) an **inscription that names a Xiyu ji place** (country, city, monastery, river, hill) and
  where it was found — this is evidence of location in itself; (2) an **editor's identification** of a place named in
  an inscription with a Xiyu ji place or a modern site, especially when it cites Xuanzang; (3) inscriptions that
  attest a kingdom or dynasty at the time and place Xuanzang describes (e.g. Kongoda, Jejākabhukti, Valabhī,
  Brahmapura, Kosala, Karṇasuvarṇa, Samataṭa). Code `confirms` / `revises` / `rejects` / `proposes` / `reports` as
  for the survey; put the inscription's own wording (place-name as inscribed) in `name_in_asr` and the find-spot or
  the editor's identification in `asr_identification`.
- Many name-triggered passages are about homonyms or other periods with no bearing on location: `relevant=no`.
- In `note`, say how the passage bears on Mizutani's identification and on the notes' current proposal
  (`data/places.tsv`, `data/notes/updates_*.tsv`).

Reply with: passages coded / relevant; inscriptions naming a Xiyu ji place (id, place, inscription, find-spot);
identifications confirmed, moved or overturned; `new` places.
