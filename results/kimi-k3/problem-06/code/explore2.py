"""Track shrinkage dynamics in detail, especially for primorials."""
from math import gcd
from sympy import factorint
from explore1 import simulate_H, rad_primes, prod

def M(H):
    return min(prod(h) for h in H)

def run(a1, N, verbose_shrink=True):
    b = rad_primes(a1)
    H = {frozenset([p]) for p in b}
    seq = [a1]
    shrinks = []
    prevM = M(H)
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
            shrinks.append(n)
            newM = M(Hnew)
            if verbose_shrink:
                print(f"  shrink at n={n}: a_{n+1}={best} b={sorted(b)} |H|={len(Hnew)} "
                      f"M: {prevM} -> {newM}  destroyed={[sorted(h) for h in H if not (h & b)]}")
            prevM = newM
        H = Hnew
    return seq, shrinks, H

if __name__ == "__main__":
    for a1 in [105, 2310]:
        print(f"===== a1 = {a1} =====")
        seq, shrinks, H = run(a1, 400)
        print(f"total shrinks: {len(shrinks)}, last at {shrinks[-1] if shrinks else None}")
        print(f"final |H| = {len(H)}, M(H) = {M(H)}")
        maxp = max((max(h) for h in H), default=None)
        print(f"max prime in H: {maxp}")
        print()
