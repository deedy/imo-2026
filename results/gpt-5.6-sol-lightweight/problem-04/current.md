# imo-2026-04 — tracking file

## Status
solved

## Problem
Shan-Yu and Mulan are playing a game. Let $\theta$ be an angle with $0^\circ<\theta<180^\circ$ known to both players. Initially, Shan-Yu makes a paper triangle $\mathcal{T}$ with measurements of his choice. Then, they repeatedly perform the following steps: If $\mathcal{T}$ has at least one angle measuring exactly $\theta$, then the game stops and Mulan wins. Otherwise, Mulan chooses a point $P$ on the perimeter of $\mathcal{T}$, different from its three vertices. She then makes a straight cut from $P$ to the opposite vertex of $\mathcal{T}$, splitting it into two triangles. Shan-Yu discards one of the two triangles. The remaining triangle becomes the new $\mathcal{T}$. For which real values of $\theta$ can Mulan guarantee her victory in finitely many steps, no matter how Shan-Yu plays?

## Approaches tried
- **Integral-multiple descent (successful).** When $180^\circ=N\theta$, regard all angles in units of $\theta$. First force both children to have an integral angle, then repeatedly split an integral angle $m$ into $1$ and $m-1$.
- **Integer-entry interval lemma (successful).** For nonintegral $a+b+c=N$, after relabeling there is an integer $k$ strictly between $b$ and $a+b$; this specifies a legal cut whose two new opposite angles are $N-k$ and $k$.
- **Quotient-group invariant (successful).** Modulo $\theta\mathbb Z$, if the class of $180^\circ$ is nonzero and all three current angle classes are nonzero, every cut has at least one child with the same property. Shan-Yu retains that child forever.
- **Computational sanity check.** Random normalized triangles for $2\le N<30$ verified the interval construction, positivity of all child angles, and the formulas for the two forced integral angles.

## Current best
Mulan can guarantee victory exactly for
\[
\boxed{\theta=\frac{180^\circ}{N}\quad\text{with an integer }N\ge 2.}
\]
For these values she first forces an integral multiple of $\theta$ to survive regardless of Shan-Yu's choice, and then decreases that multiple until it is $\theta$. For every other $\theta$, Shan-Yu starts with an equilateral triangle and uses a nonzero-class invariant modulo $\theta\mathbb Z$ to avoid $\theta$ forever.

## Full proof
We prove both directions.

### 1. Sufficiency

Suppose
\[
180^\circ=N\theta
\]
for an integer $N\ge 2$. Measure all angles in units of $\theta$, so the angles of every triangle sum to $N$.

We first record an elementary fact.

**Lemma 1.** Let $a,b,c>0$ satisfy $a+b+c=N$, where $N\ge2$ is an integer. If none of $a,b,c$ is an integer, then the variables can be relabeled so that, for some integer $k$,
\[
b<k<a+b.
\]

**Proof.** If one of the three numbers, say $a$, exceeds $1$, take either of the other two numbers as $b$. Since $b$ is not an integer,
\[
b<\lceil b\rceil<b+1<b+a.
\]
Thus $k=\lceil b\rceil$ works.

It remains to consider the case in which all three numbers are at most $1$. As none is an integer, all are in fact less than $1$, so $N=a+b+c<3$. Since $N\ge2$ is an integer, $N=2$. Choose any one of the numbers as $c$ and call the other two $a,b$. Then $b<1$ and
\[
a+b=2-c>1.
\]
Hence $k=1$ works. $\square$

Now consider any current triangle. If it already has an angle $\theta$, Mulan has won. If one of its normalized angles is an integer $m$, then necessarily $1\le m\le N-1$. We will shortly explain how Mulan wins from such a position.

It therefore remains only to handle a triangle whose normalized angles $a,b,c$ are all nonintegral. Relabel its vertices using Lemma 1, and choose an integer $k$ such that
\[
b<k<a+b.
\]
Mulan cuts from the vertex having angle $a$ to the opposite side, choosing the cut so that the part of angle $a$ adjacent to the vertex having angle $b$ is
\[
x=k-b.
\]
The inequalities above give $0<x<a$, so the ray lies strictly inside the angle and meets the interior of the opposite side. Thus this is a legal cut.

In the child adjacent to the angle $b$, the angle at the point of the cut is
\[
N-b-x=N-k,
\]
whereas in the other child the angle at the point of the cut is
\[
N-c-(a-x)=N-c-a+k-b=k,
\]
because $a+b+c=N$. Therefore, no matter which child Shan-Yu retains, its triangle has an angle that is a positive integral multiple of $\theta$. (Both $k$ and $N-k$ are strictly between $0$ and $N$, as they are angles of nondegenerate child triangles.)

Finally, suppose a current triangle has an angle $m\theta$, where $m$ is an integer with $1\le m\le N-1$. If $m=1$, Mulan wins. If $m\ge2$, she cuts from that vertex along the interior ray which splits the angle $m\theta$ into angles
\[
\theta\quad\text{and}\quad (m-1)\theta.
\]
Such a ray meets the interior of the opposite side, so the cut is legal. One child has an angle $\theta$ and the other has an angle $(m-1)\theta$. If Shan-Yu keeps the first, Mulan wins at the next stopping check; if he keeps the second, the positive integer $m$ has decreased by $1$. Repeating this argument forces victory after at most $m-1$ further cuts. This proves sufficiency.

### 2. Necessity

Suppose now that
\[
180^\circ\notin\theta\mathbb Z.
\]
We show that Shan-Yu can prevent victory indefinitely.

Work in the additive quotient group
\[
G=\mathbb R/(\theta\mathbb Z),
\]
and denote the class of a real angle $r$ by $[r]$. In particular, let
\[
t=[180^\circ]\ne0.
\]
Call a triangle *safe* if none of its three angles has class $0$ in $G$, equivalently, if none is an integral multiple of $\theta$.

Shan-Yu can initially choose an equilateral triangle. It is safe: if $[60^\circ]=0$, then $60^\circ=n\theta$ for some integer $n$, which would give $180^\circ=3n\theta$, contrary to the assumption.

We prove that after every cut of a safe triangle, at least one child is safe. Let the classes of the parent angles be $a,b,c$. Then
\[
a,b,c\ne0,\qquad a+b+c=t\ne0.
\]
Suppose Mulan cuts from the vertex with angle class $a$, splitting that angle into classes $u$ and $v$, where $u+v=a$. The two child triangles have angle-class triples
\[
(u,b,c+v)\qquad\text{and}\qquad(v,c,b+u).
\]
Indeed, for example, the third angle of the first child has class
\[
t-b-u=(a+b+c)-b-u=c+v,
\]
and similarly for the second child.

Assume for contradiction that neither child is safe. Since $b,c\ne0$, the first child can contain a zero class only if
\[
u=0\quad\text{or}\quad c+v=0,
\]
and the second can contain a zero class only if
\[
v=0\quad\text{or}\quad b+u=0.
\]
There are four possible pairings. If $u=v=0$, then $a=u+v=0$. If $u=0$ and $b+u=0$, then $b=0$. If $c+v=0$ and $v=0$, then $c=0$. Each contradicts safety. In the sole remaining case,
\[
c+v=0\quad\text{and}\quad b+u=0,
\]
so
\[
t=a+b+c=(u+v)+b+c=(b+u)+(c+v)=0,
\]
again a contradiction. Hence at least one child is safe.

After every cut, Shan-Yu retains a safe child. Since an angle equal to $\theta$ has class $0$, a safe triangle never triggers Mulan's victory. Thus Mulan cannot guarantee victory when $180^\circ\notin\theta\mathbb Z$.

Combining necessity and sufficiency, and using $0^\circ<\theta<180^\circ$, the desired values are exactly
\[
\boxed{\theta=\frac{180^\circ}{N}\quad(N=2,3,4,\ldots).}
\]
