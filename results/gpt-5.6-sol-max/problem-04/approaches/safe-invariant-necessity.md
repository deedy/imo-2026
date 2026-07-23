# Necessity via a safe-family invariant

## Idea
For a normalized target $t$, strengthen avoidance of $t$ to avoidance of every positive integral multiple of $t$. This stronger class is closed adversarially under every cut unless $1$ itself is an integral multiple of $t$.

## Safe triangles
Call a triangle **safe** if none of its three angles belongs to
\[
\{t,2t,3t,\dots\}.
\]
If $t$ is not the reciprocal of an integer, the equilateral triangle is safe: equality $1/3=kt$ would imply $t=1/(3k)$.

For a cut from angle $A$ in a safe triangle $(A,B,C)$, with children
\[
(B,x,1-B-x),\qquad(C,A-x,B+x),
\]
suppose both children were unsafe. Since inherited $B,C$ are not multiples of $t$, one of $x,1-B-x$ equals $rt$, and one of $A-x,B+x$ equals $st$, for positive integers $r,s$. Pairing the alternatives gives:
- $x=rt$, $A-x=st$: then $A=(r+s)t$;
- $x=rt$, $B+x=st$: then $B=(s-r)t$, with $s-r>0$;
- $1-B-x=rt$, $A-x=st$: then $C=(r-s)t$, with $r-s>0$;
- $1-B-x=rt$, $B+x=st$: then $1=(r+s)t$.

The first three contradict safety of the parent. The last says $t=1/(r+s)$, contradicting the nonreciprocal hypothesis. Therefore one child is safe. Shan-Yu always retains such a child, so no retained triangle ever contains $t$ and Mulan never wins.

## Status
Complete. This proves necessity for every nonreciprocal target, including irrational targets and targets greater than $1/2$.
