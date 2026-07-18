"""Independent brute-force cross-check: simulate the sequence by the raw definition
and verify a_{n+T} = a_n + L (with T,L derived from permanents), plus Step 1's
enumeration claim, for small a1."""
from math import gcd, lcm
from sympy import factorint

def supp(m):
    return frozenset(factorint(m).keys())

def prodset(s):
    r = 1
    for p in s: r *= p
    return r

def simulate_brute(a1, N):
    seq = [a1]
    for _ in range(N - 1):
        m = seq[-1] + 1
        while any(gcd(m, ai) == 1 for ai in seq):
            m += 1
        seq.append(m)
    return seq

def simulate_H(a1, N):
    b = supp(a1)
    H = {frozenset([p]) for p in b}
    seq = [a1]
    for n in range(1, N):
        an = seq[-1]
        best = min((an // prodset(h) + 1) * prodset(h) for h in H)
        seq.append(best)
        b = supp(best)
        cand = set()
        for h in H:
            if h & b: cand.add(h)
            else:
                for q in b: cand.add(h | {q})
        cl = list(cand)
        H = {t for t in cl if not any(u < t for u in cl)}
    return seq, H

if __name__ == "__main__":
    ok = True
    for a1 in list(range(2, 40)) + [90, 105, 165, 210, 330, 390, 462, 770, 1001, 1155]:
        N = 400
        sb = simulate_brute(a1, N)
        sh, H = simulate_H(a1, N)
        assert sb == sh, (a1, "sequence mismatch")
        L = 1
        for h in H: L = lcm(L, prodset(h))
        def in_Sinf(x): return any(x % prodset(h) == 0 for h in H)
        T = sum(1 for x in range(a1, a1 + L) if in_Sinf(x))
        rel = all(sb[n + T] == sb[n] + L for n in range(len(sb) - T))
        # Step 1 enumeration: every S_inf element in [a1, sb[-1]] is a term
        ts = set(sb)
        conv = all((not in_Sinf(x)) or (x in ts) for x in range(a1, sb[-1] + 1))
        print(f"a1={a1:5d} L={L:8d} T={T:5d} rel={rel} enumeration={conv}")
        ok &= rel and conv
    print("ALL OK" if ok else "FAILED")
