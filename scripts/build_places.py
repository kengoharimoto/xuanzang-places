#!/usr/bin/env python3
"""Join Mizutani's master table, the authorities' identifications and the gazetteer coding into data/places.tsv.

Usage (from xuanzang-places/): python3 -I scripts/build_places.py
Inputs: data/places_mizutani.tsv, data/coded/auth_*.tsv, data/coded/gaz_batch*.tsv, data/gaz_hits.tsv
"""
import csv, glob, collections, re
RELCOLS = ["sangharamas", "monks", "schools", "deva_temples", "other", "site_affiliation", "buddhism"]
AUTH = ["julien", "vivien", "cunningham", "beal", "watters", "majumdar", "dey", "ji"]
rd = lambda f: list(csv.DictReader((l for l in open(f, encoding="utf-8") if not l.startswith("#")), delimiter="\t"))
master = rd("data/places_mizutani.tsv")
try:   # places missing from Mizutani's numbering, added from the sources (data/places_added.tsv; ids end in .xN)
    for a in rd("data/places_added.tsv"):
        master.append({"id": a["id"], "juan": a["juan"], "level": a["level"], "parent": a["parent"], "name_zh": a["name_zh"],
                       "name_ja": "", "original_name": a["original_name"], "visit": a["visit"],
                       "mz_identification": a["identification"], "mz_other_views": a["sources"], "mz_status": "added"})
    key = lambda r: [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", r["id"])]
    master.sort(key=key)
except FileNotFoundError:
    pass
ids = {r["id"] for r in master}
RES = {}   # coded rows tagged `new`, resolved to existing or added ids (data/coded/new_resolved.tsv)
try:
    for r in rd("data/coded/new_resolved.tsv"): RES[(r["file"], r["passage_or_hit"])] = r["resolved"]
except FileNotFoundError: pass
SPLIT = {}   # multi-place passages split into per-place entries (data/coded/split/split_*.tsv; data/SPLIT_INSTRUCTIONS.md)
for f_ in glob.glob("data/coded/split/split_*.tsv"):
    for r_ in rd(f_): SPLIT[(r_["file"], r_["key"], r_["xz_id"])] = r_
def per_place(r, f, x, n_ids):
    """The passage as it bears on place x: the split entry's identification and evidence when the passage is coded to
    several places; None when the split says it does not concern x."""
    if n_ids < 2: return r
    sp = SPLIT.get((f.split("/")[-1], r.get("hit") or r.get("passage") or "", x))
    if not sp: return r
    if sp["applies"] == "no": return None
    q = dict(r)
    idf, evf = ("gaz_identification", "local_evidence") if "gaz_identification" in r else ("asr_identification", "evidence")
    q[idf] = sp["identification"] or ("named only" if sp["applies"] == "mention" else "")
    q[evf] = sp["evidence"] if sp["applies"] == "yes" else ""
    return q
def xids(r, f):
    xs = [x.strip() for x in (r.get("xz_id") or "").replace(",", ";").split(";") if x.strip()]
    res = RES.get((f.split("/")[-1], r.get("hit") or r.get("passage") or ""))
    if res and any("new" in x for x in xs):
        xs = [x for x in xs if "new" not in x] + ([] if res == "drop" else [y.strip() for y in res.split(";") if y.strip()])
    return xs
auth = collections.defaultdict(lambda: collections.defaultdict(list))
for f in glob.glob("data/coded/auth_*.tsv"):
    for r in rd(f):
        a = r.get("authority", "").strip().lower()
        if r.get("id") in ids and a:
            s = r.get("identification", "").strip()
            if r.get("stance") and r["stance"] not in ("firm",): s += f' [{r["stance"]}]'
            if r.get("page"): s += f' (p. {r["page"]})'
            auth[r["id"]][a].append(s)
hits = {r["hit"]: r for r in rd("data/gaz_hits.tsv")}
gaz = collections.defaultdict(list); unknown_ids = collections.Counter()
for f in glob.glob("data/coded/gaz_batch*.tsv"):
    for r in rd(f):
        if r.get("relevant") != "yes": continue
        for x in xids(r, f):
            x = x.strip()
            if x in ids:
                if (q := per_place(r, f, x, len(xids(r, f)))) is not None: gaz[x].append(q)
            elif x: unknown_ids[x] += 1
asr = collections.defaultdict(list); arr = collections.defaultdict(list); epg = collections.defaultdict(list); iar = collections.defaultdict(list)
for pat, store, tag in (("data/coded/epig_batch*.tsv", epg, "epig"), ("data/coded/iar_batch*.tsv", iar, "iar")):
    for f in glob.glob(pat):
        for r in rd(f):
            if r.get("relevant") != "yes": continue
            for x in xids(r, f):
                x = x.strip()
                if x in ids:
                    if (q := per_place(r, f, x, len(xids(r, f)))) is not None: store[x].append(q)
                elif x: unknown_ids[tag + ":" + x] += 1
for f in glob.glob("data/coded/ar_batch*.tsv"):
    for r in rd(f):
        if r.get("relevant") != "yes": continue
        for x in xids(r, f):
            x = x.strip()
            if x in ids:
                if (q := per_place(r, f, x, len(xids(r, f)))) is not None: arr[x].append(q)
            elif x: unknown_ids["ar:" + x] += 1
for f in glob.glob("data/coded/asr_batch*.tsv"):
    for r in rd(f):
        if r.get("relevant") != "yes": continue
        for x in xids(r, f):
            x = x.strip()
            if x in ids:
                if (q := per_place(r, f, x, len(xids(r, f)))) is not None: asr[x].append(q)
            elif x: unknown_ids["asr:" + x] += 1
def src_tag(r):
    f = r.get("file", "").replace(".txt", "")
    if f.startswith("ei_"): v = "EI " + f[3:].replace("-vol-0", ".")
    elif f.startswith("cii_"): v = "CII " + f[4:].replace("-", ".")
    elif f.startswith("iar"): v = "IAR " + f[3:]
    else: return asr_tag(r)
    return f'{r.get("author","")}, {v}' + (f' p. {r["page"]}' if r.get("page") else "")
def asr_tag(r):
    if r.get("file", "").startswith(("ar", "ec")) and not r["file"].startswith("asr"):
        f = r["file"].replace(".txt", "")
        return f'{r.get("author","")}, {"AR" if f.startswith("ar") else "Eastern Circle"} {f[2:]}' + (f' p. {r["page"]}' if r.get("page") else "")
    if r.get("file", "").startswith("foucher"): return f'Foucher, La vieille route (1942–47)' + (f' {r["page"]}' if r.get("page") else "")
    if r.get("file", "").startswith("masi"): return f'{r.get("author","")}, MASI {r["file"][4:6]}' + (f' p. {r["page"]}' if r.get("page") else "")
    v = r.get("file", "").replace(".txt", "").replace("asr", "ASR ").replace("mukherji1901_tarai", "Mukherji 1901")
    return f'{r.get("author","")}, {v}' + (f' p. {r["page"]}' if r.get("page") else "")
cols = ["id", "juan", "level", "parent", "name_zh", "name_ja", "original_name", "name_study", "name_study_basis", "visit", "mz_identification",
        "mz_other_views", "mz_status"] + AUTH + ["gaz_n", "gaz_argues", "gaz_volumes", "gaz_local_evidence", "asr", "asr_n", "asr_evidence", "ar", "ar_n", "ar_evidence", "epig", "epig_n", "epig_evidence", "iar", "iar_n", "iar_evidence", "t2087_ref", "t2087_text", "translation", "translation_source", "translation_check", "translation_issues"] + RELCOLS + ["user_obs", "user_obs_assessment", "life_ref", "life_text", "life_translation", "life_translation_check", "life_translation_issues", "life_note"]
def _load(path, key="id"):
    try: return {r[key]: r for r in rd(path)}
    except FileNotFoundError: return {}
PASS = {}
for f in sorted(glob.glob("data/text/passages_*.tsv")): PASS.update(_load(f))
TRAN = _load("data/text/translation_dm.tsv")
LPASS = {}   # the Life (T2053): parallel passages and their translations
for f in sorted(glob.glob("data/text/life_passages_*.tsv")): LPASS.update(_load(f))
LANC = {}
for f in sorted(glob.glob("data/text/life_anchors_*.tsv")): LANC.update(_load(f))
LTRAN = _load("data/text/life_translation_dm.tsv")
LREV = {}
for f in sorted(glob.glob("data/text/life_review_*.tsv")): LREV.update(_load(f))
REV, REL = {}, {}
for f in sorted(glob.glob("data/text/review_[0-9]*.tsv")): REV.update(_load(f))
try: STALE = set(open("data/text/review_stale_ids.txt").read().split())   # passages re-cut with notes; old reviews no longer apply
except FileNotFoundError: STALE = set()
for i in STALE: REV.pop(i, None)
for f in sorted(glob.glob("data/text/review2_*.tsv")): REV.update(_load(f))   # re-reviews of the re-cut passages
for f in sorted(glob.glob("data/religion/religion_*.tsv")): REL.update(_load(f))   # religion_zz_user.tsv (corrections) loads last
OBS = collections.defaultdict(list)   # K. Harimoto's own notes (data/Archive), one row per observation
for r in rd("data/user_obs/observations.tsv"): OBS[r["id"]].append(r)
NAMES = _load("data/names/proposed.tsv")
out = []
for m in master:
    row = {k: m.get(k, "") for k in cols}
    for a in AUTH: row[a] = " | ".join(auth[m["id"]].get(a, []))
    g = gaz[m["id"]]
    row["gaz_n"] = len(g)
    row["gaz_argues"] = sum(1 for r in g if r.get("stance") in ("argues", "doubts", "alternative"))
    vols = []
    for r in g:
        h = hits.get(r["hit"], {}); v = f'{h.get("place","")} {h.get("year","")}'.strip()
        if v not in vols: vols.append(v)
    row["gaz_volumes"] = "; ".join(vols)
    row["gaz_local_evidence"] = " || ".join(f'[{hits.get(r["hit"],{}).get("place","")} {hits.get(r["hit"],{}).get("year","")}] {r["local_evidence"]}' for r in g if r.get("local_evidence", "").strip())
    a = asr[m["id"]]
    row["asr"] = " | ".join(dict.fromkeys(f'{r["asr_identification"]} [{r["stance"]}; {asr_tag(r)}]' for r in a if r.get("asr_identification")))
    row["asr_n"] = len(a)
    row["asr_evidence"] = " || ".join(f'[{asr_tag(r)}] {r["evidence"]}' for r in a if r.get("evidence", "").strip())
    a = arr[m["id"]]
    row["ar"] = " | ".join(dict.fromkeys(f'{r["asr_identification"]} [{r["stance"]}; {asr_tag(r)}]' for r in a if r.get("asr_identification")))
    row["ar_n"] = len(a)
    row["ar_evidence"] = " || ".join(f'[{asr_tag(r)}] {r["evidence"]}' for r in a if r.get("evidence", "").strip())
    pz, tr = PASS.get(m["id"], {}), TRAN.get(m["id"], {})
    row["t2087_ref"] = pz.get("t_ref", ""); row["t2087_text"] = pz.get("zh", "")
    rv = REV.get(m["id"], {})
    if rv.get("en_revised", "").strip() and rv.get("verdict") in ("minor", "major"):
        row["translation"] = rv["en_revised"]; row["translation_source"] = "DharmaMitra, corrected against Mizutani and Beal"
    else:
        row["translation"] = tr.get("en", ""); row["translation_source"] = (tr.get("model", "") + " " + tr.get("date", "")).strip()
    row["translation"] = re.sub(r"\((?:Original note|Note)\s*:\s*", "(", row["translation"])   # one convention: the text's notes in plain brackets
    row["translation_check"] = rv.get("verdict", ""); row["translation_issues"] = rv.get("issues", "")
    rl = REL.get(m["id"], {})
    for c in RELCOLS: row[c] = rl.get(c, "")
    row["user_obs"] = " || ".join(f'[{o["kind"]}] {o["observation"]}' for o in OBS[m["id"]])
    lp = LPASS.get(m["id"], {})
    row["life_ref"] = lp.get("t_ref", ""); row["life_text"] = lp.get("zh", "")
    row["life_translation"] = LTRAN.get(m["id"], {}).get("en", "") if lp else ""; row["life_note"] = LANC.get(m["id"], {}).get("note", "")
    lr = LREV.get(m["id"], {}) if lp else {}
    if lr.get("en_revised", "").strip() and lr.get("verdict") in ("minor", "major"): row["life_translation"] = lr["en_revised"]
    row["life_translation_check"] = lr.get("verdict", ""); row["life_translation_issues"] = lr.get("issues", "")
    row["user_obs_assessment"] = " || ".join(o["assessment"] for o in OBS[m["id"]])
    nm = NAMES.get(m["id"], {})   # the study's proposed original form (data/names/proposed.tsv)
    row["name_study"] = nm.get("name_study", ""); row["name_study_basis"] = f'{nm["verdict"]}, {nm["confidence"]}: {nm["basis"]}' if nm else ""
    for col, store in (("epig", epg), ("iar", iar)):
        a = store[m["id"]]
        row[col] = " | ".join(dict.fromkeys(f'{r["asr_identification"]} [{r["stance"]}; {src_tag(r)}]' for r in a if r.get("asr_identification")))
        row[col + "_n"] = len(a)
        row[col + "_evidence"] = " || ".join(f'[{src_tag(r)}] {r["evidence"]}' for r in a if r.get("evidence", "").strip())
    out.append(row)
w = csv.DictWriter(open("data/places.tsv", "w", encoding="utf-8", newline=""), cols, delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(out)
print(len(out), "rows; authority coverage:", {a: sum(1 for r in out if r[a]) for a in AUTH})
print("rows with text:", sum(1 for r in out if r["t2087_text"]), "; with translation:", sum(1 for r in out if r["translation"]))
print("rows with Annual Report passages:", sum(1 for r in out if r["ar_n"]))
print("rows with ASR passages:", sum(1 for r in out if r["asr_n"]))
print("rows with gazetteer passages:", sum(1 for r in out if r["gaz_n"]), "; with argued/doubting/alternative:", sum(1 for r in out if r["gaz_argues"]))
if unknown_ids: print("xz_id not in master:", dict(unknown_ids.most_common(20)))
