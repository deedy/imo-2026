# Lemma: invariant family for nonreciprocal targets

## Statement
Normalize a straight angle to have measure $1$. Fix $t\in(0,1)$ such that $t\ne1/n$ for every integer $n\ge2$. Call a triangle **safe** if none of its angles is a positive integral multiple of $t$. After every legal cut of a safe triangle, at least one of the two child triangles is safe.

## Proof
Let the safe parent have angles $(A,B,C)$, and suppose the cut is from the vertex of angle $A$. By the angle-transition formula, for some $x\in(0,A)$ the children have angle triples
\[
(B,x,1-B-x),\qquad(C,A-x,B+x). \tag{1}
\]
Suppose for contradiction that neither child is safe. The inherited angles $B$ and $C$ are not positive integral multiples of $t$, because the parent is safe. Consequently, there are positive integers $r,s$ such that one of
\[
x=rt,\qquad 1-B-x=rt \tag{2}
\]
holds and one of
\[
A-x=st,\qquad B+x=st \tag{3}
\]
holds. We examine the four combinations.

1. If $x=rt$ and $A-x=st$, then $A=(r+s)t$, contrary to safety of the parent.
2. If $x=rt$ and $B+x=st$, then $B=(s-r)t$. Since $B>0$, we have $s-r\ge1$, again contrary to safety.
3. If $1-B-x=rt$ and $A-x=st$, then, using $A+B+C=1$,
   \[
   C=(1-B-x)-(A-x)=(r-s)t.
   \]
   Since $C>0$, $r-s\ge1$, contrary to safety.
4. If $1-B-x=rt$ and $B+x=st$, then $1=(r+s)t$. Thus $t=1/(r+s)$, where $r+s\ge2$, contrary to the hypothesis on $t$.

Every possibility is impossible. Hence at least one child is safe. $\square$
