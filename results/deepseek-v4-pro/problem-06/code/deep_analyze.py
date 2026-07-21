import math

def gen(a1, max_terms=3000):
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

def find_T_L(seq, max_T=500):
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

def find_period_in_diffs(d, start_range=500, period_range=200, check_len=200):
    n = len(d)
    for start in range(0, min(start_range, n - check_len)):
        for per in range(1, period_range):
            if start + per + check_len > n:
                continue
            ok = True
            for i in range(check_len):
                if d[start+i] != d[start+per+i]:
                    ok = False
                    break
            if ok:
                return start, per
    return None

# test a1=209 more carefully
a1 = 209
seq = gen(a1, 4000)
T, L = find_T_L(seq, 500)
print(f"a1={a1}: periodic with T={T}, L={L}" if T else "no T found")

# Let's also try to find period in diffs after some point
d = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
res = find_period_in_diffs(d, start_range=1000, period_range=300, check_len=300)
print(f"Period in diffs: {res}")
if res:
    start, per = res
    print(f"  sample: {d[start:start+per]}")
    print(f"  sum: {sum(d[start:start+per])}")
else:
    # just print some stats
    print(f"  diffs length: {len(d)}")
    # look at tail
    print(f"  last 50 diffs: {d[-50:]}")
