# Comparing the study with the standard identifications

The standard reference for the places of the Xiyu ji is 季羨林 et al., 《大唐西域記校注》 (1985; "Ji"), which in
most places agrees with Mizutani Shinjō's annotated translation (1971). The study presents its map as a visualisation
of that standard, and marks only where its evidence departs from it. This pass records, place by place, what the
standard says and how the study stands to it.

## Input

`input_<g>.tsv` (one row per place): `ji_identification` (Ji, as coded in `data/coded/auth_ji_*.tsv`; empty where Ji
was not coded or says nothing), `ji_stance`, `ji_others`, `mizutani`, and the study's current view:
`study_identification`, `study_confidence`, `study_change` (relative to Mizutani), `study_proposed`. The place's note
(`grep -n '^### <id>' data/notes/*.md`) explains the study's reasons; read it where the relation is not obvious.

## Output: `data/standard/compare_<g>.tsv` (TSV, UTF-8, header exactly; one row per input row)

| column | content |
|---|---|
| `id` | from the input |
| `standard` | the standard identification, short (modern site or region as Ji gives it). If Ji is empty or gives nothing for the place, Mizutani's. Empty if neither identifies it |
| `standard_source` | `ji` (Ji gives it and Mizutani agrees or says nothing), `ji+mz` (both, agreeing), `ji≠mz` (both, differing: `standard` is Ji's, say Mizutani's in `note`), `mz` (Mizutani only), `none` |
| `relation` | how the study stands to the standard: `agrees` (same site); `refines` (same place, the study names a more exact site within it, consistent with the standard); `open` (the study leaves the place open between the standard and another candidate); `differs` (the study puts it elsewhere); `candidate` (no standard identification; the study proposes one); `none` (no standard and no study identification) |
| `evidence` | for `refines`, `open`, `differs`, `candidate`: the decisive evidence in a few words (excavation, inscription, route figures, recent study), as in the note. Empty for `agrees` |
| `note` | anything a reader needs: e.g. Ji differs from Mizutani; the study agrees with Ji against Mizutani; a weakened rating without a different site |

Judge the substance, not the wording: "Sahet-Mahet" and "Saheth-Maheth on the Rapti" agree. A study that keeps the
standard's site but lowers the confidence is still `agrees` (say so in `note`). A study that agrees with Ji where Ji
differs from Mizutani is `agrees` (the standard is Ji's).

Report: counts by `relation` and by `standard_source`; every `differs` and `open` (id, place, one line).
