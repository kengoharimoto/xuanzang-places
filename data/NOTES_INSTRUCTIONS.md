# Writing the notes on disputed places (step 3)

Inputs (all in `xuanzang-places/data/`):
- `places.tsv`: one row per place: Mizutani's identification and status, then one column per authority
  (`julien, vivien, cunningham, beal, watters, majumdar, dey`), then a gazetteer summary (`gaz_n`, `gaz_argues`,
  `gaz_volumes`, `gaz_local_evidence`).
- Full detail behind those columns: `places_mizutani.tsv` (Mizutani: quote, refs, other views), `coded/auth_*.tsv`
  (each authority: identification, stance, page, quote), `coded/gaz_batch*.tsv` + `gaz_hits.tsv` (each gazetteer
  passage: `xz_id`, stance, authority cited, local evidence, quote; join on `hit` for volume, place, year).
- Gazetteer volumes often exist in two scans: count **volumes/passages**, not hits; cite one.

## Which places get a note

In your juan range, every place where **any** of these holds:
1. Mizutani's `mz_status` is `disputed`, `uncertain` or `unknown`;
2. two or more authorities give materially different sites (not mere spelling or precision differences);
3. at least one gazetteer passage `argues`, `doubts` or proposes an `alternative`.
Also gather the gazetteer rows coded `xz_id = new` in your range (places missing from the master table) into a
final section.

## Each note (Markdown, in `notes/notes_<range>.md`, in master-table order)

```
### <id> <name_zh> (<original_name>) — <one-line verdict>

**Identifications.** Mizutani: … (status). Julien/Vivien: … Cunningham (1871): … Majumdar (1924): … Beal: …
Watters: … Dey: … — only those who say something; give pages where available. Group agreeing authorities.

**Gazetteers.** What they add, volume by volume (district, year): their identification, whether they repeat or
argue, and the local evidence (mounds, ruins, finds, inscriptions, place-names, traditions, river courses,
measured distances, excavations). Quote the decisive phrase briefly (from the coded `quote`). If the gazetteers add
nothing, say so in one sentence ("The gazetteers repeat Cunningham and add nothing.").

**Assessment.** Two to four sentences: where the evidence assembled here points, and whether the gazetteers change
the picture Mizutani gives (strengthen, weaken, or add a candidate). Keep to the evidence in these files — don't
import later scholarship from memory; if you know the question was settled later (e.g. by excavation after 1971),
you may say "later work (not in these sources) …" in one clause, flagged as such.
```

Keep each note short (80–250 words). Plain English; Chinese and Sanskrit names as in the table.

## Also write `notes/updates_<range>.tsv`

One row per noted place: `id, name_zh, mizutani, proposed, change, basis, confidence` where
- `proposed` = the identification the evidence here supports best (may equal Mizutani's);
- `change` = `none` (Mizutani stands), `strengthened` (gazetteer evidence supports Mizutani), `weakened`
  (gazetteer evidence counts against Mizutani without a better candidate), `alternative` (a better-supported or
  equally supported different site), `new-candidate` (a site no standard authority records);
- `basis` = short: which gazetteers / authorities and what evidence;
- `confidence` = `high`, `medium`, `low`.

## Finish

Report: number of notes; the places where `change` ≠ `none`, one line each; anything in the data that looks wrong
(miscoded `xz_id`, misread authority) — say what and where, don't fix the coded files.
