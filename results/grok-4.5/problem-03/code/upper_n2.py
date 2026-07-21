"""Check whether for all LB 3-partitions, XY can force V <= 4/7."""
import numpy as np
from scipy.optimize import differential_evolution, minimize
from itertools import product

def V_of(lengths):
    a = np.sort([x for x in lengths if x > 1e-14])[::-1]
    return float(a[0::2].sum())

def minV_for_partition(A, B, C, n_cuts=2):
    """Min V over ways to distribute up to n_cuts and split sizes."""
    best = V_of([A, B, C])  # 0 cuts
    for alloc in product(range(n_cuts + 1), repeat=3):
        if sum(alloc) > n_cuts or sum(alloc) == 0:
            continue
        nparam = sum(alloc)
        bounds = [(0.0, 1.0)] * nparam

        def obj(z, alloc=alloc):
            ls = []
            idx = 0
            for sz, c in zip((A, B, C), alloc):
                if c == 0:
                    ls.append(sz)
                else:
                    fr = np.sort(np.clip(z[idx:idx + c], 0, 1))
                    idx += c
                    pts = np.concatenate(([0.0], fr, [1.0]))
                    ls.extend(list(np.diff(pts) * sz))
            return V_of(ls)

        res = differential_evolution(obj, bounds, popsize=12, seed=11, tol=1e-11,
                                     mutation=0.6, recombination=0.7, atol=1e-12)
        best = min(best, res.fun)
        rng = np.random.default_rng((hash((round(A,8), round(B,8), round(C,8), alloc)) % (2**31)))
        for _ in range(12):
            z0 = rng.uniform(0, 1, nparam)
            rr = minimize(obj, z0, method='Nelder-Mead', tol=1e-14)
            if rr.fun < best:
                best = rr.fun
    return best

def main():
    rng = np.random.default_rng(0)
    max_minv = 0.0
    worst_part = None
    # random trials
    for trial in range(150):
        pts = np.sort(rng.uniform(0, 1, 2))
        A, B, C = pts[0], pts[1] - pts[0], 1 - pts[1]
        mv = minV_for_partition(A, B, C)
        if mv > max_minv + 1e-9:
            max_minv = mv
            worst_part = (A, B, C, mv)
            print("new max_min", max_minv, worst_part)
    # grid
    g = np.linspace(0.05, 0.95, 19)
    for i, x in enumerate(g):
        for y in g:
            if y <= x + 1e-9:
                continue
            A = x
            B = y - x
            C = 1 - y
            if min(A, B, C) < 1e-8:
                continue
            mv = minV_for_partition(A, B, C)
            if mv > max_minv + 1e-9:
                max_minv = mv
                worst_part = (A, B, C, mv)
                print("grid new", max_minv, worst_part)
    print("FINAL maxmin found", max_minv, worst_part)
    print("power of two", minV_for_partition(1/7, 2/7, 4/7))
    print("equal thirds", minV_for_partition(1/3, 1/3, 1/3))
    print("1/5 1/5 3/5", minV_for_partition(1/5, 1/5, 3/5))
    print("1/4 1/4 1/2", minV_for_partition(1/4, 1/4, 1/2))

if __name__ == '__main__':
    main()
