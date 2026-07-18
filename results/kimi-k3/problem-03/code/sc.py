"""Test the strengthened invariant SC for Part A.

For a subdivision M of a super-increasing (margin delta) family (a_1<=..<=a_{n+1})
with <= n cuts, with odd-set A = {t: N(t) odd} and D = |A|:
  SC: for all tau in [0, a_1]:  |A ∩ [0,tau)| <= tau + (D - delta)/2.
Note tau=0 gives D >= delta (Part A).
"""
from fractions import Fraction
import random

def odd_set_measure(frags, lo, hi):
    """measure of {t in [lo,hi): #{frags > t} odd}."""
    pts = sorted(set([lo, hi] + [x for x in frags if lo < x < hi]))
    tot = Fraction(0)
    for i in range(len(pts) - 1):
        mid = (pts[i] + pts[i+1]) / 2
        N = sum(1 for x in frags if x > mid)
        if N % 2 == 1:
            tot += pts[i+1] - pts[i]
    return tot

def alt_sum(frags):
    s = sorted(frags, reverse=True)
    return sum(s[0::2]) - sum(s[1::2])

def random_superincreasing(n, delta, rng):
    a = []
    s = 0
    for i in range(n + 1):
        lo = delta + s if i >= 1 else delta
        num = rng.randint(int(lo * 1000), int(3 * lo * 1000) + 1)
        v = Fraction(num, 1000)
        a.append(v)
        s += v
    return a

def random_subdivision(a, cuts, rng):
    cur = [(x, i) for i, x in enumerate(a)]
    for _ in range(cuts):
        idx = rng.randrange(len(cur))
        L, p = cur[idx]
        u = Fraction(rng.randint(1, 10**6), 10**6 + 1) * L
        cur = cur[:idx] + [(u, p), (L - u, p)] + cur[idx+1:]
    return cur

def test_SC(n, trials=400, seed=1):
    rng = random.Random(seed)
    delta = Fraction(1, 50)
    for t in range(trials):
        a = random_superincreasing(n, delta, rng)
        c = rng.randint(0, n)
        cur = random_subdivision(a, c, rng)
        M = [x for x, _ in cur]
        D = alt_sum(M)
        a1 = a[0]
        # check SC for a grid of tau in [0, a1]
        for k in range(21):
            tau = a1 * k / 20
            lhs = odd_set_measure(M, Fraction(0), tau)
            rhs = tau + (D - delta) / 2
            if lhs > rhs:
                print(f"SC FAIL n={n} tau/a1={float(tau/a1):.2f}: lhs={float(lhs):.4f} rhs={float(rhs):.4f}")
                print("   family:", [float(x) for x in a], "cuts:", c)
                print("   frags:", [float(x) for x in M], "D:", float(D))
                return False
    print(f"n={n}: SC held in {trials} trials (budget <= n)")
    return True

if __name__ == "__main__":
    for n in [1, 2, 3]:
        test_SC(n)
