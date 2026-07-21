import math
from itertools import combinations

def gen(a1, max_terms=100):
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
            break
    return hitting

def max_minimal_hitting_set_size(edges):
    mhs = minimal_hitting_sets(edges)
    if not mhs:
        return 0
    return max(len(h) for h in mhs)

# Test many a1 up to 200
for a1 in range(2, 201):
    seq = gen(a1, 80)
    edges = [prime_factors_set(v) for v in seq[:50]]
    max_hs = max_minimal_hitting_set_size(edges)
    if max_hs > 2:
        print(f'a1={a1}: max minimal hitting set size = {max_hs}')
        mhs = minimal_hitting_sets(edges)
        print(f'  hitting sets: {mhs[:10]}')
    # also check if sequence is arithmetic (T=1)
    # compute differences
    diffs = [seq[i+1]-seq[i] for i in range(min(20, len(seq)-1))]
    if len(set(diffs)) == 1:
        # arithmetic
        pass
    else:
        if max_hs < 2:
            print(f'a1={a1}: max_hs={max_hs}, diffs: {diffs[:10]}')
