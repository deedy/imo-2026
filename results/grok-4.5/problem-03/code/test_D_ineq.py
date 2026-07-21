import numpy as np

def D(L):
    if len(L) == 0:
        return 0.0
    a = np.sort(np.asarray(L, dtype=float))[::-1]
    s = 0.0
    sign = 1.0
    for x in a:
        s += sign * x
        sign = -sign
    return float(s)

def check(n_trials=30000, maxk=7):
    rng = np.random.default_rng(1)
    max_viol_sub = 0.0
    max_viol_diff = 0.0
    for t in range(n_trials):
        kx = int(rng.integers(0, maxk + 1))
        ky = int(rng.integers(0, maxk + 1))
        X = rng.exponential(1.0, size=kx).tolist()
        Y = rng.exponential(1.0, size=ky).tolist()
        du = D(X + Y)
        dx, dy = D(X), D(Y)
        viol_s = du - (dx + dy)
        if viol_s > max_viol_sub + 1e-9:
            max_viol_sub = viol_s
            print("sub viol", viol_s, "X", X, "Y", Y, "du,dx,dy", du, dx, dy)
        viol_d = abs(dx - dy) - du
        if viol_d > max_viol_diff + 1e-9:
            max_viol_diff = viol_d
            print("diff viol", viol_d, "X", X, "Y", Y, "du,dx,dy", du, dx, dy)
    print("max viol sub", max_viol_sub, "max viol diff", max_viol_diff)

if __name__ == "__main__":
    check()
