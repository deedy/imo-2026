#!/usr/bin/env python3
"""Verify the move on valuations and the gcd invariant, and simulate termination."""

from math import gcd
from functools import reduce
import random

def lcm(a,b):
    return a // gcd(a,b) * b

def move(m, n):
    g = gcd(m,n)
    return g, lcm(m,n)//g

def all_primes_factor_exponents(nums, primes):
    """Return dict p -> list of v_p for each num."""
    from collections import defaultdict
    res = {p: [] for p in primes}
    for x in nums:
        for p in primes:
            v = 0
            while x % p == 0:
                x //= p
                v += 1
            res[p].append(v)
    return res

def gcd_list(lst):
    return reduce(gcd, lst, 0)  # gcd(0,a)=a, gcd of empty weird but ok

def simulate(nums, max_steps=10000, verbose=False):
    """Run random moves until done; return final M and steps."""
    board = list(nums)
    steps = 0
    while True:
        gt1 = [i for i,x in enumerate(board) if x > 1]
        if len(gt1) <= 1:
            break
        if steps >= max_steps:
            raise RuntimeError("max steps")
        i,j = random.sample(gt1, 2)
        m,n = board[i], board[j]
        a,b = move(m,n)
        board[i], board[j] = a,b
        steps += 1
        if verbose:
            print(board)
    M = next((x for x in board if x > 1), 1)
    return M, steps, board

def predicted_M(nums):
    # get all primes appearing
    primes = set()
    for x in nums:
        t=x
        d=2
        while d*d<=t:
            if t%d==0:
                primes.add(d)
                while t%d==0: t//=d
            d+=1
        if t>1: primes.add(t)
    primes = sorted(primes)
    exps = all_primes_factor_exponents(nums, primes)
    M = 1
    for p in primes:
        g = gcd_list(exps[p])
        M *= p**g
    return M

# tests
random.seed(42)
test_cases = [
    [2,3],
    [2,4],
    [2,2,2],
    [4,6,9],
    [6,10,15],
    [4,8,12],
    [30,42,70,105],
    [2,3,5,7,11],
    [100,100,100],
    [2**10, 3**10, 5**10],
    [12,18,24,36],
]

print("=== Predicted vs simulated M ===")
for tc in test_cases:
    pred = predicted_M(tc)
    results = set()
    for trial in range(20):
        M, steps, _ = simulate(tc)
        results.add(M)
    print(f"nums={tc}")
    print(f"  pred={pred}, sim_results={results}, match={results=={pred}}")

# also check invariant preservation on one path
print("\n=== Invariant check on path ===")
nums = [12,18,24,36]
primes = [2,3]
board = list(nums)
print("start", board, "gcds", {p: gcd_list(all_primes_factor_exponents(board,[p])[p]) for p in primes})
for _ in range(10):
    gt1 = [i for i,x in enumerate(board) if x>1]
    if len(gt1)<2: break
    i,j = random.sample(gt1,2)
    a,b = move(board[i],board[j])
    board[i],board[j]=a,b
    gcds = {p: gcd_list(all_primes_factor_exponents(board,[p])[p]) for p in primes}
    print(board, "gcds", gcds)
