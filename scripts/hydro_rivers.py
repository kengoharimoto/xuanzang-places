#!/usr/bin/env python3
"""River courses for burning into the fine terrain grids (scripts/country_areas.py, fine_basin).

Usage (from xuanzang-places/): python3 -I scripts/hydro_rivers.py
Input: HydroRIVERS v1.0, Asia (Lehner & Grill 2013, HydroSHEDS; free licence),
  https://data.hydrosheds.org/file/HydroRIVERS/HydroRIVERS_v10_as_shp.zip, unzipped in data/ref/hydrorivers/ (gitignored).
Output: data/ref/hydrorivers/rivers_fine.json: for each fine window of scripts/terrain_grid.py, the river reaches inside
  it whose upstream area is at least MIN_UPLAND km² (as lon/lat lines, with each reach's upstream area). Natural Earth's 1:10m centrelines lack many
  of these rivers (the Kabul river among them), so they cannot serve.
The shapefile and its dBASE table are read directly (polyline records, type 3), without GIS libraries.
"""
import json, struct

MIN_UPLAND = 1000
SRC = "data/ref/hydrorivers/HydroRIVERS_v10_as_shp/HydroRIVERS_v10_as"
FINE = {"01.05": (84.6, 40.6, 88.6, 43.6), "01.10": (68.5, 38.2, 75.1, 43.3), "01.38": (66.2, 32.5, 72.3, 37.5),
        "02.02": (69.3, 33.9, 71.1, 35.4), "02.03": (69.3, 33.4, 71.6, 35.4), "03.06": (72.1, 31.7, 77.5, 36.3),
        "04.04": (75.2, 30.5, 79.1, 33.8), "04.11": (76.6, 27.4, 82.0, 32.4), "10.12": (79.1, 18.4, 85.3, 24.2)}
X0 = min(b[0] for b in FINE.values()); Y0 = min(b[1] for b in FINE.values())
X1 = max(b[2] for b in FINE.values()); Y1 = max(b[3] for b in FINE.values())

# dBASE: the upstream area of each record
f = open(SRC + ".dbf", "rb"); h = f.read(32)
n, hl, rl = struct.unpack("<IHH", h[4:12])
fields, off = [], 1
while True:
    d = f.read(32)
    if d[0] == 0x0D: break
    name = d[:11].split(b"\0")[0].decode(); ln = d[16]
    fields.append((name, off, ln)); off += ln
fo = {nm: (o, ln) for nm, o, ln in fields}
f.seek(hl)
o, ln = fo["UPLAND_SKM"]
upland = []
for _ in range(n):
    rec = f.read(rl)
    upland.append(float(rec[o:o + ln]))

# shapefile: polylines
s = open(SRC + ".shp", "rb"); s.seek(100)
out = {cid: [] for cid in FINE}; ups = {cid: [] for cid in FINE}
for i in range(n):
    hdr = s.read(8)
    if len(hdr) < 8: break
    _, clen = struct.unpack(">ii", hdr)
    body = s.read(clen * 2)
    if upland[i] < MIN_UPLAND: continue
    st, xmin, ymin, xmax, ymax, nparts, npts = struct.unpack("<i4d2i", body[:44])
    if st != 3 or xmax < X0 or xmin > X1 or ymax < Y0 or ymin > Y1: continue
    parts = list(struct.unpack("<%di" % nparts, body[44:44 + 4 * nparts]))
    pts = struct.unpack("<%dd" % (2 * npts), body[44 + 4 * nparts:44 + 4 * nparts + 16 * npts])
    xy = [(round(pts[2 * k], 4), round(pts[2 * k + 1], 4)) for k in range(npts)]
    lines = [xy[a:b] for a, b in zip(parts, parts[1:] + [npts])]
    for cid, (a0, b0, a1, b1) in FINE.items():
        if xmax < a0 or xmin > a1 or ymax < b0 or ymin > b1: continue
        out[cid].extend(lines); ups[cid].extend([round(upland[i])] * len(lines))
json.dump(dict(source="HydroRIVERS v1.0 (Asia)", min_upland_km2=MIN_UPLAND, lines=out, upland_km2=ups),
          open("data/ref/hydrorivers/rivers_fine.json", "w"), separators=(",", ":"))
print({cid: len(v) for cid, v in out.items()})
