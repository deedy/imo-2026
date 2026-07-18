"""Direct exhaustive check of the pairing lemma (Claim 2) on a fine grid,
plus an exhaustive check that Mulan's round-up move marks both halves.
Angles are multiples of 0.5 degrees (N=360 units)."""
from fractions import Fraction

N = 360  # 0.5 degree units
D180 = Fraction(180)
H = Fraction(1, 2)  # unit


def check_n(n):
    theta = D180 / n
    tU = theta / H  # theta in half-degree units, must be integer for grid check
    if tU.denominator != 1:
        return None
    t = int(tU)
    tested = 0
    for a in range(1, N):
        if a % t == 0:
            continue  # marked
        for b in range(1, N - a):
            if b % t == 0:
                continue
            c = N - a - b
            if c < 1 or c % t == 0:
                continue
            # unmarked triple (in units); angles are a*H etc.
            def d(x):  # dist up to next multiple of t, in units
                return (x // t + 1) * t - x
            da, db, dc = d(a), d(b), d(c)
            # pairing lemma
            ok = (da < b * 1 or da < c * 1 or db < a or db < c or dc < a or dc < b)
            assert ok, (n, a, b, c)
            # check round-up move marks both halves for the found pair
            found = False
            for (u, v, w) in [(a, b, c), (a, c, b), (b, a, c),
                              (b, c, a), (c, a, c and b), (c, b, a)]:
                du = d(u)
                if du < v:
                    # cut at v with alpha=du, B=u
                    h1 = (u, du, N - u - du)
                    h2 = (w, v - du, u + du)
                    m1 = any(x % t == 0 for x in h1)
                    m2 = any(x % t == 0 for x in h2)
                    assert m1 and m2, (n, (a, b, c), (u, v, w), h1, h2)
                    found = True
                    break
            assert found
            tested += 1
    return tested


for n in range(2, 31):
    r = check_n(n)
    if r is not None:
        print(f"n={n:3d} theta={180/n:9.4f}deg: pairing+roundup verified on {r} unmarked grid triples")
