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
cols = ["id", "juan", "level", "parent", "name_zh", "name_ja", "original_name", "visit", "mz_identification",
        "mz_other_views", "mz_status"] + AUTH + ["gaz_n", "gaz_argues", "gaz_volumes", "gaz_local_evidence"]
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
    out.append(row)
w = csv.DictWriter(open("data/places.tsv", "w", encoding="utf-8", newline=""), cols, delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(out)
print(len(out), "rows; authority coverage:", {a: sum(1 for r in out if r[a]) for a in AUTH})
print("rows with gazetteer passages:", sum(1 for r in out if r["gaz_n"]), "; with argued/doubting/alternative:", sum(1 for r in out if r["gaz_argues"]))
if unknown_ids: print("xz_id not in master:", dict(unknown_ids.most_common(20)))
