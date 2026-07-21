import math
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

def diffs(seq):
    return [seq[i+1]-seq[i] for i in range(len(seq)-1)]

for start in [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]:
    seq = gen(start, 60)
    d = diffs(seq)
    print(f"a1={start}: first 30 seq: {seq[:30]}")
    print(f"  diffs first 30: {d[:30]}")
    # Also check for eventual periodicity in diffs
    # Find if diffs become constant eventually
    # Let's print up to 100 if needed
EOF
