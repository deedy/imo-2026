# Lexicographic termination potential

## Idea
For a board configuration $(x_1,\dots,x_{2026})$, set
\[
S=\sum_i\Omega(x_i),\qquad N=\#\{i:x_i>1\},
\]
where $\Omega(x)$ is the total number of prime factors of $x$, counted with multiplicity (and $\Omega(1)=0$). Order $(S,N)$ lexicographically.

## Status
Successful.

## Details
Suppose a move is performed on $m,n>1$, and put $d=\gcd(m,n)$. The two replacements have product
\[
d\cdot \frac{\operatorname{lcm}(m,n)}d=\operatorname{lcm}(m,n)=\frac{mn}{d}.
\]
By complete additivity of $\Omega$, their contribution to $S$ is therefore
\[
\Omega(m)+\Omega(n)-\Omega(d).
\]
If $d>1$, then $S$ strictly decreases. If $d=1$, then the replacements are $1$ and $mn$, so $S$ stays fixed while $N$ decreases by one. Thus $(S,N)$ strictly decreases lexicographically at every move. Since both coordinates are nonnegative integers, no infinite sequence of moves exists.

A terminal board has at most one entry greater than $1$, because any two such entries could be selected. Every move made on two nonunits produces at least one nonunit (if the second output were $1$, then $m=n=d>1$, so the first is a nonunit; otherwise the second itself is one). Since initially nonunits exist, a terminal board has exactly one.
