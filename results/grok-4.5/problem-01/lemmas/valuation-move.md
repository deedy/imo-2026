# Lemma: effect of a move on p-adic valuations

## Statement
Let $m,n>1$ be integers and let $g=\gcd(m,n)$, $\ell=\frac{\mathrm{lcm}(m,n)}{\gcd(m,n)}$. For every prime $p$, writing $\alpha=v_p(m)$ and $\beta=v_p(n)$, the $p$-adic valuations of the replacement pair satisfy
\[
v_p(g)=\min(\alpha,\beta),\qquad v_p(\ell)=\max(\alpha,\beta)-\min(\alpha,\beta).
\]
In particular, $\gcd\bigl(v_p(g),v_p(\ell)\bigr)=\gcd(\alpha,\beta)$.

## Proof
By definition of gcd and lcm in terms of valuations,
\[
v_p(g)=\min(\alpha,\beta),\qquad v_p(\mathrm{lcm}(m,n))=\max(\alpha,\beta).
\]
Hence
\[
v_p(\ell)=v_p(\mathrm{lcm}(m,n))-v_p(g)=\max(\alpha,\beta)-\min(\alpha,\beta).
\]
Without loss of generality $\alpha\le\beta$, so the new pair of valuations is $(\alpha,\beta-\alpha)$. Then
\[
\gcd(\alpha,\beta-\alpha)=\gcd(\alpha,\beta),
\]
as required. (The case $\beta\le\alpha$ is symmetric.)
