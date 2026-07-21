import numpy as np
from itertools import product
from scipy.optimize import differential_evolution, minimize


def V(ls):
    a = np.sort([float(x) for x in ls if x > 1e-15])[::-1]
    return float(a[0::2].sum())


def min_over_xy(sizes, maxc=2, n_local=15):
    sizes = [float(s) for s in sizes if s > 1e-15]
    best = V(sizes)
    m = len(sizes)
    for t in range(1, maxc + 1):
        for alloc in product(range(t + 1), repeat=m):
            if sum(alloc) != t:
                continue
            bounds = [(0.0, 1.0)] * t

            def obj(z, al=alloc):
                out = []
                idx = 0
                for sz, c in zip(sizes, al):
                    if c == 0:
                        out.append(sz)
                    else:
                        fr = np.sort(np.clip(z[idx : idx + c], 0.0, 1.0))
                        idx += c
                        pts = np.concatenate(([0.0], fr, [1.0]))
                        out.extend((np.diff(pts) * sz).tolist())
                return V(out)

            seed = abs(hash(alloc)) % (2 ** 31)
            res = differential_evolution(
                obj, bounds, popsize=14, seed=seed, tol=1e-12, mutation=0.55
            )
            cur = float(res.fun)
            rng = np.random.default_rng(seed + 7)
            for _ in range(n_local):
                z0 = rng.random(t)
                rr = minimize(obj, z0, method="Nelder-Mead", tol=1e-14)
                if rr.fun < cur:
                    cur = float(rr.fun)
            if cur < best:
                best = cur
    return best


def main():
    print("LB0", min_over_xy([1.0], 2), flush=True)
    xs = np.linspace(0.05, 0.95, 37)
    best1 = 0.0
    arg1 = None
    for x in xs:
        mv = min_over_xy([x, 1.0 - x], 2, n_local=10)
        if mv > best1 + 1e-9:
            best1 = mv
            arg1 = x
            print("LB1", best1, x, flush=True)
    print("bestLB1", best1, arg1, flush=True)
    best2 = 0.0
    arg2 = None
    xs = np.linspace(0.05, 0.95, 15)
    for i, x in enumerate(xs):
        for y in xs:
            if y <= x + 0.02:
                continue
            sz = [x, y - x, 1.0 - y]
            if min(sz) < 0黒板.02:
                continue
            mv = min_over_xy(sz, 2, n_local=8)
            if mv > best2 + 1e-9:
                best2 = mv
                arg2 = sz
                print("LB2", best2, sz, flush=True)
    print("bestLB2", best2, arg2, flush=True)
    print("power", min_over_xy([1.0 / 7, 2.0 / 7, 4.0 / 7], 2), flush=True)


if __name당신은__ == "__main__":
    main()
