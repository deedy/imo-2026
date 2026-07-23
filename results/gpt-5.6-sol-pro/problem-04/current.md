# imo-2026-04 — tracking file
## Status
solved

## Problem
Shan-Yu and Mulan are playing a game. Let $\theta$ be an angle with $0^\circ<\theta<180^\circ$ known to both players. Initially, Shan-Yu makes a paper triangle $\mathcal{T}$ with measurements of his choice. Then, they repeatedly perform the following steps: If $\mathcal{T}$ has at least one angle measuring exactly $\theta$, then the game stops and Mulan wins. Otherwise, Mulan chooses a point $P$ on the perimeter of $\mathcal{T}$, different from its three vertices. She then makes a straight cut from $P$ to the opposite vertex of $\mathcal{T}$, splitting it into two triangles. Shan-Yu discards one of the two triangles. The remaining triangle becomes the new $\mathcal{T}$. For which real values of $\theta$ can Mulan guarantee her victory in finitely many steps, no matter how Shan-Yu plays?

## Approaches tried
- Modeled a triangle by its three angle measures in units of $\theta$. A cut from a vertex of angle $a$ splitting it into $x$ and $a-x$ produces angle triples $(b,x,s-b-x)$ and $(c,a-x,b+x)$, where $s=180^\circ/\theta$.
- First observed that $90^\circ$ is universally constructible by an altitude, and hence that $90^\circ/n$ works. This was useful but not the full family: for instance $60^\circ$ can be forced by making the two supplementary angles at the cut point integral multiples of $60^\circ$.
- Developed the integral-angle strategy. If $s=N$ is an integer, any positive integral multiple of $\theta$ is a winning angle, and a suitable cut makes both possible remaining triangles contain such a multiple.
- For nonintegral $s$, found Shan-Yu's invariant: he starts with an equilateral triangle and always retains a child all of whose angles, in units of $\theta$, are nonintegral. A four-case check proves that every cut has at least one such child.

## Current best
Mulan can guarantee victory exactly for $\boxed{\theta=180^\circ/N}$, where $N$ is an integer with $N\ge 2$.

## Full proof
Put
\[
s=\frac{180^\circ}{\theta},
\]
and measure every angle in units of $\theta$. Thus every triangle has angle sum $s$, and Mulan's target angle has measure $1$.

We first record how a cut changes the angles. Suppose the current triangle is $ABC$, with normalized angles
\[
\angle A=a,\qquad \angle B=b,\qquad \angle C=c,
\]
so $a+b+c=s$. If $P$ lies in the interior of $BC$ and $\angle BAP=x$, where $0<x<a$, then the two triangles have normalized angle triples
\[
ABP:(b,x,s-b-x),
\qquad
ACP:(c,a-x,b+x).
\tag{1}
\]
Indeed, the first formula follows from the angle sum, and the two angles at $P$ are supplementary, so the last angle in the second triangle is $b+x$. Conversely, every $x$ with $0<x<a$ can be realized: the ray from $A$ inside $\angle BAC$ making angle $x\theta$ with $AB$ meets the interior of $BC$.

### 1. Sufficiency

Assume that $s=N$ is an integer. Since $0^\circ<\theta<180^\circ$, we have $N\ge2$.

First, if a current triangle has an angle equal to $m$, where $m$ is a positive integer, Mulan can force victory. This is proved by induction on $m$. For $m=1$, she has already won. If $m\ge2$, she cuts from the vertex of that angle so as to split it into angles $1$ and $m-1$. One resulting triangle has angle $1$; the other has angle $m-1$. Hence, whichever triangle Shan-Yu retains, Mulan wins either immediately or by the induction hypothesis.

It remains to show that Mulan can reach this situation from an arbitrary triangle. If one of its normalized angles is already an integer, the preceding paragraph applies. Otherwise, write its angles as $a,b,c$, all nonintegral, with
\[
a+b+c=N.
\]
We claim that the vertices can be labeled so that the open interval $(b,a+b)$ contains an integer $k$.

If some angle, say $a$, is greater than $1$, choose either of the other angles as $b$. The interval $(b,a+b)$ has length $a>1$, so it contains an integer. The only remaining possibility is that all three angles are less than $1$. Then $N<3$; since $N\ge2$ is an integer, $N=2$. For any choice of two angles $a,b$, the third angle satisfies $c<1$, and consequently
\[
b<1<a+b=2-c.
\]
Thus $k=1$ works. This proves the claim.

Choose such a labeling and such an integer $k$, and set
\[
x=k-b.
\]
The inequalities $b<k<a+b$ give $0<x<a$, so the corresponding cut is legal. By (1), one resulting triangle has angle $b+x=k$, while the other has angle
\[
N-b-x=N-k.
\]
Moreover, $0<k<N$, since $b>0$ and $k<a+b=N-c<N$. Therefore $k$ and $N-k$ are positive integers. Whichever triangle Shan-Yu retains, it has a positive integral angle, from which Mulan can force angle $1$ by the induction above. Thus Mulan has a finite winning strategy whenever $s$ is an integer.

### 2. Necessity

Assume now that $s$ is not an integer. Shan-Yu starts with an equilateral triangle. Each of its normalized angles is $s/3$, which is nonintegral: if $s/3$ were an integer, then $s$ would be an integer. In particular, none of these angles is the target value $1$.

Shan-Yu maintains the following invariant:

> All three normalized angles of the retained triangle are nonintegral.

Suppose the current normalized angles $a,b,c$ are all nonintegral, and Mulan makes an arbitrary cut. Relabeling the vertices if necessary, its two resulting angle triples have the form in (1):
\[
(b,x,s-b-x),
\qquad
(c,a-x,b+x).
\]
We prove that at least one triple consists entirely of nonintegers. Suppose, to the contrary, that each triple contains an integer. Since $b$ and $c$ are nonintegral, we must have
\[
 x\in\mathbb Z\quad\text{or}\quad s-b-x\in\mathbb Z,
\tag{2}
\]
and
\[
 a-x\in\mathbb Z\quad\text{or}\quad b+x\in\mathbb Z.
\tag{3}
\]
There are four possible pairings of these alternatives:

- if $x$ and $a-x$ are integers, then $a$ is an integer;
- if $x$ and $b+x$ are integers, then $b$ is an integer;
- if $s-b-x$ and $a-x$ are integers, then their difference $s-a-b=c$ is an integer;
- if $s-b-x$ and $b+x$ are integers, then their sum $s$ is an integer.

Every case contradicts the assumptions. Hence at least one child has three nonintegral normalized angles, and Shan-Yu retains that child.

The invariant can therefore be maintained after every cut. Since the target angle has normalized measure $1$, an integer, it never occurs. Thus Mulan cannot guarantee victory when $s$ is nonintegral.

Combining the two directions, Mulan can guarantee victory exactly when
\[
\frac{180^\circ}{\theta}=N\in\mathbb Z,
\]
that is,
\[
\boxed{\theta=\frac{180^\circ}{N}\quad\text{for an integer }N\ge2.}
\]
