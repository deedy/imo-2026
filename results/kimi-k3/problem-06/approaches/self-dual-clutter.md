# Approach: permanents as an intersecting antichain + compactness (final, successful)

**Status: successful — yields a complete proof (after one repair found in review).**

## Idea

1. The sequence is exactly the increasing enumeration of $S_\infty\cap[a_1,\infty)$ (easy; uses pairwise non-coprimality, immediate from the definition).
2. If $S_\infty$ has finitely many minimal elements $h_1,\dots,h_k$ ("permanents"), then $S_\infty$ is the union of their multiples; membership is periodic mod $L=\mathrm{lcm}(h_i)$, and the enumeration satisfies $a_{n+T}=a_n+L$ with $T=\#(S_\infty\cap[a_1,a_1+L))$.
3. The permanents are squarefree; as sets of primes they form the family $\mathcal C$ of minimal transversals of $\{\mathrm{supp}(a_i)\}$. Three short arguments show:
   - $\mathcal C$ is **intersecting**: for $t\in\mathcal C$, large pure powers $\pi(t)^k$ are terms (multiples of $\pi(t)$ lie in $S_\infty$); their support is exactly $t$, so every other member meets $t$.
   - $\mathcal C$ is **self-dual for finite transversals**: a finite minimal transversal $U$ of $\mathcal C$ meets every $\mathrm{supp}(a_i)$ (each contains a member), so $\pi(U)\in S_\infty$ contains a member $t'\subseteq U$, itself a transversal (by intersecting), forcing $U=t'$.
   - **killing property (K′)**: a finite prime-set $F$ with $\pi(F)>a_1$ containing no member is avoided by some member $t'$ with $\pi(t')<\pi(F)$. Proof: $\pi(F)\notin S_\infty$ (else it has a permanent divisor inside $F$); the greedy rule kills it by a term $a_i<\pi(F)$ coprime to it; any permanent dividing $a_i$ works.
4. **Compactness Theorem** (`lemmas/compactness.md`): $\mathcal C$ has no infinite minimal transversal. From an infinite minimal transversal $T$ (explicitly constructed, private members $e_w$), (K′) gives through each $w\in T$ a member $t^*_w\ni w$ with $\pi(t^*_w)\le a_1w$ (descent: $\pi$ drops by factor $\ge2$ per K′-application). Pigeonhole on the finitely many prime-sets of product $\le a_1$: $t^*_{w_j}=P_0\cup\{w_j\}$ for infinitely many distinct $w_j$. Every member meets $P_0$ (else it contains all $w_j$), so $P_0$ is a finite transversal; a minimal $U\subseteq P_0$ is a member (finite self-duality) strictly inside $t^*_{w_1}$ — contradicting the antichain property.
5. **Finiteness of $\mathcal C$** (`lemmas/self-dual-intersecting-clutter.md`): peeling. Fixing $t$ and an infinite $\mathcal C_I$, either some finite $I\cup Z_s$ is a transversal — its minimal sub-transversal is finite, hence a member (finite self-duality) contained in all of the infinitely many members of $\mathcal F_s$, violating antichain — or one builds $W=I\cup Z_\omega$, a transversal with NO finite sub-transversal, contradicting the Compactness Theorem.

## The gap that was found and repaired

An earlier version stated step 3's self-duality for ALL minimal transversals and applied it (via Zorn) to a minimal transversal $T\subseteq I\cup Z_\omega$. Two defects: (i) the proof of self-duality forms $\pi(U)$, requiring $U$ finite; (ii) in the relevant case $T$ is PROVABLY infinite (any finite transversal inside $I\cup Z_\omega$ lies in some $I\cup Z_s$ and would have terminated the peeling at stage $s+1$). Repair: the Compactness Theorem (step 4), proved from the killing property — the genuine number-theoretic content that pure set-system axioms lack (the star family $\{\{0,i\}\}$ satisfies antichain + intersecting but has the infinite minimal transversal $\{1,2,\dots\}$; only self-duality/(K′) rule this out).

## Verification

- `code/verify_newproof.py`: for ~85 values of $a_1$ (incl. 2310, 1925), verified: enumeration property; permanents form an antichain, pairwise intersecting, self-dual; and $a_{n+T}=a_n+L$ with predicted $(T,L)$. All pass.
- `code/bruteforce_check.py`: independent raw-definition simulation confirms the same for small cases.
- `code/check_Kprime.py`: (K) verified for all $x\le40000$ and (K′) for ~1500 prime-sets per case, for 58 values of $a_1$ including multi-permanent cases. All pass.
