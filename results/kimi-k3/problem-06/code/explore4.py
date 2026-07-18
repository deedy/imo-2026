"""Detailed trace of |H| and shrinkage for hard cases."""
from math import gcd
from sympy import factorint
from explore1 import rad_primes, prod

def run(a1, N):
    b = rad_primes(a1)
    H = {frozenset([p]) for p in b}
    seq = [a1]
    shrinks = []
    Hsize_hist = []
    for n in range(1, N):
        an = seq[-1]
        best = None
        for h in H:
            hv = prod(h)
            m = (an // hv + 1) * hv
            if best is None or m < best:
                best = m
        seq.append(best)
        b = rad_primes(best)
        cand = set()
        for h in H:
            if h & b:
                cand.add(h)
            else:
                for q in b:
                    cand.add(h | {q})
        cand = list(cand)
        Hnew = set()
        for t in cand:
            if not any(u < t for u in cand):
                Hnew.add(t)
        if Hnew != H:
            shrinks.append((n, best, sorted(b), len(Hnew)))
        H = Hnew
        Hsize_hist.append(len(H))
    return seq, shrinks, H, Hsize_hist

for a1 in [2310, 4290, 3003]:
    N = 6000
    seq, shrinks, H, hist = run(a1, N)
    print(f"=== a1={a1}: #shrinks={len(shrinks)}, last shrink step={shrinks[-1][0] if shrinks else None}")
    print(f"    final |H|={len(H)}, H sizes at end: {hist[-5:]}")
    print(f"    last 3 shrinks (n, a_{{n+1}}, b, |Hnew|): {shrinks[-3:]}")
    print(f"    final H = {[sorted(h) for h in H]}")
    gaps = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    print(f"    max gap overall = {max(gaps)}, gaps[-10:] = {gaps[-10:]}")
    print()
