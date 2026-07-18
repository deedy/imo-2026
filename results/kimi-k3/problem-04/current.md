# imo-2026-04 — tracking file

## Status

solved

## Problem

Shan-Yu and Mulan are playing a game. Let $\theta$ be an angle with
$0^\circ<\theta<180^\circ$ known to both players. Initially, Shan-Yu makes a
paper triangle $\mathcal{T}$ with measurements of his choice. Then, they
repeatedly perform the following steps: If $\mathcal{T}$ has at least one angle
measuring exactly $\theta$, then the game stops and Mulan wins. Otherwise,
Mulan chooses a point $P$ on the perimeter of $\mathcal{T}$, different from its
three vertices. She then makes a straight cut from $P$ to the opposite vertex
of $\mathcal{T}$, splitting it into two triangles. Shan-Yu discards one of the
two triangles. The remaining triangle becomes the new $\mathcal{T}$. For which
real values of $\theta$ can Mulan guarantee her victory in finitely many steps,
no matter how Shan-Yu plays?

## Approaches tried

- **Algebraic model of the cut.** A cut is a cevian: from a triangle with
  angles $(A,B,C)$, cutting at the vertex with angle $A$ with parameter
  $\alpha\in(0,A)$ (fully at Mulan's disposal) produces halves
  $\{B,\alpha,180^\circ-B-\alpha\}$ and $\{C,A-\alpha,B+\alpha\}$
  (see `lemmas/cut-geometry.md`). This reduces the game to pure angle arithmetic.
- **Retrograde analysis on a discretized game** (`code/retro.py`,
  `approaches/retrograde-analysis.md`): computed Mulan's winning region exactly
  for integer-degree states. At unit $1^\circ$ she wins all states iff
  $\theta\in\{1,2,3,4,5,6,9,10,12,15,18,20,30,36,45,60,90\}^\circ$ — exactly
  the divisors of $180^\circ$; at unit $0.5^\circ$ exactly
  $\{\theta: 180^\circ/\theta\in\mathbb Z\}$ again. This gave the conjecture.
- **Halving lemma** (`lemmas/halving-lemma.md`): for every $\theta$, any
  triangle containing an angle $k\theta$ ($k\in\mathbb Z_{>0}$) is winning for
  Mulan (cut $\theta$ off $k\theta$, induct on $k$). So the whole question is
  whether Mulan can force a multiple of $\theta$ to survive a cut.
- **Mulan's side** (`approaches/marking-strategy.md`): if $\theta=180^\circ/n$,
  a one-move "round-up" cut makes *both* halves contain multiples of $\theta$
  (here $180^\circ=n\theta$ being a multiple of $\theta$ is essential), then
  the halving lemma finishes. Win in $\le n-1$ moves.
- **Shan-Yu's side** (`approaches/invariant-avoidance.md`): if $\theta$ is not
  of the form $180^\circ/m$, Shan-Yu maintains the invariant "no angle is a
  multiple of $\theta$" forever, starting from the equilateral triangle; the
  case analysis shows the invariant can only break when $180^\circ-k\theta$ is
  a multiple of $\theta$, i.e. exactly when $\theta=180^\circ/m$.
- Both strategies verified by exact rational-arithmetic simulation
  (`code/verify.py`): Mulan's strategy wins exhaustively with worst case
  exactly $n-1$ moves for all tested $n\le 60$; Shan-Yu's invariant survived
  $200\times 300$ random cuts for several $\theta\ne 180^\circ/m$.
- Dead ends: naive invariants for Shan-Yu such as "all angles $<\theta$"
  (works only for $\theta>90^\circ$) and "no angle equal to $\theta$" alone
  (not maintainable: Mulan can put $\theta$ in one half and nothing
  forbidden in the other); replaced by the multiple-of-$\theta$ invariant.

## Current best

**Answer: Mulan can guarantee victory in finitely many steps if and only if
$\displaystyle \theta=\frac{180^\circ}{n}$ for some integer $n\ge 2$
(equivalently, iff $180^\circ/\theta$ is an integer).** In that case she wins
within $n-1$ moves: with the triangle's angles measured relative to $\theta$,
she cuts so that one angle is rounded up to the next multiple of $\theta$;
because $180^\circ=n\theta$ the supplementary angle at the cut is then also a
multiple of $\theta$, so *both* halves contain a multiple of $\theta$; then she
repeatedly cuts $\theta$ off the surviving multiple ($k\theta\to(k-1)\theta$)
until an angle exactly $\theta$ appears in every branch. For all other
$\theta$, Shan-Yu starts with an equilateral triangle and always keeps a half
having no angle equal to an integer multiple of $\theta$ (one exists among the
two halves of any cut, precisely because $\theta\ne180^\circ/m$), so Mulan can
never win.

## Full proof

### Setup and angle bookkeeping

Throughout, describe a triangle by its multiset of angles $(A,B,C)$, positive
reals with $A+B+C=180^\circ$. The game only depends on the angles.

**Lemma 0 (the cut).** *Suppose the current triangle has angles $A$ at vertex
$X$, $B$ at $Y$, $C$ at $Z$. Mulan's point $P$ lies on some side; say it lies
on $YZ$ (the opposite vertex is then $X$). Put $\alpha=\angle YXP$. Then the
two halves have angle multisets*
$$H_1=\{B,\ \alpha,\ 180^\circ-B-\alpha\},\qquad
  H_2=\{C,\ A-\alpha,\ B+\alpha\},$$
*and every value $\alpha\in(0,A)$ is achieved by a suitable interior point $P$
of $YZ$.*

*Proof.* See `lemmas/cut-geometry.md`. (Angle chase with $A+B+C=180^\circ$;
the range of $\alpha$ by continuity of $P\mapsto\angle YXP$ and the
intermediate value theorem.) $\blacksquare$

So a move of Mulan consists of: choosing which angle of $(A,B,C)$ is the *cut
angle* $A$, choosing which of the remaining angles is $B$ (the one that ends up
in the same half as $\alpha$), and choosing a real number $\alpha\in(0,A)$.
Then Shan-Yu replaces the triangle by one of $H_1,H_2$.

Call an angle **marked** if it is an integer multiple of $\theta$, i.e. equal
to $k\theta$ for some integer $k\ge1$ (necessarily $k\theta<180^\circ$ since it
is an angle of a triangle).

### The halving lemma

**Lemma 1.** *Fix any $\theta$. If the current triangle has a marked angle
$k\theta$ ($k\ge1$ integer), then Mulan can force victory from it within $k-1$
moves.*

*Proof.* Induction on $k$. If $k=1$ the triangle has an angle $\theta$ and the
game is already over. If $k\ge2$, let the angles be $A=k\theta$, $B$, $C$;
Mulan cuts at $A$ with $\alpha=\theta\in(0,A)$. By Lemma 0 the halves are
$$H_1=\{B,\ \theta,\ 180^\circ-B-\theta\},\qquad
  H_2=\{C,\ (k-1)\theta,\ B+\theta\},$$
both genuine triangles since $B<180^\circ-2\theta$. If Shan-Yu keeps $H_1$, the
game stops next (angle $\theta$ present); if he keeps $H_2$, Mulan wins from it
within $k-2$ further moves by induction. Total $\le k-1$ moves. $\blacksquare$

### Theorem 1: $\theta=180^\circ/n$ — Mulan wins

**Theorem 1.** *Let $\theta=180^\circ/n$ for an integer $n\ge2$. Then Mulan has
a strategy that wins within $n-1$ moves from every initial triangle.*

*Proof.* If the initial triangle has a marked angle $k\theta$
($1\le k\le n-1$), Lemma 1 wins within $k-1\le n-2$ moves. So assume no angle
of $\mathcal T=(A,B,C)$ is marked.

For an unmarked angle $x$ define
$$d(x)=\bigl(\lfloor x/\theta\rfloor+1\bigr)\theta-x\in(0,\theta),$$
the distance from $x$ up to the nearest multiple of $\theta$ above it.

**Claim 1.** $d(A)+d(B)+d(C)\in\{\theta,\,2\theta\}$.

*Proof.* Each $x+d(x)$ is a multiple of $\theta$, and
$(A+d(A))+(B+d(B))+(C+d(C))=180^\circ+d(A)+d(B)+d(C)=n\theta+d(A)+d(B)+d(C)$,
so the sum of the $d$'s is a multiple of $\theta$; as each lies in
$(0,\theta)$, the sum lies in $(0,3\theta)$, hence equals $\theta$ or
$2\theta$. $\blacksquare$

**Claim 2.** *There exist two distinct angles $u,v$ of $\mathcal T$ with
$d(u)<v$.*

*Proof.* Suppose not. Then in particular $d(A)\ge B$, $d(B)\ge C$, $d(C)\ge A$,
and summing gives
$$d(A)+d(B)+d(C)\ge A+B+C=180^\circ=n\theta.$$
By Claim 1 the left side is at most $2\theta$, so $n\theta\le2\theta$, i.e.
$n=2$, and all three inequalities must be equalities: $d(A)=B$, $d(B)=C$,
$d(C)=A$. But then $A+d(A)=A+B$ is a multiple of $\theta$ by definition of
$d(A)$, while $A+B=180^\circ-C=2\theta-C$ (here $n=2$). Since $0<A+B<180^\circ$
we get $A+B=\theta$, hence $C=\theta$, contradicting that $C$ is unmarked.
$\blacksquare$

**Mulan's move.** Pick a pair $u\ne v$ with $d(u)<v$ (Claim 2) and let $w$ be
the third angle. Mulan cuts at the vertex with angle $v$, putting $u$ in the
role of $B$ and
$$\alpha=d(u)\in(0,v).$$
Let $u+d(u)=k\theta$ ($k\ge1$ integer, a multiple of $\theta$ just above $u$).
Since $k\theta=u+\alpha<u+v<180^\circ=n\theta$, we have $1\le k\le n-1$. By
Lemma 0 the halves are
$$H_1=\{u,\ d(u),\ 180^\circ-u-d(u)\},\qquad H_2=\{w,\ v-d(u),\ u+d(u)\}.$$
In $H_2$ the angle $u+d(u)=k\theta$ is marked. In $H_1$ the angle
$$180^\circ-u-d(u)=n\theta-k\theta=(n-k)\theta$$
is marked as well, because $180^\circ=n\theta$ is a multiple of $\theta$ and
$1\le n-k\le n-1$. (This is the only place where the hypothesis
$\theta=180^\circ/n$ is used.)

So **both** halves contain a marked angle. Whichever half Shan-Yu keeps, the
new triangle contains some marked angle $j\theta$ with $1\le j\le n-1$, and by
Lemma 1 Mulan wins from it within $j-1\le n-2$ further moves.

Total: at most $1+(n-2)=n-1$ moves. $\blacksquare$

### Theorem 2: $\theta\ne180^\circ/m$ — Shan-Yu avoids forever

**Theorem 2.** *Suppose $\theta\ne180^\circ/m$ for every integer $m\ge2$. Then
Shan-Yu has a strategy (choice of initial triangle and of which half to
discard) ensuring that no triangle in the game ever has an angle $\theta$; in
particular Mulan cannot guarantee a win.*

*Proof.* Shan-Yu maintains the invariant:

> **(I)** no angle of the current triangle is marked (i.e. no angle is an
> integer multiple of $\theta$).

Since $\theta$ itself is a multiple of $\theta$, invariant (I) implies the game
never stops, so Mulan never wins.

*Initial triangle.* Shan-Yu builds the equilateral triangle
$(60^\circ,60^\circ,60^\circ)$. If $60^\circ=k\theta$ for an integer $k\ge1$,
then $\theta=60^\circ/k=180^\circ/(3k)$, which is of the excluded form
$180^\circ/m$ ($m=3k\ge3$). Hence (I) holds initially.

*Maintenance.* Assume $\mathcal T=(A,B,C)$ satisfies (I) and Mulan cuts at $A$
with some $\alpha\in(0,A)$ and some choice of $B$, producing
$H_1=\{B,\alpha,180^\circ-B-\alpha\}$ and $H_2=\{C,A-\alpha,B+\alpha\}$
(Lemma 0). We show at least one half satisfies (I); Shan-Yu keeps it.

**Case 1: $\alpha=k\theta$ is a multiple of $\theta$.** Then $H_2$ satisfies
(I): $C$ is unmarked by hypothesis; if $A-\alpha=j\theta$ for an integer
$j\ge1$ (note $A-\alpha>0$), then $A=(j+k)\theta$ is marked, contradiction; if
$B+\alpha=j\theta$ for an integer $j\ge1$, then $B=(j-k)\theta$ with $j-k\ge1$
(since $B>0$), so $B$ is marked, contradiction.

**Case 2: $\alpha$ is not a multiple of $\theta$, and $180^\circ-B-\alpha$ is
not a multiple of $\theta$.** Then $H_1$ satisfies (I): $B$ is unmarked by
hypothesis, and the other two angles of $H_1$ are non-multiples by the case
assumption.

**Case 3: $\alpha$ is not a multiple of $\theta$, but
$180^\circ-B-\alpha=k\theta$ for some integer $k\ge1$.** (Note
$0<k\theta<180^\circ$, since it is an angle of $H_1$.) Then $H_2$ satisfies
(I):

- $C$ is unmarked by hypothesis.
- $A-\alpha=A-\bigl(180^\circ-B-k\theta\bigr)=k\theta-C$. If $A-\alpha=j\theta$
  for an integer $j\ge1$ (it is positive), then $C=(k-j)\theta$ with
  $k-j\ge1$ (since $C>0$), so $C$ is marked — contradiction.
- $B+\alpha=180^\circ-k\theta$. If $B+\alpha=j\theta$ for an integer $j\ge1$
  (it is positive), then $180^\circ=(j+k)\theta$ with $j+k\ge2$, i.e.
  $\theta=180^\circ/(j+k)$ is of the excluded form — contradiction.

The three cases are exhaustive, so the invariant can always be maintained, and
the proof is complete. $\blacksquare$

### Conclusion

By Theorem 1, if $\theta=180^\circ/n$ for an integer $n\ge2$, Mulan guarantees
victory within $n-1$ moves against any play of Shan-Yu (any initial triangle,
any discards). By Theorem 2, for every other $\theta\in(0^\circ,180^\circ)$
Shan-Yu prevents Mulan from ever winning. Hence

$$\boxed{\ \text{Mulan can guarantee victory}\ \iff\
\theta=\frac{180^\circ}{n}\ \text{for some integer } n\ge2
\ \iff\ \frac{180^\circ}{\theta}\in\mathbb Z.\ }$$

Explicitly: $\theta\in\{90^\circ,60^\circ,45^\circ,36^\circ,30^\circ,
\tfrac{180^\circ}{7},22.5^\circ,20^\circ,\dots\}$.

**Verification.** The discretized game ($1^\circ$ and $0.5^\circ$ grids,
`code/retro.py`) yields exactly this family; the explicit strategies above were
verified with exact rational arithmetic (`code/verify.py`): for
$\theta=180^\circ/n$ Mulan's strategy wins in exactly at most $n-1$ moves
(worst case $=n-1$, tight), exhaustively over Shan-Yu's choices, for all tested
$n\le90$ on random rational triangles; the pairing Claim 2 and the round-up
move were additionally checked exhaustively on $\sim 6\times10^4$ unmarked
grid triples for each $n\mid360$, $n\le30$ (`code/check_pairing.py`); for
$\theta\ne180^\circ/m$ Shan-Yu's invariant survived $200\times300$ random
cuts for each tested $\theta$.
