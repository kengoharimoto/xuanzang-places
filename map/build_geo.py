#!/usr/bin/env python3
"""Simplify Natural Earth 1:50m countries (from the gazetteer study's map folder) to Xuanzang's frame.
Usage (from xuanzang-places/): python3 -I map/build_geo.py  -> map/geo_small.json"""
import json, os
SRC = "../gazetteer-vedanta/map/ne_50m_admin0.geojson"
BOX = (48.0, -10.0, 112.0, 47.0)
def simp(ring, tol=0.06):
    out = []
    for x, y in ring:
        x, y = round(x, 2), round(y, 2)
        if not out or abs(x - out[-1][0]) + abs(y - out[-1][1]) >= tol: out.append([x, y])
    return out if len(out) >= 4 else None
inbox = lambda ring: any(BOX[0] <= x <= BOX[2] and BOX[1] <= y <= BOX[3] for x, y in ring)
polys = lambda g: g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
out = {"countries": []}
for f in json.load(open(SRC))["features"]:
    rings = [r for r in (simp(p[0]) for p in polys(f["geometry"]) if inbox(p[0])) if r]
    if rings: out["countries"].append({"name": f["properties"].get("NAME"), "rings": rings})
json.dump(out, open("map/geo_small.json", "w"), separators=(",", ":"))
print(os.path.getsize("map/geo_small.json"), len(out["countries"]))
