#!/usr/bin/env python3
"""Search the Sanskrit e-text library for a name form, without diacritics.

Usage (from xuanzang-places/): python3 scripts/skt_search.py REGEX [MAX_HITS] [PATH_FILTER]
REGEX runs on the normalised text (data/ref/skt_norm/, scripts/skt_norm.py): lowercase a-z, words separated by single
spaces, so 'parnotsa' finds Parṇotsa and 'kasmir' finds Kaśmīra/kāśmīrāḥ inside compounds. PATH_FILTER (a substring of
the relative path, e.g. 3_purana or 7_inscriptions) narrows the search. Output: hit count per file, then up to MAX_HITS
(default 30) hits as `path:line` with the ORIGINAL line from /mnt2/kengo/E-texts/1_sanskr (trimmed to 200 chars).
"""
import os, re, sys, collections
SRC = "/mnt2/kengo/E-texts/1_sanskr"; DST = "data/ref/skt_norm"
rx = re.compile(sys.argv[1]); mx = int(sys.argv[2]) if len(sys.argv) > 2 else 30; flt = sys.argv[3] if len(sys.argv) > 3 else ""
hits, cnt = [], collections.Counter()
for root, dirs, files in os.walk(DST):
    for f in sorted(files):
        p = os.path.join(root, f); rel = os.path.relpath(p, DST)
        if flt not in rel: continue
        for i, l in enumerate(open(p), 1):
            if rx.search(l): cnt[rel] += 1; hits.append((rel, i))
print(f"{sum(cnt.values())} hits in {len(cnt)} files")
for rel, c in cnt.most_common(25): print(f"  {c:5}  {rel}")
cache = {}
for rel, i in hits[:mx]:
    if rel not in cache:
        try: cache[rel] = open(os.path.join(SRC, rel), encoding="utf-8").read().split("\n")
        except UnicodeDecodeError: cache[rel] = open(os.path.join(SRC, rel), encoding="latin-1").read().split("\n")
    print(f"{rel}:{i}: {cache[rel][i-1].strip()[:200]}")
