#!/usr/bin/env python3
"""The Life's (T2053) route legs as a segment file, for the route tests.

Usage (from xuanzang-places/): python3 -I route/life_segments.py  -> route/life_segments.tsv
Input: route/variants_*.tsv (`t2053_legs`, as read by the variant readers), route/segments.tsv (the Xiyu ji's legs,
for the starting place where the Life has none of its own).
Rules:
- "B N", "B N-M", "B N+", "B <N": one leg; bearing B, li N (or the range N–M).
- "(from X)": the Life starts the leg from X (resolved by FROM below); otherwise from the Xiyu ji's starting place.
- "B1 N1 + B2 N2": legs added as vectors; the net bearing is snapped to the nearest of the eight points.
- A figure without a bearing is kept for distance only. Days, yojanas, "(to X)" rows, rows with no figure and
  circumferences are left out (listed on stdout).
"""
import csv, glob, math, re
rd = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
X = {s["id"]: s for s in rd("route/segments.tsv")}
M = {r["id"]: r for r in rd("data/places_mizutani.tsv")}
FROM = {"赭時": "01.09", "颯秣建": "01.12", "瞢健": "12.06", "Tiladhaka": "08.04.01", "the Bodhi tree": "08.06.01",
        "Karṇasuvarṇa": "10.08", "Puṇḍravardhana": "10.04", "Tāmraliptī": "10.07", "Ānandapura": "11.09",
        "Surāṣṭra": "11.10", "Avaṇḍa": "11.22", "Langala": "11.19", "Lampā": "02.02"}
DEG = {"北": 0, "東北": 45, "東": 90, "東南": 135, "南": 180, "西南": 225, "西": 270, "西北": 315}
PT = {v: k for k, v in DEG.items()}
out, skipped = [], []
for f in sorted(glob.glob("route/variants_*.tsv")):
    for r in rd(f):
        l = r["t2053_legs"].strip(); i = r["id"]
        if not l or "(to " in l or re.search(r"day|yojana|周|—|數", l): skipped.append(f"{i}: {l or 'none'}"); continue
        m = re.search(r"\(from ([^),]+)", l)
        if m:
            fr = FROM.get(m.group(1).strip()) or (M[i]["parent"] if m.group(1).strip() == "the capital" else None)
            if not fr: skipped.append(f"{i}: unresolved start {m.group(1)}"); continue
        else:
            fr = X.get(i, {}).get("from_id", "")
        if not fr: skipped.append(f"{i}: no starting place"); continue
        legs = re.findall(r"([東西南北]{1,2})?\s*<?(\d+)(?:-(\d+))?\+?", re.sub(r"\(.*?\)", "", l))
        if not legs: skipped.append(f"{i}: {l}"); continue
        lo = hi = 0; dx = dy = 0; bear = None
        for b, a, c in legs:
            a = int(a); c = int(c) if c else a; lo += a; hi += c
            if b: th = math.radians(DEG[b]); dx += (a + c) / 2 * math.sin(th); dy += (a + c) / 2 * math.cos(th)
        if dx or dy:
            if len(legs) > 1: lo = hi = round(math.hypot(dx, dy))
            bear = PT[round((math.degrees(math.atan2(dx, dy)) % 360) / 45) % 8 * 45]
        out.append({"id": i, "from_id": fr, "legs": l, "li_lo": lo, "li_hi": hi, "bearing": bear or "",
                    "differs_from_xiyuji": "yes" if (X.get(i, {}).get("legs", "") != l.split(" (")[0] or m) else ""})
w = csv.DictWriter(open("route/life_segments.tsv", "w", encoding="utf-8", newline=""), list(out[0]), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(out)
print(len(out), "Life legs;", sum(1 for o in out if o["differs_from_xiyuji"]), "differ from the Xiyu ji;", len(skipped), "left out:")
print("\n".join(skipped))
