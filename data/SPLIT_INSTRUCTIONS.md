# Splitting multi-place coded passages into per-place entries

A coded source passage (gazetteer hit, ASR / Annual Report / IAR / EI passage) is sometimes assigned to several places
at once (`xz_id` like `08.05.01;08.05.01a`). The joined table used to give every one of those places the passage's
whole identification and evidence, so some places showed evidence about a sibling site. Your job: split each such
passage into one entry per place.

Input: `data/coded/split/todo_<k>.tsv`, one row per multi-place passage, with these columns:
- `file`, `key`: the coded file and its `hit` or `passage` number;
- `xz_ids`, `names`: the places it is coded to;
- `identification`, `stance`, `evidence`, `quote`, `note`: as coded;
- `context`: the source text around it. This is not available for every source; the original file is in
  `data/ref/...`, see `scripts/check_quotes_*.py` for where.

The places themselves are described in `data/places.tsv` (`name_zh`, `original_name`, `mz_identification`).

Output: `data/coded/split/split_<k>.tsv`, header exactly `file	key	xz_id	applies	identification	evidence`, with
one row per (passage, place), i.e. one for every id in `xz_ids`:
- `applies`:
  - `yes` if the passage says something about this particular place: an identification, site evidence, or an
    argument;
  - `mention` if it only names the place in passing, for instance listing it with neighbours;
  - `no` if it does not concern this place at all (a coding slip).
- `identification`: what the passage identifies this place with, in a few words. Leave it empty if it says nothing
  about this place's location.
- `evidence`: only the part of the coded evidence (or of the context) that concerns this place, in one or two plain
  sentences. Leave it empty for `mention` and `no`.

Rules:
- Do not invent: use only the coded fields and the source text.
- If the passage genuinely concerns several places equally (e.g. a description of a whole site complex with each
  part identified), each place gets its own part.
- Keep the source's wording for identifications (e.g. "Bakror mound, opposite Bodh Gaya").

Check: every id in every input row appears exactly once in your output, and there are no tabs or newlines inside
fields.

Report: the counts of yes, mention and no, and any coding slips you found (rows where `applies = no`).
