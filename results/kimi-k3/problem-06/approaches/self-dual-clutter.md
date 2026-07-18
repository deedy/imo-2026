# Approach: permanents as a self-dual intersecting clutter (final, successful)

**Status: successful — yields complete proof.**

## Idea

The previous session reduced the problem to showing that $S_\infty$ has finitely many minimal elements ("permanents"), i.e. that shrinkage of the minimal-transversal family $H_n$ stops. The clean bypass found this session:

1. The sequence is exactly the increasing enumeration of $S_\infty\cap[a_1,\infty)$ (easy; uses pairwise non-coprimality, which is immediate from the definition).
2. If $S_\infty$ has finitely many minimal elements $h_1,\dots,h_k$, then $S_\infty$ is the union of the multiples of the $h_i$; membership is periodic mod $L=\mathrm{lcm}(h_i)$, and the enumeration satisfies $a_{n+T}=a_n+L$ with $T=\#(S_\infty\cap[a_1,a_1+L))$.
3. The minimal elements are squarefree; as sets of primes they form the family $\mathcal C$ of minimal transversals of $\{\mathrm{supp}(a_i)\}$. Two short arguments show:
   - $\mathcal C$ is **intersecting**: for $t\in\mathcal C$, large pure powers $\pi(t)^k$ are terms (multiples of $\pi(t)$ lie in $S_\infty$); their support is exactly $t$, so every other member meets $t$.
   - $\mathcal C$ is **self-dual**: a minimal transversal $T$ of $\mathcal C$ meets every $\mathrm{supp}(a_i)$ (each contains a member), so $\pi(T)\in S_\infty$ contains a member $t'\subseteq T$, which is itself a transversal (by intersecting), forcing $T=t'$.
4. **Combinatorial core theorem** (see `lemmas/self-dual-intersecting-clutter.md`): every antichain of finite sets that is intersecting and self-dual is finite. Proof by an explicit infinite-descent process: fixing $t\in\mathcal C$ and an infinite $\mathcal C_I$, either some finite $I\cup Z_s$ is a transversal (its minimal sub-transversal is a member contained in all of the infinitely many members of $\mathcal F_s$, violating the antichain property), or one builds $Z_\omega=\{z_1,z_2,\dots\}$ which is a transversal (by a least-index enumeration argument), and again a minimal sub-transversal is a finite member contained in $I\cup Z_s$ for some finite $s$, hence properly contained in members of $\mathcal F_{s+1}$ — contradiction.

## Why this supersedes the old crux

The old approach tried to prove "shrinkage stops" via potentials (min disjoint-pair product nondecreasing, etc.). That is unnecessary: the self-duality + intersecting + antichain structure alone already forces finiteness, by pure combinatorics. The number-theoretic input is confined to Steps 1–3 (all short).

## Verification

- `code/verify_newproof.py`: for ~85 values of $a_1$ (including primorials 2310, products like 1925 with 6 permanents), verified: enumeration property; permanents form an antichain, pairwise intersecting, self-dual (blocker of permanents = permanents); and $a_{n+T}=a_n+L$ with predicted $(T,L)$. All pass.
- `code/bruteforce_check.py`: independent raw-definition simulation confirms the same for small cases.
- Blocker identity $b(b(\mathcal C))=\mathcal C$ confirmed on 300 random clutters; self-dual intersecting antichains enumerated on 4 points (12: four singletons, triangles, etc.).
