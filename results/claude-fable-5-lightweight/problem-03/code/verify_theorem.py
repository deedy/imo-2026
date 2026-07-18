"""Verify the key structural claims:

1. Picking-phase lemma: game value of alternate-picking = sum of odd-ranked
   pieces (brute-force minimax on random small multisets).

2. Cutting-game theorem: for integer pieces P=(l_1..l_k) and k-1 cuts,
   min over INTEGER cuttings of D(sorted alternating sum) satisfies
      gamma(P) <= minD  and  minD <= gamma2(P)
   where gamma(P)=min |sum eps_i l_i| over eps in {0,±1}^k \ 0, and
   gamma2 = min such value with the parity of sigma (integer cuttings force
   D ≡ sigma mod 2).  (Continuous cuttings achieve exactly gamma.)

3. max over integer configs (k pieces summing N) of minD -- should be
   attained at the geometric config when (2^k-1)|N, with value N/(2^k-1).
"""
import itertools, random
from functools import lru_cache

# ---------- 1. picking lemma ----------
def picking_value(ms):
    ms = tuple(sorted(ms, reverse=True))
    @lru_cache(maxsize=None)
    def V(state):
        if not state:
            return 0
        tot = sum(state)
        # mover takes element j, then opponent is mover on the rest
        best = -1
        for j in range(len(state)):
            rest = state[:j] + state[j+1:]
            got = state[j] + (tot - state[j]) - V(rest)
            best = max(best, got)
        return best
    return V(ms)

def oddsum(ms):
    s = sorted(ms, reverse=True)
    return sum(s[::2])

def test_picking(trials=300):
    rng = random.Random(1)
    for _ in range(trials):
        m = rng.randint(1, 8)
        ms = [rng.randint(0, 20) for _ in range(m)]
        assert picking_value(ms) == oddsum(ms), (ms, picking_value(ms), oddsum(ms))
    print("picking lemma: OK (game value == odd-rank sum) on", trials, "random multisets")

# ---------- 2. cutting game ----------
def gamma(P):
    best = None
    for eps in itertools.product((-1, 0, 1), repeat=len(P)):
        if all(e == 0 for e in eps):
            continue
        v = abs(sum(e * p for e, p in zip(eps, P)))
        best = v if best is None else min(best, v)
    return best

def gamma_parity(P):
    sig = sum(P) % 2
    best = None
    for eps in itertools.product((-1, 0, 1), repeat=len(P)):
        if all(e == 0 for e in eps):
            continue
        v = abs(sum(e * p for e, p in zip(eps, P)))
        if v % 2 == sig % 2:
            best = v if best is None else min(best, v)
    return best

def partitions_into(n, parts):
    """all multisets (sorted tuples) of `parts` positive ints summing to n"""
    if parts == 1:
        yield (n,)
        return
    for first in range(1, n - parts + 2):
        for rest in partitions_into(n - first, parts - 1):
            if rest[0] >= first:
                yield (first,) + rest

def D(ms):
    s = sorted(ms, reverse=True)
    return sum(v if i % 2 == 0 else -v for i, v in enumerate(s))

def minD_integer(P, cuts):
    k = len(P)
    best = None
    # distribute cuts among pieces
    def alloc(i, left, partsofar):
        nonlocal best
        if i == k:
            d = D(list(itertools.chain.from_iterable(partsofar)))
            best = d if best is None else min(best, d)
            return
        for c in range(0, min(left, P[i] - 1) + 1):
            for pp in partitions_into(P[i], c + 1):
                alloc(i + 1, left - c, partsofar + [pp])
    alloc(0, cuts, [])
    return best

def test_cutting(trials=60):
    rng = random.Random(7)
    for _ in range(trials):
        k = rng.randint(2, 4)
        P = sorted([rng.randint(1, 10 if k < 4 else 8) for _ in range(k)], reverse=True)
        g, gp = gamma(P), gamma_parity(P)
        md = minD_integer(P, k - 1)
        assert md >= g, ("lower bound FAIL", P, md, g)
        assert md == gp, ("expected parity-adjusted gamma", P, md, g, gp)
    print("cutting game: OK  (gamma <= minD_int == parity-adjusted gamma) on", trials, "configs")

def test_worst_config(k, N):
    best = None
    for P in partitions_into(N, k):
        P = tuple(sorted(P, reverse=True))
        md = minD_integer(P, k - 1)
        if best is None or md > best[0]:
            best = (md, P)
    print(f"k={k}, N={N}: max over configs of minD = {best[0]} at P={best[1]}",
          "(predicted", N // (2**k - 1) if N % (2**k - 1) == 0 else "n/a", ")")

if __name__ == "__main__":
    test_picking()
    test_cutting()
    test_worst_config(2, 6)
    test_worst_config(3, 14)
    test_worst_config(3, 21)
    test_worst_config(4, 15)
