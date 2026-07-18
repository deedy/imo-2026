"""Verify the components of the new proof for imo-2026-06.

Checks, for many starting values a1:
  (A) sequence == increasing enumeration of S_inf ∩ [a1, inf)   [Step 1]
  (B) permanents (minimal elements of S_inf) form an antichain that is
      pairwise intersecting and self-dual (minimal transversals of C = C) [Step 3]
  (C) a_{n+T} = a_n + L with L = lcm of permanents, T = #S_inf ∩ [a1, a1+L) [Step 2]

Also (D): sanity checks of the combinatorial theory:
  - blocker(bblocker(C)) == C for random clutters (standard identity used implicitly)
  - brute-force: on tiny ground sets, enumerate ALL self-dual intersecting antichains
    and confirm properties hold (they are finite by construction, so this tests the
    self-duality characterization rather than finiteness).
"""
from math import gcd, lcm
from sympy import factorint
from itertools import combinations
import random

def supp(m):
    return frozenset(factorint(m).keys())

def prodset(s):
    r = 1
    for p in s: r *= p
    return r

def simulate_H(a1, N):
    """Simulate sequence via minimal transversals H; returns (seq, H_final)."""
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

def is_transversal(T, family):
    return all(T & F for F in family)

def blocker(C, ground):
    """Minimal transversals of clutter C (sets from `ground`)."""
    C = [set(c) for c in C]
    # transversals of C, then take minimal ones
    Ts = []
    # incremental: start with one empty; extend
    Ts = [set()]
    for F in C:
        new = []
        for T in Ts:
            if T & F:
                new.append(T)
            else:
                for x in F:
                    new.append(T | {x})
        # prune non-minimal
        mn = []
        for T in new:
            if not any(U < T for U in new):
                mn.append(T)
        Ts = []
        seen = set()
        for T in mn:
            f = frozenset(T)
            if f not in seen:
                seen.add(f); Ts.append(T)
    return {frozenset(T) for T in Ts}

def is_antichain(C):
    C = list(C)
    return all(not (C[i] < C[j]) for i in range(len(C)) for j in range(len(C)) if i != j)

def is_intersecting(C):
    C = list(C)
    return all(C[i] & C[j] for i in range(len(C)) for j in range(i+1, len(C)))

# ---------- (D) brute force self-dual examples on tiny ground sets ----------
def all_clutters_test():
    """On ground set [4], enumerate antichains, filter intersecting & self-dual.
    Verify each one satisfies: blocker(C) == C. (Consistency check of definitions.)"""
    ground = frozenset([1,2,3,4])
    subsets = [frozenset(s) for r in range(1, 4) for s in combinations(ground, r)]
    count_sd = 0
    examples = []
    # iterate over all antichains (there are not too many on 4 points if we bound size)
    antichains = []
    for r in range(1, 30):
        for combo in combinations(subsets, r):
            if is_antichain(combo):
                antichains.append(combo)
        if len(antichains) > 200000:
            break
    for C in antichains:
        if not is_intersecting(C):
            continue
        B = blocker(C, ground)
        if B == set(C):
            count_sd += 1
            examples.append(C)
    return count_sd, examples[:5]

if __name__ == "__main__":
    random.seed(1)

    # --- Test blocker-of-blocker identity on random clutters ---
    ok = 0
    for trial in range(300):
        ground = list(range(1, 8))
        C = set()
        for _ in range(random.randint(1, 6)):
            sz = random.randint(1, 4)
            C.add(frozenset(random.sample(ground, sz)))
        # make antichain
        Cl = list(C)
        C = {c for c in Cl if not any(d < c for d in Cl)}
        B = blocker(C, ground)
        BB = blocker(B, ground)
        assert BB == C, (C, B, BB)
        ok += 1
    print(f"blocker-of-blocker identity: {ok}/300 OK")

    # --- Test self-dual intersecting enumeration on [4] ---
    n_sd, ex = all_clutters_test()
    print(f"self-dual intersecting antichains found on 4 points: {n_sd}; examples: {ex}")

    # --- Main verification on the IMO sequence ---
    cases = list(range(2, 60)) + [105, 165, 195, 210, 330, 390, 420, 462, 510, 570,
                                  630, 714, 770, 840, 910, 1001, 1155, 1290, 1365,
                                  1485, 1710, 1925, 2002, 2310]
    allok = True
    for a1 in cases:
        N = 1200
        seq, H = simulate_H(a1, N)
        # (A) enumeration property: check terms pairwise intersect and every x in
        # [a1, seq[-1]] meeting all previous terms is a term
        terms_set = set(seq)
        # check S_inf membership: x meets every term <=> x multiple of some h in H
        def in_Sinf(x):
            return any(prodset(h) and x % prodset(h) == 0 for h in H)
        enum_ok = all(in_Sinf(x) for x in seq)  # terms in S_inf
        # every S_inf element below seq[-1] is a term
        x = a1
        conv_ok = True
        while x <= seq[-1]:
            if in_Sinf(x) and x not in terms_set:
                conv_ok = False; break
            x += 1
        # (B) permanents properties
        anti = is_antichain(H)
        inter = is_intersecting(H)
        ground = set().union(*H)
        B = blocker(H, ground)
        selfdual = (B == set(H))
        # (C) final relation
        L = 1
        for h in H:
            L = lcm(L, prodset(h))
        T = sum(1 for x in range(a1, a1 + L) if in_Sinf(x))
        rel_ok = all(seq[n + T] == seq[n] + L for n in range(len(seq) - T))
        if not (enum_ok and conv_ok and anti and inter and selfdual and rel_ok):
            allok = False
            print(f"FAIL a1={a1}: enum={enum_ok} conv={conv_ok} anti={anti} inter={inter} "
                  f"selfdual={selfdual} rel={rel_ok} |H|={len(H)}")
        else:
            print(f"OK a1={a1:5d}: |H|={len(H):3d} L={L:10d} T={T:5d}")
    print("ALL OK" if allok else "SOME FAILED")
