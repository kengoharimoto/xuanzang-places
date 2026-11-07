#!/usr/bin/env python3
"""Least-cost walking routes for the tested legs: is the li closer to road distance or to travel time?

Usage (from xuanzang-places/): python3 route/li_paths.py (numpy, scipy)  -> route/li_paths.tsv
Needs: data/ref/dem/<lat>_<lon>.npy (route/dem_fetch.py: Copernicus GLO-90, 1/4 overview, about 360 m), route/li_terrain.tsv.

For each leg of li_terrain.tsv (92 legs of 100 li or more, located at town/site/district precision, not hearsay), the
fastest walking route between Mizutani's two points over the DEM, with Tobler's hiking function as the cost:
  speed = 6 exp(-3.5 |slope + 0.05|) km/h  (5.0 km/h on the flat; uphill and steep downhill slower)
on an 8-neighbour grid (coarsened where the leg's box is large, to keep under about 1.2 million cells). Sea (no tile) is
impassable; rivers, forest, snow and stops are not modelled. Output per leg: the route's length (path_km), its walking
time (hours), the detour factor (path_km / straight km), and the li per path km and per hour.
If the li measures distance, li / path_km should be steady and should not depend on relief; if it measures time,
li / hours should be steadier than li / path_km.
"""
import csv, math, os, sys
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import dijkstra
D = "data/ref/dem"; N = 300   # cells per degree in the stored overview
rd = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
C = {r["id"]: (float(r["lat"]), float(r["lon"])) for r in rd("data/coords.tsv") if r.get("lat")}
T = {r["id"]: r for r in rd("route/segment_tests.tsv")}
cache = {}
def tile(la, lo):
    k = (la, lo)
    if k not in cache:
        f = f"{D}/{la}_{lo}.npy"
        cache[k] = np.load(f).astype(np.float32) if os.path.exists(f) else None
    return cache[k]
def mosaic(la0, la1, lo0, lo1):
    """Grid for lat [la0, la1+1), lon [lo0, lo1+1) in whole degrees; row 0 = north. NaN = no data (sea)."""
    H, W = (la1 - la0 + 1) * N, (lo1 - lo0 + 1) * N
    g = np.full((H, W), np.nan, np.float32)
    for la in range(la0, la1 + 1):
        for lo in range(lo0, lo1 + 1):
            t = tile(la, lo)
            if t is None: continue
            if t.shape != (N, N):
                t = t[np.linspace(0, t.shape[0] - 1, N).astype(int)][:, np.linspace(0, t.shape[1] - 1, N).astype(int)]
            r0 = (la1 - la) * N; c0 = (lo - lo0) * N
            g[r0:r0 + N, c0:c0 + N] = t
    return g
def route(a, b):
    pad = max(0.25, 0.3 * max(abs(a[0] - b[0]), abs(a[1] - b[1])))
    la0, la1 = math.floor(min(a[0], b[0]) - pad), math.floor(max(a[0], b[0]) + pad)
    lo0, lo1 = math.floor(min(a[1], b[1]) - pad), math.floor(max(a[1], b[1]) + pad)
    g = mosaic(la0, la1, lo0, lo1)
    # crop to the padded box
    top = la1 + 1; left = lo0
    r_lo = int((top - (max(a[0], b[0]) + pad)) * N); r_hi = int((top - (min(a[0], b[0]) - pad)) * N)
    c_lo = int(((min(a[1], b[1]) - pad) - left) * N); c_hi = int(((max(a[1], b[1]) + pad) - left) * N)
    g = g[max(r_lo, 0):r_hi, max(c_lo, 0):c_hi]; top -= max(r_lo, 0) / N; left += max(c_lo, 0) / N
    f = max(1, math.ceil(math.sqrt(g.size / 1.2e6)))
    if f > 1:
        H, W = g.shape[0] // f * f, g.shape[1] // f * f
        g = np.nanmean(g[:H, :W].reshape(H // f, f, W // f, f), axis=(1, 3))
    res = f / N   # degrees per cell
    H, W = g.shape
    lat_c = top - (np.arange(H) + 0.5) * res
    dy = res * 111.32                                  # km per cell, north-south
    dx = res * 111.32 * np.cos(np.radians(lat_c))      # km per cell, east-west, by row
    ok = ~np.isnan(g); idx = np.arange(H * W).reshape(H, W)
    src, dst, wt, ln = [], [], [], []
    for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        r0, r1 = max(0, -di), H - max(0, di); c0, c1 = max(0, -dj), W - max(0, dj)
        rs, cs = slice(r0, r1), slice(c0, c1); rt, ct = slice(r0 + di, r1 + di), slice(c0 + dj, c1 + dj)
        rows = np.arange(H)[rs]
        horiz = np.sqrt((dj * dx[rows][:, None]) ** 2 + (di * dy) ** 2) * np.ones((1, W - abs(dj)))
        dz = (g[rt, ct] - g[rs, cs]) / 1000.0
        slope = dz / horiz
        speed = 6 * np.exp(-3.5 * np.abs(slope + 0.05))
        m = ok[rs, cs] & ok[rt, ct]
        src.append(idx[rs, cs][m]); dst.append(idx[rt, ct][m]); wt.append((horiz / speed)[m]); ln.append(np.sqrt(horiz ** 2 + dz ** 2)[m])
    src = np.concatenate(src); dst = np.concatenate(dst); wt = np.concatenate(wt); ln = np.concatenate(ln)
    G = coo_matrix((wt, (src, dst)), shape=(H * W, H * W)).tocsr()
    def cell(p):
        r = int((top - p[0]) / res); c = int((p[1] - left) / res)
        r = min(max(r, 0), H - 1); c = min(max(c, 0), W - 1)
        if not ok[r, c]:   # nearest land cell
            rr, cc = np.nonzero(ok); k = np.argmin((rr - r) ** 2 + (cc - c) ** 2); r, c = rr[k], cc[k]
        return r * W + c
    s, t = cell(a), cell(b)
    dist, pred = dijkstra(G, indices=s, return_predecessors=True)
    if not np.isfinite(dist[t]): return None
    # walk back: path length
    path = [t]
    while path[-1] != s: path.append(pred[path[-1]])
    path = path[::-1]
    pr, pc = np.divmod(np.array(path), W)
    km = 0.0
    for k in range(len(path) - 1):
        r1, c1, r2, c2 = pr[k], pc[k], pr[k + 1], pc[k + 1]
        h = math.hypot((c2 - c1) * dx[r1], (r2 - r1) * dy); z = (g[r2, c2] - g[r1, c1]) / 1000
        km += math.hypot(h, z)
    climb = float(np.sum(np.clip(np.diff(g[pr, pc]), 0, None)))
    return km, float(dist[t]), climb, res * 111.32, float(np.nanmax(g[pr, pc]))
out = []
for r in rd("route/li_terrain.tsv"):
    a, b = C[T[r["id"]]["from_id"]], C[r["id"]]
    q = route(a, b)
    if not q: print("no route", r["id"], file=sys.stderr); continue
    km, hrs, climb, cellkm, top = q; li = float(r["li"]); sk = float(r["km"])
    out.append({"id": r["id"], "name_zh": r["name_zh"], "juan": r["juan"], "li": r["li"], "straight_km": sk,
                "path_km": round(km, 1), "hours": round(hrs, 1), "detour": round(km / sk, 2), "climb_m": round(climb),
                "max_elev": round(top), "cell_km": round(cellkm, 2), "km_per_li_path": round(km / li, 3),
                "li_per_hour": round(li / hrs, 2), "relief_m_per_km": r["relief_m_per_km"], "text_terrain": r["text_terrain"]})
    print(r["id"], out[-1]["path_km"], out[-1]["hours"], out[-1]["detour"], flush=True)
w = csv.DictWriter(open("route/li_paths.tsv", "w", encoding="utf-8", newline=""), list(out[0]), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(out)
