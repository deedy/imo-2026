import math

def gen(a1, N):
    seq = [a1]
    for _ in range(N-1):
        an = seq[-1]
        # gather previous seq for gcd checks
        m = an+1
        while True:
            # quick check: need gcd(m, an) >1 first (since must hit last)
            # but also all
            # To speed, maybe check in order, fail fast
            ok=True
            # For efficiency, check gcd with each earlier
            # But note gcd(m, an) must >1, else immediately fail; since consecutive numbers coprime, but still
            for prev in seq:
                if math.gcd(m, prev)==1:
                    ok=False
                    break
            if ok:
                seq.append(m)
                break
            m+=1
    return seq

def detect(seq):
    # try to find eventual period for tail
    n = len(seq)
    for T in range(1, 30):
        # check tail 100 elements if additive repeated
        Ls = set()
        for i in range(n-200, n - T):
            Ls.add(seq[i+T]-seq[i])
        if len(Ls)==1:
            L = next(iter(Ls))
            # check if for all n >= some N0, pattern holds
            # count N0
            N0=None
            for start in range(0, n-T):
                ok=True
                for i in range(start, n-T):
                    if seq[i+T]-seq[i]!=L:
                        ok=False
                        break
                if ok:
                    N0=start
                    break
            if N0 is not None:
                return T, L, N0
    return None

for a1 in [15, 6, 10, 30, 3*7, 3*5*7, 2*3*5*7,  12, 14, 21, 35, 77, 105]:
    seq = gen(a1, 500)
    res = detect(seq)
    print(f"a1={a1} tail {seq[-10:]} detect {res}")
    # print first 30
    print(seq[:30])

print("---- more extensive for 15")
seq=gen(15, 2000)
res=detect(seq)
print(res)
# print diffs pattern
diffs = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
print(diffs[0:100])
# find where periodicity of multiples starts
# attempt to identify set of hitting family minimal
# Let's try to compute prime factors for first many terms to see minimal sets
from collections import Counter
def prime_factors(n):
    res=[]
    d=2
    while d*d<=n:
        if n%d==0:
            res.append(d)
            while n%d==0:
                n//=d
        d+=1 if d==2 else 2
    if n>1:
        res.append(n)
    return set(res)

pf = [prime_factors(x) for x in seq]
# compute minimal sets among first 100
def minimal_family(sets):
    # return inclusion minimal
    mins=[]
    for i,s in enumerate(sets):
        is_min=True
        for j,t in enumerate(sets):
            if i!=j and t.issubset(s) and t!=s:
                is_min=False
                break
        if is_min:
            mins.append(s)
    # deduplicate
    uniq=[]
    seen=set()
    for s in mins:
        fs=frozenset(s)
        if fs not in seen:
            seen.add(fs)
            uniq.append(s)
    return uniq

m = minimal_family(pf[:100])
print("minimal family size", len(m), "sets", m[:20])
# compute hitting sets for this family brute force
primes = set().union(*m)
primes = list(primes)
# brute force minimal hitting sets up to size maybe 4
import itertools
def hits(H, family):
    for s in family:
        if H.isdisjoint(s):
            return False
    return True

H_sets=[]
# search by increasing size
for r in range(1,6):
    for comb in itertools.combinations(primes, r):
        H=set(comb)
        if hits(H, m):
            # check minimal
            minimal=True
            for sub in itertools.combinations(comb, r-1):
                if hits(set(sub), m):
                    minimal=False
                    break
            if minimal:
                H_sets.append(H)
print("minimal hitting sets", H_sets)
# compute products
prods = [math.prod(list(H)) for H in H_sets]
print(prods)
