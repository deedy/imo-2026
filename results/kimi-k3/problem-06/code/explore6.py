"""Test structural conjectures about minimal transversals H_n.

C1: every h in H_n is a subset of some b_i = rad(a_i), i <= n.
C2: stable H is pairwise intersecting.
C3: shrinkage always stops.
"""
from math import gcd
from sympy import factorint
from explore1 import rad_primes, prod

def run(a1, N, test_C1=True):
    b_list = [rad_primes(a1)]
    H = {frozenset([p]) for p in b_list[0]}
    seq = [a1]
    shrinks = []
    C1_fail = []
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
        if test_C1:
            for h in H:
                if not any(h <= bi for bi in b_list):
                    C1_fail.append((n, sorted(h)))
    # pairwise intersecting?
    Hl = list(H)
    pw = all((Hl[i] & Hl[j]) for i in range(len(Hl)) for j in range(i+1, len(Hl)))
    return dict(a1=a1, shrinks=shrinks, H=H, pw=pw, C1_fail=C1_fail, seq=seq)

if __name__ == "__main__":
    import itertools, random
    random.seed(1)
    cases = list(range(2, 120)) + [105, 1155, 1001, 385, 165, 195, 255, 455, 595,
            665, 935, 1105, 1309, 1495, 1729, 1995, 2310, 3003, 4290, 5005,
            3315, 2431, 1925, 210, 420, 840, 1260, 1680, 2520]
    cases = sorted(set(cases))
    bad_C1 = 0
    not_pw = []
    not_stable = []
    for a1 in cases:
        r = run(a1, 2500, test_C1=True)
        if r['C1_fail']:
            bad_C1 += 1
            print(f"C1 FAIL a1={a1}: {r['C1_fail'][:3]}")
        if r['shrinks'] and r['shrinks'][-1] >= 2499:
            not_stable.append(a1)
        if not r['pw'] and r['shrinks'] and r['shrinks'][-1] < 2400:
            not_pw.append((a1, [sorted(h) for h in r['H']]))
    print(f"C1 failures: {bad_C1}")
    print(f"cases not stabilized by 2500: {not_stable}")
    print(f"stable-but-not-pairwise-intersecting: {not_pw}")
