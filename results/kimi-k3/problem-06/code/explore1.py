"""Exploration for IMO-2026-06.

Sequence: a_{n+1} = smallest m > a_n with gcd(m, a_i) > 1 for all i <= n.

Key objects:
  S_n = {m : gcd(m, a_i) > 1 for all i <= n}  (upward closed under divisibility)
  H_n = set of minimal elements of S_n under divisibility
      = minimal hitting sets (transversals) of {rad(a_1),...,rad(a_n)}, as sets of primes.
  a_{n+1} = successor of a_n in S_n = min over h in H_n of next multiple of h.
"""
from math import gcd
from sympy import factorint

def rad_primes(m):
    return frozenset(factorint(m).keys())

def prod(s):
    r = 1
    for x in s:
        r *= x
    return r

def simulate_brute(a1, N):
    seq = [a1]
    for _ in range(N - 1):
        m = seq[-1] + 1
        while True:
            ok = True
            for ai in seq:
                if gcd(m, ai) == 1:
                    ok = False
                    break
            if ok:
                seq.append(m)
                break
            m += 1
    return seq

def simulate_H(a1, N, record=False):
    """Simulate using minimal transversals H.
    Returns (seq, shrink_steps, H_list) where shrink_steps = indices n where H changed."""
    b = rad_primes(a1)
    H = {frozenset([p]) for p in b}  # minimal transversals of {b1}
    seq = [a1]
    H_list = [H]
    shrink_steps = []
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
        # prune to antichain (keep inclusion-minimal)
        cand = list(cand)
        Hnew = set()
        for t in cand:
            if not any(u < t for u in cand):
                Hnew.add(t)
        if Hnew != H:
            shrink_steps.append(n)  # H changed after adding a_{n+1}; S_{n+1} != S_n
        H = Hnew
        if record:
            H_list.append(H)
    return seq, shrink_steps, (H_list if record else H)

if __name__ == "__main__":
    # Verify H-method against brute force
    import random
    random.seed(0)
    for a1 in list(range(2, 40)) + [210, 330, 390, 462]:
        N = 60
        s1 = simulate_brute(a1, N)
        s2, _, _ = simulate_H(a1, N)
        assert s1 == s2, (a1, s1, s2)
    print("H-method matches brute force: OK")

    # Look at some sequences and shrinkage steps
    for a1 in [2, 6, 15, 30, 105, 210, 2310]:
        seq, shrink, H = simulate_H(a1, 200)
        L = 1
        for h in H:
            L = L * prod(h) // gcd(L, prod(h))
        print(f"a1={a1}: shrink_steps={shrink[:20]} |H|={len(H)} L={L}")
        print("   seq[:18]:", seq[:18])
