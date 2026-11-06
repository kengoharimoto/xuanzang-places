#!/usr/bin/env python3
"""Score candidate sites for disputed places against Xuanzang's distances and bearings.

Usage (from xuanzang-places/): python3 -I route/candidates.py  -> route/candidate_scores.tsv
Input: route/candidates.tsv (id, candidate, proposer, lat, lon, precision, note) — one row per candidate site,
including Mizutani's own (proposer = Mizutani). For each candidate, every route segment touching the place
(incoming: the place from its predecessor; outgoing: places whose from_id is this place) is recomputed with the
candidate's coordinates, using the effective li from route/model.py's calibration (route/li_calibration.txt).
Per segment: z = log(observed km / predicted km) / sigma (sigma = sd of log ratios in the calibration set);
bearing error in degrees (single-leg segments). Score = mean |z| and mean bearing error; lower is better.
Neighbours must themselves be located (data/coords.tsv); segments to neighbours with only district/country precision
are kept but marked.
"""
import csv, math, statistics as st, re
rd = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
C = {r["id"]: r for r in rd("data/coords.tsv")}
segs = [s for s in rd("route/segments.tsv") if s["li_lo"] and s["from_id"]]
tests = rd("route/segment_tests.tsv")
cal = [float(t["km_per_li"]) for t in tests if t["calib"] == "yes"]
med = st.median(cal); sig = st.pstdev([math.log(x/med) for x in cal])
DEG = {"北":0,"東北":45,"東":90,"東南":135,"南":180,"西南":225,"西":270,"西北":315}
def ll(i):
    try: return float(C[i]["lat"]), float(C[i]["lon"]), C[i]["precision"]
    except (KeyError, ValueError): return None
def hav(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0]); dl = math.radians(b[1]-a[1]); dp = p2-p1
    return 2*6371*math.asin(math.sqrt(math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2))
def brg(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0]); dl = math.radians(b[1]-a[1])
    return (math.degrees(math.atan2(math.sin(dl)*math.cos(p2), math.cos(p1)*math.sin(p2)-math.sin(p1)*math.cos(p2)*math.cos(dl)))+360) % 360
out = []
for c in rd("route/candidates.tsv"):
    try: here = (float(c["lat"]), float(c["lon"]))
    except ValueError: continue
    zs, bs, det, zp, bp = [], [], [], [], []
    for s in segs:
        if s["id"] == c["id"]: other, frm_is_other = s["from_id"], True
        elif s["from_id"] == c["id"]: other, frm_is_other = s["id"], False
        else: continue
        o = ll(other)
        if not o: continue
        a, b = (o[:2], here) if frm_is_other else (here, o[:2])
        li = (int(s["li_lo"]) + int(s["li_hi"])) / 2
        km = hav(a, b); z = math.log(max(km, 0.5) / (med * li)) / sig
        zs.append(abs(z))
        if o[2] in ("site", "town"): zp.append(abs(z))
        part = f'{"←" if frm_is_other else "→"}{other} {s["legs"]}: {km:.0f} km (pred {med*li:.0f}), z {z:+.1f}'
        legs = s["bearing"].split("+")
        if len(legs) == 1 and legs[0] in DEG and km > 3:
            d = abs((brg(a, b) - DEG[legs[0]] + 180) % 360 - 180); bs.append(d)
            if o[2] in ("site", "town"): bp.append(d)
            part += f', bearing off {d:.0f}°'
        if o[2] in ("district", "country"): part += " [neighbour imprecise]"
        det.append(part)
    out.append({**{k: c[k] for k in ("id", "candidate", "proposer")}, "n_segments": len(zs),
                "mean_abs_z": round(st.mean(zs), 2) if zs else "", "mean_bearing_off": round(st.mean(bs)) if bs else "",
                "n_precise": len(zp), "z_precise": round(st.mean(zp), 2) if zp else "", "bearing_precise": round(st.mean(bp)) if bp else "",
                "detail": " | ".join(det), "note": c.get("note", "")})
w = csv.DictWriter(open("route/candidate_scores.tsv", "w", encoding="utf-8", newline=""), out[0].keys(), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(sorted(out, key=lambda r: (r["id"], r["mean_abs_z"] if r["mean_abs_z"] != "" else 99)))
print(len(out), "candidates scored; effective li", round(med, 3), "km; sigma", round(sig, 2))
