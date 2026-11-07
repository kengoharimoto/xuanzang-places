#!/usr/bin/env python3
"""The study's proposed original forms: data/names/proposed.tsv.

Usage (from xuanzang-places/): python3 -I scripts/names_proposed.py
Sources: the Bactrian check (data/names/bactrian.tsv, appended to the basis), the pilot tests (data/names/test_*.tsv; verdict better / alternative / doubtful) and the key's list of
Mizutani forms that conflict with Xuanzang's transcription (data/names/key_notes.md §8, the CONFLICTS below).
Columns: id, name_study (the form the study proposes; '?' where every form fails), verdict, confidence, basis (one line),
source (test file or key_notes §8).
"""
import csv, glob
rd = lambda f: list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
CONFLICTS = {   # key_notes.md §8
    "01.01c": "vakṣu (縛 is v-)", "01.20.02": "Tukhāra (貨 is kh, not ṣ)", "03.01": "Uḍḍiyāna (仗 is retroflex)",
    "03.05": "Uraśā (尸 is ś)", "04.12": "Goviṣāṇa (霜 is ṣ)", "05.02": "Ayodhā (no character for -y-)",
    "07.03.12": "Licchava (婆 is never vi)", "08.04.01": "Telāḍhaka (擇 is retroflex)", "10.06.02c": "Dvārapati (鉢 never renders va)",
    "10.07": "Tāmalitti (Pkt.; Xuanzang writes the vernacular form)", "11.12": "Ujjayana (那 gives -na)", "02.02": "Lampa (only lampa is transcribed)"}
MZ_LISTS = {"01.01c", "01.20.02", "03.01", "04.12", "05.02", "08.04.01", "10.06.02c", "10.07", "11.12"}   # Mizutani gives the fitting form himself
out = []
for f in sorted(glob.glob("data/names/test_*.tsv")):
    for r in rd(f):
        if r["verdict"] not in ("better", "alternative", "doubtful"): continue
        out.append({"id": r["id"], "name_study": r["proposed_form"] or "?", "verdict": r["verdict"], "confidence": r["confidence"],
                    "basis": (r["attestation"] or r["key_fit"])[:200], "source": f})
seen = {o["id"] for o in out}
for i, v in CONFLICTS.items():
    if i in seen: continue
    form, why = v.split(" (", 1)
    among = i in MZ_LISTS
    out.append({"id": i, "name_study": form, "verdict": "key", "confidence": "medium",
                "basis": ("Mizutani lists this form among his alternatives; the key selects it: " if among else "Xuanzang's transcription: ") + why.rstrip(")"),
                "source": "data/names/key_notes.md §8"})
# Bactrian forms (Sims-Williams, BDNA I-II; data/names/bactrian.tsv): confirm, improve or contradict
byid = {o["id"]: o for o in out}
for r in rd("data/names/bactrian.tsv"):
    if r["verdict"] not in ("confirms", "better", "no-fit"): continue
    note = f'Bactrian {r["bactrian_form"]} ({r["gloss_ref"]}): {r["verdict"]}'
    o = byid.get(r["id"])
    if o:
        o["basis"] = (o["basis"] + "; " + note)[:300]; o["source"] += "; data/names/bactrian.tsv"
        if r["verdict"] in ("better", "confirms") and r["proposed_form"]: o["name_study"] = r["proposed_form"]
    elif r["verdict"] in ("confirms", "better"):
        o = {"id": r["id"], "name_study": r["proposed_form"] or r["bactrian_form"], "verdict": "bactrian-" + r["verdict"],
             "confidence": "medium", "basis": note, "source": "data/names/bactrian.tsv"}
        out.append(o); byid[r["id"]] = o
out.sort(key=lambda o: o["id"])
w = csv.DictWriter(open("data/names/proposed.tsv", "w", encoding="utf-8", newline=""), list(out[0]), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(out); print(len(out), "proposed forms")
