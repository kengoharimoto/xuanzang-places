#!/usr/bin/env python3
"""Does Xuanzang's li vary by region, and does a regional scale explain the Deccan?

Usage (from xuanzang-places/): python3 -I route/li_regions.py  -> route/li_regions.tsv, route/li_schemes.tsv
1. For every leg of >= 100 li between located places (route/segment_tests.tsv, Mizutani's points), the straight-line
   km per li, summarised by juan, by visited/hearsay destination, and by leg length.
2. For each juan and each scheme (Mizutani's points, and each authority's set as in chains_all.py), the scale that
   fits that scheme best (median km per li over the juan's legs) and the scatter left over (sd of log ratios). A
   scheme whose sites are right but whose figures are uniformly inflated or shrunk will show a deviant scale with a
   small scatter; a scheme with wrong sites shows a large scatter whatever the scale. Bearings are unaffected by the
   scale and are reported alongside.
"""
import csv, math, statistics as st, re, collections
rd = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
T = [t for t in rd("route/segment_tests.tsv") if t["km_per_li"] and float(t["li"] or 0) >= 100]
def summ(xs):
    xs = [x for x in xs if x > 0]
    if len(xs) < 3: return None
    lg = [math.log(x) for x in xs]
    return dict(n=len(xs), median_km_per_li=round(st.median(xs), 3), sd_log=round(st.pstdev(lg), 2))
rows = []
for key, f in (("juan", lambda t: t["id"][:2]), ("visit", lambda t: t["visit"] or "unclear"),
               ("leg length", lambda t: "100-499 li" if float(t["li"]) < 500 else ("500-999 li" if float(t["li"]) < 1000 else "1000+ li"))):
    g = collections.defaultdict(list)
    for t in T: g[f(t)].append(float(t["km_per_li"]))
    for k, xs in sorted(g.items()):
        s = summ(xs)
        if s: rows.append(dict(group=key, value=k, **s))
w = csv.DictWriter(open("route/li_regions.tsv", "w", encoding="utf-8", newline=""), list(rows[0]), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(rows)
for r in rows: print("\t".join(str(v) for v in r.values()))

# 2. per-scheme fitted scale and scatter, by juan
C = {r["id"]: r for r in rd("data/coords.tsv")}
segs = [s for s in rd("route/segments.tsv") if s["li_lo"] and s["from_id"]]
cands = [c for c in rd("route/candidates.tsv") if c["lat"]]
DEG = {"北": 0, "東北": 45, "東": 90, "東南": 135, "南": 180, "西南": 225, "西": 270, "西北": 315}
AUTH = ["Cunningham", "Vivien", "Beal", "Watters", "Majumdar", "Dey", "Mirchandani", "Lambrick"]
def base(i):
    try: return float(C[i]["lat"]), float(C[i]["lon"])
    except (KeyError, ValueError): return None
def hav(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0]); dl = math.radians(b[1] - a[1])
    return 2 * 6371 * math.asin(math.sqrt(math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2))
def brg(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0]); dl = math.radians(b[1] - a[1])
    return (math.degrees(math.atan2(math.sin(dl) * math.cos(p2), math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl))) + 360) % 360
byj = collections.defaultdict(list)
for s in segs:
    if float(s["li_hi"]) >= 100: byj[s["id"][:2]].append(s)
out = []
for j, L in sorted(byj.items()):
    ids = {s["id"] for s in L} | {s["from_id"] for s in L}
    schemes = {"Mizutani": {}}
    S = {r["id"]: (float(r["lat"]), float(r["lon"])) for r in rd("data/coords_study.tsv") if r["id"] in ids}
    if S: schemes["Study (proposed sites)"] = S
    for a in AUTH:
        P = {c["id"]: (float(c["lat"]), float(c["lon"])) for c in cands
             if c["id"] in ids and re.search(rf"\b{a}\b", c["proposer"]) and c["proposer"] != "Mizutani"}
        if len(P) >= 2: schemes[a] = P
    for name, P in schemes.items():
        rat, be = [], []
        for s in L:
            a, b = P.get(s["from_id"]) or base(s["from_id"]), P.get(s["id"]) or base(s["id"])
            if not a or not b or a == b: continue
            li = (float(s["li_lo"]) + float(s["li_hi"])) / 2; rat.append(hav(a, b) / li)
            if s["bearing"] in DEG: be.append(abs((brg(a, b) - DEG[s["bearing"]] + 180) % 360 - 180))
        if len(rat) < 3: continue
        out.append(dict(juan=j, scheme=name, n_legs=len(rat), fitted_km_per_li=round(st.median(rat), 3),
                        sd_log_after_fit=round(st.pstdev([math.log(x) for x in rat]), 2), mean_bearing_off=round(st.mean(be)) if be else ""))
w = csv.DictWriter(open("route/li_schemes.tsv", "w", encoding="utf-8", newline=""), list(out[0]), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(out)
print()
for r in out: print("\t".join(str(v) for v in r.values()))
