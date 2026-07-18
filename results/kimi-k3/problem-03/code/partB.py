"""Part B: test whether min over subsets of greedy-chain is always <= T_n * S.
Also test interval-chains and block-chain variants, and adversarial search."""
from fractions import Fraction
import random, itertools


def chain(sub_desc):
    """greedy nested abs diff, input sorted descending."""
    r = sub_desc[0]
    for x in sub_desc[1:]:
        r = abs(r - x)
    return r


def min_chain_subsets(fam):
    """min over nonempty subsets of chain value."""
    m = len(fam)
    best = None
    for r in range(1, m + 1):
        for I in itertools.combinations(sorted(fam, reverse=True), r):
            v = chain(list(I))
            if best is None or v < best:
                best = v
    return best


def min_chain_intervals(fam):
    f = sorted(fam)
    m = len(f)
    best = None
    for i in range(m):
        for j in range(i, m):
            v = chain(list(reversed(f[i:j+1])))
            if best is None or v < best:
                best = v
    return best


def Tn(n):
    return Fraction(1, 2**(n + 1) - 1)


def test_random(n, trials=2000, seed=42):
    rng = random.Random(seed)
    worst_sub = Fraction(0); worst_int = Fraction(0)
    ex_sub = ex_int = None
    for _ in range(trials):
        cuts = sorted(rng.randint(1, 10**6) for _ in range(n))
        pts = [0] + cuts + [10**6]
        fam = [Fraction(pts[i+1] - pts[i], 10**6) for i in range(n + 1)]
        S = sum(fam)
        v1 = min_chain_subsets(fam)
        v2 = min_chain_intervals(fam)
        if v1 / S > worst_sub:
            worst_sub = v1 / S; ex_sub = fam
        if v2 / S > worst_int:
            worst_int = v2 / S; ex_int = fam
    print(f"n={n}: worst min-subset-chain/S = {float(worst_sub):.6f}, "
          f"worst min-interval-chain/S = {float(worst_int):.6f}, T_n = {float(Tn(n)):.6f}")
    print(f"   subset-chain <= T_n: {worst_sub <= Tn(n)}; interval-chain <= T_n: {worst_int <= Tn(n)}")
    if worst_int > Tn(n):
        print("   interval counterexample:", [float(x) for x in ex_int])
    return worst_sub, worst_int


def adversarial(n, restarts=30, iters=3000, seed=7):
    """local search to MAXIMIZE min-subset-chain/S."""
    rng = random.Random(seed)
    best_fam = None; best_val = Fraction(0)
    for r in range(restarts):
        fam = [Fraction(rng.randint(1, 1000)) for _ in range(n + 1)]
        cur = min_chain_subsets(fam) / sum(fam)
        for it in range(iters):
            i = rng.randrange(n + 1)
            fam2 = list(fam)
            fam2[i] = Fraction(max(1, fam2[i].numerator + rng.randint(-50, 50)), fam2[i].denominator)
            v = min_chain_subsets(fam2) / sum(fam2)
            if v > cur:
                fam, cur = fam2, v
        if cur > best_val:
            best_val, best_fam = cur, fam
    print(f"n={n}: adversarial max of min-subset-chain/S = {float(best_val):.6f} (T_n={float(Tn(n)):.6f})")
    print("   extremal family:", sorted(float(x) for x in best_fam))
    print("   ratios to smallest:", sorted(float(x / min(best_fam)) for x in best_fam))
    return best_val


if __name__ == "__main__":
    for n in [1, 2, 3, 4]:
        test_random(n)
    print()
    for n in [2, 3]:
        adversarial(n)
