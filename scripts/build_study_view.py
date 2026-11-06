#!/usr/bin/env python3
"""The study's current view of every place: where it puts the place, and how sure it is.

Usage (from xuanzang-places/): python3 -I scripts/build_study_view.py  -> data/study_view.tsv
Inputs: data/places.tsv (all places, Mizutani's and the added ones), data/notes/updates_*.tsv (the notes' proposed
identification, kind of change and confidence), data/coords.tsv (Mizutani's points), data/coords_study.tsv (the study's
own proposed sites), data/coords_added.tsv (points for the added places).

Point: the study's proposed site where it settles on one (coords_study), else the added place's point, else
Mizutani's point (accepted, or untested). Class (the study's confidence, from the notes' assessments):
  secure      confidence high, Mizutani kept or strengthened, or a single proposed site with high confidence
  probable    confidence medium
  open        confidence low; or weakened; or an alternative left open between candidates
  untested    no note: Mizutani's identification (or, for added places, the sources'), not assessed by the study
  unlocated   no point
"""
import csv, glob, re
rd = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
P = rd("data/places.tsv")
U = {r["id"]: r for f in glob.glob("data/notes/updates_*.tsv") for r in rd(f)}
MZ = {r["id"]: r for r in rd("data/coords.tsv")}
ST = {r["id"]: r for r in rd("data/coords_study.tsv")}
try: AD = {r["id"]: r for r in rd("data/coords_added.tsv")}
except FileNotFoundError: AD = {}
def pt(r, lab_key):
    try: return float(r["lat"]), float(r["lon"]), r.get("precision", ""), r.get(lab_key, "")
    except (KeyError, ValueError, TypeError): return None
out = []
for p in P:
    i = p["id"]; u = U.get(i, {})
    if i in ST: src, q = "study", pt(ST[i], "label")
    elif i in AD: src, q = "added", pt(AD[i], "label")
    else: src, q = "Mizutani", pt(MZ.get(i, {}), "modern_name")
    conf, ch, prop = u.get("confidence", ""), u.get("change", ""), u.get("proposed", "")
    open_alt = ch == "alternative" and i not in ST and bool(re.search(r"\bor\b|\bopen\b|equal weight|; .*?rival", prop))
    if not q: cls = "unlocated"
    elif not u: cls = "untested"
    elif ch == "weakened" or conf == "low" or open_alt: cls = "open"
    elif conf == "high": cls = "secure"
    elif conf == "medium": cls = "probable"
    else: cls = "open"
    out.append({"id": i, "cls": cls, "point_from": src if q else "", "lat": q[0] if q else "", "lon": q[1] if q else "",
                "precision": q[2] if q else "", "label": q[3] if q else "", "confidence": conf, "change": ch,
                "open_alternative": "yes" if open_alt else "",
                "identification": prop or (p["mz_identification"] if p.get("mz_status") != "added" else p["mz_identification"])})
w = csv.DictWriter(open("data/study_view.tsv", "w", encoding="utf-8", newline=""), list(out[0]), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(out)
import collections
print(len(out), collections.Counter(o["cls"] for o in out), collections.Counter(o["point_from"] for o in out))
