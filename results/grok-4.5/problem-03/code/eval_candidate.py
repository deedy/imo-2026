"""Detailed evaluation of promising candidates for n=2."""
import numpy as np
from itertools import combinations

def pieces(cuts):
    pts = np.unique(np.round(np.concatenate(([0.], np.asarray(cuts,float), [1.])),12))
    return np.diff(np.sort(pts))

def lb_get(L):
    a = np.sort(L)[::-1]
    return float(np.sum(a[0::2]))

def enumerate_worst(lb, dens=200):
    """Enumerate many XY positions including strategic ones relative to LB cuts."""
    lb = list(np.sort(lb))
    # create candidate y points: midpoints of intervals, and many grid, thirds etc
    pts = [0.0] + lb + [1.0]
    cands = set()
    grid = np.linspace(1e-4, 1-1e-4, dens)
    for g in grid:
        cands.add(round(g,10))
    # add points that split large intervals in special ratios
    for i in range(len(pts)-1):
        a,b = pts[i], pts[i+1]
        for k in range(1,8):
            for m in range(1,k):
                cands.add(round(a + (b-a)*m/k, 10))
    cands = sorted(cands)
    # now all pairs + singles + empty
    best = lb_get(pieces(lb))
    best_cfg = ('empty',)
    for y in cands:
        if any(abs(y-x)<1e-11 for x in lb):
            continue
        v = lb_get(pieces(lb+[y]))
        if v < best - 1e-15:
            best = v
            best_cfg = ('one', y)
    for y1,y2 in combinations(cands,2):
        if abs(y1-y2)<1e-11: continue
        if any(abs(y1-x)<1e-11 or abs(y2-x)<1e-11 for x in lb): continue
        v = lb_get(pieces(lb+[y1,y2]))
        if v < best - 1e-15:
            best = v
            best_cfg = ('two', y1,y2)
    return best, best_cfg

def main():
    cands = [
        [1/7, 3/7],
        [1/7, 2/7],
        [1/7, 4/7],
        [2/7, 3/7],
        [2/7, 4/7],
        [1/7, 5/7],
        [3/7, 5/7],
        [1/5, 2/5],
        [1/4, 1/2],
        [1/6, 1/3],
        [1/6, 2/5],
        [1/8, 3/8],
        [2/8, 4/8],
        [1/7, 2/5],
        [0.25, 0.4],
        [1/3, 0.5],
        [2/9, 4/9],
        [1/9, 4/9],
        [2/9, 5/9],
        [1/5, 3/7],
        [3/11, 6/11],
        [1/7, 3/8],
        [2/11,5/11],
        [1/4, 3/7],
    ]
    for c in cands:
        b, cfg = enumerate_worst(c, dens=120)
        print(f"{c} -> {b:.10f} via {cfg}")

if __name__ == '__main__':
    main()
