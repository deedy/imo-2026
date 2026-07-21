# imo-2026-04 — tracking file
## Status
solved
## Problem
Shan-Yu and Mulan are playing a game. Let $\theta$ be an angle with $0^\circ<\theta<180^\circ$ known to both players. Initially, Shan-Yu makes a paper triangle $\mathcal{T}$ with measurements of his choice. Then, they repeatedly perform the following steps: If $\mathcal{T}$ has at least one angle measuring exactly $\theta$, then the game stops and Mulan wins. Otherwise, Mulan chooses a point $P$ on the perimeter of $\mathcal{T}$, different from its three vertices. She then makes a straight cut from $P$ to the opposite vertex of $\mathcal{T}$, splitting it into two triangles. Shan-Yu discards one of the two triangles. The remaining triangle becomes the new $\mathcal{T}$. For which real values of $\theta$ can Mulan guarantee her victory in finitely many steps, no matter how Shan-Yu plays?

## Approaches tried
- Modeled game as angle triples $(p,q,r)$, $p+q+r=180$. Move: donor $D$, split $D=x+(D-x)$, children $(p,x,180-p-x)$ and $(q,D-x,p+x)$.
- Computed iterative winning closure for integer angles: $W_0$ contains $\theta$, $W_1$ contains $2\theta$ (or all if $\theta=90$). Closure reaches all triangles iff $180/\theta$ integer.
- Proved sum closure for universally winning angles.
- For $180=n\theta$, gave explicit two-phase strategy: force a multiple, then decrease multiple by splitting off $\theta$.
- For $180$ not multiple of $\theta$, proved invariant $I$ of triangles with no $k\theta$ angle; adversary can stay in $I$.

## Current best
Mulan wins uniformly iff $\theta=180/n$, $n\ge2$ integer. If $\theta=90^\circ$, one move suffices; if $\theta=180/n$, $n\ge3$, $n-1$ moves suffice. Otherwise Shan-Yu chooses initial triangle in $I=\{\text{no angle }k\theta\}$ and preserves membership.

## Full proof
Let a triangle be identified with its (unordered) angle triple
$(p,q,r)$, $p,q,r>0$, $p+q+r=180$.
A move: choose a donor $D\in\{p,q,r\}$, say $T=(p,q,D)$ with $p,q$ the other two,
choose $x\in(0,D)$ and produce

\begin{equation}\tag{1}
C_{1}=(p,x,q+D-x),\qquad C_{2}=(q,D-x,p+x)
\end{equation}
since $180-p-x=q+D-x$. Shan-Yu chooses which $C_i$ survives.
Put $W_{0}=\{T:\theta\in T\}$, and

$$W_{k+1}=W_{k}\cup\{T\notin W_{k}:\exists\text{ donor }D,x\text{ with }C_{1},C_{2}\in W_{k}\}.$$
$Mulan$ can force win in $\le k$ moves uniformly iff $T\in W_{k}$.
Put $L_{k}=W_{k}^{c}$.

### 1. First move
Let $T=(p,q,D)\notin W_{0}$. When $\exists x$ with $C_{1},C_{2}\in W_{0}$?
$C_{1}\in W_{0}\iff x=\theta$ or $180-p-x=\theta$;
$C_{2}\in W_{0}\iff D-x=\theta$ or $p+x=\theta$.
Four possibilities:

- $x=\theta,\ D-x=\theta\Rightarrow D=2\theta$.
- $x=\theta,\ p+x=\theta\Rightarrow p=0$ impossible.
- $180-p-x=\theta,\ D-x=\theta\Rightarrow 180-p-\theta=\theta+q\? $ more directly $180-p-x=\theta$ gives $q+D-x=\theta$, with $D-x=\theta$ gives $q=0$ impossible.
- $180-p-x=\theta,\ p+x=\theta\Rightarrow 180=2\theta$.

Hence for $\theta\neq90^{\circ}$, $W_{1}\setminus W_{0}$ is exactly triangles
containing angle $2\theta$ (if $2\theta<180$), otherwise empty.

For $\theta=90^{\circ}$ every triangle is in $W_{1}$: let $T$ have angles
$p\le q\le D$ (or any order). At least two are acute; pick $p,q<90$.
$p>0$ and $q<90$ implies $D+p=180-q>90$, so $r:=90-p$ satisfies
$0<r<D$. Splitting $D$ as $r$ and $D-r$ gives
$C_{1}=(p,r,180-p-r)=(p,90-p,90)$, $C_{2}=(q,D-r,p+90-p)=(q,D-90+p,90)$.
Both contain $90^{\circ}$. Thus Mulan wins in one move. This is the case
$n=2$.

Assume henceforth $\theta\neq90^{\circ}$.

### 2. Multiples become universally winning
Call $\phi$ universally winning at level $k$ if every triangle containing $\phi$
lies in $W_{k}$. $\theta$ is universally winning at level $0$.
If $s,s'$ are universally winning at level $k$ and $s+s'<180$, then
$s+s'$ is universally winning at level $k+1$:
any $T=(p,q,s+s')$ with $x=s$ gives $C_{1}$ containing $s$, $C_{2}$
containing $s'$, both in $W_{k}$, so $T\in W_{k+1}$.

Inductively, if $k\theta<180$ then $k\theta$ is universally winning and

\begin{equation}\tag{2}
\{\text{triangles containing }k\theta\}\subset W_{k-1},
\end{equation}
with $W_{0}$ for $k=1$. Indeed $k\theta=(k-1)\theta+\theta$.

Explicit decrease: if $T$ contains $k\theta\ge2\theta$, cutting $k\theta$ as
$\theta+(k-1)\theta$ yields $C_{1}$ with $\theta$, $C_{2}$ with $(k-1)\theta$.
Whichever Shan-Yu keeps, either Mulan wins immediately or the new triangle
contains $(k-1)\theta$.

Let $m=\lfloor180/\theta\rfloor$, $\mathcal M=\{k\theta:1\le k\le m,\
k\theta<180\}$ with $|\mathcal M|=m$ unless $180$ multiple. After $m-1$ steps
$W_{m-1}$ contains all triangles whose angle is in $\mathcal M$.

### 3. Divisor case $\theta=180/n$ Mulan wins
Suppose $180=n\theta$, $n\ge2$ integer; $n=2$ done. Let $n\ge3$, so
$\theta\le60^{\circ}$. Then $\mathcal M=\{\theta,2\theta,\dots,(n-1)\theta\}$,
$(n-1)\theta=180-\theta$, and $180-k\theta=(n-k)\theta\in\mathcal M$.
Any triangle containing a multiple is already in $W_{n-2}$ by (2).

Let $T$ contain no angle from $\mathcal M$. Every triangle has an angle
$\le60^{\circ}$; choose $p$ minimal, so $p\le60^{\circ}$ and $p\notin\mathcal M$.
Write $p=k\theta+\alpha$ with $0<\alpha<\theta$, $k\ge0$; then
$r:=(k+1)\theta-p=\theta-\alpha\in(0,\theta)$ and $p+r=(k+1)\theta\in\mathcal M$.
Since $n\ge3$, $p+r\le60^{\circ}+\theta\le120^{\circ}<180$.

Let $D$ be a maximal angle of $T$, $D\ge60^{\circ}\ge r$, indeed
$r<\theta\le60^{\circ}\le D$; also $D\notin\mathcal M$, so $D>r$ unless
$p+r$ trivial, but $0<r<D$ holds after choosing $p$ minimal,
so $x=r$ is feasible. Cutting $D$ as $r$ and $D-r$:

$$C_{1}=(p,r,180-p-r),\quad C_{2}=(q,D-r,p+r)$$

where $q$ is the third angle. $p+r\in\mathcal M$ hence $C_{2}$ contains a multiple.
$180-p-r=180-(k+1)\theta=(n-k-1)\theta\in\mathcal M$ (as $180=n\theta$),
hence $C_{1}$ contains a multiple. Thus both children are in $W_{n-2}$.

Therefore $T\in W_{n-1}$. Mulan's uniform strategy:
- if current triangle contains $k\theta$, $k\ge2$, cut $k\theta$ into
$\theta+(k-1)\theta$; Shan-Yu loses or $k$ drops by one.
- if it contains no multiple, pick $p$ minimal, $D$ maximal, cut $D$ with
$r=\lceil p/\theta\rceil\theta-p$; both children contain multiples, so after
this move we are in previous case with $k\le n-1$.

Hence after at most $n-1$ moves $\theta$ appears, whatever Shan-Yu does.
Thus for $\theta=180/n$ Mulan guarantees finite win.

### 4. Non-divisor case Shan-Yu avoids forever
Assume $\delta:=180\bmod\theta\in(0,\theta)$, i.e. $180=q_{0}\theta+\delta$,
$0<\delta<\theta$, so $180$ is not a multiple of $\theta$.
Let $\mathcal M$ as above, $m=\lfloor180/\theta\rfloor$, and

$$I=\{T:\text{no angle of }T\text{ belongs to }\mathcal M\}.$$

Since $\mathcal M$ finite, $I\neq\varnothing$: choose $a\notin\mathcal M$ small,
choose $b\notin\mathcal M$ with $180-a-b\notin\mathcal M$.

Note $\theta\in\mathcal M$, so $I\subset L_{0}$.

Lemma: If $T=(p,q,D)\in I$ then for any choice of donor and any
$x\in(0,D)$ at least one of the two children in (1) lies in $I$.

Proof: Suppose $T\in I$, i.e. $p,q,D\notin\mathcal M$, and both children
$\notin I$. Then each contains an angle from $\mathcal M$.
Since $p,q\notin\mathcal M$, this forces

- for $C_{1}$: $x=k_{1}\theta$ or $180-p-x=k_{1}\theta$,
- for $C_{2}$: $D-x=k_{2}\theta$ or $p+x=k_{3}\theta$.

Four combos:

1. $x=k_{1}\theta,\ D-x=k_{2}\theta\Rightarrow D=(k_{1}+k_{2})\theta\in\mathcal M$,
contradiction.
2. $x=k_{1}\theta,\ p+x=k_{3}\theta\Rightarrow p=(k_{3}-k_{1})\theta$,
multiple (or zero if $k_{3}=k_{1}$, impossible as $p>0$).
3. $180-p-x=k_{1}\theta,\ D-x=k_{2}\theta\Rightarrow
   180-p-D=(k_{1}-k_{2})\theta$, i.e. $q=(k_{1}-k_{2})\theta\in\mathcal M$.
4. $180-p-x=k_{1}\theta,\ p+x=k_{3}\theta\Rightarrow
   (k_{1}+k_{3})\theta=180$, so $180$ multiple of $\theta$, contradicting $\delta\neq0$.

All impossible, so at least one child stays in $I$. ∎

Consequence: Shan-Yu can forever stay in $I$. Starting from
$T_{0}\in I$, whatever donor $D$ and split $x$ Mulan announces,
Shan-Yu chooses the child belonging to $I$ (exists by lemma). The game never
hits an angle in $\mathcal M$, in particular never hits $\theta$. Hence Mulan
has no finite winning strategy; indeed she never wins.

This includes $\theta>90^{\circ}$, $\theta\neq90^{\circ}$, where
$\mathcal M=\{\theta\}$ and the same case analysis shows $W_{1}=W_{0}$.

### 5. Answer
Mulan can force victory in boundedly many steps iff $180/\theta$ is an integer.
I.e.

$$\theta=\frac{180^{\circ}}{n}\ \text{for some integer }n\ge2.$$

For $n=2$ ($\theta=90^{\circ}$) one cut suffices; for $n\ge3$ at most $n-1$ cuts
suffice by the strategy above (force a multiple, then descend).
If $\theta$ is not of this form, Shan-Yu starts with a triangle having no angle
$k\theta$ and can keep this property forever, so Mulan can never force $\theta$.

∎
