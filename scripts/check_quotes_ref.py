#!/usr/bin/env python3
"""Check quotes in authority TSVs (data/coded/auth_*.tsv) against the reference texts in data/ref/.

Usage: python3 -I scripts/check_quotes_ref.py data/coded/auth_*.tsv
Each row needs `source_file` (a file name in data/ref/) and `quote`. Matching ignores case, whitespace and
line-end hyphenation; "…" separates fragments (each ≥ 12 chars).
"""
import csv, re, sys, pathlib, unicodedata
REF = pathlib.Path(__file__).resolve().parent.parent / "data/ref"
def norm(s):
    s = unicodedata.normalize("NFKC", s or "").lower()
    s = re.sub(r"[‘’`´]", "'", s); s = re.sub(r"[“”]", '"', s)
    s = re.sub(r"-\s*\n\s*", "", s)
    return re.sub(r"\s+", "", s)
cache = {}
def text(name):
    if name not in cache:
        p = REF / name
        cache[name] = norm(p.read_text(encoding="utf-8", errors="replace")) if p.exists() else None
    return cache[name]
total = 0
for path in sys.argv[1:]:
    ok = bad = 0
    for r in csv.DictReader((l for l in open(path, encoding="utf-8") if not l.startswith("#")), delimiter="\t"):
        t = text(r.get("source_file", ""))
        frs = [f for f in re.split(r"…|\.\.\.", norm(r.get("quote", "")).strip('"')) if len(f) >= 12]
        err = "unknown source_file" if t is None else ("quote empty/too short" if not frs else
              ("" if all(f in t for f in frs) else "quote not found"))
        if err: bad += 1; print("BAD", pathlib.Path(path).name, r.get("id"), r.get("authority"), err, "|", (r.get("quote") or "")[:70])
        else: ok += 1
    print(f"{path}: ok {ok}, bad {bad}"); total += bad
sys.exit(1 if total else 0)
