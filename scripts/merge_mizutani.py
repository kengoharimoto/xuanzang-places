#!/usr/bin/env python3
"""Merge data/coded/mz_juan*.tsv into data/places_mizutani.tsv (sorted by id) and report problems.
Usage (from xuanzang-places/): python3 -I scripts/merge_mizutani.py"""
import csv, glob, re, collections, pathlib
COLS = "id juan level parent name_zh name_ja mc_reading original_name route t_route t_verb visit visit_basis mz_identification mz_other_views mz_refs mz_status pdf_page printed_page quote mz_note".split()
rows, probs = [], []
for f in sorted(glob.glob("data/coded/mz_juan*.tsv")):
    for i, r in enumerate(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"), 2):
        if None in r or set(r) != set(COLS): probs.append(f"{f}:{i} bad columns {sorted(set(r) ^ set(COLS), key=str)}")
        r["_src"] = f; rows.append(r)
def key(r):
    return [((0, int(x), "") if x.isdigit() else (1, 0, x)) for x in re.findall(r"\d+|[a-z]+", r.get("id") or "")]
rows.sort(key=key)
ids = collections.Counter(r["id"] for r in rows)
probs += [f"duplicate id {k} ×{v}" for k, v in ids.items() if v > 1]
for r in rows:
    if r.get("level") not in ("country", "region", "site"): probs.append(f'{r["id"]}: level={r.get("level")}')
    if r.get("mz_status") not in ("agreed", "disputed", "uncertain", "unknown"): probs.append(f'{r["id"]}: mz_status={r.get("mz_status")}')
    if r.get("visit") not in ("visited", "hearsay", "unclear", ""): probs.append(f'{r["id"]}: visit={r.get("visit")}')
w = csv.DictWriter(open("data/places_mizutani.tsv", "w", encoding="utf-8", newline=""), COLS, delimiter="\t", lineterminator="\n", extrasaction="ignore")
w.writeheader(); w.writerows(rows)
c = collections.Counter((r.get("level"), r.get("mz_status")) for r in rows)
print(len(rows), "rows;", dict(sorted(c.items(), key=str)))
print("countries per juan:", dict(sorted(collections.Counter(int(r["juan"]) for r in rows if r.get("level") == "country" and r["juan"].isdigit()).items())))
print("\n".join(probs[:60]) or "no problems")
