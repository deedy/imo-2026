import math
import random

def compute_M_brute(initial, max_steps=10000):
    """Try random sequences and see if final M is always same."""
    from functools import reduce
    # We'll do random moves just to see
    state = list(initial)
    while True:
        gt1 = [i for i, x in enumerate(state) if x > 1]
        if len(gt1) <= 1:
            break
        # pick random pair
        i, j = random.sample(gt1, 2)
        m, n = state[i], state[j]
        g = math.gcd(m, n)
        h = (m * n) // (g * g)  # lcm/gcd
        # replace: remove larger index first
        if i < j:
            del state[j]
            del state[i]
        else:
            del state[i]
            del state[j]
        state.append(g)
        state.append(h)
    return max(state) if any(x>1 for x in state) else 1

def compute_M_formula(initial):
    # for each prime, gcd of exponents
    # factor each number
    from collections import defaultdict
    exp_gcd = defaultdict(int)
    # Actually we need to compute gcd of exponents for each prime across all numbers
    # We'll compute prime factorization for each number
    prime_exps = defaultdict(list)
    for a in initial:
        x = a
        p = 2
        while p * p <= x:
            if x % p == 0:
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                prime_exps[p].append(cnt)
            p += 1 if p == 2 else 2
        if x > 1:
            prime_exps[x].append(1)
    # Now compute gcd for each prime
    M = 1
    all_primes = set(prime_exps.keys())
    # Also need primes that appear with exponent 0 in some numbers
    # But that's handled: for each prime, we need gcd of all exponents (including zeros for numbers not having that prime)
    # Actually the gcd of the multiset of exponents across all numbers includes zeros for numbers that don't have that prime.
    # So for each prime, the list of exponents must have length = len(initial), with zeros for numbers not divisible by p.
    for p in all_primes:
        exps = prime_exps[p]
        # The other numbers have exponent 0
        # So the full list is exps + [0]*(len(initial)-len(exps))
        # gcd of that list = gcd of all exps (since gcd(x1,...,xk, 0,...,0) = gcd(x1,...,xk))
        g = 0
        for e in exps:
            g = math.gcd(g, e) if g else e
        M *= p ** g
    return M

def test_random():
    for _ in range(100):
        n = random.randint(2, 5)
        initial = [random.randint(2, 10) for _ in range(n)]
        M1 = compute_M_brute(list(initial))
        M2 = compute_M_formula(initial)
        if M1 != M2:
            print(f"Mismatch: {initial} -> brute {M1}, formula {M2}")
            return
    print("All tests passed")

test_random()
