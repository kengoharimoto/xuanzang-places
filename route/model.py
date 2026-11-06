#!/usr/bin/env python3
"""Test Xuanzang's distances and bearings against Mizutani's identifications.

Usage (from xuanzang-places/): python3 -I route/model.py  -> route/segment_tests.tsv, route/li_calibration.txt
1. Calibration: segments of >= 100 li whose two ends are 'agreed' in Mizutani and located to site/town precision
   (data/coords.tsv). km_per_li = straight-line km / li (li = midpoint of the stated range). Single-leg segments only.
   The ratio absorbs road sinuosity, so it is an *effective* li, shorter than the Tang li (Mizutani: c. 440 m).
2. Every segment with li and both ends located gets: predicted km (median ratio × li), observed km, log ratio,
   computed bearing vs stated bearing, and flags: DIST (outside the calibration's 10–90% band) and BEARING (> 50°
   off, single-leg only).
"""
import csv, math, statistics as st
rd = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
C = {r["id"]: r for r in rd("data/coords.tsv")}
M = {r["id"]: r for r in rd("data/places_mizutani.tsv")}
DEG = {"北":0,"東北":45,"東":90,"東南":135,"南":180,"西南":225,"西":270,"西北":315}
def ll(i):
    c = C.get(i, {})
    try: return float(c["lat"]), float(c["lon"]), c.get("precision", "")
    except (KeyError, ValueError): return None
def hav(a, b):
    R = 6371; p1, p2 = math.radians(a[0]), math.radians(b[0]); dl = math.radians(b[1]-a[1]); dp = p2-p1
    return 2*R*math.asin(math.sqrt(math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2))
def brg(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0]); dl = math.radians(b[1]-a[1])
    return (math.degrees(math.atan2(math.sin(dl)*math.cos(p2), math.cos(p1)*math.sin(p2)-math.sin(p1)*math.cos(p2)*math.cos(dl))) + 360) % 360
segs = rd("route/segments.tsv")
rows = []
for s in segs:
    if not s["li_lo"] or not s["from_id"]: continue
    a, b = ll(s["from_id"]), ll(s["id"])
    if not a or not b: continue
    li = (int(s["li_lo"]) + int(s["li_hi"])) / 2
    km = hav(a, b)
    legs = s["bearing"].split("+")
    rows.append(dict(id=s["id"], name_zh=s["name_zh"], from_id=s["from_id"], from_name=M.get(s["from_id"], {}).get("name_zh", ""),
        legs=s["legs"], li=li, km=round(km, 1), km_per_li=round(km/li, 3) if li else "",
        stated=s["bearing"], computed=round(brg(a, b)), single=len(legs) == 1,
        prec=f'{a[2]}/{b[2]}', status=f'{M.get(s["from_id"],{}).get("mz_status","")}/{s["mz_status"]}', visit=s["visit"]))
cal = [r for r in rows if r["li"] >= 100 and r["single"] and r["status"] == "agreed/agreed"
       and all(p in ("site", "town") for p in r["prec"].split("/"))]
ratios = sorted(r["km_per_li"] for r in cal)
q = lambda p: ratios[min(len(ratios)-1, int(p*len(ratios)))]
med, lo, hi = st.median(ratios), q(0.1), q(0.9)
for r in rows:
    r["pred_km"] = round(med * r["li"], 1)
    r["log_ratio"] = round(math.log(r["km"] / r["pred_km"]), 2) if r["km"] > 0 else ""
    flags = []
    if r["li"] >= 30 and r["km_per_li"] != "" and not (lo <= r["km_per_li"] <= hi): flags.append("DIST")
    if r["single"] and r["stated"] in DEG and r["km"] > 5:
        d = abs((r["computed"] - DEG[r["stated"]] + 180) % 360 - 180); r["bearing_off"] = round(d)
        if d > 50: flags.append("BEARING")
    else: r["bearing_off"] = ""
    r["calib"] = "yes" if r in cal else ""
    r["flags"] = ";".join(flags)
cols = ["id","name_zh","from_id","from_name","legs","li","km","km_per_li","pred_km","log_ratio","stated","computed","bearing_off","flags","calib","status","prec","visit"]
w = csv.DictWriter(open("route/segment_tests.tsv", "w", encoding="utf-8", newline=""), cols, delimiter="\t", lineterminator="\n", extrasaction="ignore")
w.writeheader(); w.writerows(rows)
# by region: Central Asia (juan 1, 12) vs India
def grp(r): return "Central Asia/Afghanistan (juan 1, 12)" if r["id"][:2] in ("01", "12") else "India (juan 2-11)"
txt = [f"Segments tested: {len(rows)}; calibration segments: {len(cal)}",
       f"Effective li (straight-line km per li), calibration: median {med:.3f} km, 10% {lo:.3f}, 90% {hi:.3f}"]
for g in sorted({grp(r) for r in cal}):
    rr = [r["km_per_li"] for r in cal if grp(r) == g]
    txt.append(f"  {g}: n={len(rr)}, median {st.median(rr):.3f} km/li")
vis = [r["km_per_li"] for r in cal if r["visit"] == "visited"]; hs = [r["km_per_li"] for r in cal if r["visit"] == "hearsay"]
if vis: txt.append(f"  visited destinations: n={len(vis)}, median {st.median(vis):.3f}")
if hs: txt.append(f"  hearsay destinations: n={len(hs)}, median {st.median(hs):.3f}")
txt.append(f"Flagged: DIST {sum('DIST' in r['flags'] for r in rows)}, BEARING {sum('BEARING' in r['flags'] for r in rows)}")
open("route/li_calibration.txt", "w").write("\n".join(txt) + "\n"); print("\n".join(txt))
