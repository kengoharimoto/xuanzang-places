#!/usr/bin/env python3
"""Index passages in the ASR reports (data/ref/asr/asrNN.txt, mukherji1901_tarai.txt) that mention Xuanzang or Faxian.

Usage (from xuanzang-places/): python3 -I scripts/asr_hits.py data/asr_hits.tsv [file-glob]
  e.g. python3 -I scripts/asr_hits.py data/ar_hits.tsv "data/ref/asr_annual/*.txt" for the Annual Reports
Hits closer than 1,500 characters are merged into one passage; context = 600 chars before the first hit to 1,400
after the last (whitespace collapsed). `line` = line of the first hit in the source file.
"""
import csv, glob, os, re, sys
PAT = (r"h\s*[iw]\s*[ou]?\s*[eu]?\s*[ae]?n\W{0,3}t?\s*h?\s*[st]\s*h?\s*[ai]?\s*a\s*n\s*g|hiouen|yuan\W{0,3}ch[wu]ang|"
       r"hs[uü]an\W{0,3}tsang|huen\W{0,3}tsang|hiuen|hwen\W{0,3}t|fa\W{0,2}h[ie]+a?n\b|fah\W{0,2}hian|chinese\W{1,3}pilgrim")
RX = re.compile(PAT, re.I)
out = csv.writer(open(sys.argv[1], "w", encoding="utf-8", newline=""), delimiter="\t", lineterminator="\n")
out.writerow(["passage", "file", "line", "n_hits", "context"])
n = 0; per = {}
FILES = sorted(glob.glob(sys.argv[2])) if len(sys.argv) > 2 else sorted(glob.glob("data/ref/asr/asr[0-9]*.txt")) + ["data/ref/asr/mukherji1901_tarai.txt"]
for f in FILES:
    if not os.path.exists(f): continue
    t = open(f, encoding="utf-8", errors="replace").read()
    groups = []
    for m in RX.finditer(t):
        if groups and m.start() - groups[-1][1] < 1500: groups[-1][1] = m.end(); groups[-1][2] += 1
        else: groups.append([m.start(), m.end(), 1])
    for s, e, k in groups:
        n += 1
        out.writerow([n, os.path.basename(f), t.count("\n", 0, s) + 1, k, re.sub(r"\s+", " ", t[max(0, s-600): e+1400]).strip()])
    per[os.path.basename(f)] = len(groups)
print(n, "passages;", per)
