#!/usr/bin/env python3
"""Check coded quotes against the OCR, page by page.

Usage: python3 -I scripts/check_quotes.py data/coded/*.tsv
- `quote` (Mizutani, Japanese/romanized) must occur on pdf page `pdf_page` or the next page
  (all whitespace removed before matching; "…" separates fragments, each ≥ 6 chars).
- `t_route` (Taishō Chinese), if filled, must occur in data/ref/t2087_joined.txt (whitespace removed).
"""
import csv, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
strip = lambda s: re.sub(r"\s+", "", s or "")
pages = {int(p.stem[1:]): strip(p.read_text()) for p in (ROOT / "data/mizutani/vision").glob("p*.txt")}
t2087 = strip((ROOT / "data/ref/t2087_joined.txt").read_text())
t2087 = re.sub(r"\[T51:\d+[abc]\]", "", t2087)
def frags(q):
    return [f for f in re.split(r"…|\.\.\.", strip(q).strip('"“”「」')) if len(f) >= 6]
total_bad = 0
for path in sys.argv[1:]:
    ok = bad = 0
    rows = csv.DictReader((l for l in open(path, encoding="utf-8") if not l.startswith("#")), delimiter="\t")
    for r in rows:
        errs = []
        try:
            pg = int(r["pdf_page"])
            hay = pages.get(pg, "") + pages.get(pg + 1, "")
        except (ValueError, TypeError):
            hay = ""; errs.append("bad pdf_page")
        fs = frags(r.get("quote", ""))
        if not fs: errs.append("quote empty/too short")
        elif not all(f in hay for f in fs): errs.append("quote not on page")
        tr = r.get("t_route", "")
        if tr.strip() and not all(f in t2087 for f in frags(tr) or [strip(tr)]):
            errs.append("t_route not in T2087")
        if errs:
            bad += 1; print("BAD", pathlib.Path(path).name, r.get("id"), "; ".join(errs), "|", (r.get("quote") or "")[:60])
        else:
            ok += 1
    print(f"{path}: ok {ok}, bad {bad}"); total_bad += bad
sys.exit(1 if total_bad else 0)
