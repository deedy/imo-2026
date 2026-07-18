# Lemma (realizability): greedy scheduling for nested absolute differences

For a nonempty multiset $B=\{b_1\ge\dots\ge b_r\}$ of positive reals, the *chain value* (nested absolute difference) of an ordering $(e_1,\dots,e_r)$ is $\bigl|\dots\bigl||e_1-e_2\bigr|-e_3\bigr|-\dots-e_r\bigr|$.

**Statement.** Let $P,N$ be disjoint finite multisets of positive reals, $P\cup N\ne\emptyset$, with sums $\Sigma P,\Sigma N$.
- **(a)** If $\Sigma P=\Sigma N$, some ordering of $P\cup N$ has chain value $0$.
- **(b)** If $v:=\Sigma P-\Sigma N>0$ and no subset of $P\cup N$ has sum strictly between $\Sigma N$ and $\Sigma P$, then some ordering of $P\cup N$ has chain value $v$.

**Proof.** Greedy process: $E_0:=0$; while elements remain, if $E_{k-1}>0$ append any remaining $e_k\in N$ ($E_k:=E_{k-1}-e_k$); if $E_{k-1}<0$ append any remaining $e_k\in P$ ($E_k:=E_{k-1}+e_k$); if $E_{k-1}=0$ append any remaining element of either side (with its sign).

*Never stuck.* Suppose the process halts with unprocessed remainders $P'\subseteq P$, $N'\subseteq N$ (not both empty) and processed parts $I\subseteq P$, $J\subseteq N$; current sum $E=\Sigma I-\Sigma J$.
- Halt with $E>0$: forces $J=N$, $P'\ne\emptyset$; then $\Sigma I>\Sigma N$ and $\Sigma I=\Sigma P-\Sigma P'<\Sigma P$, so $\Sigma I$ lies strictly between $\Sigma N$ and $\Sigma P$ — impossible: in (b) by hypothesis; in (a) since $\Sigma I\le\Sigma P=\Sigma N$ would force $E\le0$.
- Halt with $E<0$: forces $I=P$, $N'\ne\emptyset$; then $\Sigma P-\Sigma N=E-\Sigma N'<0$, contradicting $\Sigma P-\Sigma N>0$ in (b), $=0$ in (a).
- Halt with $E=0$: at $E=0$ either nonempty side may be drawn, so both sides must be empty — finished, not stuck.

So the process consumes all elements, ending at $E_r=\Sigma P-\Sigma N$.

*Chain value $=|E_r|$.* Let $R_1=e_1$, $R_k=|R_{k-1}-e_k|$; claim $R_k=|E_k|$. $k=1$: $E_1=\pm e_1$. Step: $E_{k-1}\ge0$, $e_k\in N$: $|E_k|=|E_{k-1}-e_k|=\big||E_{k-1}|-e_k\big|=R_k$; $E_{k-1}<0$, $e_k\in P$: $|E_k|=\big|{-}|E_{k-1}|+e_k\big|=\big||E_{k-1}|-e_k\big|=R_k$; $E_{k-1}=0$: $|E_k|=e_k=R_k$. Hence chain value $R_r=|E_r|=|\Sigma P-\Sigma N|$, i.e. $0$ in (a), $v$ in (b). $\blacksquare$

**Remarks.** The greedy rule's freedom (any element of the required side) is essential to the proof; not every signing is realizable (e.g. $P=\{5,5\},N=\{1\}$, $v=9$ is not a chain value), so the adjacency hypothesis in (b) cannot be dropped in general — it holds exactly because of where the pigeonhole places the gap (see `chain-theorem.md`).

**Verification.** `code/agr.py` — every adjacent gap of every tested family (180 families, $m=3,4,5$) is chain-realizable; greedy rule checked on targeted instances.
