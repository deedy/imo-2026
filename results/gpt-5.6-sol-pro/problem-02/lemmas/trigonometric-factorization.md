# Trigonometric factorization lemma

## Statement
Let real angles $p,q,r,x,y,\delta$ have all denominators below nonzero, and suppose
\[
\cot x=\cot p+2\cot r,\qquad \cot y=\cot p+2\cot q.
\]
Set
\[
P=\frac{\sin p}{\sin(p+x)},\quad Q=\frac{\sin p}{\sin(p+y)},\quad
U=p+r+\delta+y,\quad V=p+q+\delta+x.
\]
Then
\[
\begin{aligned}
&Q\sin p\sin(\delta+r)\sin V-P\sin p\sin(\delta+q)\sin U\\
&\quad+2(P\sin y-Q\sin x)\sin(p+r)\sin(p+q)\\
&=\sin(x-y)\bigl(PQ\sin U\sin V-\sin(p+r)\sin(p+q)\bigr). \tag{L}
\end{aligned}
\]

## Proof
The cotangent hypotheses give
\[
P=\frac{\sin r}{2\sin(r-x)},\quad Q=\frac{\sin q}{2\sin(q-y)}, \tag{1}
\]
because, for example,
\[
\frac1P=\frac{\sin(p+x)}{\sin p}=\cos x+\cot p\sin x
=2\cos x-2\cot r\sin x=\frac{2\sin(r-x)}{\sin r}.
\]
They also give
\[
\frac{\sin(p+r)}{\sin p}=\frac{\sin(r-x)}{\sin x},\qquad
\frac{\sin(p+q)}{\sin p}=\frac{\sin(q-y)}{\sin y}. \tag{2}
\]
Indeed, the first equality follows by expanding both sides and using
$\cot p=\cot x-2\cot r$; the second is analogous.

We need the auxiliary identity
\[
[2(P\sin y-Q\sin x)+\sin(x-y)]\sin(p+r)\sin(p+q)
=\sin ^2p\sin(q+x-r-y). \tag{3}
\]
By (1), after putting the left bracket over the common denominator
$\sin(r-x)\sin(q-y)$, its numerator is
\[
\begin{aligned}
S={}&\sin r\sin y\sin(q-y)-\sin q\sin x\sin(r-x)\\
&+\sin(x-y)\sin(r-x)\sin(q-y).
\end{aligned}
\]
The elementary identity
\[
S=\sin x\sin y\sin(q+x-r-y) \tag{4}
\]
follows by expanding $\sin r=\sin(r-x)\cos x+\cos(r-x)\sin x$ and
$\sin q=\sin(q-y)\cos y+\cos(q-y)\sin y$: after cancellation and division by $\sin x\sin y$, what remains is precisely the sine subtraction formula for
$\sin((q-y)-(r-x))$. Thus (1), (2), and (4) prove (3).

It remains to prove (L). Apply
$2\sin a\sin b=\cos(a-b)-\cos(a+b)$ to its products depending on $\delta$. Both sides are sums of a constant and harmonics $e^{\pm2i\delta}$. Equality of the $e^{2i\delta}$ coefficients is equivalent to
\[
\frac{\sin p}{P}e^{-i(p+y)}-\frac{\sin p}{Q}e^{-i(p+x)}=\sin(x-y). \tag{5}
\]
Since $\sin p/P=\sin(p+x)$ and $\sin p/Q=\sin(p+y)$, the left side of (5) is
\[
\sin(p+x)e^{-i(p+y)}-\sin(p+y)e^{-i(p+x)}=\sin(x-y);
\]
the last equality follows immediately by writing each sine in exponential form. Conjugation gives equality of the $e^{-2i\delta}$ coefficients.

Finally, product-to-sum expansion of the constant terms reduces their equality to (3). (Explicitly, the constant part of the difference between the left and right sides of (L) is the left side of (3) minus its right side.) Hence all three coefficients agree, proving (L).
