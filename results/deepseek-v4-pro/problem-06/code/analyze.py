import math

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

def factor_set(x):
    s = set()
    d = 2
    while d*d <= x:
        if x % d == 0:
            s.add(d)
            while x % d == 0:
                x //= d
        d += 1 if d==2 else 2  # simple
    if x > 1:
        s.add(x)
    return s

# Let's analyze a1=15 in detail
a1 = 15
seq = gen(a1, 30)
print("Sequence:", seq)
print("Prime factors:")
for i, v in enumerate(seq):
    print(f"  a{i+1}={v}: factors {factor_set(v)}")
