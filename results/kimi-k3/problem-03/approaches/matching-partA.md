# Approach: Part A (lower bound) via the matching formula

**Idea.** LB splits the stick into super-increasing (geometric) pieces $a_i=2^{i-1}T_n$. To prove any refinement by $\le n$ cuts keeps $D\ge T_n$, lower-bound $D$ via the matching formula $D=\min_\mu\operatorname{cost}(\mu)$: it suffices that *every* matching of the fragments costs $\ge\delta$.

**Status: complete, proved (Theorem 3.1 in `current.md`, lemma file `lemmas/tree-inequality.md`).**

**Key steps.**
1. Matching formula (level-set argument, see `lemmas/alternating-sum-representations.md`).
2. Loop-augmented multigraph: cross-pairs → edges, self-pairs → loops. Counting $2e+u=m+c\le2m-1$ forces a tree component $C$.
3. Tree inequality: 2-colouring signs give $\big|\sum_{i\in C}\epsilon_i a_i\big|\le\operatorname{cost}(C)$ (cross-pairs contribute exactly $|x-y|$ since adjacent pieces get opposite signs; self-pairs would break this — they are excluded because loops make a component cyclic).
4. Margin: $\big|\sum_{i\in C}\epsilon_i a_i\big|\ge a_k-\sum_{i<k,\,i\in C}a_i\ge\delta$.

**Pitfall found and fixed.** An earlier sketch applied the tree inequality to *any* acyclic component and ignored self-pairs; counterexample $\{1,100\}$, cut $100\to50+50$, matching $\{\{50,50\}\}$: isolated vertex $\{2\}$ has cost $0$. Fixed by counting self-pairs as loops (making such vertices cyclic), so the counting argument supplies a *different* tree component ($\{1\}$, cost $1\ge\delta$).

**Verification.** 1500 random trials (exact rationals), plus adversarial minimization reaching exactly $\delta$ on geometric families.
