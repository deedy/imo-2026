"""
XY strategy-space analysis (continuous, exact arithmetic with floats).

Pool model: XY starts with pool = LB pieces {a_1..a_{n+1}}.
Operations (each costs 1 cut):
  - halve(x): remove one copy of x from pool (the two halves pair up, vanish).
  - cancel(x, y) with x > y: remove one copy each of x and y, add (x - y).
After <= n operations, D = alternating sum of parity-reduced pool.
Goal: min over strategies. Check min <= T_n * S for random configs.
"""
from functools import lru_cache
from fractions import Fraction
import random
import itertools


def parity_reduce(pool):
    """Keep one copy of each value with odd multiplicity."""
    from collections import Counter
    c = Counter(pool)
    return tuple(sorted(v for v, m in c.items() if m % 2 == 1))


def alt_sum_values(vals):
    s = sorted(vals, reverse=True)
    return sum(s[0::2]) - sum(s[1::2])


def D_pool(pool):
    return alt_sum_values(parity_reduce(pool))


@lru_cache(maxsize=None)
def strategy_min(pool, budget):
    """Min achievable D over halve/cancel sequences with <= budget cuts.
    pool: sorted tuple of Fractions."""
    val = D_pool(pool)
    if budget <= 0:
        return val
    items = sorted(set(pool))
    # halve each distinct value
    for x in items:
        new = list(pool)
        new.remove(x)
        v = strategy_min(tuple(sorted(new)), budget - 1)
        if v < val:
            val = v
    # cancel each ordered pair x > y
    for x, y in itertools.combinations(items, 2):
        # x < y in combinations; cancel larger - smaller
        new = list(pool)
        new.remove(x)
        new.remove(y)
        new.append(y - x)
        v = strategy_min(tuple(sorted(new)), budget - 1)
        if v < val:
            val = v
    return val


def Tn(n):
    return Fraction(1, 2**(n + 1) - 1)


def test_random(n, trials=300, seed=1):
    random.seed(seed)
    worst = Fraction(0)
    worst_cfg = None
    for _ in range(trials):
        # random composition into n+1 parts
        cuts = sorted(random.randint(1, 10**6) for _ in range(n))
        pts = [0] + cuts + [10**6]
        pieces = [Fraction(pts[i+1] - pts[i], 10**6) for i in range(n + 1)]
        pool = tuple(sorted(pieces))
        S = sum(pool)
        v = strategy_min(pool, n)
        ratio = v / S
        if ratio > worst:
            worst = ratio
            worst_cfg = pool
    print(f"n={n}: worst min-D/S over {trials} random = {float(worst):.6f} "
          f"(T_n = {float(Tn(n)):.6f}), config={worst_cfg}")
    print(f"   upper bound holds: {worst <= Tn(n)}")
    return worst, worst_cfg


if __name__ == "__main__":
    for n in [1, 2, 3]:
        test_random(n)
    # tight case check
    for n in [1, 2, 3]:
        geo = tuple(Fraction(2**i, 2**(n+1) - 1) for i in range(n + 1))
        print(f"n={n} geometric: strategy_min = {strategy_min(geo, n)} (T_n*S = {Tn(n)})")
