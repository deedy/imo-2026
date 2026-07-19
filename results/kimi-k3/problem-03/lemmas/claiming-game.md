# Lemma: value of the claiming game

**Statement.** In the claiming game played on a multiset $M=\{p_1\ge p_2\ge\dots\ge p_m\}$ of positive reals (two players alternately take any remaining element, each maximising his own total), the **first player** can guarantee at least $\operatorname{odd}(M)=\sum_{i\text{ odd}}p_i$ and the **second player** can guarantee at least $\operatorname{even}(M)=\sum_{i\text{ even}}p_i$. Since $\operatorname{odd}+\operatorname{even}=\sum M$, under optimal play the first player obtains exactly $\operatorname{odd}(M)=\frac{\sum M + D(M)}{2}$ and the second exactly $\operatorname{even}(M)$, where $D(M)=\sum_i(-1)^{i+1}p_i$. In the IMO game Liu Bang moves first, so he obtains exactly $\operatorname{odd}(M)$.

**Proof.** Induction on $m=|M|$. $m=1$: first player takes $p_1=\operatorname{odd}(M)$, second gets $0=\operatorname{even}(M)$. Let $m\ge2$.

*First player's guarantee.* FP takes $p_1$; suppose SP takes $p_j$ ($j\ge2$). On $M'=M\setminus\{p_1,p_j\}$ FP moves first and by induction secures $\ge\operatorname{odd}(M')$ there. The sorted order of $M'$ is $p_2,\dots,p_{j-1},p_{j+1},\dots,p_m$; its odd-indexed elements are $\{p_i:i\text{ even},\,2\le i\le j-1\}\cup\{p_i:i\text{ odd},\,i\ge j+1\}$. Hence
$$\bigl(p_1+\operatorname{odd}(M')\bigr)-\operatorname{odd}(M)=\sum_{\substack{i\text{ even}\\2\le i\le j-1}}p_i-\sum_{\substack{i\text{ odd}\\3\le i\le j}}p_i=(p_2-p_3)+(p_4-p_5)+\dots\ge0,$$
ending with $(p_{j-2}-p_{j-1})$ for $j$ even, $(p_{j-1}-p_j)$ for $j$ odd (empty for $j=2$).

*Second player's guarantee.* FP takes some $p_j$; SP takes a largest remaining piece $\ell$ ($=p_1$ if $j\ge2$, else $p_2$). On $M''=M\setminus\{p_j,\ell\}$ it is FP's turn, so SP is the **second** player there and by induction secures $\ge\operatorname{even}(M'')$ — total $\ge\ell+\operatorname{even}(M'')$. (This parity assignment is the delicate point: SP does *not* get $\operatorname{odd}(M'')$.)

- If $j=1$: $M''=\{p_3,\dots,p_m\}$, even-indexed elements $p_4,p_6,\dots$, so $\ell+\operatorname{even}(M'')=p_2+p_4+p_6+\dots=\operatorname{even}(M)$.
- If $j\ge2$: $M''=M\setminus\{p_1,p_j\}$ has even-indexed elements $\{p_i:i\text{ odd},\,3\le i\le j-1\}\cup\{p_i:i\text{ even},\,i\ge j+1\}$, so
$$\bigl(\ell+\operatorname{even}(M'')\bigr)-\operatorname{even}(M)=p_1+\sum_{\substack{i\text{ odd}\\3\le i\le j-1}}p_i-\sum_{\substack{i\text{ even}\\2\le i\le j}}p_i=(p_1-p_2)+(p_3-p_4)+\dots\ge0,$$
ending with $(p_{j-1}-p_j)$ for $j$ even, $(p_{j-2}-p_{j-1})$ for $j$ odd ($=p_1-p_2$ for $j=2$). $\blacksquare$

**Sanity example.** $M=\{3,2,1\}$: $\operatorname{odd}(M)=4$, $\operatorname{even}(M)=2$. FP takes $3$, SP takes $2$, FP takes $1$: FP gets $4$, SP gets $2$ — the value is exact. (The false claim "SP gets $\ell+\operatorname{odd}(M'')$" would give $2+1=3$ here; the correct claim is $\ell+\operatorname{even}(M'')=2+0=2$.)

**Consequence (reduction of the IMO game).** With all piece lengths summing to $1$, LB's share under optimal claiming is $\frac{1+D(M)}2$. So the game is: LB chooses a composition of $1$ into $m\le n+1$ parts; XY refines it with $\le n$ further cuts; payoff to LB is $\frac{1+D}2$.

**Verification.** `code/game.py` (`pick_value` brute-force vs. alternating-sum formula) and `code/lemma11_check.py` (exact minimax = $(\operatorname{odd}(M),\operatorname{even}(M))$ on 304 multisets, incl. $\{3,2,1\}$) — exact agreement.
