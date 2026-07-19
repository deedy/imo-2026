"""Quick check of the killing properties used in the proof of imo-2026-06.

(K)  every x > a1 with x notin S_inf is coprime to some term a_i < x
(K') for finite prime-sets F with pi(F) > a1 containing no permanent,
     there is a permanent t' disjoint from F with pi(t') < pi(F).

We simulate via the permanent family H (minimal transversals), which the
previous sessions' scripts verified equals the true permanent family C
(H stabilizes; also cross-checked against raw brute force for small a1).
"""
from math import gcd
from sympy import factorint, primerange
from itertools import combinations
import sys
sys.path.insert(0, 'code')
from verify_newproof import simulate_H, supp, prodset

def check(a1, N=1500, xmax=40000):
    seq, H = simulate_H(a1, N)
    terms = sorted(seq)
    perm = [prodset(h) for h in H]

    def in_Sinf(x):
        return any(x % h == 0 for h in perm)

    # --- (K): for every x in (a1, xmax] outside S_inf, a term < x coprime to x
    badK = []
    for x in range(a1 + 1, xmax + 1):
        if in_Sinf(x):
            continue
        if not any(a < x and gcd(a, x) == 1 for a in terms):
            badK.append(x)
            if len(badK) > 3:
                break

    # --- (K'): enumerate finite prime sets F (primes <= 47) with pi(F) in
    # (a1, 10^7], containing no member of H; require disjoint permanent, smaller product
    primes = list(primerange(2, 48))
    badKp = []
    tested = 0
    for r in range(1, 5):
        for combo in combinations(primes, r):
            F = frozenset(combo)
            p = prodset(F)
            if p <= a1 or p > 10**7:
                continue
            if any(set(h) <= set(F) for h in H):
                continue  # F contains a permanent
            tested += 1
            ok = any(not (set(h) & set(F)) and prodset(h) < p for h in H)
            if not ok:
                badKp.append(F)
                if len(badKp) > 3:
                    break
    return badK, badKp, tested, len(H)

if __name__ == "__main__":
    cases = list(range(2, 45)) + [90, 105, 165, 210, 330, 390, 462, 510, 770,
                                  1001, 1155, 1925, 2310]
    allok = True
    for a1 in cases:
        badK, badKp, tested, nh = check(a1)
        status = "OK " if not badK and not badKp else "FAIL"
        if badK or badKp:
            allok = False
        print(f"{status} a1={a1:5d} |C|={nh:3d} (K) viol={badK} (K') viol={badKp} (F tested: {tested})")
    print("ALL OK" if allok else "SOME FAILED")
