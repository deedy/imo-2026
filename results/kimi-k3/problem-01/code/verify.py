"""
Verification for imo-2026-01.

Move: pick m,n > 1 at different places, replace by gcd(m,n) and lcm(m,n)/gcd(m,n).

Claims to verify:
 (a) every play terminates with exactly one entry M > 1;
 (b) M is independent of choices and equals prod_p p^{gcd_i v_p(a_i)}.
"""
from math import gcd
from itertools import combinations_with_replacement
import random
import sys

sys.setrecursionlimit(1000000)


def vp(x, p):
    e = 0
    while x % p == 0:
        x //= p
        e += 1
    return e


def primes_up_to(n):
    ps = []
    for x in range(2, n + 1):
        if all(x % p for p in ps if p * p <= x):
            ps.append(x)
    return ps


def formula_M(init):
    """prod_p p^{gcd_i v_p(a_i)}"""
    M = 1
    for p in primes_up_to(max(init)):
        g = 0
        for a in init:
            g = gcd(g, vp(a, p))
        M *= p ** g
    return M


def do_move(state, i, j):
    s = list(state)
    m, n = s[i], s[j]
    g = gcd(m, n)
    l = (m // g) * n  # lcm
    s[i] = g
    s[j] = l // g  # lcm/gcd
    return tuple(sorted(s))


def is_terminal(state):
    return sum(1 for x in state if x > 1) <= 1


def reachable_terminals(state, memo):
    if state in memo:
        return memo[state]
    if is_terminal(state):
        memo[state] = frozenset([state])
        return memo[state]
    n = len(state)
    out = set()
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] > 1 and state[j] > 1:
                out |= reachable_terminals(do_move(state, i, j), memo)
    memo[state] = frozenset(out)
    return memo[state]


def check_config(init):
    init = tuple(sorted(init))
    memo = {}
    ts = reachable_terminals(init, memo)
    assert len(ts) == 1, f"multiple terminals from {init}: {ts}"
    (t,) = ts
    big = [x for x in t if x > 1]
    assert len(big) == 1, f"terminal {t} of {init} does not have exactly one entry > 1"
    f = formula_M(init)
    assert big[0] == f, f"init {init}: terminal M={big[0]} but formula gives {f}"


def exhaustive_tests():
    # length 2
    for vals in combinations_with_replacement(range(2, 25), 2):
        check_config(vals)
    print("length 2 exhaustive: OK")
    # length 3
    for vals in combinations_with_replacement(range(2, 11), 3):
        check_config(vals)
    print("length 3 exhaustive: OK")
    # length 4
    for vals in combinations_with_replacement(range(2, 7), 4):
        check_config(vals)
    print("length 4 exhaustive: OK")
    # length 5,6 small values
    for vals in combinations_with_replacement(range(2, 5), 5):
        check_config(vals)
    for vals in combinations_with_replacement(range(2, 4), 6):
        check_config(vals)
    print("length 5,6 exhaustive: OK")


def random_playout_tests(trials=500):
    rng = random.Random(2026)
    for _ in range(trials):
        N = rng.randint(2, 12)
        init = tuple(sorted(rng.randint(2, 200) for _ in range(N)))
        f = formula_M(init)
        P0 = 1
        for a in init:
            P0 *= a
        state = list(init)
        moves = 0
        while True:
            pos = [i for i, x in enumerate(state) if x > 1]
            if len(pos) <= 1:
                break
            i, j = rng.sample(pos, 2)
            m, n = state[i], state[j]
            g = gcd(m, n)
            state[i] = g
            state[j] = (m // g) * n // g
            moves += 1
            assert moves <= N + P0.bit_length(), "move bound violated"
        big = [x for x in state if x > 1]
        assert len(big) == 1, f"random playout ended with {state}"
        assert big[0] == f, f"init {init}: random playout M={big[0]} != formula {f}"
    print(f"random playouts ({trials} trials): OK")


def invariant_tests(trials=2000):
    """Directly check gcd-of-valuations invariance under single random moves."""
    rng = random.Random(7)
    for _ in range(trials):
        N = rng.randint(2, 8)
        state = [rng.randint(2, 300) for _ in range(N)]
        pos = [i for i, x in enumerate(state) if x > 1]
        if len(pos) < 2:
            continue
        i, j = rng.sample(pos, 2)
        m, n = state[i], state[j]
        g = gcd(m, n)
        new = list(state)
        new[i] = g
        new[j] = (m // g) * n // g
        for p in primes_up_to(max(max(state), max(new))):
            b = 0
            for x in state:
                b = gcd(b, vp(x, p))
            a = 0
            for x in new:
                a = gcd(a, vp(x, p))
            assert a == b, f"invariant broken: {state} -> {new} at p={p}"
    print(f"invariant single-move tests ({trials} trials): OK")


if __name__ == "__main__":
    exhaustive_tests()
    random_playout_tests()
    invariant_tests()
    # a few illustrative examples
    for init in [(4, 6), (2, 3), (2, 4, 8), (6, 10, 15), (12, 18), (8, 12), (5, 5, 5, 5)]:
        print(init, "->", formula_M(init))
    print("ALL CHECKS PASSED")
