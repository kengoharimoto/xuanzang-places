#!/usr/bin/env python3
"""Check verbatim quotes in route/variants_*.tsv against T2088, T2053 and Mizutani's OCR (whitespace and Taishō page
markers ignored; '…' separates fragments of >= 4 chars). Usage: python3 -I route/check_variants.py route/variants_*.tsv"""
import csv, re, sys, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
clean = lambda s: re.sub(r"\[T\d+:\d+[abc]\]|<<pdf[^>]*>>|\s+", "", s or "")
T = {"t2088_text": clean((R/"data/ref/t2088_joined.txt").read_text()), "t2053_text": clean((R/"data/ref/t2053_joined.txt").read_text()),
     "mz_variant": clean((R/"data/mizutani/mizutani_ocr.txt").read_text())}
tot = 0
for p in sys.argv[1:]:
    ok = bad = 0
    for r in csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"):
        errs = []
        for col, hay in T.items():
            q = clean(r.get(col, ""))
            if not q: continue
            fr = [f for f in re.split(r"…|\.\.\.", q) if len(f) >= 4]
            if not fr or not all(f in hay for f in fr): errs.append(col)
        if errs: bad += 1; print("BAD", pathlib.Path(p).name, r.get("id"), ",".join(errs))
        else: ok += 1
    print(f"{p}: ok {ok}, bad {bad}"); tot += bad
sys.exit(1 if tot else 0)
