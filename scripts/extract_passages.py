#!/usr/bin/env python3
"""Cut T2087 into one passage per place from start anchors.

Usage (from xuanzang-places/): python3 -I scripts/extract_passages.py data/text/anchors_<range>.tsv  -> data/text/passages_<range>.tsv
       python3 -I scripts/extract_passages.py data/text/anchors_*.tsv      (all files) -> data/text/passages.tsv
anchors_*.tsv columns: id, mode, anchor, end_anchor, note
  mode = segment: the passage runs from `anchor` (verbatim T2087 text, >= 6 chars, unique after the previous segment's
                  anchor) to the next segment's anchor, or to `end_anchor` if given (inclusive).
  mode = excerpt: the place is only mentioned inside another passage; `anchor` is the start and `end_anchor` the end
                  (inclusive) of the sentence(s) that mention it.
Matching ignores whitespace and text is CBETA T2087 with real characters (no gaiji codes). Page refs [T51:NNNNx] are
recorded as `t_ref` (the page where the passage starts) and stripped from the text.
"""
import csv, glob, re, sys
raw = open("data/ref/t2087_cb_joined.txt", encoding="utf-8").read().replace("\n", "")
# position map: text without page markers, plus the page at each position
txt, pages, cur = [], [], ""
for m in re.finditer(r"\[T51:(\d+[abc])\]|.", raw, re.S):
    if m.group(1): cur = m.group(1); continue
    txt.append(m.group(0)); pages.append(cur)
T = "".join(txt)
rows = [r for f in sorted(sys.argv[1:]) for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t")]
def find(a, start=0):
    a = re.sub(r"\s+", "", a or "")
    if len(a) < 4: return -1   # empty or too-short anchors are errors
    i = T.find(a, start)
    return i
segs, out, errs = [], {}, []
pos = 0
for r in rows:   # anchors files are in master-table order; segments must appear in text order
    if r["mode"] != "segment": continue
    i = find(r["anchor"], pos)
    if i < 0: i = find(r["anchor"])
    if i < 0: errs.append(f'{r["id"]}: anchor not found: {r["anchor"][:20]}'); continue
    segs.append((i, r)); pos = i
segs.sort(key=lambda x: x[0])
for n, (i, r) in enumerate(segs):
    j = segs[n+1][0] if n + 1 < len(segs) else len(T)
    if r.get("end_anchor"):
        e = find(r["end_anchor"], i)
        if 0 <= e < len(T): j = min(j, e + len(re.sub(r"\s+", "", r["end_anchor"])))
    out[r["id"]] = ("segment", T[i:j], pages[i])
for r in rows:
    if r["mode"] != "excerpt": continue
    i = find(r["anchor"])
    if i < 0: errs.append(f'{r["id"]}: excerpt anchor not found: {r["anchor"][:20]}'); continue
    e = find(r["end_anchor"], i) if r.get("end_anchor") else -1
    j = e + len(re.sub(r"\s+", "", r["end_anchor"])) if e >= 0 else T.find("。", i) + 1
    out[r["id"]] = ("excerpt", T[i:j], pages[i])
import os
outp = "data/text/passages.tsv" if len(sys.argv) > 2 else "data/text/" + os.path.basename(sys.argv[1]).replace("anchors_", "passages_")
w = csv.DictWriter(open(outp, "w", encoding="utf-8", newline=""), ["id", "mode", "t_ref", "zh"], delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows({"id": i, "mode": m, "t_ref": "T51:" + ref, "zh": zh} for i, (m, zh, ref) in sorted(out.items()))
prev = out
print(len(out), "passages from", len(rows), "anchors ->", outp)
print("\n".join(errs) or "no errors")
