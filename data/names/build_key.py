"""Build align.tsv and key.tsv for Xuanzang's transcription key.

Input: align.tsv (hand alignments; edit it and rerun), mc.tsv, key_charnotes.txt.
Usage: python3 build_key.py data/names
Alignment convention: char=segment; segments partition the Indic form.
  'x(n)'  = nasal coda of the Chinese syllable echoes the next onset, no extra Indic sound
  'r(pre)'= 曷 written before an initial r- (no Indic sound of its own)
  consonant-only segment (e.g. 's', 'ś', 'r') = character renders the first member of a cluster
Rows whose note starts with 'non-Indic' or 'circular', rows marked 'unsure',
and duplicates ('dup') are not counted in key.tsv.
"""
import csv, re, sys, unicodedata
from collections import defaultdict, Counter
D = sys.argv[1] if len(sys.argv) > 1 else '.'
SRC = sys.argv[2] if len(sys.argv) > 2 else D + '/align.tsv'  # align.tsv is itself the editable source

# MC positions for characters absent from mc.tsv (Guangyun, same notation)
SUPP = {
 '你':'孃開三之上','儞':'孃開三之上','倶':'見合三C虞平','徳':'端開一登入','掲':'見開三C元入 / 羣開三C元入 / 溪開三B祭去','毘':'並三A脂平',
 '衆':'章三東去','駄':'定開一歌平','迷':'明開四齊平','胝':'知開三脂平','些':'心開三麻平 / 心開四齊去','繕':'常開三仙去',
 '磨':'明一歌平 / 明一歌去','藥':'以開三陽入','低':'端開四齊平','田':'定開四先平','第':'定開四齊去','鑠':'書開三陽入',
 '奈':'泥開一泰去','沒':'明一魂入','特':'定開一登入','梅':'明一灰平','曼':'明一寒去','殊':'常合三虞平','畔':'並一寒去',
 '闡':'昌開三仙上','准':'章合三真上','喬':'羣開三B宵平','𢫫':'來合一魂入','詰':'溪開三A真入','輸':'書合三虞平',
 '閼':'影開一寒入 / 影開二夬去','頻':'並三A真平','塞':'心開一登入 / 心開一咍去','杜':'定一模上','魯':'來一模上','愼':'常開三真去',
 '木':'明一東入','鴦':'影開三陽平','捺':'泥開一寒入','沓':'定開一覃入','亘':'曉開一登去','䮚':'? (not in Guangyun; cf. 楞 來開一登平)',
 '贍':'常開三鹽去','刹':'初開二刪入','旦':'端開一寒去','索':'心開一唐入','答':'端開一覃入','諾':'泥開一唐入',
}
INIT = {'幫':'p','滂':'pʰ','並':'b','明':'m','端':'t','透':'tʰ','定':'d','泥':'n','知':'ʈ','徹':'ʈʰ','澄':'ɖ','孃':'ɳ',
 '精':'ts','清':'tsʰ','從':'dz','心':'s','邪':'z','莊':'tʂ','初':'tʂʰ','崇':'dʐ','生':'ʂ','俟':'ʐ','章':'tɕ','昌':'tɕʰ',
 '船':'dʑ','書':'ɕ','常':'ʑ','見':'k','溪':'kʰ','羣':'g','疑':'ŋ','影':'ʔ','曉':'x','匣':'ɣ','云':'ɦ','以':'j','來':'l','日':'ɲ'}
NASAL = {'東':'ŋ','冬':'ŋ','鍾':'ŋ','江':'ŋ','陽':'ŋ','唐':'ŋ','庚':'ŋ','耕':'ŋ','清':'ŋ','青':'ŋ','蒸':'ŋ','登':'ŋ',
 '真':'n','臻':'n','文':'n','殷':'n','元':'n','魂':'n','痕':'n','寒':'n','刪':'n','山':'n','先':'n','仙':'n',
 '侵':'m','覃':'m','談':'m','鹽':'m','添':'m','咸':'m','銜':'m','嚴':'m','凡':'m'}
STOP = {'ŋ':'k','n':'t','m':'p'}

def mc_read(pos):
    """'端開一寒入' -> 't-…-t'"""
    out=[]
    for p in pos.split(' / '):
        p=p.strip()
        if not p or p[0] not in INIT: out.append(p); continue
        ini=INIT[p[0]]; tone=p[-1]; rh=None
        for ch in reversed(p[1:-1]):
            if ch in NASAL or ch in '歌麻模魚虞齊佳皆灰咍支脂之微祭泰夬廢蕭宵肴豪尤侯幽': rh=ch; break
        coda=''
        if rh in NASAL: coda = STOP[NASAL[rh]] if tone=='入' else NASAL[rh]
        out.append(ini+'-' + (' -'+coda if coda else ''))
    return ' / '.join(dict.fromkeys(out))

mc = {}
for r in csv.DictReader(open(D+'/mc.tsv'), delimiter='\t'):
    if r['positions'].strip(): mc[r['char']] = r['positions'].strip()
for k,v in SUPP.items(): mc.setdefault(k, v)

def norm_form(f):
    f = re.sub(r'^(Skt|Pkt|Pa|Toch\.?/local|Toch\. B|Sogd|MPers|Iran|Tib)\.?\s*', '', f)
    f = f.split(' / ')[0].split(' < ')[0]
    f = re.sub(r'\([^)]*\)', '', f).replace('-', '').replace(' ', '').lower()
    return f

rows=[]; bad=0
def src_lines():
    if SRC.endswith('.tsv'):
        for r in csv.reader(open(SRC), delimiter='\t'):
            if r and r[0] != 'id': yield r
    else:
        for l in open(SRC):
            if l.startswith('#') or not l.strip(): continue
            yield [x.strip() for x in l.rstrip('\n').split('|')]
for f in src_lines():
    f += ['']*(6-len(f))
    id_, zh, form, al, conf, note = f[:6]
    pairs=[tuple(t.split('=',1)) for t in al.split()]
    chars=''.join(c for c,_ in pairs)
    segs=''.join(re.sub(r'\([^)]*\)','',s) for _,s in pairs if '(pre)' not in s).lower()
    nf=norm_form(form)
    if chars!=zh: print('CHAR MISMATCH',id_,zh,chars); bad+=1
    if not note.startswith('non-Indic') and conf!='unsure' and segs!=nf and not (segs.startswith(nf) or nf.startswith(segs)):
        print('SEG MISMATCH',id_,nf,segs); bad+=1
    rows.append(dict(id=id_,name_zh=zh,form_used=form,alignment=al,confidence=conf,note=note,pairs=pairs))
with open(D+'/align.tsv','w',newline='') as fo:
    w=csv.writer(fo,delimiter='\t',lineterminator='\n')
    w.writerow(['id','name_zh','form_used','alignment','confidence','note'])
    for r in rows: w.writerow([r[k] for k in ['id','name_zh','form_used','alignment','confidence','note']])

def counted(r):
    return r['confidence'] in ('sure','probable') and not r['note'].startswith(('non-Indic','circular')) and 'not counted' not in r['note']

VAR={'掲':'揭','毗':'毘','徳':'德'}
vals=defaultdict(Counter); ids=defaultdict(list); unsure=defaultdict(Counter)
for r in rows:
    if not counted(r): continue
    for c,s in r['pairs']:
        c=VAR.get(c,c)
        vals[c][s]+=1
        if r['id'] not in ids[c]: ids[c].append(r['id'])
VAR_NOTE={'揭':'counts include the variant 掲','毘':'counts include the variant 毗','德':'counts include the variant 徳'}
NOTES={}
try:
    for l in open(D+'/key_charnotes.txt'):
        if '\t' in l: c,n=l.rstrip('\n').split('\t',1); NOTES[c]=n
except FileNotFoundError: pass
def vnorm(cn):
    t=str.maketrans('āīūṝ','aiuṛ'); n=Counter()
    for s,k in cn.items():
        s=re.sub(r'\([^)]*\)','',s) if '(pre)' not in s else s
        s=s.translate(t); s=re.sub(r'(.)\1',r'\1',s)  # length and gemination ignored
        n[s]+=k
    return '; '.join(f'{s} {k}' for s,k in n.most_common())
order=sorted(vals, key=lambda c:(-sum(vals[c].values()), c))
with open(D+'/key.tsv','w',newline='') as fo:
    w=csv.writer(fo,delimiter='\t',lineterminator='\n')
    w.writerow(['char','mc_position','mc_reading','values','values_norm','n_tokens','n_names','example_ids','note'])
    for c in order:
        pos=mc.get(c,'?')
        v='; '.join(f'{s} {n}' for s,n in vals[c].most_common())
        w.writerow([c,pos,mc_read(pos) if pos!='?' else '?',v,vnorm(vals[c]),sum(vals[c].values()),len(ids[c]),', '.join(ids[c][:6]),'; '.join(x for x in [NOTES.get(c,''),VAR_NOTE.get(c,'')] if x)])
print('rows',len(rows),'counted',sum(counted(r) for r in rows),'chars',len(vals),'bad',bad)
print('missing MC:',[c for c in vals if c not in mc])
