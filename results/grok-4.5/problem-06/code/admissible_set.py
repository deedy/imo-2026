#!/usr/bin/env python3
"""Understand the admissible residue classes as the sequence builds for a1=15."""
import math
from functools import reduce

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

def is_admissible(m, seq):
    return all(math.gcd(m, a) > 1 for a in seq)

def generate_and_track(a1, N=40):
    seq = [a1]
    print(f"Start with a1={a1}, primes={prime_factors(a1)}")
    
    # Track radical
    all_p = prime_factors(a1)
    
    for step in range(N-1):
        cand = seq[-1] + 1
        while not is_admissible(cand, seq):
            cand += 1
        new_p = prime_factors(cand) - all_p
        seq.append(cand)
        if new_p:
            print(f"a_{len(seq)}={cand} introduces new primes {new_p}, all_primes now {sorted(all_p|new_p)}")
            all_p |= new_p
        # else:
        #     print(f"a_{len(seq)}={cand} primes={prime_factors(cand)}")
    
    # Now check: is the set of all numbers that share factor with ALL of first k terms
    # equal to the arithmetic progressions of the sequence?
    
    print("\n--- Checking stabilization of admissible set ---")
    L = 30  # suspected
    R = [15,18,20,24,0,6,10,12]
    
    # After having first 8 terms, what's the admissible set mod something
    first8 = seq[:8]
    print(f"First 8: {first8}")
    
    # Check for numbers up to say 300, which are >42 and admissible w.r.t first 8
    # vs which are in the +30 progression from first 8
    print("\nNumbers >42 that are admissible w.r.t first 8 terms:")
    adm = []
    for m in range(43, 300):
        if is_admissible(m, first8):
            adm.append(m)
    print(adm[:50], "...")
    
    # Are all of these in the eventual sequence?
    # The eventual sequence from a9 onwards
    print("\nActual sequence from a9:", seq[8:40])
    
    # Check if admissible w.r.t all previous is automatically true for the AP
    print("\nIs every number ≡ r mod 30 for r in R admissible w.r.t. entire first 8?")
    for r in R:
        # take some large ones
        ok = all(is_admissible(r + 30*k, first8) for k in range(1, 20) if r+30*k > 42)
        print(f"  r={r}: {ok}")
    
    # Now what about after more terms that introduce new primes
    print("\n--- After introducing 7 (at a8=42) ---")
    # a8=42 already in first 8
    # a14=66 introduces 11
    print(f"seq[13]={seq[13]}")
    first14 = seq[:14]
    print("Is every large enough number in the APs still admissible after first 14?")
    for r in sorted(set(x%30 for x in seq)):
        ok = all(is_admissible(r + 30*k, first14) for k in range(3, 20))
        bad = [r+30*k for k in range(3,20) if not is_admissible(r+30*k, first14)]
        print(f"  r={r}: {ok}, bad examples {bad[:3]}")

if __name__ == "__main__":
    generate_and_track(15, 50)
