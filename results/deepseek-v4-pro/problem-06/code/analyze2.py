import math

def gen(a1, max_terms=500):
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

def diffs(seq):
    return [seq[i+1]-seq[i] for i in range(len(seq)-1)]

def find_period(diffs, max_period=100):
    # Try to find period in the difference sequence after some starting point
    n = len(diffs)
    for start in range(0, min(100, n)):
        for period in range(1, min(max_period, (n-start)//2)):
            ok = True
            for i in range(start, n - period):
                if diffs[i] != diffs[i+period]:
                    ok = False
                    break
            if ok and period > 0:
                return start, period
    return None

# Test many starting values
for a1 in range(2, 101):
    seq = gen(a1, 200)
    d = diffs(seq)
    per = find_period(d)
    if per:
        start, period = per
        print(f"a1={a1}: period {period} starting at index {start}, diffs sample: {d[start:start+period]}")
    else:
        print(f"a1={a1}: no period found, first 50 diffs: {d[:50]}")
