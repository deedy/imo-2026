import math

def gen(a1, max_terms=2000):
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

def find_T_L(seq, max_T=400):
    n = len(seq)
    for T in range(1, max_T+1):
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

def prime_factors(x):
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

def rad(x):
    p = 1
    for q in prime_factors(x):
        p *= q
    return p

for a1 in range(2, 101):
    seq = gen(a1, 3000)
    res = find_T_L(seq, 500)
    if res:
        T, L = res
        # compute set of primes appearing in first T terms? 
        # Actually first few terms radicals
        radicals = [rad(x) for x in seq[:T]]
        print(f"a1={a1:3d}: T={T:3d}, L={L:4d}, L/a1={L/a1:.3f}, rads first few: {set(radicals[:min(6,T)])}")
    else:
        print(f"a1={a1:3d}: NOT FOUND within 400")
