import numpy as np
from itertools import combinations

def pieces(cuts):
    pts = np.unique(np.round(np.concatenate(([0.], np.asarray(cuts,float), [1.])),12))
    return np.diff(np.sort(pts))

def lb_get(L):
    a = np.sort(L)[::-1]
    return float(np.sum(a[0::2])), a

lb=[0.2,0.4]
grid=np.linspace(0.001,0.999,400)
best=1
bc=None
for y in grid:
    if min(abs(y-x) for x in lb)<1e-9: continue
    v,_=lb_get(pieces(lb+[y]));
    if v<best: best=v; bc=('1',y,v)
print('best1',best,bc)

best2=1
bc2=None
for i,y1 in enumerate(grid[::3]):
    for y2 in grid[i*3+1::3]:
        if abs(y1-y2)<1e-9: continue
        if any(abs(y1-x)<1e-9 or abs(y2-x)<1e-9 for x in lb): continue
        v,a=lb_get(pieces(lb+[y1,y2]))
        if v<best2: best2=v; bc2=('2',y1,y2,v,a)
print('best2',best2,bc2)

for cfg in [[0.6,0.8],[0.5,0.7],[0.5,0.6],[0.6,0.7],[0.1,0.6],[0.3,0.6],[0.3,0.7],[0.5,0.9],[0.55,0.75],[0.1,0.3],[0.6,0.9],[0.7,0.9],[0.45,0.7]]:
    v,a=lb_get(pieces(lb+cfg))
    print(cfg, v, a)
