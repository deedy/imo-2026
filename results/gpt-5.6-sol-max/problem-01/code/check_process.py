#!/usr/bin/env python3
"""Finite sanity checks for the blackboard operation.

This is not part of the proof.  It exhaustively explores every legal move for
small initial multisets and checks strict descent of the proposed potential,
termination, and the formula for the unique terminal entry.
"""

from functools import lru_cache
from itertools import combinations_with_replacement
from math import gcd, lcm


def factor(n: int) -> dict[int, int]:
    ans: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            ans[p] = ans.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        ans[n] = ans.get(n, 0) + 1
    return ans


def predicted(state: tuple[int, ...]) -> int:
    facs = [factor(x) for x in state]
    primes = set().union(*(f.keys() for f in facs))
    out = 1
    for p in primes:
        g = 0
        for f in facs:
            g = gcd(g, f.get(p, 0))
        out *= p**g
    return out


def potential(state: tuple[int, ...]) -> int:
    product = 1
    nonunits = 0
    for x in state:
        product *= x
        nonunits += x > 1
    return product * 2**nonunits


def children(state: tuple[int, ...]):
    n = len(state)
    for i in range(n):
        if state[i] == 1:
            continue
        for j in range(i + 1, n):
            if state[j] == 1:
                continue
            d = gcd(state[i], state[j])
            q = lcm(state[i], state[j]) // d
            child = list(state)
            child[i] = d
            child[j] = q
            child = tuple(sorted(child))
            assert potential(child) < potential(state), (state, child)
            yield child


@lru_cache(None)
def endpoints(state: tuple[int, ...]) -> frozenset[int]:
    nxt = set(children(state))
    if not nxt:
        nonunits = [x for x in state if x > 1]
        assert len(nonunits) == 1
        return frozenset(nonunits)
    ans: set[int] = set()
    for child in nxt:
        ans.update(endpoints(child))
    return frozenset(ans)


def main() -> None:
    tested = 0
    for size in range(2, 5):
        for tup in combinations_with_replacement(range(2, 11), size):
            state = tuple(sorted(tup))
            ends = endpoints(state)
            want = predicted(state)
            assert ends == {want}, (state, ends, want)
            tested += 1
    print(f"checked all move trees for {tested} initial multisets; all tests passed")
    print(f"cached states: {endpoints.cache_info().currsize}")


if __name__ == "__main__":
    main()
