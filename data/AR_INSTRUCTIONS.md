# Coding the ASR Annual Reports (1903–37) and the Eastern/Bengal Circle reports

Follow `data/ASR_INSTRUCTIONS.md` exactly (same columns, same stances, same quote rules, same checker:
`python3 -I scripts/check_quotes_asr.py data/coded/ar_batchN.tsv`), with these differences:

- Input: `data/ar_batches/ar_batchN.tsv` (rows of `data/ar_hits.tsv`); full texts in `data/ref/asr_annual/<file>`
  (`arYYYY-YY.txt` = Director-General's Annual Report; `ecYYYY-YY.txt` = Bengal/Eastern Circle report).
- `author`: the excavator or writer of the section, as the report names him (Marshall, Vogel, Bloch, Spooner,
  Konow, Hargreaves, Banerji, Page, Sahni, Chanda, Dikshit, Stein, Garde, Kuraishi, Ghosh…). Sections are usually
  signed at the end; look for the signature or the "by …" heading.
- These reports are **excavation reports**: give most weight to what was dug and found — inscriptions and seals
  naming a place or monastery (e.g. Kasia's copper plate with "parinirvāṇa-caitya", Nālandā's seals, Sahet-Mahet's
  Jetavana plate, Kauśāmbī, Sarnath's Dharmarājikā inscription), stratigraphy, dates, plans — and to explicit
  confirmations or rejections of Cunningham's identifications. Use `confirms` when a dig confirms an identification,
  `revises` when it moves it, `rejects` when it overturns it.
- In `note`, always say how the find bears on Mizutani's identification (`data/places.tsv`, `mz_identification`)
  and on the survey's (`asr` column).

Reply with: passages coded / relevant; identifications confirmed by excavation or inscription (id, place, find,
one line each); identifications overturned or moved; `new` places.
