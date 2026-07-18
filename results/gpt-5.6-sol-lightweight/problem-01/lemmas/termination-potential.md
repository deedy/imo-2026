# Lemma: every sequence of moves terminates

**Lemma.** Starting from any finite board containing positive integers, the prescribed operation cannot be performed infinitely many times if each move selects two entries greater than $1$.

**Proof.** Let $\Omega(t)$ be the number of prime factors of $t$, counted with multiplicity, and let $\Omega(1)=0$. For a configuration $(x_1,\dots,x_k)$ define
\[
S=\sum_{i=1}^k\Omega(x_i),\qquad N=\#\{i:x_i>1\}.
\]
We order the pairs $(S,N)\in\mathbb Z_{\ge0}^2$ lexicographically.

For a move on $m,n>1$, let $d=\gcd(m,n)$. Since
\[
d\cdot\frac{\operatorname{lcm}(m,n)}d=\operatorname{lcm}(m,n)=\frac{mn}{d},
\]
the complete additivity of $\Omega$ gives
\[
\Omega(d)+\Omega\left(\frac{\operatorname{lcm}(m,n)}d\right)
=\Omega(m)+\Omega(n)-\Omega(d).
\]
If $d>1$, then $\Omega(d)>0$, so $S$ decreases. If $d=1$, the replacements are $1$ and $mn$; hence $S$ is unchanged, while two nonunits are replaced by exactly one nonunit, so $N$ decreases by one. Every move therefore strictly decreases $(S,N)$ lexicographically.

There is no infinite strictly decreasing sequence in $\mathbb Z_{\ge0}^2$ with lexicographic order: the first coordinate can decrease only finitely many times, and between two such decreases the second coordinate can decrease only finitely many times. Hence every sequence of moves terminates. $\square$
