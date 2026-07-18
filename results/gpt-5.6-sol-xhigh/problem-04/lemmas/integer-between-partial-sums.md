# Integer between two partial sums

## Statement
Let $n\ge2$ be an integer and let $a,b,c$ be positive, nonintegral real numbers satisfying
\[
a+b+c=n.
\]
After permuting $a,b,c$, there is an integer $k$ such that
\[
 b<k<a+b.
\]
Necessarily $1\le k\le n-1$.

## Proof
First suppose one of the three numbers is greater than $1$. Call it $a$, call either one of the other numbers $b$, and set $k=\lceil b\rceil$. Since $b$ is not an integer,
\[
0<k-b<1<a,
\]
which gives $b<k<a+b$.

It remains to consider the case in which none of the three numbers is greater than $1$. Since none is integral and all are positive, all three are strictly less than $1$. Consequently $n=a+b+c<3$. As $n\ge2$ is an integer, $n=2$. For any choice of $c$, we then have $a+b=2-c>1$ for the other two numbers. Since $b<1$, taking $k=1$ gives $b<k<a+b$.

In either case, $k>b>0$, so $k\ge1$. Also $k<a+b=n-c<n$, so the integer $k$ is at most $n-1$. $\square$
