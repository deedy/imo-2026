"""Check: is every h in H_n contained in some b_i for all sufficiently large n?
Track max n where containment fails. Also track potential functions."""
from math import gcd
from sympy import factorint
from explore1 import rad_primes, prod

def run(a1, N):
    b_list = [rad_primes(a1)]
    H = {frozenset([p]) for p in b_list[0]}
    seq = [a1]
    shrinks = []
    max_fail_n = -1
    maxHsize = 1
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
        b_list.append(b)
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
        H = Hnew
        maxHsize = max(maxHsize, len(H))
        for h in H:
            if not any(h <= bi for bi in b_list):
                max_fail_n = n
    return dict(a1=a1, shrinks=shrinks, H=H, max_fail_n=max_fail_n, seq=seq, maxHsize=maxHsize)

if __name__ == "__main__":
    cases = sorted(set(list(range(2, 200)) + [105, 1155, 1001, 385, 165, 195, 255, 455, 595,
            665, 935, 1105, 1309, 1495, 1729, 1995, 2310, 3003, 4290, 5005,
            3315, 2431, 1925, 210, 420, 840, 1260, 1680, 2520, 4620, 6006, 9690]))
    worst = 0
    worst_a1 = None
    for a1 in cases:
        r = run(a1, 2000)
        if r['max_fail_n'] > worst:
            worst = r['max_fail_n']
            worst_a1 = a1
    print(f"max over all cases of (largest n where some h not subset of any b_i): {worst} (a1={worst_a1})")
