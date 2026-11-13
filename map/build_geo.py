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

# Major rivers: HydroRIVERS v1.0, Asia (data/ref/hydrorivers/, gitignored; see scripts/hydro_rivers.py), reaches with
# at least RIV_MIN km² upstream, in three width classes by upstream area. The Asia file starts at 57.6° E.
import struct
RIV_MIN, CLASSES = 20000, (20000, 80000, 300000)
SRC_R = "data/ref/hydrorivers/HydroRIVERS_v10_as_shp/HydroRIVERS_v10_as"
f = open(SRC_R + ".dbf", "rb"); h = f.read(32)
n, hl, rl = struct.unpack("<IHH", h[4:12]); fo, off = {}, 1
while (d := f.read(32))[0] != 0x0D:
    fo[d[:11].split(b"\0")[0].decode()] = (off, d[16]); off += d[16]
f.seek(hl); o, ln = fo["UPLAND_SKM"]
upland = [float(f.read(rl)[o:o + ln]) for _ in range(n)]
s = open(SRC_R + ".shp", "rb"); s.seek(100)
riv = [[] for _ in CLASSES]
for i in range(n):
    _, clen = struct.unpack(">ii", s.read(8)); body = s.read(clen * 2)
    if upland[i] < RIV_MIN: continue
    st, xmin, ymin, xmax, ymax, nparts, npts = struct.unpack("<i4d2i", body[:44])
    if xmax < BOX[0] or xmin > BOX[2] or ymax < BOX[1] or ymin > BOX[3]: continue
    pts = struct.unpack("<%dd" % (2 * npts), body[44 + 4 * nparts:44 + 4 * nparts + 16 * npts])
    riv[sum(upland[i] >= c for c in CLASSES) - 1].append([(round(pts[2 * k], 3), round(pts[2 * k + 1], 3)) for k in range(npts)])
def chain(lines):   # join reaches end to start where the river runs on in the same class, then thin
    starts = {}
    for j, l in enumerate(lines): starts.setdefault(l[0], []).append(j)
    ends = {}
    for j, l in enumerate(lines): ends.setdefault(l[-1], []).append(j)
    nxt = {j: starts[l[-1]][0] for j, l in enumerate(lines) if len(starts.get(l[-1], [])) == 1 and len(ends[l[-1]]) == 1}
    heads = set(range(len(lines))) - set(nxt.values()); res = []
    for j in heads:
        line = list(lines[j])
        while j in nxt: j = nxt[j]; line += lines[j][1:]
        keep = [line[0]]
        for p in line[1:-1]:
            if abs(p[0] - keep[-1][0]) + abs(p[1] - keep[-1][1]) >= 0.05: keep.append(p)
        keep.append(line[-1])
        res.append([[round(x, 2), round(y, 2)] for x, y in keep])
    return res
out["rivers"] = [chain(r) for r in riv]
json.dump(out, open("map/geo_small.json", "w"), separators=(",", ":"))
print("rivers", [len(r) for r in riv], os.path.getsize("map/geo_small.json"))
