#!/usr/bin/env python3
"""Build data/ref/t2087_cb_joined.txt from the CBETA TEI XML, keeping the text's interlinear notes.

Usage (from xuanzang-places/): python3 -I scripts/build_t2087_xml.py
The plain-text CBETA conversion used before dropped all notes, including the text's own interlinear notes (夾註:
唐言…, 舊曰…訛也, 反切). Here: printed Taishō readings are kept (<app> → <lem>; CBETA <choice> → <sic> when present,
else <orig>/<reg> first child), the text's inline notes (<note place="inline">) are kept in full-width brackets
（…）, all other notes (CBETA editorial, variant apparatus) are dropped, gaiji (<g ref="#CB…">) are resolved through
the charDecl (unicode mapping, then normalised form), and page markers [T51:NNNNx] are inserted at <pb>.
"""
import re, xml.etree.ElementTree as ET
X = "/mnt2/kengo/E-texts/10_sources_raw/CBETA/xml-p5/T/T51/T51n2087.xml"
NS = {"tei": "http://www.tei-c.org/ns/1.0", "cb": "http://www.cbeta.org/ns/1.0"}
T = "{http://www.tei-c.org/ns/1.0}"; CB = "{http://www.cbeta.org/ns/1.0}"; XID = "{http://www.w3.org/XML/1998/namespace}id"
root = ET.parse(X).getroot()
gmap = {}
for ch in root.iter(T + "char"):
    cid, val = ch.get(XID), None
    for m in ch.iter(T + "mapping"):
        if m.get("type") == "unicode" and m.text: val = chr(int(m.text.strip()[2:], 16)); break
    if not val:
        for m in ch.iter(T + "mapping"):
            if m.get("type") == "normal_unicode" and m.text: val = chr(int(m.text.strip()[2:], 16)); break
    if not val:
        for p in ch.iter(T + "charProp"):
            if p.findtext(T + "localName") == "normalized form": val = p.findtext(T + "value"); break
    gmap[cid] = val or "□"
out = []
def walk(e):
    tag = e.tag
    if tag == T + "teiHeader": return
    if tag == T + "pb" and e.get("ed", "T") == "T": out.append(f"[T51:{e.get('n')}]")
    if tag == T + "g":
        out.append(gmap.get((e.get("ref") or "#").lstrip("#"), "□")); out.append(e.tail or ""); return
    if tag == T + "note":
        if e.get("place") == "inline":
            out.append("（"); out.append(e.text or "")
            for c in e: walk(c)
            out.append("）")
        out.append(e.tail or ""); return
    if tag in (T + "app",):
        lem = e.find(T + "lem")
        if lem is not None:
            out.append(lem.text or "")
            for c in lem: walk(c)
        out.append(e.tail or ""); return
    if tag == T + "choice":
        pick = e.find(T + "sic")
        if pick is None: pick = e.find(T + "orig")
        if pick is None and len(e): pick = e[0]
        if pick is not None:
            out.append(pick.text or "")
            for c in pick: walk(c)
        out.append(e.tail or ""); return
    if tag in (T + "rdg", CB + "mulu", T + "back", CB + "docNumber", T + "figure"):
        out.append(e.tail or ""); return
    out.append(e.text or "")
    for c in e: walk(c)
    out.append(e.tail or "")
walk(root.find(T + "text"))
t = re.sub(r"\s+", "", "".join(out)).replace("＠", "")
t = t.replace("。", "。\n"); t = re.sub(r"(卷第[一二三四五六七八九十]+)", r"\n\n\1", t)
open("data/ref/t2087_cb_joined.txt", "w", encoding="utf-8").write(t)
print(len(t), "chars;", t.count("（"), "notes;", t.count("□"), "unresolved gaiji")
