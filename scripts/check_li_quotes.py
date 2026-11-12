#!/usr/bin/env python3
"""Check that every li_quote in a review3_li_*.tsv occurs verbatim (whitespace-normalised) in Li Rongxi's text, and
that the file has the right columns and verdicts. Usage (from xuanzang-places/): python3 -I scripts/check_li_quotes.py FILE"""
import csv, re, sys
norm = lambda s: re.sub(r"\s+", " ", s).strip()
src = norm(open("data/ref/lit/C/li1996_great_tang_record.txt", encoding="utf-8").read())
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t"))
assert rows and list(rows[0]) == ["id", "verdict", "issues", "en_revised", "li_quote", "li_page"], list(rows[0]) if rows else "empty"
bad = 0
for r in rows:
    v = r["verdict"]
    if v not in ("ok", "minor", "major"): print("verdict?", r["id"], v); bad += 1
    if v in ("minor", "major") and not r["en_revised"].strip(): print("no en_revised", r["id"]); bad += 1
    q = norm(r["li_quote"])
    if q and q not in src:
        parts = [p.strip() for p in q.split("…") if p.strip()]
        if not all(p in src for p in parts): print("quote not found", r["id"], q[:80]); bad += 1
print(len(rows), "rows; bad", bad)
