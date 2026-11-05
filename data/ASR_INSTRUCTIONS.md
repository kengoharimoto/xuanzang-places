# Coding the Archaeological Survey of India Reports (Cunningham series, vols. I–XXIII, 1871–87)

Input: `data/asr_batches/asr_batchN.tsv`, rows of `data/asr_hits.tsv`: one row per **passage** (mentions of
Xuanzang/Hwen Thsang, Faxian/Fa-Hian or "the Chinese pilgrim" within 1,500 characters merged). Columns:
`passage, file, line, n_hits, context`. The full OCR is `data/ref/asr/<file>`; open it at `line` when the argument
starts earlier or runs on (it often does: Cunningham's identifications run over pages, with measurements and plans).
`mukherji1901_tarai.txt` is P. C. Mukherji's *Report on a Tour of Exploration of the Antiquities in the Tarai, Nepal*
(1901), not an ASR volume, coded the same way.

Master table of places: `data/places.tsv` (ids, Chinese names, `original_name`, Mizutani's identification and status,
other authorities). Authors of the volumes (verify on the title page of the file): I–III, V, IX–XI, XIV–XVII,
XIX–XXI Cunningham; IV Beglar & Carlleyle; VI, XII, XVIII, XXII Carlleyle; VII, VIII, XIII Beglar; XXIII Garrick.
Some Cunningham volumes include assistants' reports — code the author of the passage.

Goal: what the **survey** says about where a Xiyu ji place is, and what fieldwork it reports: measured ruins,
excavations, finds (sculpture, seals, coins, inscriptions), local names and traditions, distances measured on the
ground, river courses. The ASR is where Cunningham and his assistants argued identifications in detail, often
revising the *Ancient Geography* (1871); note revisions explicitly.

## Columns (TSV, UTF-8, header exactly; one row per passage — every passage in the batch gets a row)

| column | content |
|---|---|
| `passage` | from the batch |
| `file` | from the batch |
| `author` | `Cunningham`, `Beglar`, `Carlleyle`, `Garrick`, `Mukherji`, or other |
| `relevant` | `yes` if the passage locates or discusses the location of a Xiyu ji place (Faxian-only places: `yes` only if also in the Xiyu ji); `no` otherwise (chronology, Buddhism in general, iconography without location, OCR false matches) |
| `xz_id` | master-table id(s), `;`-separated; `new` for a Xiyu ji place missing from the table (name it in `note`) |
| `name_in_asr` | the name as written (e.g. `Kia-pi-li`, `Kapilavastu`, `Po-lo-ki-pu-ti`) |
| `asr_identification` | the site identified (modern names as written; add district) |
| `stance` | `proposes` (new identification argued here), `confirms` (repeats/strengthens an earlier one with new evidence), `revises` (changes the author's or Cunningham's earlier identification), `rejects` (only rejects a proposal), `reports` (cites others without deciding) |
| `evidence` | concise summary of the field evidence (measurements, excavation, finds, inscriptions, local names, measured distances); empty if none |
| `page` | printed page number if visible near the passage in the OCR, else empty |
| `quote` | **verbatim** from the OCR file (copy, don't retype; OCR errors included), ≤ 400 chars, the sentence(s) stating the identification and key evidence; join non-adjacent fragments with `…` (each ≥ 12 chars). Empty only if `relevant=no`. |
| `note` | short: disagreement with Mizutani's identification; whether this revises *Ancient Geography*; cross-refs |

## Checks

Run `python3 -I scripts/check_quotes_asr.py data/coded/asr_batchN.tsv` from `xuanzang-places/` until `bad 0`.
Reply with: passages coded / relevant; the identifications that **differ from Mizutani** or that **revise
Cunningham's 1871 view** (id, place, one line each); the strongest field evidence found (one line each); `new`
places.
