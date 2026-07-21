import math
import random
from collections import defaultdict

def formula(initial):
    """Compute the final M = product p^gcd(exponents)."""
    exp_gcd = {}
    for a in initial:
        x = a
        p = 2
        while p * p <= x:
            if x % p == 0:
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                exp_gcd[p] = math.gcd(exp_gcd.get(p, cnt), cnt)
            p += 1 if p == 2 else 2
        if x > 1:
            exp_gcd[x] = math.gcd(exp_gcd.get(x, 1), 1)
    M = 1
    for p, e in exp_gcd.items():
        M *= p ** e
    return M

def final_M_brute(initial, max_moves=10000):
    """Simulate a random sequence of moves until termination."""
    state = list(initial)
    moves = 0
    while True:
        gt1 = [i for i, x in enumerate(state) if x > 1]
        if len(gt1) <= 1:
            break
        if moves > max_moves:
            return None
        i, j = random.sample(gt1, 2)
        m, n = state[i], state[j]
        g = math.gcd(m, n)
        h = (m * n) // (g * g)
        if i > j:
            i, j = j, i
        del state[j]
        del state[i]
        state.append(g)
        state.append(h)
        moves += 1
    return max(state) if any(x > 1 for x in state) else 1

if __name__ == '__main__':
    for _ in range(500):
        init = [random.randint(2, 30) for _ in range(5)]
        f = formula(init)
        b = final_M_brute(list(init))
        if b is None:
            print(f"Timeout: {init}")
        elif f != b:
            print(f"Mismatch: {init} -> formula {f}, brute {b}")
            raise SystemExit
    print("All tests passed.")
