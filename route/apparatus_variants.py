#!/usr/bin/env python3
"""Variant readings recorded in the Taishō apparatus of T2087 (CBETA TEI XML) at route sentences.

Usage (from xuanzang-places/): python3 -I route/apparatus_variants.py  -> route/apparatus_variants.tsv
For every apparatus note (type="mod": the CBETA collated reading, e.g. 西【大】，東【宋】【元】【明】【甲】【乙】),
records the lemma, the readings and their witnesses, the sentence it sits in, and the place passage
(data/text/passages*.tsv) that contains the sentence. A note is flagged `route` when its lemma or a reading contains a
direction or a numeral, or its sentence contains 里/行/至 with a numeral. 【大】 = the Korean edition (Taishō base),
【宋】 = the Sixi (思溪) edition of 1132, 【元】【明】 = Yuan and Ming editions, 【甲】【乙】 = Japanese manuscripts.
"""
import re, csv, glob
X = "/mnt2/kengo/E-texts/10_sources_raw/CBETA/xml-p5/T/T51/T51n2087.xml"
s = open(X, encoding="utf-8").read()
notes = {}
for m in re.finditer(r'<note n="(\d+)"[^>]*type="mod"[^>]*>(.*?)</note>', s): notes[m.group(1)] = re.sub(r"<[^>]+>", "", m.group(2))
body = s[s.find("<body>"):]
# plain text with markers at begNNN/endNNN anchors
txt = re.sub(r'<anchor xml:id="beg(\d+)"[^>]*/>', r"⟦\1|", body)
txt = re.sub(r'<anchor xml:id="end(\d+)"[^>]*/>', r"⟧", txt)
txt = re.sub(r"<note[^>]*>.*?</note>", "", txt, flags=re.S)
txt = re.sub(r"<[^>]+>", "", txt); txt = re.sub(r"\s+", "", txt)
P = {}
for f in sorted(glob.glob("data/text/passages*.tsv")):
    for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"): P[r["id"]] = re.sub(r"\s", "", r["zh"])
DIR = set("東西南北"); NUM = set("一二三四五六七八九十百千萬兩數")
rows = []
for m in re.finditer(r"⟦(\d+)\|([^⟦⟧]*)⟧", txt):
    n, lem = m.group(1), m.group(2)
    if n not in notes: continue
    a = txt.rfind("。", 0, m.start()) + 1; b = txt.find("。", m.end()); sent = re.sub(r"⟦\d+\||⟧", "", txt[a:b + 1])
    note = notes[n]
    readings = re.findall(r"([^，【】]+)((?:【[^】]+】)+)", note)
    chars = lem + "".join(r[0] for r in readings)
    route = bool(set(chars) & (DIR | NUM)) or (re.search(r"[里行至]", sent) and bool(set(sent) & NUM) and bool(set(chars) & (DIR | NUM)))
    pid = next((i for i, z in P.items() if sent[:12] and sent[:12] in z), "")
    rows.append(dict(note=n, place=pid, lemma=lem, apparatus=note, route="yes" if route else "", sentence=sent[:120]))
w = csv.DictWriter(open("route/apparatus_variants.tsv", "w", encoding="utf-8", newline=""), list(rows[0]), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(rows)
print(len(rows), "apparatus notes;", sum(1 for r in rows if r["route"]), "touch a direction or numeral;", sum(1 for r in rows if r["route"] and "宋" in r["apparatus"]), "of these with a Song reading")
