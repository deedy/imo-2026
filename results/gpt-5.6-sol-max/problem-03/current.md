# imo-2026-03 — tracking file
## Status
unsolved

## Problem
Let $n$ be a positive integer. Liu Bang and Xiang Yu have a stick of length $1$ and want to divide it between themselves. Liu Bang marks at most $n$ points on the stick, and then Xiang Yu marks at most $n$ points on the stick. The marked points are distinct. Then, the stick is cut at all marked points, creating a number of pieces. Afterwards, they take turns claiming any unclaimed piece of the stick, with Liu Bang going first. Each player's goal is to maximise the total length of their own pieces. For each $n$, determine the largest value $c$ such that Liu Bang may guarantee a total length of at least $c$, regardless of Xiang Yu's play.

## Approaches tried
- Reformulated the claiming phase: rational play consists of taking a currently longest piece, so Liu Bang's payoff is the sum of the odd-indexed lengths after sorting all pieces nonincreasingly.
- Began investigating the equivalent alternating-sum discrepancy of refinements of Liu Bang's initial partition.

## Current best
No final expression yet. If the final piece lengths are $x_1\ge\cdots\ge x_m$, Liu Bang receives $x_1+x_3+\cdots$, equivalently $(1+D)/2$ where $D=x_1-x_2+x_3-\cdots+(-1)^{m+1}x_m\ge0$.

## Full proof
Not yet complete.
