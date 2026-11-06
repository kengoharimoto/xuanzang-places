#!/usr/bin/env python3
"""Join Mizutani's master table, the authorities' identifications and the gazetteer coding into data/places.tsv.

Usage (from xuanzang-places/): python3 -I scripts/build_places.py
Inputs: data/places_mizutani.tsv, data/coded/auth_*.tsv, data/coded/gaz_batch*.tsv, data/gaz_hits.tsv
"""
import csv, glob, collections
AUTH = ["julien", "vivien", "cunningham", "beal", "watters", "majumdar", "dey"]
rd = lambda f: list(csv.DictReader((l for l in open(f, encoding="utf-8") if not l.startswith("#")), delimiter="\t"))
master = rd("data/places_mizutani.tsv")
ids = {r["id"] for r in master}
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
        for x in (r.get("xz_id") or "").replace(",", ";").split(";"):
            x = x.strip()
            if x in ids: gaz[x].append(r)
            elif x: unknown_ids[x] += 1
asr = collections.defaultdict(list); arr = collections.defaultdict(list)
for f in glob.glob("data/coded/ar_batch*.tsv"):
    for r in rd(f):
        if r.get("relevant") != "yes": continue
        for x in (r.get("xz_id") or "").replace(",", ";").split(";"):
            x = x.strip()
            if x in ids: arr[x].append(r)
            elif x: unknown_ids["ar:" + x] += 1
for f in glob.glob("data/coded/asr_batch*.tsv"):
    for r in rd(f):
        if r.get("relevant") != "yes": continue
        for x in (r.get("xz_id") or "").replace(",", ";").split(";"):
            x = x.strip()
            if x in ids: asr[x].append(r)
            elif x: unknown_ids["asr:" + x] += 1
def asr_tag(r):
    if r.get("file", "").startswith(("ar", "ec")) and not r["file"].startswith("asr"):
        f = r["file"].replace(".txt", "")
        return f'{r.get("author","")}, {"AR" if f.startswith("ar") else "Eastern Circle"} {f[2:]}' + (f' p. {r["page"]}' if r.get("page") else "")
    v = r.get("file", "").replace(".txt", "").replace("asr", "ASR ").replace("mukherji1901_tarai", "Mukherji 1901")
    return f'{r.get("author","")}, {v}' + (f' p. {r["page"]}' if r.get("page") else "")
cols = ["id", "juan", "level", "parent", "name_zh", "name_ja", "original_name", "visit", "mz_identification",
        "mz_other_views", "mz_status"] + AUTH + ["gaz_n", "gaz_argues", "gaz_volumes", "gaz_local_evidence", "asr", "asr_n", "asr_evidence", "ar", "ar_n", "ar_evidence"]
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
    out.append(row)
w = csv.DictWriter(open("data/places.tsv", "w", encoding="utf-8", newline=""), cols, delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(out)
print(len(out), "rows; authority coverage:", {a: sum(1 for r in out if r[a]) for a in AUTH})
print("rows with Annual Report passages:", sum(1 for r in out if r["ar_n"]))
print("rows with ASR passages:", sum(1 for r in out if r["asr_n"]))
print("rows with gazetteer passages:", sum(1 for r in out if r["gaz_n"]), "; with argued/doubting/alternative:", sum(1 for r in out if r["gaz_argues"]))
if unknown_ids: print("xz_id not in master:", dict(unknown_ids.most_common(20)))
