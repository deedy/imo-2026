# imo-2026-04 — tracking file

## Status
solved

## Problem
Shan-Yu and Mulan are playing a game. Let $\theta$ be an angle with $0^\circ<\theta<180^\circ$ known to both players. Initially, Shan-Yu makes a paper triangle $\mathcal{T}$ with measurements of his choice. Then, they repeatedly perform the following steps: If $\mathcal{T}$ has at least one angle measuring exactly $\theta$, then the game stops and Mulan wins. Otherwise, Mulan chooses a point $P$ on the perimeter of $\mathcal{T}$, different from its three vertices. She then makes a straight cut from $P$ to the opposite vertex of $\mathcal{T}$, splitting it into two triangles. Shan-Yu discards one of the two triangles. The remaining triangle becomes the new $\mathcal{T}$. For which real values of $\theta$ can Mulan guarantee her victory in finitely many steps, no matter how Shan-Yu plays?

## Approaches tried
- **Cut parametrization** (`lemmas/cut-parametrization.md`): a cut through the vertex with angle $A$, with $\alpha=\angle BAP\in(0,A)$, produces children with angle multisets $\{B,\alpha,180^\circ-B-\alpha\}$ and $\{C,A-\alpha,B+\alpha\}$. Verified numerically (`code/verify.py`, `geo_check`). This is the foundation of everything below.
- **Immediate-win analysis**: with generic angles, a single cut can put a multiple of $\theta$ into *both* children only if the split angle is a multiple of $\theta$, or if the two supplementary angles at $P$ are both multiples of $\theta$ — the latter forces $180^\circ\in\theta\mathbb N$. This suggested the dichotomy "$\theta$ divides $180^\circ$ or not".
- **Mulan's strategy for $\theta=180^\circ/n$** (`approaches/mulan-strategy-divisor-theta.md`): chain lemma (angle $k\theta$ ⇒ win in $\le k-1$ cuts) plus a double-threat cut through the largest angle making both angles at $P$ multiples of $\theta$. Complete; verified exactly for $n=2,\dots,8$ against random play.
- **Shan-Yu's invariant for $180^\circ/\theta\notin\mathbb Z$** (`approaches/shanyu-invariant.md`): keep all three angles outside $\theta\mathbb N$; a 4-case algebraic check shows this is always possible. Complete; verified exactly for several such $\theta$ with adversarial cut values.
- **Dead ends**: order-type invariants for Shan-Yu ("all angles $<\theta$", "all angles $>\theta$", "all in $(\theta,2\theta)$") — only the first works and only for $\theta>90^\circ$; all subsumed by the arithmetic invariant.

## Current best
**Answer: Mulan can guarantee victory exactly for the angles $\theta$ such that $180^\circ/\theta$ is an integer, i.e. $\theta = 180^\circ/n$ for some integer $n\ge 2$** (namely $\theta\in\{90^\circ,60^\circ,45^\circ,36^\circ,30^\circ,\dots\}$). If $n\theta=180^\circ$, Mulan wins within at most $n-1$ cuts via a "double threat + chain" strategy; if $180^\circ$ is not an integer multiple of $\theta$, Shan-Yu survives forever by keeping all three angles outside $\{\theta,2\theta,3\theta,\dots\}$, which a short case analysis shows is always possible. Full proof below; all key computations sanity-checked exactly in `code/verify.py`.

## Full proof

Throughout, we identify a triangle with the (unordered) triple of its angles, all measured in degrees; the triple consists of positive reals summing to $180^\circ$. Let
$$\theta\mathbb N:=\{k\theta:\ k=1,2,3,\dots\}$$
denote the set of positive integer multiples of $\theta$. Note that only the finitely many elements of $\theta\mathbb N\cap(0^\circ,180^\circ)$ can occur as angles of a triangle.

**Answer.** Mulan can guarantee victory in finitely many steps if and only if
$$\theta=\frac{180^\circ}{n}\quad\text{for some integer } n\ge 2,$$
equivalently, iff $180^\circ\in\theta\mathbb N$. (Since $0^\circ<\theta<180^\circ$, the integer $n=180^\circ/\theta$ automatically satisfies $n\ge2$.)

### Lemma 0 (Cut parametrization)

*Let $\mathcal T$ be a triangle with angles $A,B,C$ at vertices also named $A,B,C$. Mulan's legal cuts through vertex $A$ (i.e. with $P$ in the interior of side $BC$) are parametrized bijectively by $\alpha:=\angle BAP\in(0^\circ,A)$, and the resulting two triangles have angle multisets*
$$T_1=\{B,\ \alpha,\ 180^\circ-B-\alpha\},\qquad T_2=\{C,\ A-\alpha,\ B+\alpha\}.$$

*Proof.* As $P$ traverses the open segment $BC$, the ray $AP$ sweeps the open angular sector at $A$ between the rays $AB$ and $AC$; the map $P\mapsto\alpha=\angle BAP$ is a continuous strictly monotone bijection from the interior of $BC$ onto $(0^\circ,A)$. Triangle $ABP$ has angle $B$ at $B$ and $\alpha$ at $A$, hence angle $180^\circ-B-\alpha$ at $P$. Triangle $APC$ has angle $C$ at $C$ and $A-\alpha$ at $A$, hence at $P$ the angle
$$180^\circ-C-(A-\alpha)=(180^\circ-A-B-C)+B+\alpha=B+\alpha. \qquad\blacksquare$$

Note for later use: the two angles at $P$, namely $180^\circ-B-\alpha$ (in $T_1$) and $B+\alpha$ (in $T_2$), are supplementary.

A **round** consists of: the stopping check, then (if the game did not stop) one cut by Mulan and one discard by Shan-Yu. "Mulan wins within $m$ cuts" means: whatever Shan-Yu does, the stopping check succeeds after at most $m$ cuts have been made.

### Part 1: If $n\theta=180^\circ$ for an integer $n\ge2$, Mulan wins (within at most $n-1$ cuts)

Here $\theta\mathbb N\cap(0^\circ,180^\circ)=\{k\theta:\ 1\le k\le n-1\}$.

**Lemma 1 (Chain lemma).** *For any $\theta\in(0^\circ,180^\circ)$: if at the start of a round the triangle has an angle equal to $k\theta$ for some integer $k\ge1$, then Mulan can win within at most $k-1$ further cuts.*

*Proof.* Induction on $k$.

Base $k=1$: the triangle has an angle exactly $\theta$, so the stopping check ends the game at once; Mulan has won with $0$ further cuts.

Step $k\ge2$: let $A=k\theta$ be such an angle (note $k\theta<180^\circ$), and let $B,C$ be the other two angles. Since $0^\circ<\theta<k\theta=A$, Lemma 0 allows Mulan to cut through vertex $A$ with $\alpha=\theta$. The children are
$$T_1=\{B,\ \theta,\ 180^\circ-B-\theta\},\qquad T_2=\{C,\ (k-1)\theta,\ B+\theta\}.$$
If Shan-Yu keeps $T_1$, then the next round starts with a triangle having an angle exactly $\theta$, and the game stops with Mulan's victory: $1\le k-1$ cut was used. If Shan-Yu keeps $T_2$, it has the angle $(k-1)\theta$, so by the induction hypothesis Mulan wins within $k-2$ further cuts, for a total of at most $k-1$. $\blacksquare$

**Lemma 2 (Double threat).** *Assume $n\theta=180^\circ$, $n\ge 2$. If at the start of a round the triangle has no angle in $\theta\mathbb N$, then Mulan has a cut such that **both** children contain an angle of the form $k\theta$ with $1\le k\le n-1$.*

*Proof.* Let $A$ be a largest angle of the triangle and $B,C$ the other two, so $A\ge 60^\circ$. We claim there is an integer $k\ge 1$ with
$$C<k\theta<180^\circ-B. \tag{$*$}$$
The interval $(C,180^\circ-B)$ is open with length $180^\circ-B-C=A$.

*Case $n\ge3$:* then $\theta\le60^\circ\le A$, and $A\notin\theta\mathbb N$ (hypothesis) gives $A\ne\theta$, hence $A>\theta$. Let $k$ be the least positive integer with $k\theta>C$ (it exists since $\theta>0$). Since $C\notin\theta\mathbb N$ and $(k-1)\theta\le C$, we get $k\theta\le C+\theta<C+A=180^\circ-B$. Thus $(*)$ holds.

*Case $n=2$ (so $\theta=90^\circ$):* we show $B,C<90^\circ$, whence $(*)$ holds with $k=1$: indeed $C<90^\circ$ and $180^\circ-B>90^\circ$. To see $B,C<90^\circ$: if $A<90^\circ$ then all three angles are $<90^\circ$; $A=90^\circ$ is impossible because no angle lies in $\theta\mathbb N\ni 90^\circ$; and if $A>90^\circ$ then $B+C=180^\circ-A<90^\circ$, so $B,C<90^\circ$.

Fix such $k$, and note $k\theta<180^\circ-B<180^\circ=n\theta$ forces $1\le k\le n-1$. Mulan cuts through vertex $A$ with
$$\alpha:=180^\circ-B-k\theta.$$
By $(*)$, $0<\alpha<180^\circ-B-C=A$, so the cut is legal by Lemma 0. The children are
$$T_1=\{B,\ \alpha,\ 180^\circ-B-\alpha\}=\{B,\ 180^\circ-B-k\theta,\ k\theta\},$$
$$T_2=\{C,\ A-\alpha,\ B+\alpha\}=\{C,\ k\theta-C,\ 180^\circ-k\theta\}=\{C,\ k\theta-C,\ (n-k)\theta\},$$
where we used $A-\alpha=A-180^\circ+B+k\theta=k\theta-C$ and $180^\circ-k\theta=(n-k)\theta$ with $1\le n-k\le n-1$. Thus $T_1$ contains $k\theta$ and $T_2$ contains $(n-k)\theta$, both in $\{\theta,\dots,(n-1)\theta\}$. $\blacksquare$

**Mulan's complete strategy for $\theta=180^\circ/n$.** At the start of the game (round 1), either the triangle already has an angle $k\theta$ for some $1\le k\le n-1$ — then by Lemma 1 Mulan wins within $k-1\le n-2$ cuts — or it has no angle in $\theta\mathbb N$. In the latter case Mulan plays the cut of Lemma 2; whichever child Shan-Yu keeps, the next round starts with a triangle containing an angle $k'\theta$ with $1\le k'\le n-1$, and by Lemma 1 Mulan wins within $k'-1\le n-2$ further cuts. In total Mulan wins within at most $n-1$ cuts, no matter how Shan-Yu chooses the initial triangle and his discards. This proves Part 1.

### Part 2: If $180^\circ\notin\theta\mathbb N$, Shan-Yu can avoid defeat forever

Call a triangle **safe** if none of its three angles belongs to $\theta\mathbb N$. Since $\theta\in\theta\mathbb N$, a safe triangle never triggers the stopping check.

**Lemma 3 (Existence of a safe start).** *A safe triangle exists.*

*Proof.* The set $F:=\theta\mathbb N\cap(0^\circ,180^\circ)$ is finite. Pick any $A\in(0^\circ,180^\circ)\setminus F$ (possible: $F$ is finite, the interval is infinite). Now pick $B\in(0^\circ,180^\circ-A)$ with $B\notin F$ and $180^\circ-A-B\notin F$: this excludes only finitely many values of $B$ from an interval of positive length, so such $B$ exists. Set $C=180^\circ-A-B>0$. Then $(A,B,C)$ is safe. $\blacksquare$

**Lemma 4 (Closure).** *Assume $180^\circ\notin\theta\mathbb N$. If the current triangle is safe, then for every legal cut of Mulan, at least one of the two children is safe.*

*Proof.* Suppose Mulan cuts through the vertex whose angle is $A$; let $B,C$ be the other two angles and $\alpha\in(0^\circ,A)$ the cut parameter. By Lemma 0 the children are
$$T_1=\{B,\ \alpha,\ 180^\circ-B-\alpha\},\qquad T_2=\{C,\ A-\alpha,\ B+\alpha\}.$$
By safety, $B\notin\theta\mathbb N$ and $C\notin\theta\mathbb N$. Hence:
- if $T_1$ is unsafe, then $\alpha\in\theta\mathbb N$ or $180^\circ-B-\alpha\in\theta\mathbb N$;
- if $T_2$ is unsafe, then $A-\alpha\in\theta\mathbb N$ or $B+\alpha\in\theta\mathbb N$.

Assume for contradiction both children are unsafe. There are four cases, with $k,m\ge1$ integers:

1. $\alpha=k\theta$ and $A-\alpha=m\theta$. Then $A=(k+m)\theta\in\theta\mathbb N$, contradicting safety of the current triangle.
2. $\alpha=k\theta$ and $B+\alpha=m\theta$. Then $B=(m-k)\theta$; since $B>0$, $m-k\ge1$, so $B\in\theta\mathbb N$ — contradiction.
3. $180^\circ-B-\alpha=k\theta$ and $A-\alpha=m\theta$. Subtracting: $180^\circ-A-B=(k-m)\theta$, i.e. $C=(k-m)\theta$; since $C>0$, $k-m\ge1$, so $C\in\theta\mathbb N$ — contradiction.
4. $180^\circ-B-\alpha=k\theta$ and $B+\alpha=m\theta$. Adding: $180^\circ=(k+m)\theta\in\theta\mathbb N$ — contradicting the hypothesis of Part 2.

All cases are impossible, so at least one child is safe. $\blacksquare$

**Shan-Yu's complete strategy for $180^\circ\notin\theta\mathbb N$.** He creates a safe initial triangle (Lemma 3). Whenever Mulan cuts, he keeps a safe child, which exists by Lemma 4. By induction, at the start of every round the triangle is safe, hence has no angle equal to $\theta$, hence the stopping check never succeeds. Therefore no strategy of Mulan wins in finitely many steps: against Shan-Yu's strategy the game runs forever. This proves Part 2.

### Conclusion

Combining Parts 1 and 2: Mulan can guarantee victory in finitely many steps **iff** $180^\circ$ is an integer multiple of $\theta$, i.e.
$$\boxed{\ \theta=\frac{180^\circ}{n}\ \text{for some integer } n\ge2\ }$$
(equivalently $\theta\in\{90^\circ,60^\circ,45^\circ,36^\circ,30^\circ,180^\circ/7,\dots\}$), and when she can, she needs at most $n-1$ cuts. $\blacksquare$
