# Lemma: invariance of the gcd of prime-adic valuations

**Lemma.** Fix a prime $p$. For a board $(x_1,\dots,x_k)$ of positive integers, the quantity
\[
G_p=\gcd\bigl(v_p(x_1),\dots,v_p(x_k)\bigr)
\]
(where the gcd of an all-zero list is taken to be $0$) is invariant under the prescribed move.

**Proof.** Suppose the selected entries are $m,n$, and write $a=v_p(m)$ and $b=v_p(n)$. The corresponding valuations of the replacement entries are
\[
v_p(\gcd(m,n))=\min(a,b)
\]
and
\[
v_p\left(\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right)
=\max(a,b)-\min(a,b)=|a-b|.
\]
If, without loss of generality, $a\le b$, then
\[
\gcd(\min(a,b),|a-b|)=\gcd(a,b-a)=\gcd(a,b).
\]
Let $H$ denote the gcd of the valuations at all unchanged positions (with $H=0$ if there are no such positions). Before the move the gcd of every valuation is $\gcd(H,a,b)$; after it is
\[
\gcd(H,\min(a,b),|a-b|)=\gcd(H,a,b).
\]
Thus $G_p$ is unchanged. $\square$
