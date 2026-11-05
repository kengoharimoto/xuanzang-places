import csv, math, sys
src = sys.argv[1]; places = sys.argv[2]; out = sys.argv[3]
P = list(csv.DictReader(open(places), delimiter='\t'))
D = {}
for line in open(src):
    line = line.rstrip('\n')
    if not line: continue
    f = line.split('|'); assert len(f) == 7, line
    assert f[0] not in D, f[0]; D[f[0]] = f
ids = [p['id'] for p in P]
print('missing', [i for i in ids if i not in D]); print('extra', [i for i in D if i not in ids])
with open(out, 'w', newline='') as fh:
    w = csv.writer(fh, delimiter='\t', lineterminator='\n')
    w.writerow(['id','name_zh','modern_name','lat','lon','precision','basis','note'])
    for p in P:
        f = D[p['id']]
        w.writerow([p['id'], p['name_zh']] + f[1:])
