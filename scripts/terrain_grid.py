#!/usr/bin/env python3
"""Elevation on the country-areas grid, from the open AWS terrain tiles (Terrarium encoding, zoom 5).

Usage (from xuanzang-places/): python3 -I scripts/terrain_grid.py  -> data/ref/terrain/grid.json, fine_<id>.json
Input: data/ref/terrain/z5_{x}_{y}.png, x 20-25, y 11-16, fetched from
https://s3.amazonaws.com/elevation-tiles-prod/terrarium/5/{x}/{y}.png (Mapzen/Tilezen terrain tiles: SRTM, GMTED2010,
ETOPO1 and others; open data). Also fine grids (0.01 degree, zoom-8 tiles z8_{x}_{y}.png, fetched here when
missing) over windows round the mountain-ringed countries whose rivers the coarse grid cannot route (Agni's Kaidu,
Brahmapura's Ramganga); scripts/country_areas.py takes their basins from these. Decoded here without imaging libraries (8-bit RGB PNG, no interlace);
elevation = R*256 + G + B/256 - 32768 metres. Each grid cell takes the pixel at its centre (zoom 5 is c. 4.9 km
per pixel at the equator, finer than the 0.08 degree grid). The grid and box are those of scripts/country_areas.py.
"""
import json, math, os, struct, urllib.request, zlib

RES = 0.08
BOX = (48.0, -2.0, 112.0, 47.0)
Z = 5

def png_rgb(path):
    data = open(path, "rb").read()
    assert data[:8] == b"\x89PNG\r\n\x1a\n"
    pos, idat, w = 8, b"", 0
    while pos < len(data):
        ln, typ = struct.unpack(">I4s", data[pos:pos + 8]); body = data[pos + 8:pos + 8 + ln]; pos += 12 + ln
        if typ == b"IHDR":
            w, h, depth, ctype, _, _, inter = struct.unpack(">IIBBBBB", body)
            assert depth == 8 and ctype == 2 and inter == 0, (path, depth, ctype, inter)
        elif typ == b"IDAT": idat += body
        elif typ == b"IEND": break
    raw = zlib.decompress(idat); bpp = 3; stride = w * bpp
    rows, prev, p = [], bytearray(stride), 0
    for _ in range(h):
        f = raw[p]; line = bytearray(raw[p + 1:p + 1 + stride]); p += 1 + stride
        for i in range(stride):
            a = line[i - bpp] if i >= bpp else 0; b = prev[i]; c = prev[i - bpp] if i >= bpp else 0
            if f == 1: line[i] = (line[i] + a) & 255
            elif f == 2: line[i] = (line[i] + b) & 255
            elif f == 3: line[i] = (line[i] + (a + b) // 2) & 255
            elif f == 4:
                pa, pb, pc = abs(b - c), abs(a - c), abs(a + b - 2 * c)
                line[i] = (line[i] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        rows.append(line); prev = line
    return w, rows

tiles = {}
def elev(lon, lat, z=Z):
    n = 2 ** z
    x = (lon + 180) / 360 * n
    y = (1 - math.log(math.tan(math.radians(lat)) + 1 / math.cos(math.radians(lat))) / math.pi) / 2 * n
    tx, ty = int(x), int(y)
    if (z, tx, ty) not in tiles:
        f = "data/ref/terrain/z%d_%d_%d.png" % (z, tx, ty)
        if z != Z and not os.path.exists(f):
            urllib.request.urlretrieve("https://s3.amazonaws.com/elevation-tiles-prod/terrarium/%d/%d/%d.png" % (z, tx, ty), f)
        try: tiles[(z, tx, ty)] = png_rgb(f)
        except FileNotFoundError: tiles[(z, tx, ty)] = None
    t = tiles[(z, tx, ty)]
    if not t: return None
    w, rows = t
    px = min(w - 1, int((x - tx) * w)); py = min(w - 1, int((y - ty) * w))
    r, g, b = rows[py][px * 3:px * 3 + 3]
    return round(r * 256 + g + b / 256 - 32768)

NX = int((BOX[2] - BOX[0]) / RES); NY = int((BOX[3] - BOX[1]) / RES)
grid = []
for j in range(NY):
    lat = BOX[1] + (j + 0.5) * RES
    for i in range(NX):
        e = elev(BOX[0] + (i + 0.5) * RES, lat)
        grid.append(0 if e is None else e)
json.dump(dict(res=RES, box=BOX, nx=NX, ny=NY, elev=grid), open("data/ref/terrain/grid.json", "w"), separators=(",", ":"))
print(NX, NY, "cells; max", max(grid), "min", min(grid))

# fine grids: window (lon0, lat0, lon1, lat1) round the capital, wide enough for 1.6 times the target radius
FRES, FZ = 0.01, 8
FINE = {"01.05": (84.6, 40.6, 88.6, 43.6), "04.11": (76.6, 27.4, 82.0, 32.4)}
for cid, (x0, y0, x1, y1) in FINE.items():
    nx, ny = round((x1 - x0) / FRES), round((y1 - y0) / FRES)
    g = [elev(x0 + (i + 0.5) * FRES, y0 + (j + 0.5) * FRES, FZ) for j in range(ny) for i in range(nx)]
    json.dump(dict(res=FRES, box=(x0, y0, x1, y1), nx=nx, ny=ny, elev=[0 if e is None else e for e in g]),
              open("data/ref/terrain/fine_%s.json" % cid.replace(".", "_"), "w"), separators=(",", ":"))
    print(cid, nx, ny, "fine cells")
