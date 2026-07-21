"""Check min D after <=n cuts on bins {1,2,...,2^n} equals 2^n."""
import numpy as np
from itertools import product
from scipy.optimize import differential_evolution, minimize


def D(ls):
    a = np.sort([float(x) for x in ls if x > 1e-15])[::-1]
    s = 0.0
    sign = 1.0
    for x in a:
        s += sign * x
        sign = -sign
    return s


def min_D(bins, maxc, popsize=15, n_local=10):
    bins = [float(b) for b in bins]
    m = len(bins)
    best = D(bins)
    best_al = None
    for alloc in product(range(maxc + 1), repeat=m):
        sc = sum(alloc)
        if sc == 0 or sc > maxc:
            continue
        nparam = sc
        bounds = [(0.0, 1.0)] * nparam

        def obj(z, al=alloc):
            out = []
            idx = 0
            for sz, c in zip(bins, al):
                if c == 0:
                    out.append(sz)
                else:
                    fr = np.sort(np.clip(z[idx : idx + c], 0.0, 1.0))
                    idx += c
                    pts = np.concatenate(([0.0], fr, [1.0]))
                    out.extend((np.diff(pts) * sz).tolist())
            return D(out)

        seed = abs(hash(alloc)) % (2 ** 31)
        res = differential_evolution(
            obj,
            bounds,
            popsize=popsize,
            seed=seed,
            tol=1e-11,
            mutation=0.55,
            recombination=0.7,
        )
        cur = float(res.fun)
        rng = np.random.default_rng(seed + 99)
        for _ in range(n_local):
            z0 = rng.random(nparam)
            rr = minimize(obj, z0, method="Nelder-Mead", tol=1e-14)
            if rr.fun < cur:
                cur = float(rr.fun)
        if cur < best - 1e-12:
            best = cur
            best_al = alloc
    return best, best_al


def main():
    for n in range(0, 4):
        bins = [2 ** i for i in range(n + 1)]
        md, al = min_D(bins, n, popsize=16 if n < 3 else 11, n_local=12)
        print(
            f"n={n} bins={bins} minD={md} target={2**n} worst_alloc={al}",
            flush=True,
        )
    extras = [[1, 1, 1, 4], [3, 4], [2, 2, 3], [1, 3, 3], [5, 2], [2.5, 2.5, 2], [6, 1]]
    for tb in extras:
        md, al = min_D(tb, 2)
        print("extra", tb, "minD", md, "alloc", al, flush=True)


if __name__ == "__main__":
    main()
