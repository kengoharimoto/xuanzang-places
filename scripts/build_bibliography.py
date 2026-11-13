#!/usr/bin/env python3
"""The study's bibliography as a page: BIBLIOGRAPHY.html.

Usage (from xuanzang-places/): python3 -I scripts/build_bibliography.py
Inputs:
  data/bibliography.tsv      texts, translations, authorities, surveys, geographers, names, sources used to test
                             K. Harimoto's notes, map data (hand-kept)
  data/ref/asr, asr_annual, iar, epig (file names)   the survey and epigraphy series, volume by volume
  data/gaz_hits.tsv, data/coded/gaz_batch*.tsv       gazetteers: 557 searched, those with passages listed
  data/literature.tsv, data/coded/lit_batch*.tsv     scholarship since 1985: read (coded or used) vs not yet read
Counts printed and written into the page; FINDINGS.html quotes them ("Sources and method").
"""
import csv, glob, html, os, re, collections

E = html.escape
def md(s):   # *italic* -> <i>, after escaping
    return re.sub(r"\*([^*]+)\*", r"<i>\1</i>", E(s))
def rows(f): return list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"))
def link(u): return f' <a href="{E(u)}" target="_blank" rel="noopener">link</a>' if u else ""

hand = rows("data/bibliography.tsv")

# --- series, volume by volume, from the files the study read
def vols(d, pat, fmt):
    return sorted(fmt(m) for f in os.listdir(d) if (m := re.fullmatch(pat, f)))
ROMAN = lambda n: ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI",
                   "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII"][n]
asr = [ROMAN(int(m)) for m in sorted(re.fullmatch(r"asr(\d\d)\.txt", f).group(1) for f in os.listdir("data/ref/asr") if re.fullmatch(r"asr\d\d\.txt", f))]
ar = vols("data/ref/asr_annual", r"ar(\d{4}-\d\d)\.txt", lambda m: m.group(1).replace("-", "–"))
ec = vols("data/ref/asr_annual", r"ec(\d{4}-\d\d)\.txt", lambda m: m.group(1).replace("-", "–"))
iar = vols("data/ref/iar", r"iar(\d{4}-\d\d)\.txt", lambda m: m.group(1).replace("-", "–"))
ei = sorted({int(m.group(1)) for f in os.listdir("data/ref/epig") if (m := re.fullmatch(r"ei_(\d\d).*\.txt", f))})
cii = vols("data/ref/epig", r"cii_(.+)\.txt", lambda m: m.group(1).replace("-", "."))
series = [
    ("Archaeological Survey of India, <i>Reports</i>, by A. Cunningham, J. D. Beglar, A. C. L. Carlleyle and H. B. W. Garrick. "
     "1871–87; with V. A. Smith, <i>General Index</i> (1887)", "vols. " + ", ".join(asr), len(asr) + 1,
     "Searched for every place; passages coded."),
    ("Archaeological Survey of India, <i>Annual Report</i>", ", ".join(ar), len(ar), "Searched; passages coded."),
    ("Archaeological Survey of India, Eastern Circle (Bengal), <i>Annual Report</i>", ", ".join(ec), len(ec), "Searched; passages coded."),
    ("Archaeological Survey of India, <i>Indian Archaeology – A Review</i>", ", ".join(iar), len(iar),
     "Searched for every place; passages coded. Re-OCR'd with Surya; 2007–14 from the ASI Aurangabad Circle's PDFs."),
    ("<i>Epigraphia Indica</i>", "vols. " + ", ".join(map(str, ei)), len(ei), "Searched; inscriptions coded."),
    ("<i>Corpus Inscriptionum Indicarum</i>", "vols. " + ", ".join(cii) + " (vol. 3 in D. R. Bhandarkar's revised edition)", len(cii),
     "Searched; inscriptions coded."),
]

# --- gazetteers
hits = rows("data/gaz_hits.tsv")
coded_gaz = collections.Counter()
for f in glob.glob("data/coded/gaz_batch*.tsv"):
    for r in rows(f):
        if r.get("relevant") == "yes": coded_gaz[r["hit"]] += 1
hit_id = {r["hit"]: r["identifier"] for r in hits}
used_ids = collections.Counter(hit_id[h] for h in coded_gaz if h in hit_id)
def clean_series(s):
    s = s.split(";")[0].strip()
    return "" if s.startswith("region=") or s.startswith("backup") or "identify" in s else s
gaz = {}
for r in hits:
    if r["identifier"] in used_ids and r["identifier"] not in gaz:
        gaz[r["identifier"]] = (r["place"], r["year"], clean_series(r["series"]))
gaz_searched = 557

# --- literature since 1985
L, seen = [], set()
for r in rows("data/literature.tsv"):
    if r["key"] not in seen: seen.add(r["key"]); L.append(r)
byfile = {r["file"].split("/")[-1]: r["key"] for r in L if r["file"]}
coded_lit = set()
for f in glob.glob("data/coded/lit_batch*.tsv"):
    for r in rows(f):
        k = byfile.get(r["file"].split("/")[-1])
        if k: coded_lit.add(k)
EXTRA_READ = {"kuwayama1999_kapisi_kabul", "simswilliams2002_guzgan"}   # read to test K. Harimoto's notes
SKIP = lambda r: r["key"].startswith("li1996") or r["key"].startswith("lirongxi1996") or r["key"] == "iar_online_2006_2014"
IN_IAR = lambda r: r["status"].startswith("in study (data/ref/iar")   # reports inside the IAR volumes above
iar_reports = [r for r in L if IN_IAR(r) and not SKIP(r)]
read = [r for r in L if not SKIP(r) and not IN_IAR(r) and (r["key"] in coded_lit or r["key"] in EXTRA_READ or r["status"].startswith("in study"))]
unread = [r for r in L if not SKIP(r) and not IN_IAR(r) and r not in read]
IS_LI = lambda r: r["key"].startswith("li1996") or r["key"].startswith("lirongxi1996")
n_items = sum(not IS_LI(r) for r in L) + 1   # Li Rongxi 1996 is entered under four keys
GROUP = {"A": "Central Asia and the return (juans 1 and 12)", "B": "Afghanistan, the North-West and Kashmir (juans 2–3)",
         "C": "The Ganges plain (juans 4–7)", "D": "Magadha (juans 8–9)", "E": "Eastern, southern and western India (juans 10–11)",
         "X": "General"}

series[3] = series[3][:3] + (series[3][3] + f" With them, {len(iar_reports)} excavation reports of 1985–2014 found in the search for later scholarship.",)
# --- counts
n_hand = len(hand)
n_series_vols = sum(s[2] for s in series)
n_gaz_used = len(gaz)
n_read = len(read)
works = n_hand + len(series) + n_gaz_used + n_read          # each series counted once
volumes = n_hand + n_series_vols + n_gaz_used + n_read
print(dict(hand=n_hand, series=len(series), series_volumes=n_series_vols, gazetteers_used=n_gaz_used,
           gazetteers_searched=gaz_searched, lit_read=n_read, lit_unread=len(unread), works=works, volumes=volumes, lit_items=n_items))

# --- page
SECT = [("text", "The text and its witnesses"), ("translation", "Translations"),
        ("authority", "Identifications: the commentators and Kuwayama"), ("survey", "Surveys, tours and early epigraphy"),
        ("iran", "Historical geography of Iran, Central Asia and the North-West"), ("names", "Names"),
        ("obs", "Sources used to test K. Harimoto's notes"), ("data", "Map and terrain data")]
def item(cit, use, url=""):
    return f'<li><span class="cit">{cit}</span>{link(url)}<span class="use">{md(use)}</span></li>'
out = []
for key, title in SECT:
    its = [r for r in hand if r["section"] == key]
    out.append(f'<section><h2>{title}</h2><ul class="bib">' +
               "".join(item(md(r["citation"]), r["use"], r["url"]) for r in its) + "</ul></section>")
    if key == "survey":
        out.append('<section><h2>Survey reports and inscriptions, by series</h2><ul class="bib">' +
                   "".join(item(f"{c}: {E(v)}.", use + f" {n} volume{'s' if n > 1 else ''}.") for c, v, n, use in series) +
                   "</ul></section>")
gl = sorted(gaz.items(), key=lambda kv: (kv[1][0], kv[1][1]))
out.insert(5, f'''<section><h2>Gazetteers</h2>
<p>The {gaz_searched} British Indian district and provincial gazetteers, census reports and glossaries assembled for two
earlier studies (on Vedānta and on yoga in the gazetteers) were searched for Xuanzang's places; {n_gaz_used} volumes had passages
that were coded, listed here. The Baluchistan gazetteers (1906–08) and the Hazara gazetteers were added for this study.</p>
<details><summary>{n_gaz_used} volumes with coded passages</summary><ul class="bib gaz">''' +
    "".join(f'<li><span class="cit">{E(p)} ({E(y)}){", " + E(s) if s else ""}.</span>'
            f' <a href="https://archive.org/details/{E(i)}" target="_blank" rel="noopener">archive.org</a></li>' for i, (p, y, s) in gl) +
    "</ul></details></section>")
def litlist(rs):
    g = collections.defaultdict(list)
    for r in rs: g[r["group"]].append(r)
    s = ""
    for k in "ABCDEX":
        if g[k]:
            s += f'<h3>{GROUP[k]} <span class="n">{len(g[k])}</span></h3><ul class="bib">' + "".join(
                f'<li><span class="cit">{E(r["citation"])}</span>{link(r["url"])}</li>'
                for r in sorted(g[k], key=lambda r: (r["year"] or "9999", r["citation"]))) + "</ul>"
    return s
out.append(f'<section><h2>Scholarship since 1985</h2><p>A bibliography of {n_items} later items was built region by region in '
           f'English, Japanese, Chinese and European languages. The {n_read} read for the study (coded, or used for a particular '
           f'question) are listed here by the part of the text they bear on.</p>' + litlist(read) + "</section>")
out.append(f'<section><h2>Found but not yet read</h2><p>The other {len(unread)} items: books and paywalled articles still '
           f'wanted, free items not yet fetched, and items of low relevance not sought.</p><details><summary>Show the '
           f'{len(unread)} items</summary>' + litlist(unread) + "</details></section>")

page = open("scripts/bibliography_template.html", encoding="utf-8").read()
page = (page.replace("{{WORKS}}", f"{works:,}").replace("{{VOLUMES}}", f"{volumes:,}").replace("{{READ}}", str(n_read))
        .replace("{{SERIESVOLS}}", str(n_series_vols)).replace("{{GAZ}}", str(n_gaz_used)).replace("{{GAZALL}}", str(gaz_searched))
        .replace("{{HAND}}", str(n_hand)).replace("{{GAZNONE}}", str(gaz_searched - n_gaz_used)).replace("{{UNREAD}}", str(len(unread))).replace("{{BODY}}", "\n".join(out)))
open("BIBLIOGRAPHY.html", "w", encoding="utf-8").write(page)
