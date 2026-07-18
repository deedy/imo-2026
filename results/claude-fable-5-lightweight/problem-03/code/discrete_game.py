"""Brute-force the full discrete game on a stick of integer length N.

Model: stick [0,N], marks at integer points 1..N-1. Liu picks a set L of at
most n points; Xiang (seeing L) picks a set X of at most n points disjoint
from L. Stick cut at L∪X. Then alternate picking pieces, Liu first, both
optimal -> Liu gets the odd-ranked pieces (sum of 1st,3rd,... largest).

Conjecture: continuous value c_n = 2^n/(2^{n+1}-1); for N divisible by
2^{n+1}-1 the discrete value should be exactly c_n * N.
"""
from itertools import combinations
import sys

def liu_share(cuts, N):
    prev = 0
    pieces = []
    for c in cuts:
        pieces.append(c - prev)
        prev = c
    pieces.append(N - prev)
    pieces.sort(reverse=True)
    return sum(pieces[::2])

def value(N, n, verbose=False):
    pts = list(range(1, N))
    best = -1
    bestL = None
    Lsets = [c for r in range(n + 1) for c in combinations(pts, r)]
    for L in Lsets:
        Lset = set(L)
        rem = [p for p in pts if p not in Lset]
        worst = None
        pruned = False
        for r in range(n + 1):
            for X in combinations(rem, r):
                cuts = sorted(L + X)
                sh = liu_share(cuts, N)
                if worst is None or sh < worst:
                    worst = sh
                    if worst <= best:
                        pruned = True
                        break
            if pruned:
                break
        if not pruned and worst is not None and worst > best:
            best, bestL = worst, L
    if verbose:
        print(f"N={N} n={n}: value={best} (= {best}/{N}), Liu's optimal marks: {bestL}")
    return best, bestL

if __name__ == "__main__":
    tests = [(6,1),(9,1),(12,1),(7,2),(14,2),(21,2),(10,2),(15,3)]
    for N, n in tests:
        v, L = value(N, n, verbose=True)
        denom = 2**(n+1) - 1
        pred = (2**n * N) // denom if N % denom == 0 else None
        if pred is not None:
            status = "OK" if v == pred else "MISMATCH!!!"
            print(f"   predicted {pred}  -> {status}")
    if len(sys.argv) > 1 and sys.argv[1] == "big":
        v, L = value(30, 3, verbose=True)
        print("   predicted", 16, "->", "OK" if v == 16 else "MISMATCH!!!")
