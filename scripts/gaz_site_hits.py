#!/usr/bin/env python3
"""Site-name search in the gazetteer OCR (used for Mirchandani's Sindh/Baluchistan sites, 2026-11-06).
Usage (from the research root): python3 -I xuanzang-places/scripts/gaz_site_hits.py <out.tsv>
Keeps a hit when its context has >= 2 antiquity words (SIG). Selected rows were appended to data/gaz_hits.tsv
as hits 1966-1971 (kind "site") and coded in data/coded/gaz_batch9.tsv."""
import glob,re,csv,sys,collections
SITES=r"\bmithankot\b|\bmithan\s?kot\b|\blas\s?bela\b|\bgondakahar\b|\bgonda\s?kahar\b|\barmab[eī]l\b|\barmanbel\b|\bkasarkand\b|\bkhozdar\b|\bkhuzdar\b|\bkusdar\b|\bkuzdar\b|\bt[uū]r[aā]n\b|\bjhalawan\b|\bgand[aā]v[aā]\b|\bkandabil\b|\bkandab[eē]l\b|\bkachhi\b|\bduki\b|\bloralai\b|\bkikan[aā]n\b|\bkaikan[aā]n\b|\bsehwan\b|\bvijnot\b|\bbudhiya\b"
SIG=re.compile(r"buddh|st[uū]pa|tope\b|hindu|temple|ruin|ancient|\barab|chach|hiuen|hwen|chinese|brahman|inscri|coins?\b|fort",re.I)
RX=re.compile(SITES,re.I)
files=sorted(set(glob.glob("gazetteer-vedanta/*/data/ia_ocr/*.txt")+glob.glob("yoga-gazetteers/*/data/ia_ocr/*.txt")))
out=[];cnt=collections.Counter()
for f in files:
  t=open(f,encoding='utf-8',errors='replace').read(); last=-10**9
  for m in RX.finditer(t):
    if m.start()-last<1500: continue
    ctx=re.sub(r"\s+"," ",t[max(0,m.start()-600):m.end()+900])
    if len(SIG.findall(ctx))<2: continue
    last=m.start(); cnt[f.split('/')[-1]]+=1
    out.append([f.split('/')[-1][:-4],m.group(0).lower(),t.count("\n",0,m.start())+1,ctx])
w=csv.writer(open(sys.argv[1],'w'),delimiter='\t'); w.writerow(['identifier','match','line','context']); w.writerows(out)
print(len(out)); print(cnt.most_common(30))
print(collections.Counter(o[1] for o in out).most_common())
