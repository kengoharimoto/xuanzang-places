#!/usr/bin/env python3
"""Line-aligned, diacritic-free copy of the Sanskrit e-text library, for name searching (read-only on the library).

Usage (from xuanzang-places/): python3 scripts/skt_norm.py   -> data/ref/skt_norm/<same relative path>.txt (gitignored)
Source: /mnt2/kengo/E-texts/1_sanskr (40_tools, _trash, _notes skipped). Files mostly IAST; a file with many more
Harvard-Kyoto markers than IAST letters is converted with the library's own converter (sanskrit-etexts skill,
arlo2iast.py, 'plain' mode) first. Normalisation: lowercase; ā→a ī→i ū→u ṛ/ṝ→r ḷ→l ṃ/ṁ→m ḥ→h ṅ/ñ/ṇ→n ṭ→t ḍ→d ś/ṣ→s;
combining marks dropped; everything not a-z becomes a space. Line numbers are kept, so a hit maps to the original line.
"""
import os, sys, unicodedata, re
SRC = "/mnt2/kengo/E-texts/1_sanskr"; DST = "data/ref/skt_norm"
SK = [d for d in [os.path.expanduser("~/.claude/skills/synced")] if os.path.isdir(d)]
conv = None
for root, dirs, files in os.walk(SK[0]) if SK else []:
    if "arlo2iast.py" in files: sys.path.insert(0, root); from arlo2iast import convert_arlo as conv; break
MAP = str.maketrans({"ā": "a", "ī": "i", "ū": "u", "ṛ": "r", "ṝ": "r", "ḷ": "l", "ṃ": "m", "ṁ": "m", "ḥ": "h", "ṅ": "n",
                     "ñ": "n", "ṇ": "n", "ṭ": "t", "ḍ": "d", "ś": "s", "ṣ": "s"})
def norm(line):
    s = unicodedata.normalize("NFC", line.lower()).translate(MAP)
    s = "".join(c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c))
    return re.sub(r"[^a-z]+", " ", s)
n = 0
for root, dirs, files in os.walk(SRC):
    dirs[:] = [d for d in dirs if d not in ("40_tools", "_trash", "_notes")]
    for f in files:
        if not f.endswith(".txt"): continue
        p = os.path.join(root, f)
        try: t = open(p, encoding="utf-8").read()
        except UnicodeDecodeError: t = open(p, encoding="latin-1").read()
        iast = sum(t.count(c) for c in "āīūṛṃṭḍṇṣśñṅḥ"); hk = sum(t.count(s) for s in (".m", ".s", ".t", ".n", "aa", "ii", '"s'))
        if conv and hk > 3 * iast and hk > 50: t = conv(t, mode="plain")
        out = os.path.join(DST, os.path.relpath(p, SRC)); os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w").write("\n".join(norm(l) for l in t.split("\n"))); n += 1
print(n, "files normalised")
