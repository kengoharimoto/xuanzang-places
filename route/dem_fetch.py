#!/usr/bin/env python3
"""Fetch Copernicus GLO-90 DEM tiles (AWS open data) around each tested leg, keep the 1/4 overview (300x300 per 1° tile,
about 360 m) as int16 .npy in data/ref/dem/ (gitignored), delete the full tile. Missing tiles (sea) are recorded as such.
Usage (from xuanzang-places/): PYTHONPATH=<dir with tifffile, imagecodecs> python3 route/dem_fetch.py"""
import csv, math, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
import numpy as np, tifffile
D = "data/ref/dem"; os.makedirs(D, exist_ok=True)
rd = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
C = {r["id"]: (float(r["lat"]), float(r["lon"])) for r in rd("data/coords.tsv") if r.get("lat")}
T = {r["id"]: r for r in rd("route/segment_tests.tsv")}
tiles = set()
for r in rd("route/li_terrain.tsv"):
    a, b = C[T[r["id"]]["from_id"]], C[r["id"]]
    pad = max(0.25, 0.3 * max(abs(a[0] - b[0]), abs(a[1] - b[1])))
    for la in range(math.floor(min(a[0], b[0]) - pad), math.floor(max(a[0], b[0]) + pad) + 1):
        for lo in range(math.floor(min(a[1], b[1]) - pad), math.floor(max(a[1], b[1]) + pad) + 1): tiles.add((la, lo))
def name(la, lo): return f"Copernicus_DSM_COG_30_{'N' if la >= 0 else 'S'}{abs(la):02d}_00_{'E' if lo >= 0 else 'W'}{abs(lo):03d}_00_DEM"
def get(t):
    la, lo = t; n = name(la, lo); out = f"{D}/{la}_{lo}.npy"
    if os.path.exists(out) or os.path.exists(out + ".sea"): return
    tif = f"{D}/{n}.tif"
    rc = subprocess.run(["curl", "-s", "-f", "-m", "300", "--retry", "3", "-o", tif, f"https://copernicus-dem-90m.s3.amazonaws.com/{n}/{n}.tif"]).returncode
    if rc == 22: open(out + ".sea", "w").close(); return
    if rc: print("fail", t, rc); return
    with tifffile.TiffFile(tif) as f:
        p = f.pages[2] if len(f.pages) > 2 else f.pages[0]
        a = p.asarray()
    a = np.asarray(a, dtype=np.float32)
    if a.shape[1] != 300: a = np.repeat(a, 300 // a.shape[1], axis=1) if 300 % a.shape[1] == 0 else a   # high-latitude tiles are narrower
    np.save(out, a.astype(np.int16)); os.remove(tif)
with ThreadPoolExecutor(4) as ex: list(ex.map(get, sorted(tiles)))
print(len(tiles), "tiles;", sum(f.endswith(".npy") for f in os.listdir(D)), "land", sum(f.endswith(".sea") for f in os.listdir(D)), "sea")
