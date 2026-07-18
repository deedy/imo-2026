"""Tests for this session's proof ingredients."""
from fractions import Fraction
from functools import lru_cache
import random, itertools, sys, math
sys.setrecursionlimit(100000)


def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[0::2]) - sum(s[1::2])


# ---------------- matching formula for D ----------------
def D_matching(pieces):
    """min over matchings of sum|p-q| + sum(unmatched).  DP over sorted pieces."""
    p = sorted(pieces, reverse=True)
    m = len(p)
    # DP: process pieces; state = parity (is there a pending unmatched piece to pair)
    # Simple O(2^m) for small m: choose set of pairs.
    best = [None]

    @lru_cache(maxsize=None)
    def go(tup):
        tup = tuple(tup)
        if len(tup) <= 1:
            return sum(tup)  # leftover unmatched
        # option: leave first unmatched
        v = tup[0] + go(tup[1:])
        # option: pair first with some other
        for j in range(1, len(tup)):
            rest = tup[1:j] + tup[j+1:]
            c = abs(tup[0] - tup[j]) + go(rest)
            if c < v:
                v = c
        return v
    return go(tuple(p))


def test_matching_formula():
    rng = random.Random(0)
    for _ in range(300):
        m = rng.randint(1, 7)
        pieces = [Fraction(rng.randint(1, 20), rng.randint(1, 5)) for _ in range(m)]
        d1 = alt_sum(pieces)
        d2 = D_matching(pieces)
        assert d1 == d2, (pieces, d1, d2)
    print("matching formula D == min-cost matching: OK (300 tests)")


# ---------------- block lemma ----------------
def test_block_lemma():
    rng = random.Random(1)
    for trial in range(3000):
        n = rng.randint(1, 5)
        delta = Fraction(1, rng.randint(1, 10))
        # super-increasing family with margin delta
        a = []
        s = Fraction(0)
        for i in range(n + 1):
            lo = delta + s if i >= 1 else delta
            v = Fraction(rng.randint(math.ceil(lo * 100), int(3 * lo * 100) + 1), 100)
            a.append(v)
            s += v
        m = len(a)
        # random partition of a subset into blocks + random signs
        idx = list(range(m))
        rng.shuffle(idx)
        blocks = []
        cur = []
        for i in idx:
            if rng.random() < 0.4 and cur:
                blocks.append(cur)
                cur = [i]
            else:
                cur.append(i)
        if cur:
            blocks.append(cur)
        # randomly drop some blocks (deletion)
        kept = [B for B in blocks if rng.random() < 0.8]
        if not kept:
            continue
        vals = []
        for B in kept:
            sgn = [rng.choice([1, -1]) for _ in B]
            v = abs(sum(s * a[i] for s, i in zip(sgn, B)))
            vals.append(v)
        d = alt_sum(vals)
        assert d >= delta, (a, delta, kept, vals, d)
    print("block lemma: OK (3000 trials)")


# ---------------- Part A full statement ----------------
def test_part_A():
    rng = random.Random(2)
    for trial in range(1500):
        n = rng.randint(1, 4)
        delta = Fraction(1, rng.randint(1, 10))
        a = []
        s = Fraction(0)
        for i in range(n + 1):
            lo = delta + s if i >= 1 else delta
            v = Fraction(rng.randint(math.ceil(lo * 100), int(3 * lo * 100) + 1), 100)
            a.append(v)
            s += v
        # random subdivision with <= n cuts
        cur = list(a)
        ncuts = rng.randint(0, n)
        for _ in range(ncuts):
            i = rng.randrange(len(cur))
            L = cur[i]
            u = Fraction(rng.randint(1, 10**6), 10**6 + 1) * L
            cur = cur[:i] + [u, L - u] + cur[i+1:]
        d = alt_sum(cur)
        assert d >= delta, (a, delta, cur, d)
    print("Part A (subdiv of super-increasing, <= m-1 cuts, D >= delta): OK (1500 trials)")


# ---------------- dominance: min-subdiv == min-h/c ----------------
@lru_cache(maxsize=None)
def xy_min(pieces, cuts):
    """min D over subdivisions on integer grid."""
    val = alt_sum(pieces)
    if cuts > 0:
        for i, L in enumerate(pieces):
            for j in range(1, L):
                new = tuple(sorted(pieces[:i] + pieces[i+1:] + (j, L - j)))
                v = xy_min(new, cuts - 1)
                if v < val:
                    val = v
    return val


def parity_reduce(pool):
    from collections import Counter
    c = Counter(pool)
    return tuple(sorted(v for v, m in c.items() if m % 2 == 1))


def D_pool(pool):
    return alt_sum(parity_reduce(pool))


@lru_cache(maxsize=None)
def hc_min(pool, budget):
    """min D over halve/cancel ops."""
    val = D_pool(pool)
    if budget <= 0:
        return val
    items = sorted(set(pool))
    for x in items:
        new = list(pool); new.remove(x)
        v = hc_min(tuple(sorted(new)), budget - 1)
        if v < val: val = v
    for x, y in itertools.combinations(items, 2):
        new = list(pool); new.remove(x); new.remove(y); new.append(y - x)
        v = hc_min(tuple(sorted(new)), budget - 1)
        if v < val: val = v
    return val


def test_dominance():
    rng = random.Random(3)
    for _ in range(60):
        m = rng.randint(2, 4)
        pool = tuple(sorted(rng.randint(1, 9) for _ in range(m)))
        b = rng.randint(1, min(3, m))
        d1 = xy_min(pool, b)
        d2 = hc_min(pool, b)
        status = "OK" if d1 == d2 else "MISMATCH"
        if d1 != d2:
            print(f"  {status}: pool={pool} budget={b} subdiv={d1} hc={d2}")
    print("dominance test done (mismatches printed above, if any)")


if __name__ == "__main__":
    test_matching_formula()
    test_block_lemma()
    test_part_A()
    test_dominance()
