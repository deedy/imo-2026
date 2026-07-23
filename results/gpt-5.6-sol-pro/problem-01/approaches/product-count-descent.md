# Product-and-count descent

## Idea
For a board state $(x_1,\ldots,x_{2026})$, let
\[
P=\prod_i x_i,\qquad K=\#\{i:x_i>1\}.
\]
If the selected entries are $m,n$ and $g=\gcd(m,n)$, then the product of the two selected entries changes from
\[
mn=g\,\operatorname{lcm}(m,n)
\]
to
\[
g\cdot\frac{\operatorname{lcm}(m,n)}g=\operatorname{lcm}(m,n)=\frac{mn}{g}.
\]
Thus the total product becomes $P/g$.

## Status
Successful.

## Details
If $g>1$, then $P$ strictly decreases. If $g=1$, the selected pair becomes $(1,mn)$, so $P$ stays fixed but $K$ decreases by one. In every move $K$ cannot increase, since two nonunit entries are replaced by at most two nonunit entries. Hence $(P,K)$ decreases lexicographically in every move (equivalently, $P+K$ strictly decreases: when $g>1$, $P$ decreases and $K$ does not increase; when $g=1$, $K$ decreases). Since these are positive integers, an infinite play is impossible.

A move is available exactly when $K\ge 2$. Also, replacing two nonunits can never produce two units: if $g=1$, the second output is $mn>1$; if $g>1$, the first output is $g>1$. Thus $K$ never becomes zero. Consequently a terminal board has $K=1$.
