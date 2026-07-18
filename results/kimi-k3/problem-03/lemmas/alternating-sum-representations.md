# Lemma: two representations of the alternating sum $D$

For a multiset $M=\{p_1\ge\dots\ge p_m\}$ of positive reals, $D(M)=\sum_i(-1)^{i+1}p_i$.

## (a) Odd-set identity
Let $N(t)=\#\{x\in M:x>t\}$ ($t\ge0$). Then
$$D(M)=\bigl|\{t\ge0:N(t)\text{ is odd}\}\bigr|.$$
**Proof.** For $t\in[p_{i+1},p_i)$ (with $p_{m+1}=0$), $N(t)=i$; ties give empty intervals. Hence the odd set has measure $\sum_{i\text{ odd}}(p_i-p_{i+1})=D(M)$. $\blacksquare$

## (b) Matching formula
For a matching $\mu$ of $M$ (a set of disjoint unordered pairs; elements may be unpaired) define
$\operatorname{cost}(\mu)=\sum_{\{x,y\}\in\mu}|x-y|+\sum_{z\text{ unmatched}}z$. Then
$$D(M)=\min_\mu\operatorname{cost}(\mu).$$
**Proof.** Write $|x-y|=\int_0^\infty\mathbf 1[\text{exactly one of }x,y>t]dt$ and $z=\int_0^\infty\mathbf 1[z>t]dt$, so $\operatorname{cost}(\mu)=\int_0^\infty c_\mu(t)dt$ where $c_\mu(t)$ = (# pairs split by level $t$) + (# unmatched $>t$). With $b(t)$ = # pairs with both elements $>t$, $N(t)=2b(t)+c_\mu(t)$, hence $c_\mu(t)\equiv N(t)\pmod2$ and $c_\mu(t)\ge\mathbf 1[N(t)\text{ odd}]$ pointwise. Integrate and use (a): $\operatorname{cost}(\mu)\ge D(M)$ for all $\mu$. The adjacent matching $(p_1,p_2),(p_3,p_4),\dots$ has cost $\sum_{i\text{ odd}}(p_i-p_{i+1})=D(M)$. $\blacksquare$

## (c) Parity cancellation
If $M$ contains two equal elements $x,x$ then $D(M)=D(M\setminus\{x,x\})$. In particular, if every value in $M$ has even multiplicity, $D(M)=0$.
**Proof.** The two copies of $x$ sit at adjacent positions $j,j+1$ in the decreasing order, contributing $(-1)^{j+1}x+(-1)^{j+2}x=0$; removing them shifts later terms by two positions, preserving signs. $\blacksquare$

**Verification.** `code/tests2.py::test_matching_formula` — 300 random multisets, exact rational agreement.
