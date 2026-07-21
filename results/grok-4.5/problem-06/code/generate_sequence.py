#!/usr/bin/env python3
"""Generate the sequence starting from a given a1, up to N terms."""
import math
from functools import reduce

def gcd(a, b):
    return math.gcd(a, b)

def generate_sequence(a1, N=100):
    seq = [a1]
    while len(seq) < N:
        prev = seq[-1]
        candidate = prev + 1
        while True:
            # Check if gcd(candidate, a_i) > 1 for all i
            if all(gcd(candidate, a) > 1 for a in seq):
                seq.append(candidate)
                break
            candidate += 1
    return seq

def analyze(seq):
    print(f"Sequence: {seq}")
    diffs = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    print(f"Diffs: {diffs}")
    # Check for arithmetic period
    for T in range(1, len(seq)//3):
        L_candidates = set()
        consistent = True
        for n in range(len(seq)-T):
            L = seq[n+T] - seq[n]
            L_candidates.add(L)
            if len(L_candidates) > 1:
                consistent = False
                break
        if consistent and len(L_candidates) == 1:
            L = L_candidates.pop()
            print(f"Found T={T}, L={L}")
            return T, L
    return None, None

if __name__ == "__main__":
    for a1 in [2, 3, 4, 6, 8, 9, 10, 12, 15, 30]:
        print(f"\n=== a1 = {a1} ===")
        seq = generate_sequence(a1, 50)
        analyze(seq)
