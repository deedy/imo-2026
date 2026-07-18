# Lemma: two elementary square-root estimates

**(E1)** For all real $u$ with $-1\le u\le 3$: $\sqrt{1+u}\ \ge\ 1+\dfrac u2-\dfrac{u^2}2$.

*Proof.* If the right-hand side is negative the claim is trivial ($\sqrt{1+u}\ge0$).
Otherwise both sides are nonnegative and squaring is an equivalence. Expanding,
$$(1+u)-\Bigl(1+\tfrac u2-\tfrac{u^2}2\Bigr)^2
=\tfrac34u^2+\tfrac12u^3-\tfrac14u^4
=-\tfrac{u^2}{4}(u-3)(u+1)\ \ge\ 0 \quad\text{for } -1\le u\le 3. \qquad\blacksquare$$
(Expansion checked symbolically/exactly in `code/verify.py` and exact-rational tests.)

**(E2)** For $A>0$ and $B\ge0$: $\sqrt{A^2+B}\ \le\ A+\dfrac{B}{2A}$.

*Proof.* Both sides positive; $\Bigl(A+\tfrac{B}{2A}\Bigr)^2=A^2+B+\tfrac{B^2}{4A^2}\ge A^2+B$. $\blacksquare$

**Auxiliary identity used in Step 3 of the main proof:**
$2x^2+2(x+\varepsilon)^2=(2x+\varepsilon)^2+\varepsilon^2$ — immediate by expansion
(both sides equal $4x^2+4\varepsilon x+2\varepsilon^2$).
