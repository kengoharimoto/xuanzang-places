#!/usr/bin/env python3
"""Inputs for the name-reconstruction pilot (data/names/).

Usage (from xuanzang-places/): PYTHONPATH=<dir with tshet_uinh> python3 scripts/names_prep.py
  data/names/targets.tsv   places whose original form is a reconstruction (*) or queried (?), juans 2-11 and the
                           Indian/NW part of juans 1 and 12 marked by region
  data/names/secure.tsv    places with an original form that is neither asterisked nor queried (the key's training set)
  data/names/mc.tsv        every Chinese character in these names with its Qieyun position(s) (tshet_uinh, Guangyun)
"""
import csv, re, collections
import tshet_uinh as T
rd = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
P = rd("data/places.tsv")
def core(z): return re.sub(r"[（(].*?[)）]|・.*|僧伽藍$|故國$|國$|城$|山$|河$|川$|伽藍$|窣堵波$", "", z).strip()
tg, sc, chars = [], [], set()
for p in P:
    f = p["original_name"].strip()
    if not f: continue
    j = int(p["id"][:2])
    region = "Central Asia" if j == 1 and p["id"] < "01.26" else ("Tokharistan/Afghanistan" if j in (1, 12) else "India and the North-West")
    row = {"id": p["id"], "name_zh": p["name_zh"], "translit": core(p["name_zh"]), "original_name": f, "region": region,
           "identification": p.get("mz_identification", "")[:120]}
    (tg if ("*" in f or "?" in f) else sc).append(row)
    chars.update(c for c in row["translit"] if "一" <= c <= "鿿" or c >= "\U00020000")
for name, rows in (("targets", tg), ("secure", sc)):
    w = csv.DictWriter(open(f"data/names/{name}.tsv", "w", encoding="utf-8", newline=""), list(rows[0]), delimiter="\t", lineterminator="\n")
    w.writeheader(); w.writerows(rows)
with open("data/names/mc.tsv", "w", encoding="utf-8") as f:
    f.write("char\tpositions\tfanqie\n")
    for c in sorted(chars):
        r = T.資料.query字頭(c)
        f.write(f"{c}\t{' / '.join(dict.fromkeys(x.音韻地位.描述 for x in r))}\t{' / '.join(dict.fromkeys(x.反切 or '' for x in r))}\n")
print(len(tg), "targets", collections.Counter(r["region"] for r in tg), len(sc), "secure", len(chars), "chars")
