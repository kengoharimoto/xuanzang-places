#!/usr/bin/env python3
"""Approximate extents of Xuanzang's countries, from the circuit he gives for each (國周N里).

Usage (from xuanzang-places/): python3 -I scripts/country_areas.py
  -> data/country_areas.tsv (one row per country: circuit, scale, target and drawn area)
  -> map/country_areas.json (rings in lon/lat, read by map/build_page.py)

Method (README, "Country areas"):
1. The circuit: the first 周N里 of the country's passage that is not a city's (城周); ranges take the mean, 餘
   ("over") is ignored, 減 ("less than") takes 0.9. Where the text gives 東西X里，南北Y里 instead, the area is that of an ellipse X by Y.
2. The scale: straight-line km per li, the median of the route legs of the country's juan (route/li_regions.tsv;
   0.24 where a juan has no figure). So the Deccan's inflated figures are scaled down as its distances are.
3. The target area: a region whose perimeter is the circuit, at a compactness of 0.75 of a circle's
   (A = 0.75 * P^2 / 4 pi).
4. The shape: from the study's point for the capital (data/study_view.tsv), every country grows over land at once,
   cell by cell (0.08 degree grid) in order of distance, until it reaches its target area or 1.6 times the radius of
   its target; a cell goes to the country that reaches it first. Sea stops growth. So neighbours meet half-way
   where they press on each other, and a country with room becomes roughly round.
These are not borders: the capital need not have been central, mountains and rivers are not modelled, and the
circuit figures themselves are rough.
"""
import csv, json, math, re, heapq, collections

RES = 0.08
BOX = (48.0, -2.0, 112.0, 47.0)          # lon0, lat0, lon1, lat1
COMPACT = 0.75
CAP = 1.6
rd = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))

# --- Chinese numerals -------------------------------------------------------------------------------------------
D = dict(zip("一二三四五六七八九", range(1, 10)))
def cn(s):
    """'七千' -> 7000, '四五千' -> 4500, '萬' -> 10000, '千' -> 1000, '二三十' -> 25."""
    s = s.replace("餘", "").replace("有", "").replace("、", "")
    if s.startswith("減"): return (cn(s[1:]) or 0) * 0.9 or None   # 周減千里, "less than a thousand li"
    m = re.fullmatch(r"([一二三四五六七八九]?)([一二三四五六七八九]?)(萬|千|百|十)?(.*)", s)
    if not m: return None
    a, b, unit, rest = m.groups()
    u = dict(萬=10000, 千=1000, 百=100, 十=10).get(unit, 1)
    if a and b: base = (D[a] + D[b]) / 2 * u
    elif a: base = D[a] * u
    elif unit: base = u
    else: return None
    r = cn(rest) if rest else 0
    return base + (r or 0)

def circuit(zh):
    for m in re.finditer(r"周([一二三四五六七八九十百千萬餘、減]{1,9})里", zh):
        if "城" in zh[max(0, m.start() - 4):m.start()]: continue
        v = cn(m.group(1))
        if v: return ("circuit", v, m.group(0))
    m = re.search(r"東西([一二三四五六七八九十百千萬餘]{1,8})里[，、]?南北([一二三四五六七八九十百千萬餘]{1,8})里", zh)
    if m:
        a, b = cn(m.group(1)), cn(m.group(2))
        if a and b: return ("dims", (a, b), m.group(0))
    return None

# --- inputs -----------------------------------------------------------------------------------------------------
P = {r["id"]: r for r in rd("data/places.tsv")}
SV = {r["id"]: r for r in rd("data/study_view.tsv")}
TX = {r["id"]: r["zh"] for r in rd("data/text/passages.tsv")}
scale = {r["value"]: float(r["median_km_per_li"]) for r in rd("route/li_regions.tsv") if r["group"] == "juan"}

countries = []
rows = []
for cid, r in P.items():
    if r["level"] != "country": continue
    sv = SV.get(cid, {})
    c = circuit(TX.get(cid, ""))
    k = scale.get(cid[:2], 0.24)
    row = dict(id=cid, name_zh=r["name_zh"], cls=sv.get("cls", ""), text=c[2] if c else "", circuit_li="", dims_li="",
               km_per_li=k, target_km2="", drawn_km2="", note="")
    if not c:
        row["note"] = "no circuit in the text"; rows.append(row); continue
    if c[0] == "circuit":
        row["circuit_li"] = int(c[1]); per = c[1] * k; A = COMPACT * per * per / (4 * math.pi)
    else:
        row["dims_li"] = "%d x %d" % c[1]; A = math.pi / 4 * c[1][0] * k * c[1][1] * k
    row["target_km2"] = round(A)
    if not sv.get("lat") or sv.get("cls") in ("unlocated", "text", ""):
        row["note"] = "no point for the capital"; rows.append(row); continue
    countries.append(dict(id=cid, lat=float(sv["lat"]), lon=float(sv["lon"]), A=A, R=math.sqrt(A / math.pi), row=row))
    rows.append(row)

# --- land mask (scanline over the simplified Natural Earth rings) -----------------------------------------------
NX = int((BOX[2] - BOX[0]) / RES); NY = int((BOX[3] - BOX[1]) / RES)
land = bytearray(NX * NY)
geo = json.load(open("map/geo_small.json", encoding="utf-8"))["countries"]
for cty in geo:
    rings = cty["rings"]
    for j in range(NY):
        y = BOX[1] + (j + 0.5) * RES
        xs = []
        for ring in rings:
            for (x1, y1), (x2, y2) in zip(ring, ring[1:] + ring[:1]):
                if (y1 > y) != (y2 > y): xs.append(x1 + (y - y1) * (x2 - x1) / (y2 - y1))
        xs.sort()
        for a, b in zip(xs[0::2], xs[1::2]):
            i0 = max(0, math.ceil((a - BOX[0]) / RES - 0.5)); i1 = min(NX - 1, math.floor((b - BOX[0]) / RES - 0.5))
            for i in range(i0, i1 + 1): land[j * NX + i] = 1

# 16 directions (king and knight moves), so distances on the grid come out nearly round, not octagonal
STEPS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1),
         (2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
cellkm = lambda j: (RES * 111.32) ** 2 * math.cos(math.radians(BOX[1] + (j + 0.5) * RES))
owner = [-1] * (NX * NY)
area = [0.0] * len(countries)
pq = []
for n, c in enumerate(countries):
    i = int((c["lon"] - BOX[0]) / RES); j = int((c["lat"] - BOX[1]) / RES)
    if not (0 <= i < NX and 0 <= j < NY): continue
    if not land[j * NX + i]:          # capital on a coast cell judged sea: take the nearest land cell
        best = min(((abs(di) + abs(dj), i + di, j + dj) for di in range(-4, 5) for dj in range(-4, 5)
                    if 0 <= i + di < NX and 0 <= j + dj < NY and land[(j + dj) * NX + i + di]), default=None)
        if not best: continue
        _, i, j = best
    heapq.heappush(pq, (0.0, n, i, j))
while pq:
    d, n, i, j = heapq.heappop(pq)
    idx = j * NX + i
    if owner[idx] != -1 or area[n] >= countries[n]["A"]: continue
    owner[idx] = n; area[n] += cellkm(j)
    lat = BOX[1] + (j + 0.5) * RES; kx = 111.32 * RES * math.cos(math.radians(lat)); ky = 111.32 * RES
    for di, dj in STEPS:
        a, b = i + di, j + dj
        if not (0 <= a < NX and 0 <= b < NY): continue
        k2 = b * NX + a
        if owner[k2] != -1 or not land[k2]: continue
        if abs(di) + abs(dj) == 3 and not land[(j + (dj // 2 if abs(dj) == 2 else 0)) * NX + i + (di // 2 if abs(di) == 2 else 0)]: continue
        nd = d + math.hypot(di * kx, dj * ky)
        if nd <= CAP * countries[n]["R"]: heapq.heappush(pq, (nd, n, a, b))

# --- outlines: cell edges with the country on the right (clockwise exteriors, as d3-geo wants) -------------------
def outline(n):
    E = collections.defaultdict(list)
    O = lambda i, j: owner[j * NX + i] if 0 <= i < NX and 0 <= j < NY else -1
    for j in range(NY):
        for i in range(NX):
            if owner[j * NX + i] != n: continue
            # corners (i,j) bottom-left .. ; walk clockwise round the cell: left side up, top right, right down, bottom left
            if O(i - 1, j) != n: E[(i, j)].append((i, j + 1))
            if O(i, j + 1) != n: E[(i, j + 1)].append((i + 1, j + 1))
            if O(i + 1, j) != n: E[(i + 1, j + 1)].append((i + 1, j))
            if O(i, j - 1) != n: E[(i + 1, j)].append((i, j))
    rings = []
    while E:
        start = next(iter(E)); ring = [start]; cur = start; prev = None
        while True:
            outs = E[cur]
            if len(outs) > 1 and prev:   # pinch vertex: take the sharpest right turn
                dx, dy = cur[0] - prev[0], cur[1] - prev[1]
                outs.sort(key=lambda v: dx * (v[1] - cur[1]) - dy * (v[0] - cur[0]))
            nxt = outs.pop(0)
            if not outs: del E[cur]
            prev, cur = cur, nxt
            if cur == start: break
            ring.append(cur)
        rings.append(ring)
    return rings

def dp(ring, tol=0.75):
    """Douglas-Peucker on a closed ring (grid units), to take out the stair steps before smoothing."""
    if len(ring) < 8: return ring
    def rec(pts):
        a, b = pts[0], pts[-1]; dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy) or 1e-9
        best, bi = -1, 0
        for k in range(1, len(pts) - 1):
            d = abs(dy * (pts[k][0] - a[0]) - dx * (pts[k][1] - a[1])) / L
            if d > best: best, bi = d, k
        return rec(pts[:bi + 1])[:-1] + rec(pts[bi:]) if best > tol else [a, b]
    h = len(ring) // 2
    out = rec(ring[:h + 1])[:-1] + rec(ring[h:] + [ring[0]])[:-1]
    return out if len(out) >= 4 else ring

def chaikin(ring, it=3):
    for _ in range(it):
        out = []
        for p, q in zip(ring, ring[1:] + ring[:1]):
            out += [(0.75 * p[0] + 0.25 * q[0], 0.75 * p[1] + 0.25 * q[1]), (0.25 * p[0] + 0.75 * q[0], 0.25 * p[1] + 0.75 * q[1])]
        ring = out
    return ring

def sarea(r):
    return sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(r, r[1:] + r[:1])) / 2
def inside(pt, r):
    x, y = pt; c = False
    for (x1, y1), (x2, y2) in zip(r, r[1:] + r[:1]):
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1): c = not c
    return c

features = []
for n, c in enumerate(countries):
    c["row"]["drawn_km2"] = round(area[n])
    if area[n] < c["A"] * 0.98:
        c["row"]["note"] = "drawn smaller than the target: hemmed in by neighbours, the sea or the radius cap"
    rings = [[(round(BOX[0] + x * RES, 3), round(BOX[1] + y * RES, 3)) for x, y in chaikin(dp(r))] for r in outline(n)]
    ext = [r for r in rings if sarea(r) < 0]     # clockwise in lon/lat
    holes = [r for r in rings if sarea(r) > 0]
    polys = [[e] for e in ext]
    for h in holes:
        for p in polys:
            if inside(h[0], p[0]): p.append(h); break
    if polys:
        features.append(dict(id=c["id"], cls=c["row"]["cls"], text=c["row"]["text"], kpl=c["row"]["km_per_li"],
                             target=c["row"]["target_km2"], drawn=round(area[n]),
                             polys=[[[list(pt) for pt in r] for r in p] for p in polys]))

json.dump(dict(note="approximate extents from Xuanzang's stated circuits; not historical borders (scripts/country_areas.py)",
               features=features), open("map/country_areas.json", "w", encoding="utf-8"), ensure_ascii=False,
          separators=(",", ":"))
w = csv.DictWriter(open("data/country_areas.tsv", "w", encoding="utf-8", newline=""), list(rows[0]), delimiter="\t",
                   lineterminator="\n")
w.writeheader(); w.writerows(sorted(rows, key=lambda r: r["id"]))
cnt = collections.Counter(r["note"] or "drawn in full" for r in rows)
print(len(rows), "countries;", len(features), "drawn;", dict(cnt))
