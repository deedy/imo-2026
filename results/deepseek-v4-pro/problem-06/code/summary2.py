import math
from itertools import combinations

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

def prime_factors_set(x):
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

def minimal_hitting_sets(edges, max_size=5):
    universe = sorted(set.union(*edges)) if edges else []
    hitting = []
    for r in range(1, min(max_size+1, len(universe)+1)):
        for combo in combinations(universe, r):
            if all(set(combo) & e for e in edges):
                minimal = True
                for i in range(len(combo)):
                    sub = set(combo[:i] + combo[i+1:])
                    if all(sub & e for e in edges):
                        minimal = False
                        break
                if minimal:
                    hitting.append(set(combo))
        if hitting:
            return hitting
    return []

def find_period(seq):
    n = len(seq)
    for T in range(1, n//2):
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
    return None

for a1 in range(2, 101):
    seq = gen(a1, 500)
    per = find_period(seq)
    if per is None:
        per = (None, None)
    T, L = per
    edges = [prime_factors_set(v) for v in seq[:30]]
    mhs = minimal_hitting_sets(edges)
    if not mhs:
        mhs = []
    # Get all primes involved in hitting sets
    all_p = set()
    for h in mhs:
        all_p |= h
    # print summary
    is_arith = (T == 1)
    print(f'a1={a1:3d}: T={T!s:5s}, L={L!s:5s}, hitting sets={mhs}, primes={sorted(all_p)}')
