"""n=3 bins 1,2,4,8; check min V under <=3 cuts is >=8."""
import numpy as np
from scipy.optimize import differential_evolution, minimize
from itertools import product

def V_of(lengths):
    a = np.sort([x for x in lengths if x > 1e-14])[::-1]
    return float(a[0::2].sum())

def min_V(bin_sizes=(1.0, 2.0, 4.0, 8.0), maxc=3):
    n_bins = len(bin_sizes)
    best_overall = V_of(bin_sizes)
    best_alloc = None
    best_lens = None
    count = 0
    for alloc in product(range(maxc + 1), repeat=n_bins):
        if sum(alloc) > maxc:
            continue
        count += 1
        nparam = sum(alloc)
        if nparam == 0:
            continue
        bounds = [(0.0, 1.0)] * nparam

        def obj(z, alloc_=alloc):
            ls = []
            idx = 0
            for sz, c in zip(bin_sizes, alloc_):
                if c == 0:
                    ls.append(sz)
                else:
                    fr = np.sort(np.clip(z[idx:idx + c], 0.0, 1.0))
                    idx += c
                    pts = np.concatenate(([0.0], fr, [1.0]))
                    ls.extend(list(np.diff(pts) * sz))
            return V_of(ls)

        res = differential_evolution(
            obj, bounds, popsize=18, seed=3, tol=1e-11,
            mutation=0.55, recombination=0.7, workers=1, polish=True
        )
        cur = res.fun
        rng = np.random.default_rng(7 + sum(a * (11 ** i) for i, a in enumerate(alloc)))
        for _ in range(15):
            z0 = rng.uniform(0, 1, nparam)
            rr = minimize(obj, z0, method="Nelder-Mead", tol=1e-14)
            if rr.fun < cur:
                cur = float(rr.fun)
        if cur < best_overall - 1e-12:
            best_overall = cur
            best_alloc = alloc
            # reconstruct with DE x
            z = res.x
            ls = []
            idx = 0
            for sz, c in zip(bin_sizes, alloc):
                if c == 0:
                    ls.append(sz)
                else:
                    fr = np.sort(np.clip(z[idx:idx + c], 0, 1))
                    idx += c
                    pts = np.concatenate(([0.0], fr, [1.0]))
                    ls.extend(list(np.diff(pts) * sz))
            best_lens = ls
            print("new best", best_overall, "alloc", alloc, "lens", np.round(ls, 5))
        elif count % 10 == 0:
            print("checked", count, "alloc", alloc, "V", cur)

    print("FINAL", best_overall, best_alloc, "from", count, "allocs")
    return best_overall

if __name__ == "__main__":
    min_V()
