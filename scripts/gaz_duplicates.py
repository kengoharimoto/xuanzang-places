#!/usr/bin/env python3
"""Find gazetteer hits that are the same passage in two scans of one volume (same place and year, different Internet
Archive identifier, contexts alike: difflib ratio > 0.6 on the first 600 letters).
Usage (from xuanzang-places/): python3 -I scripts/gaz_duplicates.py -> data/gaz_duplicates.tsv (hit, same_as, place,
year, ratio); scripts/build_places.py counts each passage once (the lower hit number stands for the pair)."""
import csv, collections, difflib, re
HK = lambda h: (not h.isdigit(), int(h) if h.isdigit() else 0, h)   # hit ids: numbers, then B003 etc.
hits = list(csv.DictReader(open("data/gaz_hits.tsv", encoding="utf-8"), delimiter="\t"))
norm = lambda s: re.sub(r"[^a-z]", "", s.lower())[:600]
by = collections.defaultdict(list)
for h in hits: by[(h["place"], h["year"])].append(h)
parent = {}
def find(x):
    while parent.get(x, x) != x: x = parent[x]
    return x
rows = []
for (pl, yr), L in by.items():
    if len({h["identifier"] for h in L}) < 2: continue
    for i, a in enumerate(L):
        for b in L[i + 1:]:
            if a["identifier"] == b["identifier"]: continue
            r = difflib.SequenceMatcher(None, norm(a["context"]), norm(b["context"])).ratio()
            if r > 0.6:
                ra, rb = find(a["hit"]), find(b["hit"])
                if ra != rb:
                    lo, hi = sorted((ra, rb), key=HK); parent[hi] = lo
                rows.append((b["hit"], a["hit"], pl, yr, round(r, 2)))
w = csv.writer(open("data/gaz_duplicates.tsv", "w", encoding="utf-8", newline=""), delimiter="\t", lineterminator="\n")
w.writerow(["hit", "same_as", "place", "year", "ratio"])
for h in sorted({x["hit"] for x in hits}, key=HK):
    if find(h) != h:
        p = next(r for r in rows if h in (r[0], r[1]))
        w.writerow([h, find(h), p[2], p[3], p[4]])
print(sum(1 for h in hits if find(h["hit"]) != h["hit"]), "hits are second scans of another hit")
