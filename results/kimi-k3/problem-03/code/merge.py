"""Test the 'non-positive merge' lemma (NM):
In a subdivision of a super-increasing family, there exist two fragments of the
same original piece whose merge does NOT increase D. This gives a clean induction."""
from fractions import Fraction
import random, itertools


def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[0::2]) - sum(s[1::2])


def subdivisions(pieces, ncuts, trials, rng):
    """Random subdivisions: each of ncuts cuts splits a random current piece."""
    for _ in range(trials):
        cur = list(pieces)
        for _ in range(ncuts):
            i = rng.randrange(len(cur))
            L = cur[i]
            u = Fraction(rng.randrange(1, 1000), 1000) * L
            cur = cur[:i] + cur[i+1:] + [u, L - u]
        yield cur


def test_NM(n, trials=200, seed=5):
    rng = random.Random(seed)
    delta = Fraction(1)
    pieces = [delta * 2**i for i in range(n + 1)]  # geometric, margin delta
    S = sum(pieces)
    fails = 0
    for _ in range(trials):
        # random subdivision with <= n cuts
        ncuts = rng.randrange(0, n + 1)
        cur = list(pieces)
        parents = list(range(n + 1))
        for _ in range(ncuts):
            i = rng.randrange(len(cur))
            L = cur[i]
            u = Fraction(rng.randrange(1, 1000), 1000) * L
            cur = cur[:i] + cur[i+1:] + [u, L - u]
            parents = parents[:i] + parents[i+1:] + [parents[i], parents[i]]
        D = alt_sum(cur)
        # check D >= delta
        assert D >= delta, ("Part A violated!", cur, D)
        # NM: exists same-parent pair whose merge doesn't increase D
        if ncuts >= 1:
            ok = False
            for i, j in itertools.combinations(range(len(cur)), 2):
                if parents[i] == parents[j]:
                    new = cur[:]
                    v = new[i] + new[j]
                    new = [x for k, x in enumerate(cur) if k not in (i, j)] + [v]
                    if alt_sum(new) <= D:
                        ok = True
                        break
            if not ok:
                fails += 1
                print("NM FAIL:", cur, parents, D)
    print(f"n={n}: Part A (D>=delta) held in all {trials} random subdivisions; NM fails: {fails}")


if __name__ == "__main__":
    for n in [1, 2, 3, 4]:
        test_NM(n)
