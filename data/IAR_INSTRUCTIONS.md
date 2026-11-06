# Coding Indian Archaeology – A Review (1953–54 to 2000–01)

Follow `data/AR_INSTRUCTIONS.md` (and `data/ASR_INSTRUCTIONS.md` beneath it) exactly — same columns, stances, quote
rules and checker (`python3 -I scripts/check_quotes_asr.py data/coded/iar_batchN.tsv`). Differences:

- Input: `data/iar_batches/iar_batchN.tsv` (rows of `data/iar_hits.tsv`); texts `data/ref/iar/iarYYYY-YY.txt`, OCR'd with
  Surya, page markers `<<page N>>` (scan pages; give the printed page if visible, else `scan N`).
- IAR reports are short, by excavation (often "excavation at X by Y of the Department / University …"). `author` = the
  excavating body and director as named (e.g. "G. R. Sharma, Allahabad University").
- These are the excavations after independence: Kauśāmbī (Sharma), Śrāvastī, Rājagṛha, Nālandā, Vaiśālī (Altekar,
  Sinha), Kumrahar, Rajbadidanga/Rangamati (S. R. Das: sealings naming Raktamṛttikā), Piprahwa and Ganwaria (K. M.
  Srivastava: sealings naming Kapilavastu), Tilaurakot, Sirpur, Nāgārjunakoṇḍa, Ahicchatra, Hastinapura, Sanghol, etc.
  Give the most weight to inscribed finds naming a place or monastery, and to explicit statements that an excavation
  confirms, moves or rejects an identification. Note the date of the find (report year).
- The OCR is good but tables, plate captions and lists come out as broken text; these are usually `relevant=no`.
