"""Identify a minimal sufficient family of XY strategies for the upper bound."""
from fractions import Fraction
import random
import itertools
from strategy import strategy_min, Tn, parity_reduce, alt_sum_values, D_pool


def chain(pieces_desc):
    """Decreasing chain: runner cancels with next piece each time. pieces_desc sorted descending."""
    r = pieces_desc[0]
    for x in pieces_desc[1:]:
        r = abs(r - x)
    return r


def subset_alt(pool, I):
    """Alternating sum of pieces at indices I (0-based, ascending pool)."""
    vals = [pool[i] for i in I]
    return alt_sum_values(vals)


def family_value(pool, n):
    """Min over a candidate family; returns dict of named families."""
    m = len(pool)
    S = sum(pool)
    # all subsets (halving complement)
    best_subset = None
    for r in range(1, m + 1):
        for I in itertools.combinations(range(m), r):
            v = subset_alt(pool, I)
            if best_subset is None or v < best_subset:
                best_subset = v
    # full decreasing chain
    full_chain = chain(tuple(sorted(pool, reverse=True)))
    # prefix chains (chain on {a_1..a_k}, halve the rest)
    prefix = min(chain(tuple(sorted(pool[:k], reverse=True))) for k in range(1, m + 1))
    # suffix chains
    suffix = min(chain(tuple(sorted(pool[k:], reverse=True))) for k in range(m))
    return {
        "subset": best_subset,
        "full_chain": full_chain,
        "prefix_chain": prefix,
        "suffix_chain": suffix,
    }


def test(n, trials=2000, seed=3):
    random.seed(seed)
    need = {"subset_only": 0, "chain": 0, "other": 0}
    fail = 0
    examples = []
    for _ in range(trials):
        cuts = sorted(random.randint(1, 10**6) for _ in range(n))
        pts = [0] + cuts + [10**6]
        pool = tuple(sorted(Fraction(pts[i+1] - pts[i], 10**6) for i in range(n + 1)))
        S = sum(pool)
        T = Tn(n) * S
        fv = family_value(pool, n)
        best = min(fv.values())
        if best > T:
            fail += 1
            examples.append((pool, fv))
        # classify
        if fv["subset"] <= T:
            need["subset_only"] += 1
        elif min(fv["full_chain"], fv["prefix_chain"], fv["suffix_chain"]) <= T:
            need["chain"] += 1
        else:
            need["other"] += 1
    print(f"n={n}: family min > T_n*S in {fail}/{trials} configs")
    print(f"   classification: {need}")
    for pool, fv in examples[:5]:
        print("   FAIL:", pool, {k: float(v) for k, v in fv.items()}, "T=", float(Tn(n)*sum(pool)))
    return fail


if __name__ == "__main__":
    for n in [2, 3]:
        test(n)
