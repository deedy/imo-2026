# imo-2026-04 — tracking file
## Status
unsolved

## Problem
Shan-Yu and Mulan are playing a game. Let $\theta$ be an angle with $0^\circ<\theta<180^\circ$ known to both players. Initially, Shan-Yu makes a paper triangle $\mathcal{T}$ with measurements of his choice. Then, they repeatedly perform the following steps: If $\mathcal{T}$ has at least one angle measuring exactly $\theta$, then the game stops and Mulan wins. Otherwise, Mulan chooses a point $P$ on the perimeter of $\mathcal{T}$, different from its three vertices. She then makes a straight cut from $P$ to the opposite vertex of $\mathcal{T}$, splitting it into two triangles. Shan-Yu discards one of the two triangles. The remaining triangle becomes the new $\mathcal{T}$. For which real values of $\theta$ can Mulan guarantee her victory in finitely many steps, no matter how Shan-Yu plays?

## Approaches tried
- Began an angle-state formulation: normalize $180^\circ$ to $1$ and represent a triangle by $(a,b,c)$ with $a+b+c=1$. A cut splitting $a$ into $x$ and $a-x$ gives children $(x,b,1-b-x)$ and $(a-x,c,b+x)$.
- Observed two basic forcing moves: bisecting an angle $2\theta$ puts $\theta$ in both children; for $\theta=90^\circ$, a suitable cut puts a right angle in both children, so $90^\circ$ is winning.
- Exploring finite rational-grid game models and possible invariants/recursive characterizations.

## Current best
A complete characterization is not yet established. It is already proved at the exploratory level that $\theta=90^\circ$ is winning, and any occurrence of an angle $2\theta<180^\circ$ lets Mulan win on the next cut by bisecting that angle.

## Full proof
Not yet complete.
