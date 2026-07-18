# Determinant factorization

## Statement
For $x,y,z,t\in\mathbb R$ such that $\sin(x+y)\sin(x+z)\ne0$, let
\[
 k=1+\frac{\sin x}{\sin(x+z)}e^{iz},\qquad
 l=2-te^{-i(x+y)},\qquad
 l=\lambda n,
\]
where
\[
 \lambda=1+\frac{\sin x}{\sin(x+y)}e^{-iy}.
\]
For complex numbers $u,v$, write $[u,v]=\operatorname{Im}(\bar u v)$. Set
\[
 Q=[k-2n,e^{i(x+z)}n]
\]
and
\[
 D=[k,l](|n|^2-1)-[k,n-1]|l|^2+[l,n-1]|k|^2.
\]
Then
\[
D=\frac{\sin x(t\sin x+\sin y)}{\sin(x+y)\sin(x+z)}Q.
\]

## Proof
Put $X=e^{ix}$, $Y=e^{iy}$, $Z=e^{iz}$. Use
\[
\sin\theta=\frac{e^{i\theta}-e^{-i\theta}}{2i},\qquad [u,v]=\frac{\bar u v-u\bar v}{2i}.
\]
The defining quantities become
\[
 k=\frac{2X^2Z^2-Z^2-1}{X^2Z^2-1},
\quad
 \lambda=\frac{X^2Y^2+X^2-2}{X^2Y^2-1},
\quad
 l=2-\frac{t}{XY},
\quad n=\frac l\lambda.
\]
Their conjugates are obtained by replacing $(X,Y,Z)$ with $(X^{-1},Y^{-1},Z^{-1})$ and leaving $t$ fixed. Substitution in the definitions of $D,Q$, multiplication by the common denominator, and collection according to the powers of $t$ yields the asserted identity.

**Open presentation issue:** The last sentence is exact but too terse for the desired rigor bar unless the resulting small coefficient table or a more conceptual derivation is included. This file is not yet ready for citation as a final lemma.
