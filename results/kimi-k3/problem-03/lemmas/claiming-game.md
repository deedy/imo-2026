# Lemma: value of the claiming game

**Statement.** In the claiming game played on a multiset $M$ of positive reals (players alternately take any remaining element, Liu Bang first, each maximising his own total), Liu Bang can guarantee at least $\operatorname{odd}(M)$ and Xiang Yu can guarantee at least $\operatorname{even}(M)$, where $M=\{p_1\ge p_2\ge\dots\ge p_m\}$ and $\operatorname{odd}(M)=\sum_{i\text{ odd}}p_i$, $\operatorname{even}(M)=\sum_{i\text{ even}}p_i$. Hence, as $\operatorname{odd}+\operatorname{even}=\sum M$, under optimal play Liu Bang obtains exactly $\operatorname{odd}(M)=\frac{\sum M + D(M)}{2}$ with $D(M)=\sum_i(-1)^{i+1}p_i$.

**Proof.** Induction on $|M|$. $|M|=1$ trivial. Let $|M|\ge2$.

*Liu Bang's guarantee.* LB takes $p_1$; suppose XY takes $p_j$ ($j\ge2$). On $M'=M\setminus\{p_1,p_j\}$ LB moves first and, by induction, gets $\ge\operatorname{odd}(M')$. The sorted order of $M'$ is $p_2,\dots,p_{j-1},p_{j+1},\dots$, so its odd-indexed elements are $\{p_i:i\text{ even},i<j\}\cup\{p_i:i\text{ odd},i>j\}$. Thus
$$\text{LB total}\;\ge\;p_1+\sum_{\substack{i\text{ even}\\i<j}}p_i+\sum_{\substack{i\text{ odd}\\i>j}}p_i
=\operatorname{odd}(M)+\Big(\sum_{\substack{i\text{ even}\\i<j}}p_i-\sum_{\substack{i\text{ odd}\\3\le i\le j}}p_i\Big),$$
and the bracket is a sum of consecutive differences $(p_2-p_3)+(p_4-p_5)+\dots\ge0$ (it ends at $\pm p_{j-1}$ if $j$ even, $\pm p_j$ if $j$ odd).

*Xiang Yu's guarantee.* LB takes some $p_j$; XY takes a largest remaining piece $\ell$ ($=p_1$ if $j\ne1$, else $p_2$), then moves first on $M''=M\setminus\{p_j,\ell\}$ and by induction gets $\ge\operatorname{odd}(M'')$.
If $j=1$: XY total $\ge p_2+\sum_{i\text{ odd}\ge3}p_i=\operatorname{even}(M)+\sum_{i\text{ odd}\ge3}(p_i-p_{i+1})\ge\operatorname{even}(M)$.
If $j\ge2$: XY total $\ge p_1+\operatorname{odd}(M\setminus\{p_1,p_j\})\ge\operatorname{odd}(M)\ge\operatorname{even}(M)$ by the same computation as above and $D(M)=\operatorname{odd}-\operatorname{even}\ge0$ (telescoping pairs). $\blacksquare$

**Consequence (reduction of the IMO game).** With all piece lengths summing to $1$, LB's share under optimal claiming is $\frac{1+D(M)}2$. So the game is: LB chooses a composition of $1$ into $m\le n+1$ parts; XY refines it with $\le n$ further cuts; payoff to LB is $\frac{1+D}2$.

**Verification.** `code/game.py` (`pick_value` brute-force vs. alternating-sum formula) — exact agreement on all small multisets.
