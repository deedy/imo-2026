"""Is min over signed sums |sum delta_i a_i| (delta in {-1,0,1}, not all 0)
always EQUAL to min over subsets of greedy-chain?  If so, Part B = pigeonhole."""
from fractions import Fraction
import random, itertools


def chain(sub_desc):
    r = sub_desc[0]
    for x in sub_desc[1:]:
        r = abs(r - x)
    return r


def min_chain(fam):
    m = len(fam)
    best = None
    for r in range(1, m + 1):
        for I in itertools.combinations(sorted(fam, reverse=True), r):
            v = chain(list(I))
            if best is None or v < best:
                best = v
    return best


def min_signed(fam):
    m = len(fam)
    best = None
    for delta in itertools.product([0, 1, -1], repeat=m):
        if all(d == 0 for d in delta):
            continue
        v = abs(sum(d * a for d, a in zip(delta, fam)))
        if best is None or v < best:
            best = v
    return best


def test_equal(n, trials=300, seed=11):
    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        fam = [Fraction(rng.randint(1, 60), rng.randint(1, 4)) for _ in range(n + 1)]
        c = min_chain(fam)
        s = min_signed(fam)
        if c != s:
            bad += 1
            if bad <= 5:
                print(f"  DIFFER n={n}: fam={sorted(float(x) for x in fam)} chain-min={float(c):.4f} signed-min={float(s):.4f}")
    print(f"n={n}: differ in {bad}/{trials}")
    return bad


if __name__ == "__main__":
    for n in [1, 2, 3, 4]:
        test_equal(n)
