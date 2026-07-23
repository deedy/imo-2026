# imo-2026-04 — tracking file
## Status
solved

## Problem
Shan-Yu and Mulan are playing a game. Let $\theta$ be an angle with $0^\circ<\theta<180^\circ$ known to both players. Initially, Shan-Yu makes a paper triangle $\mathcal{T}$ with measurements of his choice. Then, they repeatedly perform the following steps: If $\mathcal{T}$ has at least one angle measuring exactly $\theta$, then the game stops and Mulan wins. Otherwise, Mulan chooses a point $P$ on the perimeter of $\mathcal{T}$, different from its three vertices. She then makes a straight cut from $P$ to the opposite vertex of $\mathcal{T}$, splitting it into two triangles. Shan-Yu discards one of the two triangles. The remaining triangle becomes the new $\mathcal{T}$. For which real values of $\theta$ can Mulan guarantee her victory in finitely many steps, no matter how Shan-Yu plays?

## Approaches tried
- **Angle-coordinate game:** Normalize $180^\circ$ to $1$. Cutting from angle $A$ and splitting it as $x+(A-x)$ in a triangle $(A,B,C)$ yields children $(B,x,1-B-x)$ and $(C,A-x,B+x)$. This exact transition model underlies both directions.
- **Finite rational-grid attractor computation:** For targets $p/q$ and grid-restricted states/cuts through $q=20$, all states were winning exactly when $p\mid q$, suggesting the answer $t=1/n$. This was exploratory only; arbitrary real cuts required a proof independent of computation.
- **Reciprocal-target construction:** For $t=1/n$, complementary angles at the cut point can be chosen as $m/n$ and $(n-m)/n$. An interval argument finds an admissible $m$ for every starting triangle; then an induction reduces any retained angle $k/n$ to $1/n$.
- **Safe-family invariant for necessity:** For nonreciprocal $t$, call a triangle safe when no angle is a positive integral multiple of $t$. An exhaustive four-case use of the transition formula proves that every cut of a safe triangle has a safe child. An equilateral starting triangle is safe, so Shan-Yu can avoid the target forever.
- **Earlier acute-triangle idea:** For $t>1/2$, retaining an acute child gives a special-case avoidance strategy, but the safe-family invariant supersedes it and handles all nonreciprocal targets uniformly.

## Current best
The complete characterization is
\[
\boxed{\theta=\frac{180^\circ}{n}\quad\text{for some integer }n\ge2.}
\]
For these and only these values, Mulan has a finite winning strategy. In fact, after at most one initialization cut she forces a positive integral multiple $k\theta$ in either possible child, and then needs at most $k-1\le n-2$ further cuts.

## Full proof
Normalize all angle measures by dividing by $180^\circ$. Thus a triangle's angles sum to $1$, and put
\[
t=\frac{\theta}{180^\circ}\in(0,1).
\]
We prove that Mulan can force a win exactly when $t=1/n$ for an integer $n\ge2$.

### 1. The transition rule
Suppose the current triangle has angles $(A,B,C)$. Mulan cuts from the vertex of angle $A$ to the opposite side, and let $x$ be the portion of angle $A$ lying in the child containing the vertex of angle $B$. Since the cut is interior,
\[
0<x<A.
\]
The two children have angle triples
\[
(B,x,1-B-x) \tag{1}
\]
and
\[
(C,A-x,B+x). \tag{2}
\]
Indeed, the first two angles of the first child are $B,x$, so its third angle is $1-B-x$. The second child has angles $C,A-x$ at old vertices, so its angle at the cut point is
\[
1-C-(A-x)=B+x.
\]
Conversely, every $x\in(0,A)$ is attainable: the unique ray inside the angle $A$ making angle $x$ with the appropriate side meets the opposite side at an interior point.

### 2. Sufficiency when $t=1/n$
Let $n\ge2$ be an integer and suppose $t=1/n$. We first show that, from any triangle not already containing angle $t$, Mulan can make a cut after which either possible child contains an angle $k/n$ for some integer $k\in\{1,\dots,n-1\}$.

Let the triangle's angles be $(A,B,C)$.

If $n=2$, then at least two angles are less than $1/2$: otherwise either one is exactly $1/2$, in which case Mulan has already won, or two are greater than $1/2$, which is impossible because the angle sum is $1$. Label two angles below $1/2$ as $B,C$ and the third as $A$. Then
\[
C<\frac12<1-B=A+C. \tag{3}
\]

Now let $n\ge3$, and choose $A$ to be a largest angle. Then $A\ge1/3$. In fact,
\[
nA>1. \tag{4}
\]
For $n>3$ this follows from $nA\ge n/3>1$. For $n=3$, if $3A=1$, then maximality and the angle sum force $A=B=C=1/3=t$, contrary to the assumption that the triangle does not already contain the target.

The open interval
\[
(nC,n(A+C))
\]
has length $nA>1$, so it contains an integer $m$. To justify this explicitly, choose the least integer strictly greater than $nC$; it is at most $nC+1<n(A+C)$. Moreover,
\[
0<nC<m<n(A+C)=n(1-B)<n,
\]
so $m\in\{1,\dots,n-1\}$. Consequently,
\[
C<\frac mn<A+C. \tag{5}
\]
For $n=2$, the same conclusion holds with $m=1$ by (3).

Mulan now cuts from the vertex with angle $A$, choosing
\[
x=A+C-\frac mn=1-B-\frac mn.
\]
The right inequality in (5) gives $x>0$, and the left inequality gives $x<A$, so this is a legal cut. By (1) and (2), the angles at the new point in the two children are
\[
1-B-x=\frac mn
\quad\text{and}\quad
B+x=1-\frac mn=\frac{n-m}{n}. \tag{6}
\]
Both are positive integral multiples of $t=1/n$. Hence whichever child Shan-Yu retains has an angle $kt$ with $1\le k\le n-1$.

It remains to show that any such multiple can be reduced to the target. We use induction on $k$. If $k=1$, Mulan has already won. If $k\ge2$, she cuts from the vertex whose angle is $kt$, using the interior ray which splits it into
\[
t+(k-1)t.
\]
This is legal because both portions are positive. One child contains angle $t$, while the other contains angle $(k-1)t$. Thus Shan-Yu either retains a triangle with the target angle, or leaves a strictly smaller positive integral multiple, to which the induction hypothesis applies. Mulan therefore wins after finitely many cuts. This proves sufficiency.

### 3. Necessity for all other $t$
Suppose now that
\[
t\ne\frac1n\qquad\text{for every integer }n\ge2. \tag{7}
\]
Call a triangle **safe** if none of its angles is a positive integral multiple of $t$.

Shan-Yu can choose an equilateral initial triangle, and it is safe. Indeed, if its angle $1/3$ were $kt$ for a positive integer $k$, then $t=1/(3k)$, contrary to (7).

We claim that after any legal cut of a safe triangle, at least one child is safe. Let the safe parent have angles $(A,B,C)$, and suppose the cut is from the vertex of angle $A$. Use the parameter $x\in(0,A)$ from (1)--(2). Assume for contradiction that both children are unsafe.

The inherited angle $B$ in the first child is not a positive integral multiple of $t$, because the parent is safe. Therefore one of the other two angles of that child must be such a multiple: for some positive integer $r$,
\[
x=rt\quad\text{or}\quad 1-B-x=rt. \tag{8}
\]
Likewise, inherited angle $C$ in the second child is not a multiple, so for some positive integer $s$,
\[
A-x=st\quad\text{or}\quad B+x=st. \tag{9}
\]
There are four possibilities.

- If $x=rt$ and $A-x=st$, then $A=(r+s)t$, contradicting safety of the parent.
- If $x=rt$ and $B+x=st$, then $B=(s-r)t$. As $B>0$, we have $s-r\ge1$, again contradicting safety.
- If $1-B-x=rt$ and $A-x=st$, then
  \[
  C=1-A-B=(1-B-x)-(A-x)=(r-s)t.
  \]
  Since $C>0$, we have $r-s\ge1$, contradicting safety.
- If $1-B-x=rt$ and $B+x=st$, adding gives $1=(r+s)t$. Hence $t=1/(r+s)$. Since $r+s\ge2$, this contradicts (7).

All four cases are impossible, proving the claim. Shan-Yu can therefore retain a safe child after every cut. Every retained triangle remains safe, and in particular never has an angle equal to $t$. Thus Mulan cannot guarantee a win when (7) holds.

Combining the two directions and restoring degrees gives exactly
\[
\boxed{\theta=\frac{180^\circ}{n}\quad(n=2,3,4,\dots)}.
\]
