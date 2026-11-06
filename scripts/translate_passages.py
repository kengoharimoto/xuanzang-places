#!/usr/bin/env python3
"""Translate each place's T2087 passage with DharmaMitra's public cat-translate API.

Usage (from xuanzang-places/): python3 -I scripts/translate_passages.py [passages_file.tsv] [--limit N]
       python3 -I scripts/translate_passages.py data/text/life_passages.tsv   (the Life -> life_translation_dm.tsv)
Input: data/text/passages.tsv (id, mode, t_ref, zh). Output (appended, resumable): data/text/translation_dm.tsv
(id, en, chunks, model, date). Each passage is split at sentence ends into chunks of <= 320 characters; each call's
`context` gives the work, the place, a glossary of the master table's names that occur in the chunk (Chinese name =
original name), and the end of the previous chunk's English, so names and voice stay consistent.
Endpoint: https://dharmamitra.org/api-search/cat-translate/v1/translate (public; see
/mnt2/kengo/dharmamitra-claude-code-agent/CLAUDE.md). Run one stream at a time: the public endpoint rate-limits (HTTP 429); the script pauses 1.5 s between calls and
waits a minute after a 429.
"""
import csv, json, re, sys, time, datetime, urllib.request, urllib.error
URL = "https://dharmamitra.org/api-search/cat-translate/v1/translate"
STYLE = ("academic register: faithful and complete, plain modern English; translate every clause; keep Xuanzang's "
         "measures (li, paces, feet), numbers and directions exactly as written; give the Sanskrit or original name with "
         "the Chinese in parentheses on first occurrence, e.g. 'the country of Kapiśa (迦畢試國)', then the Sanskrit form; "
         "render interlinear notes in round brackets as '(Original note: ...)'; no commentary, no headings")
lim = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 10**9
M = list(csv.DictReader(open("data/places_mizutani.tsv", encoding="utf-8"), delimiter="\t"))
gloss = {}
for r in M:
    zh = re.sub(r"[（(].*?[）)]|\s", "", r["name_zh"])
    if len(zh) >= 2 and r["original_name"]: gloss.setdefault(zh, re.sub(r"\s*\(OCR[^)]*\)", "", r["original_name"])[:80])
names = {r["id"]: r["name_zh"] for r in M}
SRC = next((a for a in sys.argv[1:] if a.endswith(".tsv")), "data/text/passages.tsv")
P = list(csv.DictReader(open(SRC, encoding="utf-8"), delimiter="\t"))
LIFE = "life_passages" in SRC   # the Life (T2053) -> data/text/life_translation_dm.tsv
OUT = "data/text/life_translation_dm.tsv" if LIFE else "data/text/translation_dm.tsv"
done = set()
try: done = {r["id"] for r in csv.DictReader(open(OUT, encoding="utf-8"), delimiter="\t")}
except FileNotFoundError:
    open(OUT, "w", encoding="utf-8").write("id\ten\tchunks\tmodel\tdate\n")
def chunks(t, n=320):
    sents = [s for s in re.split(r"(?<=[。！？])", t) if s.strip()]
    out, cur = [], ""
    for s in sents:
        if cur and len(cur) + len(s) > n: out.append(cur); cur = ""
        cur += s
    if cur: out.append(cur)
    return out
def call(body):
    for attempt in range(8):
        try:
            req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
            return json.load(urllib.request.urlopen(req, timeout=100))["translation"].strip()
        except urllib.error.HTTPError as e:
            err = e; time.sleep(60 if e.code == 429 else 10 * (attempt + 1))   # rate-limited: wait a minute
        except Exception as e:
            err = e; time.sleep(10 * (attempt + 1))
    raise err
n = 0
for p in P:
    if p["id"] in done or not p["zh"].strip(): continue
    if n >= lim: break
    prev, parts = "", []
    for c in chunks(p["zh"]):
        g = "; ".join(f"{k} = {v}" for k, v in gloss.items() if k in c)[:900]
        ctx = (f"Source: {'Huili and Yancong, Life of Xuanzang (Da Ci’en si sanzang fashi zhuan, T2053)' if LIFE else 'Xuanzang, Da Tang Xiyu ji (T2087)'}, {p['t_ref']}. Place: {names.get(p['id'], '')}. "
               + (f"Names: {g}. " if g else "") + (f"Preceding translation: ...{prev[-500:]}" if prev else ""))
        en = call({"input_chinese": c, "context": ctx, "focus": "chinese", "target_language": "english", "style_instruction": STYLE})
        parts.append(en); prev = en; time.sleep(1.5)
    with open(OUT, "a", encoding="utf-8") as f:
        f.write("\t".join([p["id"], " ".join(parts).replace("\t", " ").replace("\n", " "), str(len(parts)),
                           "DharmaMitra cat-translate", datetime.date.today().isoformat()]) + "\n")
    n += 1
    print(p["id"], len(p["zh"]), "chars,", len(parts), "chunks", flush=True)
print("translated", n)
