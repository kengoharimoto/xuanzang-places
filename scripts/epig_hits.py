#!/usr/bin/env python3
"""Index passages in Epigraphia Indica / CII (data/ref/epig/*.txt) that bear on Xiyu ji places.

Usage (from xuanzang-places/): python3 -I scripts/epig_hits.py data/epig_hits.tsv
Two channels, merged when within 2,000 characters:
  P = a mention of Xuanzang / Faxian / "the Chinese pilgrim";
  N = the Sanskrit name of a disputed, uncertain or revised place (master table `original_name`, places with a
      note in data/notes/updates_*.tsv whose change != none, or mz_status != agreed), within 300 chars of an
      identification word (identif-, identical, modern, now called, site of).
Names are matched with diacritics stripped. Context: 700 chars before to 1,800 after, capped at 4,000.
"""
import csv, glob, os, re, sys, unicodedata
fold = lambda s: "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)).lower()
PIL = re.compile(r"h\s*[iw]\s*[ou]?\s*[eu]?\s*[ae]?n\W{0,3}t?\s*h?\s*[st]\s*h?\s*[ai]?\s*a\s*n\s*g|hiouen|hieun|yuan\W{0,3}ch[wu]ang|"
                 r"hs[uü]an\W{0,3}tsang|hiuen|hwen\W{0,3}t|fa\W{0,2}h[ie]+a?n\b|chinese\W{1,3}pilgrim", re.I)
IDW = re.compile(r"identif|identical|\bmodern\b|now called|site of", re.I)
M = {r["id"]: r for r in csv.DictReader(open("data/places_mizutani.tsv", encoding="utf-8"), delimiter="\t")}
want = {i for i, r in M.items() if r["mz_status"] != "agreed"}
for f in glob.glob("data/notes/updates_*.tsv"):
    want |= {r["id"] for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t") if r["change"] != "none"}
STOP = set("""skt pali prakrit sanskrit maybe perhaps other chinese tibetan iranian turkic persian arabic greek
cunningham watters beal julien vivien mizutani majumdar ptolemy stein foucher marshall telugu tamil kanarese kannada
ganga gangā grama narayana asoka buddha bodhisattva later great names original follows proposed light water forest
island lotus personal conjecture unknown monastery pillar mount mountain river south north east west""".split())
names = {}
for i in want:
    for tok in re.findall(r"[A-ZĀ-ŞḀ-Ỹ][A-Za-zĀ-ſḀ-ỿ\-]{4,}", M[i]["original_name"]):
        t = fold(tok).strip("-")
        if t in STOP: continue
        names.setdefault(t, set()).add(i)
NRX = re.compile(r"\b(" + "|".join(sorted(map(re.escape, names), key=len, reverse=True)) + r")\b")
out = csv.writer(open(sys.argv[1], "w", encoding="utf-8", newline=""), delimiter="\t", lineterminator="\n")
out.writerow(["passage", "file", "line", "pilgrim", "names", "candidate_ids", "context"])
n = 0; per = {}
for f in sorted(glob.glob("data/ref/epig/*.txt")):
    raw = open(f, encoding="utf-8", errors="replace").read(); low = fold(raw)
    hits = [(m.start(), m.end(), "P", "") for m in PIL.finditer(raw)]
    for m in NRX.finditer(low):
        if IDW.search(low[max(0, m.start()-300): m.end()+300]): hits.append((m.start(), m.end(), "N", m.group(1)))
    hits.sort(); groups = []
    for s, e, k, nm in hits:
        if groups and s - groups[-1][1] < 2000:
            g = groups[-1]; g[1] = max(g[1], e); g[2].add(k); nm and g[3].add(nm)
        else: groups.append([s, e, {k}, {nm} - {""}])
    for s, e, ks, nms in groups:
        n += 1
        ids = sorted({i for nm in nms for i in names.get(nm, ())})
        out.writerow([n, os.path.basename(f), raw.count("\n", 0, s) + 1, "yes" if "P" in ks else "", ";".join(sorted(nms)),
                      ";".join(ids), re.sub(r"\s+", " ", raw[max(0, s-700): e+1800]).strip()[:4000]])
    per[os.path.basename(f)[:-4]] = len(groups)
print(n, "passages; names searched:", len(names)); print(per)
