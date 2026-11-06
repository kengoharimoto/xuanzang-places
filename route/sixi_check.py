#!/usr/bin/env python3
"""Check the Taishō apparatus's Song readings, and the route figures, against a scan of the Sixi (思溪) edition (1132).

Usage (from xuanzang-places/): python3 -I route/sixi_check.py
Inputs: data/ref/sixi/ocr/pNNNN.txt (Google Vision OCR of the National Diet Library copy, 8 of 12 juan surviving,
scan in the Internet Archive item `datangxiyuji`), the CBETA TEI XML of T2087, route/segments.tsv.
Outputs:
  route/sixi_apparatus.tsv  every apparatus note whose readings touch a direction or numeral: what the scan shows at
                            that spot (the stretch between the matched left and right contexts), and whether it
                            agrees with 【大】 (Korean/Taishō) or 【宋】
  route/sixi_route.tsv      every route sentence with li (route/segments.tsv): its directions and numerals in
                            CBETA and in the scan, flagged where they differ
Matching: OCR text normalised (variant forms → standard), contexts of 8 characters on each side located by
best-scoring fuzzy match (difflib) over the whole scan; a match below 0.6 is reported as not found (lost juan or OCR).
"""
import re, glob, csv, difflib, collections
NORM = str.maketrans("乗敎号竒舎爲旣㝷畧徳羣冣徃顯緣遶麤叅亊卽吿", "乘教號奇舍為既尋略德群最往顯緣繞麁參事即告")
def norm(s): return re.sub(r"[^㐀-鿿\U00020000-\U0002ffff]", "", s.translate(NORM))
S = "".join(norm(open(f, encoding="utf-8").read()) for f in sorted(glob.glob("data/ref/sixi/ocr/p*.txt")))
X = open("/mnt2/kengo/E-texts/10_sources_raw/CBETA/xml-p5/T/T51/T51n2087.xml", encoding="utf-8").read()
notes = {m.group(1): re.sub(r"<[^>]+>", "", m.group(2)) for m in re.finditer(r'<note n="(\d+)"[^>]*type="mod"[^>]*>(.*?)</note>', X)}
body = X[X.find("<body>"):]
t = re.sub(r'<anchor xml:id="beg(\d+)"[^>]*/>', r"⟦\1|", body); t = re.sub(r'<anchor xml:id="end(\d+)"[^>]*/>', "⟧", t)
t = re.sub(r"<note[^>]*>.*?</note>", "", t, flags=re.S); t = re.sub(r"<[^>]+>", "", t)
plain, marks = [], []          # CBETA text (normalised) with the positions of each noted lemma
for m in re.finditer(r"⟦(\d+)\||⟧|.", t, re.S):
    if m.group(0).startswith("⟦"): marks.append([m.group(1), len(plain), None])
    elif m.group(0) == "⟧":
        for mk in reversed(marks):
            if mk[2] is None: mk[2] = len(plain); break
    else:
        c = norm(m.group(0))
        if c: plain.append(c)
C = "".join(plain)
DIR, NUM = set("東西南北"), set("一二三四五六七八九十百千萬兩數減餘")

TRI = collections.defaultdict(list)
for i in range(len(S) - 2): TRI[S[i:i + 3]].append(i)
def locate(ctx, approx=None, near=None):
    """Best fuzzy position of ctx anywhere in S (candidates from shared 3-character substrings); returns (pos, ratio).
    With `near`, only candidates within 40 characters after it are considered."""
    cand = set()
    for k in range(len(ctx) - 2):
        for i in TRI.get(ctx[k:k + 3], []):
            p = i - k
            if p >= 0 and (near is None or 0 <= p - near <= 40): cand.add(p)
    best = (None, 0)
    for i in cand:
        r = difflib.SequenceMatcher(None, ctx, S[i:i + len(ctx)]).ratio()
        if r > best[1]: best = (i, r)
    return best

def scan_reading(a, b):
    """The scan's text between CBETA positions a..b (lemma), via contexts left and right."""
    L, R = C[max(0, a - 6):a], C[b:b + 6]
    approx = int(a / len(C) * len(S))
    L, R = C[max(0, a - 8):a], C[b:b + 8]
    pl, rl = locate(L)
    if pl is None or rl < 0.6: return None, rl
    pr, rr = locate(R, near=pl + len(L))
    if pr is None or rr < 0.6 or pr < pl + len(L) or pr - (pl + len(L)) > (b - a) + 6: return None, min(rl, rr)
    return S[pl + len(L):pr], min(rl, rr)

rows = []
for n, a, b in marks:
    if n not in notes or b is None: continue
    note = notes[n]; lem = C[a:b]
    readings = re.findall(r"([^，【】]+)((?:【[^】]+】)+)", note)
    chars = lem + "".join(r[0] for r in readings)
    if not set(chars) & (DIR | NUM) or "宋" not in note: continue
    song = next((r[0] for r in readings if "宋" in r[1]), "")
    got, q = scan_reading(a, b)
    verdict = "not found" if got is None else ("Song" if norm(song) == got else ("Korean" if got == lem else "other"))
    rows.append(dict(note=n, lemma=lem, song=song, apparatus=note, scan=got or "", match=round(q, 2), agrees_with=verdict,
                     context=C[max(0, a - 12):b + 12]))
w = csv.DictWriter(open("route/sixi_apparatus.tsv", "w", encoding="utf-8", newline=""), list(rows[0]), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(rows)
import collections
print("apparatus notes with Song readings at directions/numerals:", len(rows), collections.Counter(r["agrees_with"] for r in rows))

# route sentences: compare the sequence of directions and numerals
seg = [s for s in csv.DictReader(open("route/segments.tsv", encoding="utf-8"), delimiter="\t") if s["li_lo"]]
out = []
for s in seg:
    sent = norm(re.sub(r"m\d+", "", s["t_route"]))
    if len(sent) < 8: continue
    i = C.find(sent[:10])
    if i < 0: continue
    j = i + len(sent)
    got, q = scan_reading(i + 6, j - 6)   # middle of the sentence, between 6-char contexts
    if got is None: out.append(dict(id=s["id"], cbeta=sent, scan="", match=round(q, 2), differs="not found")); continue
    mid = C[i + 6:j - 6]
    key = lambda z: "".join(ch for ch in z if ch in DIR | NUM)
    out.append(dict(id=s["id"], cbeta=sent, scan=sent[:6] + got + sent[-6:], match=round(q, 2),
                    differs="yes" if key(mid) != key(got) else ""))
w = csv.DictWriter(open("route/sixi_route.tsv", "w", encoding="utf-8", newline=""), list(out[0]), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(out)
print("route sentences:", len(out), collections.Counter(r["differs"] for r in out))
