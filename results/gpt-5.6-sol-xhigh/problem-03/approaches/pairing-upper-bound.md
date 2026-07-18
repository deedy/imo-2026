# Equal-pair response (non-sharp upper bound)

## Idea and proof
Let the initial interval lengths be $a_1,\dots,a_m$. If $m\le n$, Xiang Yu bisects every interval, producing equal pairs and hence alternating discrepancy $D=0$.

Suppose $m=n+1$ and put $t=1/(2n+1)$. If some $a_i\le t$, leave that interval intact and bisect all other $n$ intervals. The final multiset consists of equal pairs and one singleton of length at most $t$, so $D\le t$.

Otherwise all $a_i>t$. On sorting the lengths increasingly, two consecutive lengths differ by at most $t$. Indeed, if all consecutive gaps exceeded $t$, then $a_i>it$, and
\[
1=\sum_{i=1}^{n+1}a_i>t\frac{(n+1)(n+2)}2\ge 1,
\]
a contradiction (for $n=1$ the last comparison is equality but the preceding inequality is strict; for $n\ge2$ it is strict). For a pair $a\le b$ with $b-a\le t$, cut a piece of length $a$ from the interval of length $b$, and bisect each of the other $n-1$ intervals. Again all pieces pair equally except for a singleton of length $b-a\le t$, so $D\le t$.

Thus the game value is at most $(1+t)/2=(n+1)/(2n+1)$. This bound is not sharp for at least $n=2$.

## Status
Rigorous but non-sharp upper bound.
