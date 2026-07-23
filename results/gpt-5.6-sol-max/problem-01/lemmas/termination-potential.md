# Lemma: strict descent of the blackboard potential

## Statement
For a board of positive integers, let
\[
P=\prod_i x_i,\qquad r=\#\{i:x_i>1\},\qquad \Phi=P2^r.
\]
Every legal move in the problem strictly decreases the positive integer $\Phi$. Moreover, if the board has at least one nonunit before a sequence of legal moves, it has at least one nonunit afterward.

## Proof
Select $m,n>1$, and set $d=\gcd(m,n)$. Since
\[
\gcd(m,n)\operatorname{lcm}(m,n)=mn,
\]
the replacement pair has product $mn/d$, so the total product changes from $P$ to $P'=P/d$.

If $d=1$, the replacement pair is $(1,mn)$; hence $r'=r-1$ and $\Phi'=\Phi/2<\Phi$. If $d>1$, the first replacement entry is a nonunit and the second is a positive integer. Thus the selected two nonunits are replaced by at most two nonunits, so $r'\le r$. Consequently
\[
\Phi'=\frac Pd2^{r'}\le \frac1dP2^r<\Phi.
\]
This proves strict descent.

Finally, the product of the replacement pair equals $\operatorname{lcm}(m,n)>1$, so its two entries cannot both equal $1$. Thus a move always leaves at least one nonunit among the two selected positions, proving the last assertion. $\square$
