#!/usr/bin/env python3
"""Index every mention of Xuanzang (old spellings), 'Chinese pilgrim' and Faxian in the gazetteer OCR.

Usage (from the research root): python3 -I xuanzang-places/scripts/gaz_hits.py xuanzang-places/data/gaz_hits.tsv
Scans */data/ia_ocr/*.txt under gazetteer-vedanta/ and yoga-gazetteers/; metadata from selection*.tsv and
ia_candidates.tsv. One row per hit; hits closer than 300 chars in the same file are merged.
"""
import csv, glob, re, sys, os
ROOTS = ["gazetteer-vedanta", "yoga-gazetteers"]
PAT = {
    "xuanzang": r"h\s*[iw]\s*[ou]?\s*[eu]?\s*[ae]?n\W{0,3}t?\s*h?\s*[st]\s*h?\s*[ai]?\s*a\s*n\s*g|hiouen|yuan\W{0,3}ch[wu]ang|hs[uü]an\W{0,3}tsang|huen\W{0,3}tsang|hiuen|hwen\W{0,3}t",
    "chinese_pilgrim": r"chinese\W{1,3}(?:buddhist\W{1,3})?(?:pilgrim|traveller|traveler)s?",
    "faxian": r"fa\W{0,2}h[ie]+a?n\b|fah\W{0,2}hian",
}
RX = re.compile("|".join(f"(?P<{k}>{v})" for k, v in PAT.items()), re.I)
meta = {}
for root in ROOTS:
    for f in glob.glob(f"{root}/**/data/ia_candidates.tsv", recursive=True):
        for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
            meta.setdefault(r["identifier"], {}).update(title=r.get("title", ""), year=r.get("year", ""))
    for f in glob.glob(f"{root}/**/data/selection*.tsv", recursive=True):
        for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
            place = r.get("district") or r.get("region") or r.get("volume") or ""
            if r.get("region") and r.get("district"): place = f'{r["region"]}: {r["district"]}'
            for key in ("primary", "backup", "ia"):
                if r.get(key):
                    meta.setdefault(r[key], {}).update(vol=r.get("vol") or r.get("id", ""), place=place,
                        year=r.get("year", ""), series=r.get("note", "") or r.get("kind", ""), study=f)
files = sorted(set(glob.glob("gazetteer-vedanta/*/data/ia_ocr/*.txt") + glob.glob("yoga-gazetteers/*/data/ia_ocr/*.txt")))
seen = {}
out = csv.writer(open(sys.argv[1], "w", encoding="utf-8", newline=""), delimiter="\t", lineterminator="\n")
out.writerow(["hit", "identifier", "vol", "place", "year", "series", "kind", "match", "line", "context"])
n = 0
for f in files:
    ident = os.path.basename(f)[:-4]
    if ident in seen: continue
    seen[ident] = f
    t = open(f, encoding="utf-8", errors="replace").read()
    m_ = meta.get(ident, {})
    last = -10**9
    for m in RX.finditer(t):
        if m.start() - last < 300: continue
        last = m.start()
        kind = m.lastgroup
        ctx = re.sub(r"\s+", " ", t[max(0, m.start()-500): m.end()+700]).strip()
        n += 1
        out.writerow([n, ident, m_.get("vol", ""), m_.get("place", "") or m_.get("title", "")[:80], m_.get("year", ""),
                      m_.get("series", ""), kind, re.sub(r"\s+", " ", m.group(0)), t.count("\n", 0, m.start()) + 1, ctx])
print(f"{len(seen)} volumes scanned, {n} hits")
