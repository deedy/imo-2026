"""
Model for IMO 2026 P3 (stick cutting game).

Setup:
- LB marks <= n points, XY marks <= n points (all distinct), stick [0,1] cut into pieces.
- Players alternately claim any remaining piece, LB first.
- Both maximize own total length.

Claiming game value: with pieces sorted p1 >= p2 >= ... >= pm and both players
able to pick ANY piece, optimal play is greedy (take largest). LB gets odd-indexed
sum, XY gets even-indexed sum. So the game reduces to:

LB chooses n+1 pieces (composition of 1), XY subdivides with <= n further cuts;
payoff D = alternating sum = p1 - p2 + p3 - ... ; LB share = (1 + D)/2.

We discretize lengths on a grid of K atoms.
"""
from functools import lru_cache
import random
import sys

sys.setrecursionlimit(1000000)


def alt_sum(pieces):
    """D = p1 - p2 + p3 - ... for pieces sorted decreasing."""
    s = sorted(pieces, reverse=True)
    return sum(s[0::2]) - sum(s[1::2])


def lb_share(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[0::2])


# ---------- sanity: picking game value equals alternating-sum formula ----------
@lru_cache(maxsize=None)
def pick_value(state):
    """Value (total) for the player to move in the pick-any-piece game."""
    if not state:
        return 0
    total = sum(state)
    best = -1
    for i, p in enumerate(state):
        rest = state[:i] + state[i + 1:]
        val = total - pick_value(rest)
        if val > best:
            best = val
    return best


def test_picking():
    random.seed(0)
    for _ in range(200):
        m = random.randint(1, 8)
        pieces = tuple(sorted(random.randint(1, 9) for _ in range(m)))
        v = pick_value(pieces)
        formula = (sum(pieces) + alt_sum(pieces)) / 2
        assert v == formula, (pieces, v, formula)
    print("picking game value == odd-position sum: OK (200 random tests)")


# ---------- the cutting game on a grid ----------
@lru_cache(maxsize=None)
def xy_min(pieces, cuts):
    """pieces: sorted ascending tuple of ints (grid atoms). XY may make <= cuts
    further cuts (each cut splits one piece into two positive parts).
    Returns min achievable alternating sum D (in atoms)."""
    val = alt_sum(pieces)
    if cuts > 0:
        for i, L in enumerate(pieces):
            for j in range(1, L):
                new = tuple(sorted(pieces[:i] + pieces[i + 1:] + (j, L - j)))
                v = xy_min(new, cuts - 1)
                if v < val:
                    val = v
    return val


@lru_cache(maxsize=None)
def xy_min_strategy(pieces, cuts):
    """Returns (min D, best first move description)."""
    val = alt_sum(pieces)
    bestmove = ("stop",)
    if cuts > 0:
        for i, L in enumerate(pieces):
            for j in range(1, L):
                new = tuple(sorted(pieces[:i] + pieces[i + 1:] + (j, L - j)))
                v = xy_min(new, cuts - 1)
                if v < val:
                    val = v
                    bestmove = ("cut", L, j, new)
    return val, bestmove


def multisets(K, m, lo=0):
    """nondecreasing m-tuples of ints >= lo summing to K."""
    if m == 1:
        if K >= lo:
            yield (K,)
        return
    for first in range(lo, K // m + 1):
        for rest in multisets(K - first, m - 1, first):
            yield (first,) + rest


def lb_value(K, n, verbose=True):
    """max over LB multisets of (min over XY plays of D). Returns (D, argmax)."""
    best = -1
    arg = None
    for comp in multisets(K, n + 1):
        v = xy_min(comp, n)
        if v > best:
            best = v
            arg = comp
    if verbose:
        c = (K + best) / 2 / K
        print(f"n={n} K={K}: max-min D = {best} atoms = {best/K:.6f}, "
              f"LB share c = {c:.6f}, optimal LB pieces {arg}")
    return best, arg


if __name__ == "__main__":
    test_picking()
    print()
    print("Target values: n=1: 2/3=%.6f, n=2: 4/7=%.6f, n=3: 8/15=%.6f" %
          (2/3, 4/7, 8/15))
    print()
    for K in [3, 6, 9, 12]:
        lb_value(K, 1)
    print()
    for K in [7, 14]:
        lb_value(K, 2)
    print()
    for K in [6, 10]:
        lb_value(K, 2)
    print()
    lb_value(15, 3)
