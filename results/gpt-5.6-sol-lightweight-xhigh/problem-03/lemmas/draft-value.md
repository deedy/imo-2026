# Lemma: value of the claiming stage

## Statement
Let pieces of total length $T$ have lengths
\[
x_1\ge x_2\ge\cdots\ge x_k\ge0.
\]
If two players alternately claim one remaining piece, with the first player moving first, then under optimal play the difference
\[
(\text{first player's total})-(\text{second player's total})
\]
is
\[
D(x_1,\ldots,x_k)=x_1-x_2+x_3-x_4+\cdots.
\]
Consequently, the first player's total is $(T+D)/2$.

## Proof
For a finite multiset $X$, let $V(X)$ be the optimal difference between the total of the player whose turn it is and the other player's total, counting only the pieces in $X$. Zero-sum backward induction gives
\[
V(X)=\max_{x\in X}\bigl(x-V(X\setminus\{x\})\bigr).
\]
We prove the claimed formula by induction on $|X|$. It is immediate when $X$ is empty. Assume it for all multisets of fewer than $k$ elements, and write $X=(x_1,\ldots,x_k)$ in nonincreasing order. If the current player chooses $x_1$, the induction hypothesis gives
\[
x_1-V(X\setminus\{x_1\})
=x_1-(x_2-x_3+x_4-\cdots)=D(X).
\]
It remains to show that choosing any $x_j$ gives no larger value. By the induction hypothesis this value is $x_j-D(X\setminus\{x_j\})$. Direct cancellation gives
\[
D(X)-\bigl(x_j-D(X\setminus\{x_j\})\bigr)
=
\begin{cases}
2\bigl((x_1-x_2)+\cdots +(x_{j-2}-x_{j-1})\bigr),&j\text{ odd},\\[2mm]
2\bigl((x_1-x_2)+\cdots +(x_{j-3}-x_{j-2})+(x_{j-1}-x_j)\bigr),&j\text{ even}.
\end{cases}
\]
(An empty sum is $0$.) Every parenthesis on the right is nonnegative, so the choice $x_1$ is optimal and $V(X)=D(X)$.

The two players' totals sum to $T$ and differ by $D$, proving that the first player's total is $(T+D)/2$. ∎
