from fractions import Fraction as F
from functools import lru_cache
import itertools, random

def minimax(M):
    """Return (value FP can force, value SP can force) via exact minimax.
    State: tuple of remaining pieces, FP to move. Returns (FP_total, SP_total) under optimal play."""
    @lru_cache(maxsize=None)
    def solve(state):
        state = tuple(state)
        if not state: return (F(0), F(0))
        best = None
        for i, x in enumerate(state):
            rest = state[:i] + state[i+1:]
            fp2, sp2 = solve(rest)  # after taking x, roles swap: current player gets x + opponent-of-rest value
            cand = (x + sp2, fp2)   # current player takes x, then is second player on rest
            if best is None or cand[0] > best[0]: best = cand
        return best
    v = solve(tuple(sorted(M, reverse=True)))
    return v  # (FP total, SP total) under optimal play with FP choosing to maximize own total

def oddeven(M):
    s = sorted(M, reverse=True)
    odd = sum(s[0::2], F(0)); even = sum(s[1::2], F(0))
    return odd, even

tests = [[F(3),F(2),F(1)], [F(5),F(3),F(2)], [F(4),F(4),F(1),F(1)], [F(7),F(1),F(1),F(1),F(1)]]
random.seed(1)
for _ in range(300):
    m = random.randint(1,7)
    tests.append([F(random.randint(1,20), random.choice([1,2,4])) for _ in range(m)])

ok = True
for M in tests:
    fp, sp = minimax(M)
    odd, even = oddeven(M)
    if not (fp == odd and sp == even):
        ok = False
        print("MISMATCH", M, "minimax:", fp, sp, "odd/even:", odd, even)
print("reviewer example {3,2,1}: FP gets", minimax([F(3),F(2),F(1)])[0], ", SP gets", minimax([F(3),F(2),F(1)])[1], "(even(M)=2)")
print("ALL OK" if ok else "FAILURES FOUND", f"({len(tests)} multisets)")
