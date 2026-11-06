#!/usr/bin/env python3
"""Make country passages open with their arrival sentence ("從此…至X國。") — the convention of anchors_02-03/04-05.

Usage (from xuanzang-places/): python3 -I scripts/normalize_anchors.py data/text/anchors_<range>.tsv   (rewrites it)
For each `segment` row of a country/region (master `level`), if the sentence immediately before its anchor in
t2087_cb_joined.txt contains 至 and the first two characters of the country name, the anchor is moved to the start of
that sentence. The first country of a juan is left alone when the preceding text is the juan heading.
"""
import csv, re, sys
T = re.sub(r"\[T51:\d+[abc]\]", "", open("data/ref/t2087_cb_joined.txt", encoding="utf-8").read().replace("\n", ""))
M = {r["id"]: r for r in csv.DictReader(open("data/places_mizutani.tsv", encoding="utf-8"), delimiter="\t")}
f = sys.argv[1]; rows = list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t")); moved = 0
for r in rows:
    if r["mode"] != "segment" or M.get(r["id"], {}).get("level") not in ("country", "region"): continue
    a = re.sub(r"\s+", "", r["anchor"]); i = T.find(a)
    if i < 0: continue
    j = T.rfind("。", 0, i - 1) + 1          # start of the preceding sentence
    prev = T[j:i]
    name = re.sub(r"[（(].*", "", M[r["id"]]["name_zh"])[:2]
    if "至" in prev and name in prev and "卷第" not in prev and len(prev) < 120:
        r["anchor"] = prev[:min(20, len(prev))]; moved += 1
        r["note"] = (r.get("note", "") + "; anchor moved to the arrival sentence").strip("; ")
w = csv.DictWriter(open(f, "w", encoding="utf-8", newline=""), rows[0].keys(), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(rows); print(f, "moved", moved)
