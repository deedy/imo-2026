"""Verify binary construction: intervals of length 2^0, 2^1, ..., 2^n over sum=2^{n+1}-1."""
import numpy as np
from itertools import combinations

def positions(n):
    """Return LB cut positions for unit 1/S, S=2^{n+1}-1, cumsum of 2^0 .. 2^{n-1}"""
    S = 2**(n+1) - 1
    cum = 0
    cuts = []
    for k in range(n):  # n cuts, n+1 pieces: 2^0 .. 2^n
        cum += 2**k
        cuts.append(cum / S)
    return cuts, S

def pieces(cuts):
    pts = np.unique(np.round(np.concatenate(([0.], np.asarray(cuts,float), [1.])), 12))
    return np.diff(np.sort(pts))

def lb_get(L):
    a = np.sort(L)[::-1]
    return float(np.sum(a[0::2]))

def check_n2():
    lb, S = positions(2)
    print("n=2 LB cuts", lb, "S", S)
    # Exhaustive-ish: XY can put cuts anywhere. The final pieces are from subdividing the 3 intervals of 1,2,4.
    # With 2 cuts, possibilities: 
    # - put both in one interval
    # - put one each in two intervals
    # - one interval gets both, etc.
    # For exact, we can reason lengths as positive reals summing to interval sizes
    # But numerically dense grid relative to binary
    unit = 1/S
    # cand points every unit/4
    grid = np.arange(0.5, S, 0.25) * unit
    best = 1.0
    bestc = None
    # empty
    v = lb_get(pieces(lb)); best=min(best,v)
    for y in grid:
        if any(abs(y-x)<1e-12 for x in lb): continue
        v = lb_get(pieces(lb+[y]))
        if v < best: best=v; bestc=('1',y)
    for y1,y2 in combinations(grid,2):
        if abs(y1-y2)<1e-12: continue
        if any(abs(y1-x)<1e-12 or abs(y2-x)<1e-12 for x in lb): continue
        v = lb_get(pieces(list(lb)+[y1,y2]))
        if v < best - 1e-15:
            best=v; bestc=('2',y1,y2, pieces(list(lb)+[y1,y2]))
    print("n2 worst found", best, bestc)
    return best

def check_generic(n, dens_factor=4):
    lb, S = positions(n)
    print(f"n={n} LB cuts", lb, "S", S, "target", 2**n / S)
    unit = 1.0/S
    # grid density jelas
    step = unit / dens_factor
    grid = np.arange(step/2, 1, step)
    # XY has n points. Combinatorial explosion for n>=3. Use random + strategic + optimize
    # Even for n=2 we did combinations
    # For rigor we need analytic. For now MonteCarlo + place in the large intervals
    rng = np.random.default_rng(0)
    best = lb_get(pieces(lb))
    # sample many
    Nsamp = 5000 if n<=3 else 2000
    for _ in range(Nsamp):
        k = rng.integers(0, n+1)  # number of XY cuts used 0..n
        ys = rng.uniform(0,1,size=k)
        # avoid exact collision
        ok=True
        for y in ys:
            if any(abs(y-x)<1e-9 for x in lb):
                ok=False
        if not ok: continue
        v = lb_get(pieces(list(lb)+list(ys)))
        if v < best:
            best = v
    print("random worst", best)
    # Also try: subdivide each power-of-two into halves systematically
    # e.g. cut every interval in half if possible
    return best

if __name__ == '__main__':
    check_n2()
    check_generic(2)
    check_generic(3, dens_factor=2)
