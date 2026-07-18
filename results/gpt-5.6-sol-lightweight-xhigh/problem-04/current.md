# imo-2026-04 — tracking file
## Status
solved

## Problem
Shan-Yu and Mulan are playing a game. Let $\theta$ be an angle with $0^\circ<\theta<180^\circ$ known to both players. Initially, Shan-Yu makes a paper triangle $\mathcal{T}$ with measurements of his choice. Then, they repeatedly perform the following steps: If $\mathcal{T}$ has at least one angle measuring exactly $\theta$, then the game stops and Mulan wins. Otherwise, Mulan chooses a point $P$ on the perimeter of $\mathcal{T}$, different from its three vertices. She then makes a straight cut from $P$ to the opposite vertex of $\mathcal{T}$, splitting it into two triangles. Shan-Yu discards one of the two triangles. The remaining triangle becomes the new $\mathcal{T}$. For which real values of $\theta$ can Mulan guarantee her victory in finitely many steps, no matter how Shan-Yu plays?

## Approaches tried
- **Angle-coordinate model (successful):** If the current angles are $(A,B,C)$ and a cut from the $A$-vertex splits $A$ into $x$ and $A-x$, the children have angles $(B,x,180^\circ-B-x)$ and $(C,A-x,B+x)$. Thus the two new angles at the cut point are supplementary.
- **Finite-horizon backward sets (partially useful):** Starting from triangles already containing $\theta$, an attempted full description of successive winning sets became unwieldy. Its useful consequence was the recursive observation that every triangle containing $m\theta$, for a positive integer $m$, is winning.
- **Complementary cut-point angles (successful):** When $180^\circ=n\theta$, a cut can be chosen so that the two children have cut-point angles $k\theta$ and $(n-k)\theta$. An elementary integer-between-partial-sums lemma guarantees such a legal cut from every triangle not already containing an integral multiple of $\theta$.
- **Safe-triangle invariant (successful):** Call a triangle safe if none of its angles is a positive integral multiple of $\theta$. If $180^\circ/\theta$ is not an integer, every cut of a safe triangle has a safe child. Starting from an equilateral safe triangle, Shan-Yu can therefore avoid defeat forever.
- **Sanity checks:** `code/sanity_checks.py` checked the safe-child invariant on $130242$ rational-grid cut configurations and the integer interval lemma on $18744$ rational-grid triples. These computations are not used as proof.

## Current best
The complete characterization is
\[
\boxed{\theta=\frac{180^\circ}{n}\quad\text{for an integer }n\ge2.}
\]
For these and only these values Mulan has a finite winning strategy. In fact, the proof gives a bound depending only on $n$ for the number of cuts.

## Full proof
We prove both directions. All angles below are measured in degrees.

### 1. The effect of a cut

Let a triangle $ABC$ have angles $A,B,C$. Suppose that $P$ is an interior point of $BC$, and put
\[
x=\angle BAP.
\]
Then $0<x<A$. The angle triples of the two resulting triangles $ABP$ and $ACP$ are, respectively,
\[
(B,x,180^\circ-B-x)                                      \tag{1}
\]
and
\[
(C,A-x,B+x).                                               \tag{2}
\]
Indeed, the first two entries displayed in each triple are the inherited angles at the original vertices, and the third follows from the angle sum of a triangle, using $A+B+C=180^\circ$.

Conversely, every $x$ with $0<x<A$ can be realized by a legal cut: the ray from $A$ inside $\angle BAC$ which makes angle $x$ with $AB$ meets the opposite side $BC$ at an interior point. Thus, in using (1)--(2), it is enough to verify $0<x<A$.

### 2. Triangles containing integral multiples of $\theta$

We first establish a forcing observation.

**Lemma 1.** If the current triangle has an angle $m\theta$, where $m$ is a positive integer, then Mulan can force a win after at most $m-1$ further cuts.

**Proof.** We use induction on $m$. For $m=1$, the stopping condition already holds, so no cut is needed.

Let $m\ge2$. From the vertex with angle $m\theta$, Mulan makes the cut which divides that angle into
\[
\theta+(m-1)\theta.
\]
Both parts are positive, so this is a legal cut by the observation above. One child has an angle $\theta$, while the other has an angle $(m-1)\theta$. If Shan-Yu retains the first, Mulan wins at the next stopping check. If he retains the second, the induction hypothesis gives a win after at most $m-2$ additional cuts. In either case at most $m-1$ cuts are required. $\square$

### 3. Sufficiency

Suppose
\[
180^\circ=n\theta                                             \tag{3}
\]
for an integer $n\ge2$. We show that Mulan can win from every initial triangle.

If the current triangle has an angle equal to a positive integral multiple of $\theta$, Lemma 1 applies. It remains to handle a triangle none of whose angles is an integral multiple of $\theta$.

Divide its three angles by $\theta$, obtaining positive, nonintegral real numbers $a,b,c$ such that
\[
a+b+c=n.                                                    \tag{4}
\]
We need the following elementary claim.

**Claim.** After possibly relabeling $a,b,c$, there is an integer $k$ such that
\[
b<k<a+b.                                                    \tag{5}
\]
Moreover, $1\le k\le n-1$.

**Proof of the claim.** First suppose at least one of $a,b,c$ is greater than $1$. Name such a number $a$, name either of the remaining numbers $b$, and take $k=\lceil b\rceil$. Because $b$ is not an integer,
\[
0<k-b<1<a,
\]
which proves (5).

Otherwise all three numbers are less than $1$: they are not equal to $1$ because they are nonintegral. Hence (4) gives $n<3$. Since $n\ge2$ is an integer, $n=2$. Name the numbers in any order. We have $b<1$, while
\[
a+b=2-c>1.
\]
Thus $k=1$ satisfies (5).

Finally, in either case, (5) and positivity give $k>b>0$, and
\[
k<a+b=n-c<n.
\]
Since $k$ is an integer, $1\le k\le n-1$. This proves the claim. $\square$

Label the original triangle so that its angles are
\[
A=a\theta,\qquad B=b\theta,\qquad C=c\theta,
\]
where (5) holds. Mulan cuts from the vertex with angle $A$, choosing
\[
x=(k-b)\theta.
\]
The inequalities (5) give
\[
0<x<a\theta=A,
\]
so this is a legal cut. By (1)--(2), one child has at the cut point the angle
\[
B+x=b\theta+(k-b)\theta=k\theta,                             \tag{6}
\]
while the other has at the cut point the angle
\[
180^\circ-B-x=n\theta-k\theta=(n-k)\theta.                  \tag{7}
\]
Both $k$ and $n-k$ are positive integers. Whichever child Shan-Yu retains, it therefore contains a positive integral multiple of $\theta$, so Lemma 1 gives Mulan a win after finitely many further cuts. This proves sufficiency.

### 4. Necessity

Now suppose that
\[
\frac{180^\circ}{\theta}\notin\mathbb Z.                    \tag{8}
\]
Call a triangle **safe** if none of its angles is a positive integral multiple of $\theta$. We show that after every cut of a safe triangle, at least one child is safe.

Let the safe parent have angles $A,B,C$, and consider a cut from the vertex with angle $A$. With the notation of (1)--(2), its children have angle triples
\[
(B,x,180^\circ-B-x),\qquad(C,A-x,B+x).                       \tag{9}
\]
Assume for contradiction that both children are not safe. The inherited angles $B$ and $C$ are not integral multiples of $\theta$, because the parent is safe. Hence there are positive integers $p,q$ such that one equality from each of the following rows holds:
\[
x=p\theta\quad\text{or}\quad 180^\circ-B-x=p\theta,       \tag{10}
\]
\[
A-x=q\theta\quad\text{or}\quad B+x=q\theta.               \tag{11}
\]
There are four possible pairings:

1. If $x=p\theta$ and $A-x=q\theta$, then
   \[
   A=(p+q)\theta,
   \]
   contradicting safety of the parent.
2. If $x=p\theta$ and $B+x=q\theta$, then
   \[
   B=(q-p)\theta.
   \]
   Since $B>0$, $q-p$ is a positive integer, again contradicting safety.
3. If $180^\circ-B-x=p\theta$ and $A-x=q\theta$, then, using $A+B+C=180^\circ$,
   \[
   C=(180^\circ-B-x)-(A-x)=(p-q)\theta.
   \]
   Since $C>0$, this contradicts safety.
4. If $180^\circ-B-x=p\theta$ and $B+x=q\theta$, then adding gives
   \[
   180^\circ=(p+q)\theta,
   \]
   contradicting (8).

All possibilities are impossible. Therefore at least one child of every cut of a safe triangle is safe.

Finally, Shan-Yu can choose an equilateral initial triangle. It is safe: if its angle $60^\circ$ were $m\theta$ for some positive integer $m$, then
\[
\frac{180^\circ}{\theta}=3m
\]
would be an integer, contrary to (8). After every cut, Shan-Yu retains a safe child, which exists by the preceding argument. Every retained triangle is nondegenerate because the cut point is not a vertex. Since a safe triangle has no angle $\theta$, the stopping condition never occurs. Thus Mulan cannot guarantee a finite victory when (8) holds.

Combining sufficiency and necessity, and observing that $0^\circ<\theta<180^\circ$ makes an integral value $180^\circ/\theta$ at least $2$, yields exactly
\[
\boxed{\theta=180^\circ/n\quad(n=2,3,4,\ldots)}.
\]
