#!/usr/bin/env python3
"""Check that religion-coding quotes occur in the place's T2087 passage, and codes are from the allowed sets.
Usage (from xuanzang-places/): python3 -I scripts/check_religion.py data/religion/religion_*.tsv"""
import csv, re, sys
P = {r["id"]: (lambda z: z + "\n" + re.sub(r"（[^（）]*）", "", z))(re.sub(r"\s", "", r["zh"])) for r in csv.DictReader(open("data/text/passages.tsv", encoding="utf-8"), delimiter="\t")}
SCH = set("Mahayana Hinayana Sarvastivada Sammatiya Sthavira Mahayana-Sthavira Mahasanghika Lokottaravada Dharmaguptaka Mahisasaka Kasyapiya both".split())
OTH = set("Jain-Digambara Jain-Svetambara Jain Saiva Pasupata Kapalika Surya Devi Brahmanical heretics-many".split())
tot = 0
for f in sys.argv[1:]:
    ok = bad = 0
    for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
        e = []
        q = [x for x in re.split(r"…|\.\.\.", re.sub(r"\s", "", r.get("quote", ""))) if len(x) >= 3]
        if q and not all(x in P.get(r["id"], "") for x in q): e.append("quote not in passage")
        for col, allowed in (("schools", SCH), ("other", OTH)):
            for c in filter(None, (r.get(col) or "").split(";")):
                c = c.strip()
                if c and c not in allowed and not c.startswith("other:"): e.append(f"{col} code {c}")
        if e: bad += 1; print("BAD", r["id"], "; ".join(e))
        else: ok += 1
    print(f"{f}: ok {ok}, bad {bad}"); tot += bad
sys.exit(1 if tot else 0)
