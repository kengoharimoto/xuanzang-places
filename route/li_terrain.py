#!/usr/bin/env python3
"""Does Xuanzang's li behave like a measure of time? Test: km per li against the terrain of each leg.

Usage (from xuanzang-places/): python3 -I route/li_terrain.py  -> route/li_terrain.tsv (elevation cache in route/elev_cache.json)
If li were days' marches converted at a fixed rate, rough legs (slow) should give fewer km per li than open legs.
Legs: route/segment_tests.tsv, ≥100 li, both ends at town/site/district precision (the same points as §1, §8).
Terrain, two independent measures:
  text   the leg's own route sentence (segments.tsv t_route): rough = 山 嶺 谷 磧 沙 雪 林 險 棧 崖 峻 踰 越 渉; open = 平 川 (平川) with none of those
  relief SRTM 90 m (api.opentopodata.org) sampled at 40 points on the straight line: summed |rise| per km, and the highest point
"""
import csv, json, math, os, re, statistics, time, urllib.request
rd = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
T = rd("route/segment_tests.tsv"); S = {r["id"]: r for r in rd("route/segments.tsv")}
C = {r["id"]: (float(r["lat"]), float(r["lon"])) for r in rd("data/coords.tsv") if r.get("lat")}
CACHE = "route/elev_cache.json"; cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
ROUGH = re.compile(r"[山嶺谷磧沙雪林險棧崖峻踰越渉涉]")
def interp(a, b, n=40): return [(a[0] + (b[0] - a[0]) * k / (n - 1), a[1] + (b[1] - a[1]) * k / (n - 1)) for k in range(n)]
def elev(pts):
    need = [p for p in pts if f"{p[0]:.4f},{p[1]:.4f}" not in cache]
    for i in range(0, len(need), 100):
        q = "|".join(f"{a:.4f},{b:.4f}" for a, b in need[i:i + 100])
        for _ in range(5):
            try:
                js = json.load(urllib.request.urlopen(f"https://api.opentopodata.org/v1/srtm90m?locations={q}", timeout=60)); break
            except Exception: time.sleep(5)
        for p, r in zip(need[i:i + 100], js["results"]): cache[f"{p[0]:.4f},{p[1]:.4f}"] = r["elevation"]
        time.sleep(1.1)
    json.dump(cache, open(CACHE, "w"))
    return [cache[f"{a:.4f},{b:.4f}"] for a, b in pts]
out = []
for r in T:
    if float(r["li"] or 0) < 100 or r["visit"] == "hearsay": continue
    if any(p == "country" for p in r["prec"].split("/")): continue
    a, b = C.get(r["from_id"]), C.get(r["id"])
    if not a or not b: continue
    km = float(r["km"]); pts = interp(a, b); e = [x if x is not None else 0 for x in elev(pts)]
    rise = sum(abs(e[k + 1] - e[k]) for k in range(len(e) - 1))
    txt = S.get(r["id"], {}).get("t_route", "")
    tt = "rough" if ROUGH.search(txt) else ("open" if "平" in txt or "川" in txt else "unstated")
    out.append({"id": r["id"], "name_zh": r["name_zh"], "juan": r["id"][:2], "li": r["li"], "km": km, "km_per_li": r["km_per_li"],
                "text_terrain": tt, "relief_m_per_km": round(rise / km, 1), "max_elev": max(e), "t_route": txt[:60]})
w = csv.DictWriter(open("route/li_terrain.tsv", "w", encoding="utf-8", newline=""), list(out[0]), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(out)
print(len(out), "legs")
