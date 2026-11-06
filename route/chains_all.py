#!/usr/bin/env python3
"""Whole-route test for every juan: each authority's set of sites against Mizutani's, and the best-fitting
combination of candidates.

Usage (from xuanzang-places/): python3 -I route/chains_all.py [route/life_segments.tsv]
  (with the Life's legs from route/life_segments.py, outputs carry the suffix _life)
  -> route/chain_scores_all.tsv  one row per (juan, scheme): legs, mean |z|, mean bearing error, legs |z| > 1.5
  -> route/chain_best.tsv        places where the best-fitting combination picks a candidate other than Mizutani's

A scheme takes the authority's candidate (route/candidates.tsv, matched on the proposer field) wherever there is one,
and Mizutani's point (data/coords.tsv) elsewhere. Every leg (route/segments.tsv) whose destination lies in the juan is
measured between the scheme's own points. An authority is scored only where it differs from Mizutani at two or more
places in the juan. z and bearing error as in candidates.py; the score adds |z| and bearing error / 45 per leg.
The best-fitting combination is found by coordinate descent from Mizutani's points (each place in turn takes the
candidate that lowers the juan's total, until nothing changes). It shows where the figures pull towards a rival site;
it is not a proposal by itself, since the figures are only one kind of evidence.
"""
import csv, math, statistics as st, re, collections, sys
SEG = sys.argv[1] if len(sys.argv) > 1 else "route/segments.tsv"   # route/life_segments.tsv: the Life's legs
SUF = "_life" if "life" in SEG else ""
rd = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
C = {r["id"]: r for r in rd("data/coords.tsv")}
segs = [s for s in rd(SEG) if s["li_lo"] and s["from_id"]]
cands = [c for c in rd("route/candidates.tsv") if c["lat"]]
cal = [float(t["km_per_li"]) for t in rd("route/segment_tests.tsv") if t["calib"] == "yes"]
med = st.median(cal); sig = st.pstdev([math.log(x / med) for x in cal])
DEG = {"北": 0, "東北": 45, "東": 90, "東南": 135, "南": 180, "西南": 225, "西": 270, "西北": 315}
AUTH = ["Cunningham", "Vivien", "Beal", "Watters", "Majumdar", "Dey", "Smith", "Stein", "Mirchandani", "Lambrick", "Fergusson"]

def hav(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0]); dl = math.radians(b[1] - a[1])
    return 2 * 6371 * math.asin(math.sqrt(math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2))
def brg(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0]); dl = math.radians(b[1] - a[1])
    return (math.degrees(math.atan2(math.sin(dl) * math.cos(p2), math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl))) + 360) % 360
def base(i):
    try: return float(C[i]["lat"]), float(C[i]["lon"])
    except (KeyError, ValueError): return None
def leg(s, P):
    a, b = P.get(s["from_id"]) or base(s["from_id"]), P.get(s["id"]) or base(s["id"])
    if not a or not b or a == b: return None
    li = (float(s["li_lo"]) + float(s["li_hi"])) / 2; z = math.log(max(hav(a, b), 1) / (li * med)) / sig
    be = abs((brg(a, b) - DEG[s["bearing"]] + 180) % 360 - 180) if s["bearing"] in DEG else 0
    return z, be
def score(legs_, P):
    r = [x for x in (leg(s, P) for s in legs_) if x]
    return r, sum(abs(z) + be / 45 for z, be in r)

byjuan = collections.defaultdict(list)
for s in segs: byjuan[s["id"][:2]].append(s)
opts = collections.defaultdict(list)            # id -> [(candidate, proposer, (lat, lon))]
for c in cands: opts[c["id"]].append((c["candidate"], c["proposer"], (float(c["lat"]), float(c["lon"]))))

rows, best = [], []
for j, L in sorted(byjuan.items()):
    ids = sorted({s["id"] for s in L} | {s["from_id"] for s in L if s["from_id"][:2] == j})
    schemes = {"Mizutani": {}}
    for a in AUTH:
        P = {}
        for i in ids:
            for name, prop, pt in opts.get(i, []):
                if re.search(rf"\b{a}\b", prop) and prop != "Mizutani" and pt != base(i): P[i] = pt; break
        if len(P) >= 2: schemes[a] = P
    for name, P in schemes.items():
        r, tot = score(L, P)
        if not r: continue
        rows.append(dict(juan=j, scheme=name, places_changed=len(P), n_legs=len(r), mean_abs_z=round(st.mean(abs(z) for z, _ in r), 2),
                         mean_bearing_off=round(st.mean(b for _, b in r)), legs_z_over_1_5=sum(1 for z, _ in r if abs(z) > 1.5),
                         total=round(tot, 1)))
    # coordinate descent from Mizutani's points over all candidates of the juan's places
    P = {}; _, cur = score(L, P); changed = True
    while changed:
        changed = False
        for i in ids:
            for name, prop, pt in opts.get(i, []):
                Q = dict(P); Q[i] = pt
                _, t = score(L, Q)
                if t < cur - 0.3: P, cur, changed = Q, t, True
    r, _ = score(L, P)
    if not r: continue   # no measurable leg in this juan
    mz_r, mz_tot = score(L, {})
    rows.append(dict(juan=j, scheme="best-fitting combination", places_changed=len(P), n_legs=len(r),
                     mean_abs_z=round(st.mean(abs(z) for z, _ in r), 2), mean_bearing_off=round(st.mean(b for _, b in r)),
                     legs_z_over_1_5=sum(1 for z, _ in r if abs(z) > 1.5), total=round(cur, 1)))
    for i, pt in P.items():
        if pt == base(i): continue
        name, prop = next((n, p) for n, p, q in opts[i] if q == pt)
        mz = next((n for n, p, q in opts[i] if p == "Mizutani"), C.get(i, {}).get("modern_name", ""))
        best.append(dict(juan=j, id=i, mizutani=mz, best_fit=name, proposer=prop))

w = csv.DictWriter(open(f"route/chain_scores_all{SUF}.tsv", "w", encoding="utf-8", newline=""), list(rows[0]), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(rows)
w = csv.DictWriter(open(f"route/chain_best{SUF}.tsv", "w", encoding="utf-8", newline=""), list(best[0]), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(best)
for r in rows: print("\t".join(str(v) for v in r.values()))
print(len(best), "places where the best-fitting combination departs from Mizutani")
