import csv, math, sys
R = {r['id']: r for r in csv.DictReader(open(sys.argv[1]), delimiter='\t')}
P = {r['id']: r for r in csv.DictReader(open(sys.argv[2]), delimiter='\t')}
def hav(a,b,c,d):
    a,b,c,d = map(math.radians,(a,b,c,d))
    return 6371*2*math.asin(math.sqrt(math.sin((c-a)/2)**2+math.cos(a)*math.cos(c)*math.sin((d-b)/2)**2))
from collections import Counter
print(Counter(r['precision'] or '(blank)' for r in R.values()), Counter(r['basis'] or '(blank)' for r in R.values()))
for i,r in R.items():
    if bool(r['lat'])!=bool(r['lon']) or bool(r['lat'])!=bool(r['precision']) or bool(r['lat'])!=bool(r['basis']): print('INCONSISTENT', i)
    if r['precision'] not in ('','site','town','district','country'): print('BADPREC',i)
    if r['lat']:
        la,lo=float(r['lat']),float(r['lon'])
        if not (0<=la<=50 and 55<=lo<=105): print('RANGE', i, la, lo, r['modern_name'])
print('---distance')
for i,r in R.items():
    par = P[i]['parent']
    if par and r['lat'] and R.get(par,{}).get('lat'):
        d = hav(float(r['lat']),float(r['lon']),float(R[par]['lat']),float(R[par]['lon']))
        if d>150: print('FAR %s -> %s %.0f km | %s | %s'%(i,par,d,r['modern_name'],r['note']))
