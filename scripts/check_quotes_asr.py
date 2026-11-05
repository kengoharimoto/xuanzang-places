#!/usr/bin/env python3
"""Check quotes in ASR coding files (data/coded/asr_batch*.tsv) against data/ref/asr/<file>.
Usage (from xuanzang-places/): python3 -I scripts/check_quotes_asr.py data/coded/asr_batch*.tsv"""
import csv, re, sys, pathlib, unicodedata
D = pathlib.Path(__file__).resolve().parent.parent / "data/ref/asr"
def norm(s):
    s = unicodedata.normalize("NFKC", s or "").lower()
    s = re.sub(r"[‘’`´]", "'", s); s = re.sub(r"[“”]", '"', s); s = re.sub(r"-\s*\n\s*", "", s)
    return re.sub(r"\s+", "", s)
cache, total = {}, 0
for path in sys.argv[1:]:
    ok = bad = 0
    for r in csv.DictReader((l for l in open(path, encoding="utf-8") if not l.startswith("#")), delimiter="\t"):
        if r.get("relevant", "").strip() == "no" and not r.get("quote", "").strip(): ok += 1; continue
        f = D / (r.get("file") or "")
        if f.exists() and f not in cache: cache[f] = norm(f.read_text(encoding="utf-8", errors="replace"))
        frs = [x for x in re.split(r"…|\.\.\.", norm(r.get("quote", "")).strip('"')) if len(x) >= 12]
        err = "unknown file" if not f.exists() else ("quote empty/too short" if not frs else ("" if all(x in cache[f] for x in frs) else "quote not found"))
        if err: bad += 1; print("BAD", pathlib.Path(path).name, r.get("passage"), err, "|", (r.get("quote") or "")[:70])
        else: ok += 1
    print(f"{path}: ok {ok}, bad {bad}"); total += bad
sys.exit(1 if total else 0)
