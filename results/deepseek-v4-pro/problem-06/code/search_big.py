import math
from itertools import combinations
import sys

def gen(a1, max_terms=200):
    a = [a1]
    for n in range(1, max_terms):
        cand = a[-1] + 1
        while True:
            ok = True
            for prev in a:
                if math.gcd(cand, prev) == 1:
                    ok = False
                    break
            if ok:
                a.append(cand)
                break
            cand += 1
    return a

def prime_set(x):
    s = set()
    d = 2
    while d*d <= x:
        if x % d == 0:
            s.add(d)
            while x % d == 0:
                x //= d
        d += 1 if d==2 else 2
    if x > 1:
        s.add(x)
    return s

def max_minimal_hitting_set_size(edges, limit=6):
    universe = sorted(set.union(*edges)) if edges else []
    if not universe:
        return 0, []
    max_size = 0
    worst = []
    for r in range(1, min(limit+1, len(universe)+1)):
        found_any = False
        for combo in combinations(universe, r):
            if all(set(combo) & e for e in edges):
                # check minimal
                minimal = True
                for i in range(len(combo)):
                    sub = set(combo[:i] + combo[i+1:])
                    if all(sub & e for e in edges):
                        minimal = False
                        break
                if minimal:
                    found_any = True
                    if r > max_size:
                        max_size = r
                        worst = [set(combo)]
                    elif r == max_size:
                        worst.append(set(combo))
        if found_any and r > max_size:
            pass
    return max_size, worst

def find_T_L(seq, max_T=500):
    n = len(seq)
    for T in range(1, min(max_T, n//2)+1):
        L = seq[T] - seq[0]
        if L <= 0:
            continue
        ok = True
        for i in range(n - T):
            if seq[i+T] - seq[i] != L:
                ok = False
                break
        if ok:
            return T, L
    return None, None

# Test all a1 from 2 to 300 for max hitting set size
found_big = []
for a1 in range(2, 301):
    seq = gen(a1, 300)
    edges = [prime_set(v) for v in seq[:150]]
    sz, worst = max_minimal_hitting_set_size(edges, 6)
    if sz > 2:
        T, L = find_T_L(seq, 400)
        found_big.append((a1, sz, worst, T, L))
        print(f'a1={a1}: max MHS size = {sz}')
        print(f'  examples: {worst[:5]}')
        print(f'  T={T}, L={L}')
        if sz >= 4:
            print('  *** LARGE ***')

if not found_big:
    print('All a1 up to 300 have max MHS size <= 2')
