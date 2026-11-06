#!/usr/bin/env python3
"""Score whole alternative routes (schemes) for a stretch of the itinerary, each leg measured between the scheme's own
sites, so that interdependent identifications (e.g. Mirchandani's Baluchistan route) are tested on their own terms.

Usage (from xuanzang-places/): python3 -I route/chains.py  -> route/chain_scores.tsv
Inputs: route/segments.tsv (legs, after segment_overrides), route/candidates.tsv (coordinates, matched by id and a
substring of the candidate name), route/segment_tests.tsv (li calibration). z and bearing error as in candidates.py.
"""
import csv, math, statistics as st
rd = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
segs = {s["id"]: s for s in rd("route/segments.tsv") if s["li_lo"] and s["from_id"]}
cands = rd("route/candidates.tsv")
cal = [float(t["km_per_li"]) for t in rd("route/segment_tests.tsv") if t["calib"] == "yes"]
med = st.median(cal); sig = st.pstdev([math.log(x / med) for x in cal])
DEG = {"北": 0, "東北": 45, "東": 90, "東南": 135, "南": 180, "西南": 225, "西": 270, "西北": 315}
def pt(i, name):
    for c in cands:
        if c["id"] == i and name.lower() in c["candidate"].lower() and c["lat"]:
            return float(c["lat"]), float(c["lon"])
    raise SystemExit(f"no candidate {i} ~ {name}")
def hav(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0]); dl = math.radians(b[1] - a[1])
    return 2 * 6371 * math.asin(math.sqrt(math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2))
def brg(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0]); dl = math.radians(b[1] - a[1])
    return (math.degrees(math.atan2(math.sin(dl) * math.cos(p2), math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl))) + 360) % 360

# Sindh–Baluchistan stretch, juan 11 (Gurjara → Sindhu → … → Varṇa). Each scheme: id -> candidate-name substring.
FIX = {"11.11": "Bhinmal", "11.16": "Multan", "11.17": "Harappa"}
SCHEMES = {
    "Mizutani (study)": {"11.15": "Aror", "11.18": "Karachi", "11.19": "Lakorian", "11.21": "Hyderabad", "11.22": "Brahmanabad", "11.23": "Bannu"},
    "Mirchandani 1967": {"11.15": "Mithankot", "11.18": "Gondakahar", "11.19": "Kasarkand", "11.21": "Khuzdar", "11.22": "Gandava", "11.23": "Duki"},
    "Lambrick 1964 (with Mizutani where silent)": {"11.15": "Aror", "11.18": "Banbhore", "11.19": "Lakorian", "11.21": "Sehwan", "11.22": "Badah", "11.23": "Bannu"},
    "Cunningham (Kotesar) with Mizutani": {"11.15": "Aror", "11.18": "Kotesar", "11.19": "Lakorian", "11.21": "Hyderabad", "11.22": "Brahmanabad", "11.23": "Bannu"},
    "Mizutani, but Kasarkand for 11.19": {"11.15": "Aror", "11.18": "Karachi", "11.19": "Kasarkand", "11.21": "Hyderabad", "11.22": "Brahmanabad", "11.23": "Bannu"},
}
LEGS = ["11.15", "11.16", "11.17", "11.18", "11.19", "11.21", "11.22", "11.23"]
out = []
for name, sch in SCHEMES.items():
    P = {**{k: pt(k, v) for k, v in FIX.items()}, **{k: pt(k, v) for k, v in sch.items()}}
    zs, bs, det = [], [], []
    for i in LEGS:
        s = segs[i]; a, b = P[s["from_id"]], P[i]
        li = (float(s["li_lo"]) + float(s["li_hi"])) / 2; pred = li * med; km = hav(a, b)
        z = math.log(km / pred) / sig; be = abs((brg(a, b) - DEG[s["bearing"]] + 180) % 360 - 180) if s["bearing"] in DEG else None
        zs.append(abs(z)); bs.append(be if be is not None else 0)
        det.append(f'{s["from_id"]}→{i} {s["legs"]}: {km:.0f} km (pred {pred:.0f}), z {z:+.1f}, bearing off {be:.0f}°')
    out.append({"scheme": name, "n_legs": len(LEGS), "mean_abs_z": round(st.mean(zs), 2), "max_abs_z": round(max(zs), 2),
                "mean_bearing_off": round(st.mean(bs)), "legs_z_over_1.5": sum(1 for z in zs if z > 1.5), "detail": " | ".join(det)})
out.sort(key=lambda r: r["mean_abs_z"])
w = csv.DictWriter(open("route/chain_scores.tsv", "w", encoding="utf-8", newline=""), list(out[0]), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(out)
for r in out: print(f'{r["scheme"]:45} mean|z| {r["mean_abs_z"]:.2f}  max {r["max_abs_z"]:.2f}  bearing {r["mean_bearing_off"]}°  legs z>1.5: {r["legs_z_over_1.5"]}')
