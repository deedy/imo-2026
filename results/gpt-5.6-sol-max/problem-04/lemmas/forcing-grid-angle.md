# Lemma: forcing complementary grid angles

## Statement
Normalize a straight angle to have measure $1$, and let $n\ge2$ be an integer. From every triangle, either it already has an angle $1/n$, or Mulan can make one cut such that each of the two child triangles has an angle of the form $k/n$ for some integer $k\in\{1,\dots,n-1\}$ (the integer may differ between the children).

## Proof
Write the triangle's angles as $A,B,C$.

First suppose $n=2$ and no angle is $1/2$. At least two of the three angles are less than $1/2$: otherwise two angles would be greater than $1/2$, whose sum would exceed $1$. Label two such angles $B,C$, and call the remaining angle $A$. Then
\[
C<\frac12<1-B=A+C.
\]

Now suppose $n\ge3$ and no angle is $1/n$. Choose $A$ to be a largest angle and let $B,C$ be the other two in either order. We claim that the open interval
\[
(nC,\,n(A+C))
\]
contains an integer. Its length is $nA$. If $n>3$, then $nA\ge n/3>1$. If $n=3$, then $A\ge1/3$; equality would force $A=B=C=1/3$, contrary to the assumption that no angle is $1/n$, so again $nA>1$. Every open interval of length greater than $1$ contains an integer. Hence there is an integer $m$ such that
\[
nC<m<n(A+C).
\]
Since $C>0$ and $A+C=1-B<1$, necessarily $1\le m\le n-1$. Thus, in all cases (taking $m=1$ when $n=2$), we have found labels and an integer $m\in\{1,\dots,n-1\}$ satisfying
\[
C<\frac mn<A+C=1-B. \tag{1}
\]

Make a cut from the vertex of angle $A$. In the notation of the angle-transition lemma, choose
\[
x=1-B-\frac mn=A+C-\frac mn.
\]
The two strict inequalities in (1) give $0<x<A$, so this is a legal cut. The angle at the new boundary point in one child is
\[
1-B-x=\frac mn,
\]
and the supplementary angle there in the other child is
\[
B+x=1-\frac mn=\frac{n-m}{n}.
\]
Both numerators lie in $\{1,\dots,n-1\}$. Therefore each child has an angle which is a positive integral multiple of $1/n$. $\square$
