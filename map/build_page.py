#!/usr/bin/env python3
"""Build the places page: map/xuanzang_places.html from the template plus the study's data.

Usage (from xuanzang-places/): python3 -I scripts/build_places.py && python3 -I map/build_geo.py && python3 -I map/build_page.py
Inputs: data/places.tsv, data/coords.tsv, data/notes/updates_*.tsv, data/notes/notes_*.md, map/geo_small.json
"""
import csv, glob, html, json, re
rd = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
AUTH = ["julien", "vivien", "cunningham", "majumdar", "beal", "watters", "dey"]
coords = {r["id"]: r for r in rd("data/coords.tsv")}
upd = {}
for f in glob.glob("data/notes/updates_*.tsv"):
    for r in rd(f): upd[r["id"]] = r

def md(s):
    s = html.escape(s.strip())
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"<i>\1</i>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    paras = [p.strip() for p in re.split(r"\n\s*\n", s) if p.strip()]
    return "".join(f"<p>{p}</p>" for p in paras)

OBS = {}   # K. Harimoto's own notes (data/user_obs/observations.tsv)
for o in rd("data/user_obs/observations.tsv"):
    OBS.setdefault(o["id"], []).append({"kind": o["kind"], "obs": o["observation"], "src": o["source_note"], "as": o["assessment"]})
ALT = {}   # rival candidate sites with their route scores (route/candidates.tsv, route/candidate_scores.tsv)
SC = {(r["id"], r["candidate"]): r for r in rd("route/candidate_scores.tsv")}
for c in rd("route/candidates.tsv"):
    if c["proposer"] == "Mizutani" or not c["lat"]: continue
    sc = SC.get((c["id"], c["candidate"]), {})
    ALT.setdefault(c["id"], []).append({"name": c["candidate"], "by": c["proposer"], "lat": float(c["lat"]), "lon": float(c["lon"]),
        "z": sc.get("mean_abs_z", ""), "b": sc.get("mean_bearing_off", ""), "note": c["note"]})
MZS = {r["id"]: r for r in rd("route/candidate_scores.tsv") if r["proposer"] == "Mizutani"}
BEST = {r["id"]: r["best_fit"] for r in rd("route/chain_best.tsv")}
notes = {}
for f in sorted(glob.glob("data/notes/notes_*.md")):
    t = open(f, encoding="utf-8").read()
    for m in re.finditer(r"^###\s+(\S+)\s+(.*?)\n(.*?)(?=^#{2,3}\s|\Z)", t, re.S | re.M):
        notes[m.group(1)] = {"head": m.group(2).strip(), "body": md(m.group(3))}

out = []
for r in rd("data/places.tsv"):
    c = coords.get(r["id"], {})
    try: lat, lon = float(c.get("lat") or "x"), float(c.get("lon") or "x")
    except ValueError: lat = lon = None
    u = upd.get(r["id"], {})
    out.append({
        "id": r["id"], "juan": int(r["juan"]) if r["juan"].isdigit() else 0, "level": r["level"], "parent": r["parent"],
        "zh": r["name_zh"], "ja": r["name_ja"], "orig": r["original_name"], "visit": r["visit"],
        "mz": r["mz_identification"], "mzOther": r["mz_other_views"], "status": r["mz_status"],
        "auth": {a: r[a] for a in AUTH if r.get(a)},
        "gazN": int(r["gaz_n"] or 0), "gazArg": int(r["gaz_argues"] or 0), "gazVols": r["gaz_volumes"],
        "gazEv": r["gaz_local_evidence"][:1500],
        "asr": r.get("asr", "")[:1500], "asrN": int(r.get("asr_n") or 0), "asrEv": r.get("asr_evidence", "")[:1500],
        "ar": r.get("ar", "")[:1500], "arN": int(r.get("ar_n") or 0), "arEv": r.get("ar_evidence", "")[:1500],
        "ep": r.get("epig", "")[:1500], "epN": int(r.get("epig_n") or 0), "epEv": r.get("epig_evidence", "")[:1500],
        "ia": r.get("iar", "")[:1500], "iaN": int(r.get("iar_n") or 0), "iaEv": r.get("iar_evidence", "")[:1500],
        "tsrc": r.get("translation_source", ""), "tchk": r.get("translation_check", ""),
        "rel": {k: r.get(k, "") for k in ("sangharamas", "monks", "schools", "deva_temples", "other", "site_affiliation", "buddhism")},
        "tref": r.get("t2087_ref", ""), "zht": r.get("t2087_text", ""), "en": r.get("translation", ""),
        "lat": lat, "lon": lon, "prec": c.get("precision", ""), "modern": c.get("modern_name", ""), "cnote": c.get("note", ""),
        "change": u.get("change", ""), "proposed": u.get("proposed", ""), "basis": u.get("basis", ""), "conf": u.get("confidence", ""),
        "note": notes.get(r["id"]),
        "kh": OBS.get(r["id"], []),
        "lref": r.get("life_ref", ""), "lzh": r.get("life_text", ""), "len": r.get("life_translation", ""), "lnote": r.get("life_note", ""),
        "alt": ALT.get(r["id"], []), "mzz": MZS.get(r["id"], {}).get("mean_abs_z", ""), "mzb": MZS.get(r["id"], {}).get("mean_bearing_off", ""),
        "best": BEST.get(r["id"], ""),
    })
t = open("map/template.html", encoding="utf-8").read()
t = t.replace("/*PLACES*/[]", json.dumps(out, ensure_ascii=False, separators=(",", ":")))
t = t.replace("/*GEO*/{}", open("map/geo_small.json").read())
open("map/xuanzang_places.html", "w", encoding="utf-8").write(t)
print(len(t), "bytes;", len(out), "places;", sum(1 for p in out if p["lat"] is not None), "mapped;", sum(1 for p in out if p["note"]), "with notes")
