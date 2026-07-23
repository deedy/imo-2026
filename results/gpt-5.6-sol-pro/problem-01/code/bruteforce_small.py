"""Explore all legal move sequences for small boards and check the formula for M."""
from functools import lru_cache
from itertools import combinations, product
from math import gcd, lcm


def predicted(board):
    primes = set()
    for x in board:
        d = 2
        while d * d <= x:
            if x % d == 0:
                primes.add(d)
                while x % d == 0:
                    x //= d
            d += 1
        if x > 1:
            primes.add(x)
    ans = 1
    for p in primes:
        exponents = []
        for x in board:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            exponents.append(e)
        g = 0
        for e in exponents:
            g = gcd(g, e)
        ans *= p**g
    return ans


@lru_cache(None)
def terminal_values(state):
    state = tuple(sorted(state))
    nonunits = [i for i, x in enumerate(state) if x > 1]
    if len(nonunits) == 1:
        return frozenset([state[nonunits[0]]])
    out = set()
    for i, j in combinations(nonunits, 2):
        m, n = state[i], state[j]
        g = gcd(m, n)
        nxt = list(state)
        nxt[i] = g
        nxt[j] = lcm(m, n) // g
        out.update(terminal_values(tuple(sorted(nxt))))
    return frozenset(out)


for length in range(2, 5):
    for board in product(range(2, 11), repeat=length):
        values = terminal_values(tuple(sorted(board)))
        target = predicted(board)
        assert values == frozenset([target]), (board, values, target)
print("All boards of lengths 2..4 with entries 2..10 passed.")
