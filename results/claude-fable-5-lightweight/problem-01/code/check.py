import itertools, math, random
from math import gcd
from functools import reduce

def lcm(a,b): return a*b//gcd(a,b)

def moves(state):
    """All states reachable in one move. state: sorted tuple."""
    out = set()
    n = len(state)
    for i in range(n):
        for j in range(i+1, n):
            m, k = state[i], state[j]
            if m > 1 and k > 1:
                g = gcd(m, k)
                h = lcm(m, k)//g
                new = list(state)
                new[i], new[j] = g, h
                out.add(tuple(sorted(new)))
    return out

def factorize(x):
    f = {}
    d = 2
    while d*d <= x:
        while x % d == 0:
            f[d] = f.get(d,0)+1
            x //= d
        d += 1
    if x > 1: f[x] = f.get(x,0)+1
    return f

def predicted_M(start):
    primes = set()
    for x in start: primes |= set(factorize(x))
    M = 1
    for p in primes:
        exps = []
        for x in start:
            e = 0
            y = x
            while y % p == 0:
                e += 1; y //= p
            exps.append(e)
        g = reduce(gcd, exps)
        M *= p**g
    return M

def bfs_check(start, verbose=False):
    start = tuple(sorted(start))
    seen = {start}
    frontier = [start]
    terminals = set()
    steps = 0
    while frontier:
        nxt = []
        for s in frontier:
            ms = moves(s)
            if not ms:
                terminals.add(s)
            else:
                for t in ms:
                    if t not in seen:
                        seen.add(t); nxt.append(t)
        frontier = nxt
        steps += 1
        assert steps < 10000
    # checks
    Ms = set()
    for t in terminals:
        big = [x for x in t if x > 1]
        assert len(big) == 1, (start, t)   # part (a): exactly one entry > 1
        Ms.add(big[0])
    assert len(Ms) == 1, (start, terminals)  # part (b): unique M
    M = Ms.pop()
    assert M == predicted_M(start), (start, M, predicted_M(start))
    if verbose:
        print(start, "-> M =", M, "#reachable states:", len(seen), "#terminals:", len(terminals))
    return M

random.seed(2026)

# exhaustive over all triples 2..14
cnt = 0
for a in range(2,15):
    for b in range(a,15):
        for c in range(b,15):
            bfs_check((a,b,c)); cnt += 1
print("all triples 2..14 OK:", cnt)

# random 4-tuples
for _ in range(300):
    s = tuple(random.randint(2,30) for _ in range(4))
    bfs_check(s)
print("random 4-tuples OK")

# random 5-tuples smallish
for _ in range(60):
    s = tuple(random.randint(2,12) for _ in range(5))
    bfs_check(s)
print("random 5-tuples OK")

# a few illustrative
for s in [(4,8,6),(2,2,2,2),(12,18,30),(8,8,8),(9,27,81,243)]:
    bfs_check(s, verbose=True)

# also verify the potential T+N strictly decreases along every edge
def Omega(x):
    return sum(factorize(x).values())
def pot(s):
    return sum(Omega(x) for x in s) + sum(1 for x in s if x>1)
def check_pot(start):
    start = tuple(sorted(start))
    seen={start}; frontier=[start]
    while frontier:
        nxt=[]
        for s in frontier:
            for t in moves(s):
                assert pot(t) <= pot(s)-1, (s,t)
                if t not in seen:
                    seen.add(t); nxt.append(t)
        frontier=nxt
for a in range(2,12):
    for b in range(a,12):
        for c in range(b,12):
            check_pot((a,b,c))
print("potential strictly decreases: OK")
