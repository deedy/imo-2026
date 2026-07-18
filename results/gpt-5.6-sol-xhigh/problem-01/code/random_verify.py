#!/usr/bin/env python3
"""Randomly verify termination outcomes and the predicted valuation formula."""

from collections import Counter
from functools import reduce
from math import gcd, lcm
from random import Random


def factor(n: int) -> Counter:
    ans = Counter()
    d = 2
    while d * d <= n:
        while n % d == 0:
            ans[d] += 1
            n //= d
        d += 1
    if n > 1:
        ans[n] += 1
    return ans


def predicted(xs):
    fs = [factor(x) for x in xs]
    primes = set().union(*(f.keys() for f in fs))
    out = 1
    for p in primes:
        e = reduce(gcd, (f[p] for f in fs))
        out *= p**e
    return out


def play(xs, rng, limit=100_000):
    xs = list(xs)
    for moves in range(limit):
        active = [i for i, x in enumerate(xs) if x > 1]
        if len(active) < 2:
            return max(xs), moves
        i, j = rng.sample(active, 2)
        m, n = xs[i], xs[j]
        d = gcd(m, n)
        xs[i], xs[j] = d, lcm(m, n) // d
    raise RuntimeError("move limit exceeded")


def main():
    rng = Random(202601)
    max_moves = 0
    for _ in range(5000):
        length = rng.randint(2, 12)
        xs = [rng.randint(2, 300) for _ in range(length)]
        want = predicted(xs)
        # Check several choices from the same initial board.
        for _ in range(4):
            got, moves = play(xs, rng)
            assert got == want, (xs, want, got)
            max_moves = max(max_moves, moves)
    print(f"all random tests passed; maximum observed moves = {max_moves}")


if __name__ == "__main__":
    main()
