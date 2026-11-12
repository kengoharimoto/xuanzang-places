#!/usr/bin/env python3
"""Extract route segments (from → to, li, bearing) from the master table's T2087 route sentences.

Usage (from xuanzang-places/): python3 -I route/segments.py  -> route/segments.tsv
- li: parsed from the Chinese numerals before 里 (ranges like 二三里, 五六十里, 百四五十 give lo/hi; 餘 = "over").
  Several legs in one sentence (e.g. SW 200 + SE 300) are summed; `legs` keeps them.
- bearing: the direction word nearest before 行/至/... in each leg (東, 東南, 西北…); multi-leg bearings joined by '+'.
- from_id: resolved from the `route` column ("from <name>") against the master table's names.
"""
import csv, re
NUM = {"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9,"兩":2}
def cn(s):
    """Parse a Chinese numeral, returning (lo, hi). Handles 百四五十, 二三, 五六十, 千, 萬."""
    s = s.replace("〇", "")
    if not s: return None
    def single(t):
        total, cur = 0, 0
        for ch in t:
            if ch in NUM: cur = NUM[ch]
            elif ch == "十": total += (cur or 1) * 10; cur = 0
            elif ch == "百": total += (cur or 1) * 100; cur = 0
            elif ch == "千": total += (cur or 1) * 1000; cur = 0
            elif ch == "萬": total = (total + cur) * 10000; cur = 0
        return total + cur
    # ranges: two adjacent digits (e.g. 二三, 四五十, 百四五十)
    m = re.search(r"([一二三四五六七八九])([一二三四五六七八九])(十|百|千)?$", s)
    if m and NUM[m.group(2)] == NUM[m.group(1)] + 1:
        unit = m.group(3) or ""
        pre = s[:m.start()]
        return single(pre + m.group(1) + unit), single(pre + m.group(2) + unit)
    v = single(s); return (v, v)
DIRS = ["東北", "東南", "西北", "西南", "東", "西", "南", "北"]
DEG = {"北":0,"東北":45,"東":90,"東南":135,"南":180,"西南":225,"西":270,"西北":315}
LEG = re.compile(r"(東北|東南|西北|西南|東|西|南|北)[^。里]{0,14}?([一二三四五六七八九十百千萬兩]+)(餘)?里")
rows = list(csv.DictReader(open("data/places_mizutani.tsv", encoding="utf-8"), delimiter="\t"))
names = {}
for r in rows:
    for n in {r["name_zh"], r["name_zh"].replace("國", ""), r["name_ja"], r["name_ja"].replace("国", "").replace("國", "")}:
        n = re.sub(r"\s*\(.*?\)|（.*?）", "", n).strip()
        if len(n) >= 2: names.setdefault(n, r["id"])
def resolve(fr):
    m = re.match(r"(.+?)\s*\((.+?)\)", fr)
    if m:
        cid = names.get(m.group(2).strip()) or names.get(m.group(2).strip().replace("國", ""))
        if cid:
            for r in rows:
                if r["id"].startswith(cid) and (m.group(1).strip() in r["name_zh"] or m.group(1).strip() in r["name_ja"]):
                    return r["id"]
            return cid
    fr = re.sub(r"\s*\(.*?\)", "", fr).strip()
    if fr in names: return names[fr]
    for n, i in sorted(names.items(), key=lambda x: -len(x[0])):
        if n in fr: return i
    return ""
EN = re.compile(r"\b(NNE|ENE|ESE|SSE|SSW|WSW|WNW|NNW|NE|NW|SE|SW|N|S|E|W)\b[^;+]*?(\d+)(?:\s*[–-]\s*(\d+))?\s*(余|餘|\+)?\s*(?:里|li)")
ENDEG = {"N":"北","NE":"東北","E":"東","SE":"東南","S":"南","SW":"西南","W":"西","NW":"西北"}
def en_legs(route):
    body = route.split(";", 1)[1] if ";" in route else route
    out = []
    for d, a, b, e in EN.findall(body):
        d = ENDEG.get(d, ENDEG.get(d[-2:], ENDEG.get(d[-1:], d)))
        out.append((d, (int(a), int(b or a)), bool(e)))
    return out
out = []
for r in rows:
    t = re.sub(r"m\d{5}", "□", r["t_route"])   # any code left unmapped (merge_mizutani.py writes the characters)
    t = re.sub(r"（.*?）", "", t)
    legs = [(d, cn(n), bool(e)) for d, n, e in LEG.findall(t)]
    legs = [(d, v, e) for d, v, e in legs if v and v[0] > 0]
    el = en_legs(r["route"])
    if el and (not legs or sum(v[0] for _, v, _ in el) != sum(v[0] for _, v, _ in legs)):
        src = "route"; legs = el
    else: src = "t_route"
    m = re.match(r"from ([^;]+);", r["route"])
    fr = m.group(1).strip() if m else ""
    out.append({"id": r["id"], "name_zh": r["name_zh"], "level": r["level"], "parent": r["parent"],
        "from_text": fr, "from_id": (r["parent"] if re.fullmatch(r"(the )?(capital|city|大城|王城|大都城|都城|宮城|the city)", fr or "") else resolve(fr)) if fr else "",
        "legs": " + ".join(f"{d} {v[0]}{'-'+str(v[1]) if v[1]!=v[0] else ''}{'+' if e else ''}" for d, v, e in legs),
        "li_lo": sum(v[0] for _, v, _ in legs) if legs else "", "li_hi": sum(v[1] for _, v, _ in legs) if legs else "",
        "bearing": "+".join(d for d, _, _ in legs), "parsed_from": src if legs else "", "t_verb": r["t_verb"], "visit": r["visit"],
        "mz_status": r["mz_status"], "t_route": r["t_route"]})
OV = {r["id"]: r for r in csv.DictReader(open("route/segment_overrides.tsv", encoding="utf-8"), delimiter="\t")}
for o in out:
    v = OV.get(o["id"])
    if not v: continue
    if v["action"] == "exclude":
        o.update(legs="", li_lo="", li_hi="", bearing="", parsed_from="override: " + v["reason"])
    elif v["action"] == "set":
        L = [(d, tuple(map(int, n.split("-"))) if "-" in n else (int(n.rstrip("+")),)*2) for d, n in (x.split() for x in v["legs"].split(" + "))]
        o.update(legs=v["legs"], li_lo=sum(a for _, (a, b) in L), li_hi=sum(b for _, (a, b) in L), bearing="+".join(d for d, _ in L),
                 from_id=v["from_id"] or o["from_id"], parsed_from="override: " + v["reason"])
w = csv.DictWriter(open("route/segments.tsv", "w", encoding="utf-8", newline=""), out[0].keys(), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(out)
ok = [o for o in out if o["li_lo"] != ""]
print(len(out), "rows;", len(ok), "with li;", sum(1 for o in ok if o["from_id"]), "with li and from_id")
for o in ok[:12]: print(o["id"], o["from_text"], "->", o["from_id"], "|", o["legs"])
