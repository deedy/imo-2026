# Lemma: Separation of zero and positive $c$

**Statement:** Under same hypotheses, let $p>0$ be common positive value (if exists).
If $a\in Q$, $b\in Z=\{c=0\}$, then $|a-b|\ge p$ and indeed
$(a-b)^2\ge p^2+2p(a+b)$. Consequently $Z,Q$ are $p$-separated and both open;
hence they cannot both be non-empty.

**Proof:** $P(a,b)$ with squared upper bound: $2a^2+2f(b)^2\ge(f(a)+b)^2$.
We have $f(b)=b$, $f(a)=a+p$, so $2a^2+2b^2\ge(a+b+p)^2$.
Expanding gives $(a-b)^2\ge p^2+2p(a+b)>p^2$.
Thus any $a\in Q$, $b\in Z$ are at distance $>p$. For $z\in Z$, the interval
$(z-p,z+p)\cap(0,\infty)$ cannot meet $Q$, so it lies in $Z$; $Z$ open. Similarly
$Q$ open. Since $(0,\infty)$ connected and $Z\sqcup Q=(0,\infty)$ when $c$ only
takes values $0,p$, one must be empty.
∎
