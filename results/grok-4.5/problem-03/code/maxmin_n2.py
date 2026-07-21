"""Maximize over LB partitions the min over XY of V; expect ~4/7 for n=2."""
import numpy as np
from itertools import product
from scipy.optimize import differential_evolution, minimize

def V(ls):
    a = np.sort([x for x in ls if x > 1e-15])[::-1]
    return float(a[0::2].sum())

def min_V_for(sizes, max_cuts=2, n_tries=20):
    sizes = [float(s) for s in sizes if s > 1e-15]
    m = len(sizes)
    best = V(sizes)
    for alloc in product(range(max_cuts + 1), repeat=m):
        sc = sum(alloc)
        if sc == 0 or sc > max_cuts:
            continue
        nparam = sc
        bounds = [(0.0, 1.0)] * nparam

        def obj(z, al=alloc):
            out = []
            idx = 0
            for sz, c in zip(sizes, al):
                if c == 0:
                    out.append(sz)
                else:
                    fr = np.sort(np.clip(z[idx:idx + c], 0, 1))
                    idx += c
                    pts = np.concatenate(([0.0], fr, [1.0]))
                    out.extend((np.diff(pts) * sz).tolist())
            return V(out)

        seed = int(hash(alloc) % (2**31 - 1))
        res = differential_evolution(
            obj, bounds, popsize=14, seed=seed, tol=1e-12,
            mutation=0.5, recombination=0.7
        )
        cur = float(res.fun)
        rng = np.random.default_rng(seed + 17)
        for _ in range(n_tries):
            z0 = rng.random(nparam)
            rr = minimize(obj, z0, method="Nelder-Mead", tol=1e-14)
            if rr.fun < cur:
                cur = float(rr.fun)
        if cur < best:
            best = cur
    return best

def main():
    print("power", min_V_for([1/7, 2/7, 4/7]))
    print("equal", min_V_for([1/3, 1/3, 1/3]))
    print("1/5s", min_V_for([1/5, 1/5, 3/5]))
    rng = np.random.default_rng(0)
    mx = 0.0
    arg = None
    for t in range(60):
        pts = np.sort(rng.random(2))
        sz = [pts[0], pts[1] - pts[0], 1 - pts[1]]
        mv = min_V_for(sz)
        if mv > mx + 1e-9:
            mx = mv
            arg = sz
            print("new rng", mx, sz, flush=True)
    g = np.linspace(0.04, 0.96, 18)
    for i, x in enumerate(g):
        for y in g[i + 1 :]:
            sz = [x, y - x, 1 - y]
            if min(sz) < 0.03:
                continue
            mv = min_V_for(sz, n_tries=12)
            if mv > mx + 1e-9:
                mx = mv
                arg = sz
                print("new grid", mx, sz, flush=True)
    # 2 pieces
    for x in g:
        sz = [x, 1 - x]
        if min(sz) < 0.03:
            continue
        mv = min_V_for(sz)
        if mv > mx + 1e-9:
            mx = mv
            arg = sz
            print("new 2pc", mx, sz, flush=True)
    print("single", min_V_for([1.0]))
    print("FINAL", mx, arg)

if __name__ == "__main__":
    main()
