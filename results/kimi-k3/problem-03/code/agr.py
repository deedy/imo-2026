"""Adjacent-Gap Realizability (AGR):
If two subset sums sA > sB have NO subset sum strictly between them,
then v = sA - sB is realizable as a nested-abs chain on P=A\B, N=B\A in some order.

Test: for random families, for every adjacent gap, search an order realizing v.
Also test the greedy scheduling rule.
"""
from fractions import Fraction
import random, itertools


def nested_abs(order):
    r = order[0]
    for x in order[1:]:
        r = abs(r - x)
    return r


def realizable_brute(P, N, v):
    """search an order of P+N with nested abs == v."""
    elems = list(P) + list(N)
    seen = set()
    for perm in itertools.permutations(elems):
        if perm in seen:
            continue
        seen.add(perm)
        if nested_abs(list(perm)) == v:
            return perm
    return None


def greedy_order(P, N):
    """scheduling rule: D>=0 -> process largest N; D<0 -> process largest P."""
    P = sorted(P, reverse=True)
    N = sorted(N, reverse=True)
    order = []
    D = Fraction(0)
    i = j = 0
    # start: D == 0 counts as >= 0 (process N) -- but if N empty process P
    while i < len(P) or j < len(N):
        if D >= 0 and j < len(N):
            order.append(N[j]); D -= N[j]; j += 1
        elif D < 0 and i < len(P):
            order.append(P[i]); D += P[i]; i += 1
        elif j < len(N):
            order.append(N[j]); D -= N[j]; j += 1
        else:
            order.append(P[i]); D += P[i]; i += 1
    return order


def subset_sums(fam):
    m = len(fam)
    d = {}
    for mask in range(1 << m):
        s = sum(fam[i] for i in range(m) if mask >> i & 1)
        d.setdefault(s, []).append(mask)
    return d


def masks_to_PN(A, B):
    P = [i for i in range(64) if (A >> i & 1) and not (B >> i & 1)]
    N = [i for i in range(64) if (B >> i & 1) and not (A >> i & 1)]
    return P, N


def test_family(fam, verbose=False):
    """check ALL adjacent gaps of one family for realizability."""
    m = len(fam)
    ss = subset_sums(fam)
    sums = sorted(ss)
    fails = []
    for k in range(len(sums) - 1):
        sB, sA = sums[k], sums[k + 1]
        if sA == sB:
            continue
        # adjacent in the value list; check no subset sum strictly between (by construction: none)
        v = sA - sB
        # try all mask pairs achieving these sums (any A,B with these sums)
        ok = False
        for A in ss[sA]:
            for B in ss[sB]:
                Pi, Ni = masks_to_PN(A, B)
                P = [fam[i] for i in Pi]
                N = [fam[i] for i in Ni]
                # AGR needs: no subset sum strictly between sB and sA (given)
                # but we should check THIS pair (A,B): the realizability of v=sum(P)-sum(N)
                if sum(P) - sum(N) != v:
                    continue
                perm = realizable_brute(P, N, v)
                if perm is not None:
                    ok = True
                    break
            if ok:
                break
        if not ok:
            fails.append((sB, sA, v))
    return fails


def test_random(m, trials=100, seed=5):
    rng = random.Random(seed)
    total_fail = 0
    for t in range(trials):
        fam = [Fraction(rng.randint(1, 25)) for _ in range(m)]
        fails = test_family(fam)
        if fails:
            total_fail += 1
            if total_fail <= 3:
                print(f"  fam={sorted(float(x) for x in fam)}: {len(fails)} adjacent gaps NOT realizable: {fails[:3]}")
    print(f"m={m}: families with failures: {total_fail}/{trials}")
    return total_fail


if __name__ == "__main__":
    for m in [3, 4, 5]:
        test_random(m, trials=60)
    print()
    # targeted: greedy rule check on the examples
    for P, N in [([8,9,10],[11,12]), ([5,9],[6,7]), ([10,9],[8,7,6])]:
        P = [Fraction(x) for x in P]; N = [Fraction(x) for x in N]
        v = sum(P) - sum(N)
        o = greedy_order(P, N)
        print(f"P={P} N={N} v={v}: greedy order {o} -> {nested_abs(o)}")
