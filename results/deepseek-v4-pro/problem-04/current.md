# imo-2026-04 — tracking file

## Status
partial

## Problem
Shan-Yu and Mulan are playing a game. Let $\theta$ be an angle with $0^\circ<\theta<180^\circ$ known to both players. Initially, Shan-Yu makes a paper triangle $\mathcal{T}$ with measurements of his choice. Then, they repeatedly perform the following steps: If $\mathcal{T}$ has at least one angle measuring exactly $\theta$, then the game stops and Mulan wins. Otherwise, Mulan chooses a point $P$ on the perimeter of $\mathcal{T}$, different from its three vertices. She then makes a straight cut from $P$ to the opposite vertex of $\mathcal{T}$, splitting it into two triangles. Shan-Yu discards one of the two triangles. The remaining triangle becomes the new $\mathcal{T}$. For which real values of $\theta$ can Mulan guarantee her victory in finitely many steps, no matter how Shan-Yu plays?

## Approaches tried
- Initial analysis of one-move win conditions. Realized Mulan needs both resulting triangles to be winning.
- Quick discretized search for some θ values (depth 3-4, limited split points). Results:
  - 45°, 60°, 90° appear winning (no counterexample found).
  - 30° mostly winning but (91,44,45) loses.
  - 36° appears winning.
  - 72°, 108°, 120°, 150° lose from many states.
- Formalized the operation algebraically: split angle a into p, q; triangle options are (p, b, c+q) and (q, c, b+p).
- One-move win analysis: Mulan can win in one move if she can split such that both resulting triangles contain θ.
  - This is possible when θ = 90° (if both other angles < 90°, split as 90 - b and 90 - c).
  - Also possible if some angle = kθ? But need both triangles to have θ.
- Search too slow to explore thoroughly. Need a theoretical characterization.

## Current best
We suspect the answer might be: Mulan can force a win if and only if θ is not a divisor of 180° in the sense that 180°/θ is not an integer? Or perhaps θ = 90° is the only winning? But search suggests 36°, 45°, 60° also winning. Let's compute more precisely.

The state space is continuous; discretization may miss moves. Need a mathematical invariant or strategy.

## Full proof
(Not yet complete)
