# Approach: arithmetic orbits and a forbidden interval

## Status
Successful; this is the second half of the final proof.

## Idea
From $f(f(t))=2f(t)-t$, forward iterates form an arithmetic progression:
\[
f^{[n]}(t)=t+n(f(t)-t).
\]
Since all iterates must remain positive, $p(t)=f(t)-t$ cannot be negative. If $p(t)=c>0$, one can descend by subtracting $c$ until reaching $r\in(0,c]$ with the same increment; then the whole orbit $r+nc$ has increment $c$.

To prove $p$ is constant, suppose it takes values $c>d\ge0$. For a $d$-increment point $y$, the left original inequality restricts a $c$-increment point $X$ by
\[
2(X^2+(y+d)^2)\ge (X+c+y)^2.
\]
As a quadratic in $X$, this fails exactly on an open interval centered at $c+y$ with half-length
\[
s=\sqrt{2(c-d)(c+d+2y)}.
\]
By replacing $y$ with a large forward iterate when $d>0$ (and by a direct check when $d=0$), we can make $2s>c$. The $c$-orbit $r+nc$ starts at $r\le c$, below the top of this interval, and has step smaller than the interval length; hence it must land inside the forbidden interval, contradiction.

## Outcome
This proves $p(t)$ is constant. The verification that $f(t)=t+c$ works is then immediate from QM-AM-GM. Full details are in `lemmas/iterate-positivity.md`, `lemmas/descent.md`, and `lemmas/constancy.md`.
