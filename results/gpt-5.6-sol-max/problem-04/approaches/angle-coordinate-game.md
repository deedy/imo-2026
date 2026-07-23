# Angle-coordinate game

## Idea
Normalize the angle sum to $1$ (so the target is $t=\theta/180^\circ$). Describe cuts entirely in angle coordinates and study the resulting perfect-information reachability game.

## Exact transition formula
Let the current triangle have angles $(A,B,C)$, with $A+B+C=1$. Cut from the vertex of angle $A$ to a point $P$ on the opposite side, and let the portion of $A$ in the child containing the vertex of angle $B$ be $x$, where $0<x<A$. The two children have angle triples
\[
 (B,x,1-B-x),\qquad (C,A-x,B+x).
\]
Indeed, the two angles at $P$ are supplementary, and their values are $1-B-x$ and $B+x$.

Thus Mulan chooses a vertex and a real splitting parameter $x$; Shan-Yu chooses one of these two triples.

## Finite-grid experiments
For rational $t=p/q$, I restricted all angles and splitting parameters to multiples of $1/q$ and computed the attractor of states containing $p/q$. For $q\le20$, all grid states are winning exactly when $p\mid q$, i.e. $t=1/n$ after reduction. This strongly supports the conjectured answer.

Examples of grid-losing states for non-reciprocal targets:
- $t=2/5$: $(1/5,1/5,3/5)$;
- $t=2/7$: $(1/7,1/7,5/7)$ and $(1/7,3/7,3/7)$;
- $t=3/8$: $(1/8,2/8,5/8)$ and $(2/8,2/8,4/8)$.

These experiments are only heuristic because Mulan may make arbitrary real cuts even from a rational state.

## Status
Transition formula established. Computation supports $t=1/n$ and suggests useful adversarial initial triangles, but does not prove necessity.
