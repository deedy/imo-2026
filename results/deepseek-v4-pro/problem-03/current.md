# imo-2026-03 — tracking file

## Status
partial

## Problem
Let $n$ be a positive integer. Liu Bang and Xiang Yu have a stick of length $1$ and want to divide it between themselves. Liu Bang marks at most $n$ points on the stick, and then Xiang Yu marks at most $n$ points on the stick. The marked points are distinct. Then, the stick is cut at all marked points, creating a number of pieces. Afterwards, they take turns claiming any unclaimed piece of the stick, with Liu Bang going first. Each player's goal is to maximise the total length of their own pieces. For each $n$, determine the largest value $c$ such that Liu Bang may guarantee a total length of at least $c$, regardless of Xiang Yu's play.

## Approaches tried
- Brute-force discrete search for small n: n=1 gives 2/3; n=2 gives 3/5=0.6; n=3 appears around 4/7≈0.5714 but discrete search suggests possibly lower.
- Hypothesized formula: c = (n+1)/(2n+1). For n=1: 2/3 correct. For n=2: 3/5 correct. For n=3: 4/7 seems plausible but needs verification.
- Attempted to compute X's optimal response to L's marks via discretized search; results suggest L can guarantee at least (n+1)/(2n+1) by placing marks at 1/(2n+1), 2/(2n+1), ..., n/(2n+1).

## Current best
Conjecture: Liu Bang can guarantee c = (n+1)/(2n+1). The strategy is to mark points at 1/(2n+1), 2/(2n+1), ..., n/(2n+1). Xiang Yu's optimal response seems to be to also mark n points at the remaining positions n+1/(2n+1), ..., 2n/(2n+1), making all pieces equal to 1/(2n+1). Then Liu Bang gets n+1 pieces out of 2n+1, totaling (n+1)/(2n+1). Need to prove both that Liu Bang can guarantee at least this much (lower bound) and that Xiang Yu can prevent Liu Bang from getting more (upper bound).

We need a rigorous proof: 
- Upper bound: Xiang Yu can limit Liu Bang to at most (n+1)/(2n+1). Strategy for X?
- Lower bound: Liu Bang's strategy ensures at least (n+1)/(2n+1).

## Full proof
(To be completed)
