#!/usr/bin/env python3
"""Index passages in the ASR Annual Reports / Circle reports (data/ref/asr_annual/*.txt) that bear on Xiyu ji places.

Usage (from xuanzang-places/): python3 -I scripts/ar_hits.py data/ar_hits.tsv [file-glob] [start-number]
Unlike the Cunningham series, these excavation reports often discuss a site without naming the pilgrim, so a passage
is any stretch mentioning Xuanzang/Faxian OR one of the excavated sites tied to a Xiyu ji place (SITES below).
Hits within 3,000 characters are merged; context = 800 chars before to 2,000 after (whitespace collapsed), capped at
4,000 chars. Passages kept: those naming the pilgrim, or with >= 2 excavation/identification words (SIG).
"""
import csv, glob, os, re, sys
PILGRIM = (r"h\s*[iw]\s*[ou]?\s*[eu]?\s*[ae]?n\W{0,3}t?\s*h?\s*[st]\s*h?\s*[ai]?\s*a\s*n\s*g|hiouen|yuan\W{0,3}ch[wu]ang|"
           r"hs[uü]an\W{0,3}tsang|hiuen|hieun|hiuan|y[iu]{1,2}an\W{0,3}ch|hwen\W{0,3}t|fa\W{0,2}h[ie]+a?n\b|chinese\W{1,3}pilgrim")
SITES = (r"kasia|ku[sś]inaga?ra|matha.?kua?r|sahe?th?.?mahe?th?|[sś]r[aā]vast[iī]|jetavana|s[aā]rn[aā]th|dh[aā]mekh|"
         r"n[aā]land[aā]|r[aā]jgir|r[aā]jag[rṛ]iha|bodh.?gay[aā]|mah[aā]bodhi|basarh|vai[sś][aā]l[iī]|kosam|kau[sś][aā]mb[iī]|"
         r"taxila|sirkap|sirsukh|dharmar[aā]jik[aā]|kun[aā]la|charsadda|pushkal[aā]vat[iī]|shah.?ji.?ki.?dheri|"
         r"takht.?i.?bahi|sahri.?bahlol|jam[aā]lgarhi|mah[aā]sth[aā]n|rangam[aā]ti|r[aā]jb[aā]d[iī]d[aā]ng[aā]|p[aā][tṭ]aliputra|"
         r"kumrahar|bulandi.?bagh|piprahwa|lumbin[iī]|rummindei|tilaura|lauriya|nandangarh|rampurwa|sankisa|ahichchh?atra|"
         r"bhita\b|kesariya|bakhra|kolhua|tilaurakot|ketas|katas|manikiala|manikyala|hadda|begram|tapoban|giriyek|giriak|"
         r"kurkihar|sirpur|n[aā]g[aā]rjunako[nṇ][dḍ]a|amar[aā]vat[iī]|dhara[nṇ]ikota|ajanta|bhinm[aā]l|vadnagar|"
         r"thanesar|sugh\b|bilsar|sanchankot|aphsar|parbati|tillara|kauwa.?dol|dharawat|gurpa|ramabhar|anrudhwa|"
         r"mahaban|malot|ohind|\bund\b|sialkot|mathur[aā]|katra\b|kank[aā]l[iī]|govis[aā][nṇ]a|kashipur|ujain")
SIG = re.compile(r"identif|inscri|\bseal|sealing|copper.?plate|excavat|\bdug\b|digging|trench|stratum|relic.?casket", re.I)
RX = re.compile(f"(?P<p>{PILGRIM})|(?P<s>{SITES})", re.I)
out = csv.writer(open(sys.argv[1], "w", encoding="utf-8", newline=""), delimiter="\t", lineterminator="\n")
out.writerow(["passage", "file", "line", "n_hits", "pilgrim", "sites", "context"])
n = int(sys.argv[3]) if len(sys.argv) > 3 else 0; per = {}   # optional: file glob and starting passage number
for f in sorted(glob.glob(sys.argv[2] if len(sys.argv) > 2 else "data/ref/asr_annual/*.txt")):
    t = open(f, encoding="utf-8", errors="replace").read()
    groups = []
    for m in RX.finditer(t):
        key = "P" if m.group("p") else m.group("s").lower()
        if groups and m.start() - groups[-1][1] < 3000:
            g = groups[-1]; g[1] = m.end(); g[2] += 1; g[3].add(key)
        else: groups.append([m.start(), m.end(), 1, {key}])
    kept = 0
    for s, e, k, keys in groups:
        ctx = re.sub(r"\s+", " ", t[max(0, s-800): e+2000]).strip()
        if "P" not in keys and len(SIG.findall(ctx)) < 2: continue   # keep pilgrim passages, or sites with excavation/identification signals
        n += 1; kept += 1
        out.writerow([n, os.path.basename(f), t.count("\n", 0, s) + 1, k, "yes" if "P" in keys else "",
                      ";".join(sorted(x for x in keys if x != "P"))[:200], ctx[:4000]])
    per[os.path.basename(f)] = kept
print(n, "passages"); print(per)
