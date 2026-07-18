# Lemma (Theorem 3.1): subdivisions of a super-increasing family keep $D\ge\delta$

**Statement.** Let $a_1\le\dots\le a_m$ be super-increasing with margin $\delta>0$ ($a_1\ge\delta$ and $a_i\ge\delta+\sum_{j<i}a_j$ for $i\ge2$), and let $M$ be obtained from these $m$ pieces by at most $m-1$ cuts (each cut splits one current piece into two positive pieces). Then $D(M)\ge\delta$.

**Proof.** By the matching formula (`alternating-sum-representations.md` (b)) it suffices to show every matching $\mu$ of $M$ has $\operatorname{cost}(\mu)\ge\delta$. Fix $\mu$ and build a multigraph $G$ on $\{1,\dots,m\}$ (vertices = original pieces):
- cross-pair $\{x,y\}\in\mu$ (fragments of different pieces $i\ne j$) → edge $\{i,j\}$;
- self-pair $\{x,y\}\in\mu$ (two fragments of the same piece $i$) → **loop** at $i$;
- unmatched fragments → nothing.

Let $e$ = #edges (loops included), $u$ = #unmatched fragments, $c\le m-1$ = #cuts. Counting fragments:
$$2e+u=m+c\le 2m-1\quad\Longrightarrow\quad e\le m-1.$$
If every connected component $C$ of $G$ satisfied $e_C\ge v_C$, summing over components would give $e\ge m$ (as $\sum v_C=m$) — contradiction. So some component $C$ has $e_C\le v_C-1$; connected, hence a **tree**; in particular loopless, so **no self-pair occurs inside $C$**: all pairs of $\mu$ within $C$ are cross-pairs, exactly the $v_C-1$ tree edges.

**Tree inequality.** 2-colour the tree: signs $\epsilon_i\in\{\pm1\}$ with $\epsilon_i=-\epsilon_j$ on every edge. Then
$$\Big|\sum_{i\in C}\epsilon_i a_i\Big|\le\operatorname{cost}(C).$$
Indeed, expand each $a_i$ as the sum of its fragments and group by $\mu$: a cross-pair $\{x,y\}$ ($x$ from $i$, $y$ from $j$) contributes $\epsilon_i x+\epsilon_j y=\epsilon_i(x-y)$, absolute value $|x-y|$; an unmatched fragment $z$ of piece $i$ contributes $\epsilon_i z$, absolute value $z$. Triangle inequality gives the claim.

**Margin.** With $k$ the largest index in $C$,
$$\Big|\sum_{i\in C}\epsilon_i a_i\Big|\ge a_k-\sum_{i\in C\setminus\{k\}}a_i\ge\delta,$$
since $C\setminus\{k\}\subseteq\{1,\dots,k-1\}$: for $k\ge2$, $a_k\ge\delta+\sum_{j<k}a_j\ge\delta+\sum_{i\in C\setminus\{k\}}a_i$; for $k=1$, $C=\{1\}$ and $a_1\ge\delta$.

Hence $\operatorname{cost}(\mu)\ge\operatorname{cost}(C)\ge\delta$, and $D(M)\ge\delta$ follows. $\blacksquare$

**Remarks.** (i) Loops are essential: a self-pair with cost $0$ inside an isolated vertex would otherwise fake a "tree component" of cost $0$ (e.g. pieces $\{1,100\}$, one cut $100\to50+50$, matching $\{\{50,50\}\}$: component $\{2\}$ has cost $0<a_2$, but it carries a loop and is cyclic; the counting then forces the tree component $\{1\}$ with cost $1\ge a_1$). (ii) The bound is sharp: the geometric family $a_i=2^{i-1}\delta$ admits a subdivision with $D=\delta$ (XY's chain strategy from `chain-theorem.md`).

**Verification.** `code/tests2.py::test_part_A` — 1500 random super-increasing families with random subdivisions ($\le m-1$ cuts), exact rational check $D\ge\delta$; plus adversarial local search (`code/partA.py`) finding minimum exactly $\delta$ on geometric families.
