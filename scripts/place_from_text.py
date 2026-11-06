#!/usr/bin/env python3
"""Approximate points for places the study cannot locate, placed from Xuanzang's own figures.

Usage (from xuanzang-places/): python3 -I scripts/place_from_text.py  -> data/coords_text.tsv
For each place without a point in data/study_view.tsv that has a route leg in route/segments.tsv (bearing and
distance from a starting place), the point is the starting place's point (the study's view, or a point already
placed this way: the loop repeats until nothing changes) moved by the stated distance along the stated bearing, at the
calibrated 0.239 km per li (route/README.md §1). Multi-leg segments are added as vectors. A leg of under 1 li
("not far", 不遠) is not placed. Precision is "from the text": no identification is claimed, and the point can be
wrong by the scatter of the li (§1, §8). data/study_view.tsv picks these up as its last fallback.
"""
import csv, math, re
rd = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
KM = 0.239
DEG = {"北": 0, "東北": 45, "東": 90, "東南": 135, "南": 180, "西南": 225, "西": 270, "西北": 315}
V = {r["id"]: r for r in rd("data/study_view.tsv")}
PT = {i: (float(r["lat"]), float(r["lon"])) for i, r in V.items() if r["lat"] and r.get("point_from") != "text"}   # not this script's own earlier output
segs = {s["id"]: s for s in rd("route/segments.tsv") if s["li_lo"] and s["from_id"]}
def move(p, brg, km):
    la, lo = math.radians(p[0]), math.radians(p[1]); d = km / 6371; b = math.radians(brg)
    la2 = math.asin(math.sin(la) * math.cos(d) + math.cos(la) * math.sin(d) * math.cos(b))
    lo2 = lo + math.atan2(math.sin(b) * math.sin(d) * math.cos(la), math.cos(d) - math.sin(la) * math.sin(la2))
    return math.degrees(la2), math.degrees(lo2)
out, placed = [], {}
changed = True
while changed:
    changed = False
    for i, s in segs.items():
        if i in PT or i in placed: continue
        start = PT.get(s["from_id"]) or placed.get(s["from_id"])
        if not start: continue
        legs = re.findall(r"([東西南北]{1,2})\s*(\d+)(?:-(\d+))?", s["legs"])
        if not legs: continue
        dx = dy = 0
        for b, a, c in legs:
            li = (int(a) + int(c or a)) / 2; th = math.radians(DEG[b]); dx += li * math.sin(th); dy += li * math.cos(th)
        li = math.hypot(dx, dy)
        if li < 1: continue
        p = move(start, math.degrees(math.atan2(dx, dy)) % 360, li * KM)
        placed[i] = p; changed = True
        out.append({"id": i, "lat": round(p[0], 4), "lon": round(p[1], 4), "precision": "from the text",
                    "label": f"placed from the text: {s['legs']} from {s['from_id']}", "note": s.get("t_route", "")[:80]})
# second stage: sites whose own passage opens with a position, e.g. 城東南三四里有窣堵波 or 伽藍西北五十餘步
NUM = {"一": 1, "二": 2, "兩": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
def cnum(t):
    """Chinese numeral (with ranges like 三四, 二三十) to a number: the mean of a range."""
    t = t.replace("餘", "")
    if not t: return None
    vals = []
    m = re.fullmatch(r"([一二三四五六七八九兩]?)([一二三四五六七八九兩]?)(百|十)?([一二三四五六七八九]?)([一二三四五六七八九]?)(十)?", t)
    if not m: return None
    if m.group(3) == "百": base = (NUM.get(m.group(1), 1) + NUM.get(m.group(2), NUM.get(m.group(1), 1))) / 2 * 100; rest = (m.group(4), m.group(5), m.group(6))
    elif m.group(3) == "十": return (NUM.get(m.group(1), 1) + NUM.get(m.group(2), NUM.get(m.group(1), 1))) / 2 * 10 + (NUM.get(m.group(4), 0) + NUM.get(m.group(5), NUM.get(m.group(4), 0))) / 2
    else:
        a, b = NUM.get(m.group(1)), NUM.get(m.group(2))
        if a is None: return None
        v = (a + (b or a)) / 2
        return v * 10 if m.group(6) else v
    v = base
    if rest[0]: v += (NUM.get(rest[0], 0) + NUM.get(rest[1], NUM.get(rest[0], 0))) / 2 * (10 if rest[2] else 1)
    return v
M = rd("data/places.tsv"); order = [r["id"] for r in M]; parent = {r["id"]: r["parent"] for r in M}
TX = {r["id"]: re.sub(r"\s|（[^）]*）", "", r["t2087_text"]) for r in M}
changed = True
while changed:
    changed = False
    for k, i in enumerate(order):
        if i in PT or i in placed or not TX.get(i): continue
        m = re.match(r"(.{0,10}?)(東北|東南|西北|西南|東|西|南|北)(?:行)?([一二三四五六七八九十百兩餘]+)(里|步)", TX[i])
        if not m: continue
        n = cnum(m.group(3))
        if not n: continue
        li = n if m.group(4) == "里" else n / 360    # 360 paces to the li
        if li < 1: continue
        pre = m.group(1)
        ref = parent.get(i) if (not pre or "城" in pre) else next((order[j] for j in range(k - 1, -1, -1) if parent.get(order[j]) == parent.get(i) or order[j] == parent.get(i)), parent.get(i))
        start = PT.get(ref) or placed.get(ref) or PT.get(parent.get(i)) or placed.get(parent.get(i))
        if not start: continue
        p = move(start, DEG[m.group(2)], li * KM); placed[i] = p; changed = True
        out.append({"id": i, "lat": round(p[0], 4), "lon": round(p[1], 4), "precision": "from the text",
                    "label": f"placed from the text: {m.group(0)} (from {ref})", "note": TX[i][:60]})
w = csv.DictWriter(open("data/coords_text.tsv", "w", encoding="utf-8", newline=""), ["id", "lat", "lon", "precision", "label", "note"], delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(out)
print(len(out), "places placed from the text;", sum(1 for r in V.values() if not r["lat"] or r.get("point_from") == "text") - len(out), "still without a point")
