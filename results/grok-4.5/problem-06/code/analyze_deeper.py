#!/usr/bin/env python3
"""Deeper analysis of sequences, especially prime factors."""
import math
from collections import defaultdict

def generate_sequence(a1, N=200):
    seq = [a1]
    while len(seq) < N:
        candidate = seq[-1] + 1
        while True:
            if all(math.gcd(candidate, a) > 1 for a in seq):
                seq.append(candidate)
                break
            candidate += 1
    return seq

def prime_factors(n):
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return factors

def analyze_detailed(a1, N=100):
    seq = generate_sequence(a1, N)
    print(f"\n=== a1 = {a1} ===")
    print(f"First 40: {seq[:40]}")
    
    # Find period
    for T in range(1, min(50, len(seq)//3)):
        Ls = [seq[n+T] - seq[n] for n in range(len(seq)-T)]
        if len(set(Ls)) == 1:
            print(f"Period T={T}, L={Ls[0]}")
            # Show one period of residues mod L
            print(f"Residues mod L: {[x % Ls[0] for x in seq[:T]]}")
            break
    
    # Which primes appear?
    all_primes = set()
    prime_first_appearance = {}
    for i, a in enumerate(seq):
        pfs = prime_factors(a)
        for p in pfs:
            if p not in all_primes:
                all_primes.add(p)
                prime_first_appearance[p] = (i, a)
    
    print(f"Primes used (first appearance): sorted by first")
    for p in sorted(prime_first_appearance.keys(), key=lambda p: prime_first_appearance[p][0]):
        print(f"  p={p} first at a_{prime_first_appearance[p][0]+1}={prime_first_appearance[p][1]}")
    
    # For each term, which primes divide it
    print("Factorizations of first 30:")
    for i, a in enumerate(seq[:30]):
        print(f"  a_{i+1}={a} = {prime_factors(a)}")
    
    return seq

if __name__ == "__main__":
    for a1 in [15, 21, 33, 35, 105, 14, 22, 26, 34, 38, 45, 75, 7, 5, 25, 27, 49, 11]:
        analyze_detailed(a1, 150)
