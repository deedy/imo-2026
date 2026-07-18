# Lemma: alternating discrepancy and pairing cost

## Statement
For nonnegative numbers $x_1\ge\cdots\ge x_k$, put
\[
D=x_1-x_2+x_3-x_4+\cdots.
\]
If $k$ is even, $D$ is the minimum, over all partitions of the numbers into pairs, of the sum of the absolute differences within the pairs. If $k$ is odd, $D$ is the minimum, over all partitions into pairs and one singleton, of the sum of the pairwise absolute differences plus the value of the singleton.

In particular, if a multiset consists of some prescribed equal pairs together with further numbers of total sum at most $\delta$, then its alternating discrepancy is at most $\delta$.

## Proof
First suppose there are $2r$ numbers. We show that a minimum-cost perfect pairing can pair $x_1$ with $x_2$. In any pairing in which they are not paired together, suppose the two relevant pairs are $(x_1,x_j)$ and $(x_2,x_\ell)$, where $j,\ell\ge3$. Replacing them by $(x_1,x_2)$ and $(x_j,x_\ell)$ does not increase the cost. Indeed, if $\ell<j$, the old cost minus the new cost is
\[
(x_1-x_j+x_2-x_\ell)-(x_1-x_2+x_\ell-x_j)=2(x_2-x_\ell)\ge0;
\]
if $j<\ell$, it is similarly $2(x_2-x_j)\ge0$. Induction on $r$ therefore shows that pairing adjacent terms is optimal. Its cost is
\[
(x_1-x_2)+(x_3-x_4)+\cdots +(x_{2r-1}-x_{2r})=D.
\]

For $2r+1$ numbers, append one additional number $0$. Pairing one of the original numbers with $0$ is exactly the same as declaring it the singleton and charging its value. The even case applied to
\[
x_1\ge\cdots\ge x_{2r+1}\ge0
\]
shows that the minimum cost is
\[
(x_1-x_2)+\cdots +(x_{2r+1}-0)=D.
\]

For the final assertion, retain all prescribed equal pairs, pair the further numbers arbitrarily, and leave one of them as a singleton if necessary. The equal pairs cost $0$, while for nonnegative $u,v$ one has $|u-v|\le u+v$; hence the total cost is at most the sum of the further numbers, which is at most $\delta$. The minimum-cost characterization gives $D\le\delta$. ∎
