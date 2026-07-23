# Complex determinant identity

## Statement
Let $\alpha,\beta,\gamma,t$ be real numbers such that
\[
\sin(\alpha+\beta)\sin(\alpha+\gamma)\ne0.
\]
Put $s=\alpha+\beta$, $r=\alpha+\gamma$, and
\[
 k=1-\frac{\sin\gamma}{2\sin r}e^{-i\alpha},\qquad
 g=1-\frac{\sin\beta}{2\sin s}e^{i\alpha},\qquad
 l=1-te^{-is},\qquad w=\frac l g.
\]
Then
\[
\begin{aligned}
&\frac1i\det\begin{pmatrix}
 |k|^2&k&\bar k\\
 |l|^2&l&\bar l\\
 \dfrac{1-|w|^2}{4}&\dfrac{1-w}{2}&\dfrac{1-\bar w}{2}
\end{pmatrix}\\[2mm]
&\qquad=\frac{\sin\alpha\,(2t\sin\alpha+\sin\beta)}
 {4\sin s\sin r}\,
 \Im\!\left((w-k)\bar w e^{-ir}\right).
\end{aligned}
\]

## Proof
This is an elementary algebraic identity. A compact derivation is still being prepared; direct expansion after replacing each exponential by its sine and cosine verifies both sides term by term, but the final write-up will include enough intermediate formulas to make the verification transparent.
