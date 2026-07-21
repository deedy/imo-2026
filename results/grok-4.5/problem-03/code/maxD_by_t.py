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


def extremum_D(bins, t, mode="min", popsize=12, n_local=8):
    bins = [float(b) for b in bins]
    m = len(bins)
    if t == 0:
        return D(bins)
    sign_obj = 1.0 if mode == "min" else -1.0
    best = 999.0 if mode == "min" else -999.0
    for alloc in product(range(t + 1), repeat=m):
        if sum(alloc) != t:
            continue
        bounds = [(0.0, 1.0)] * t

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
                    out.extend(list(np.diff(pts) * sz))
            return sign_obj * D(out)

        seed = abs(hash((alloc, mode))) % (2 ** 31)
        res = differential_evolution(
            obj, bounds, popsize=popsize, seed=seed, tol=1e-11
        )
        cur = sign_obj * float(res.fun)
        rng = np.random.default_rng(seed + 5)
        for _ in range(n_local):
            z0 = rng.random(t)
            rr = minimize(obj, z0, method="Nelder-Mead", tol=1e-14)
            val = sign_obj * float(rr.fun)
            if (mode == "min" and val < best) or (mode == "max" and val > best):
                best = val
        if (mode == "min" and cur < best) or (mode == "max" and cur > best):
            best = cur
    return best


def main():
    for n in [1, 2, 3]:
        bins = [2 ** i for i in range(n + 1)]
        for t in range(0, n + 1):
            mn = extremum_D(bins, t, "min")
            mx = extremum_D(bins, t, "max")
            print(f"n={n} t={t} minD={mn} maxD={mx}", flush=True)


if __name__ == "__main__":
    main()
