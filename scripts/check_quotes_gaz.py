#!/usr/bin/env python3
"""Check quotes in gazetteer coding files (data/coded/gaz_*.tsv) against the volume's OCR.

Usage (from xuanzang-places/): python3 -I scripts/check_quotes_gaz.py data/coded/gaz_*.tsv
Rows need `identifier` and `quote` (rows with relevant=no may have an empty quote).
"""
import csv, glob, re, sys, pathlib, unicodedata
R = pathlib.Path(__file__).resolve().parent.parent.parent
files = {pathlib.Path(f).stem: f for f in glob.glob(str(R / "gazetteer-vedanta/*/data/ia_ocr/*.txt")) + glob.glob(str(R / "yoga-gazetteers/*/data/ia_ocr/*.txt")) + glob.glob(str(R / "xuanzang-places/data/ref/baluch/*.txt"))}   # baluch/: Baluchistan District Gazetteers, downloaded for this study
def norm(s):
    s = unicodedata.normalize("NFKC", s or "").lower()
    s = re.sub(r"[‘’`´]", "'", s); s = re.sub(r"[“”]", '"', s); s = re.sub(r"-\s*\n\s*", "", s)
    return re.sub(r"\s+", "", s)
cache = {}
total = 0
for path in sys.argv[1:]:
    ok = bad = 0
    for r in csv.DictReader((l for l in open(path, encoding="utf-8") if not l.startswith("#")), delimiter="\t"):
        if r.get("relevant", "").strip() == "no" and not r.get("quote", "").strip(): ok += 1; continue
        f = files.get(r.get("identifier", ""))
        if f and f not in cache: cache[f] = norm(open(f, encoding="utf-8", errors="replace").read())
        frs = [x for x in re.split(r"…|\.\.\.", norm(r.get("quote", "")).strip('"')) if len(x) >= 12]
        err = "unknown identifier" if not f else ("quote empty/too short" if not frs else ("" if all(x in cache[f] for x in frs) else "quote not found"))
        if err: bad += 1; print("BAD", pathlib.Path(path).name, r.get("hit"), err, "|", (r.get("quote") or "")[:70])
        else: ok += 1
    print(f"{path}: ok {ok}, bad {bad}"); total += bad
sys.exit(1 if total else 0)
