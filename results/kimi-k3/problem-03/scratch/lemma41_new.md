**Lemma 4.1 (realizability lemma).** *Let $P,N$ be disjoint finite multisets of positive reals, with sums $\Sigma P,\Sigma N$, and $P\cup N\ne\emptyset$.*
- *(a) If $\Sigma P=\Sigma N$, then some ordering of $P\cup N$ has nested absolute difference $0$.*
- *(b) If $v:=\Sigma P-\Sigma N>0$ and no subset of $P\cup N$ has sum strictly between $\Sigma N$ and $\Sigma P$, then some ordering of $P\cup N$ has nested absolute difference $v$.*

*Proof.* We construct an ordering $e_1,\dots,e_r$ of $P\cup N$ by a greedy process. Set $E_0=0$. At step $k$, while elements remain: if $E_{k-1}>0$, append any remaining element $e_k\in N$ and put $E_k=E_{k-1}-e_k$; if $E_{k-1}<0$, append any remaining element $e_k\in P$ and put $E_k=E_{k-1}+e_k$; if $E_{k-1}=0$, append any remaining element from either (nonempty) side, with the corresponding sign.

We claim this process never gets stuck, i.e. the side it must draw from is never empty while the other side is nonempty. Indeed, suppose the process halts with a remaining part $P'\subseteq P$ and $N'\subseteq N$, not both empty, and let $I\subseteq P$ and $J\subseteq N$ be the parts already processed, so the current signed sum is $E=\Sigma I-\Sigma J$.

- *Halt with $E>0$:* this requires $N$ exhausted ($J=N$) and $P'\ne\emptyset$. Then $E=\Sigma I-\Sigma N>0$, so $\Sigma I>\Sigma N$, while $\Sigma I=\Sigma P-\Sigma P'<\Sigma P$ (as $P'\ne\emptyset$ and all elements are positive). Hence $\Sigma I$ lies strictly between $\Sigma N$ and $\Sigma P$: impossible — in case (b) by the hypothesis, and in case (a) because $\Sigma I\le\Sigma P=\Sigma N$ would give $E\le0$.
- *Halt with $E<0$:* this requires $P$ exhausted ($I=P$) and $N'\ne\emptyset$. Then the full signed sum is $\Sigma P-\Sigma N=E-\Sigma N'<0$, contradicting $\Sigma P-\Sigma N=v>0$ in case (b) and $\Sigma P-\Sigma N=0$ in case (a).
- *Halt with $E=0$:* then both sides are empty (at $E=0$ either nonempty side may be drawn from), so nothing remains — the process is finished, not stuck.

Hence the process consumes all of $P\cup N$ and ends at $E_r=\Sigma P-\Sigma N$.

Finally we check that the nested absolute difference of the ordering $e_1,\dots,e_r$ equals $|E_r|$. Define $R_1=e_1$ and $R_k=|R_{k-1}-e_k|$; we claim $R_k=|E_k|$ for all $k$. This holds for $k=1$ since $E_1=\pm e_1$. Inductively: if $E_{k-1}\ge0$ and $e_k\in N$, then $E_k=E_{k-1}-e_k$ and $|E_k|=\big||E_{k-1}|-e_k\big|=|R_{k-1}-e_k|=R_k$; if $E_{k-1}<0$ and $e_k\in P$, then $E_k=-|E_{k-1}|+e_k$ and again $|E_k|=\big||E_{k-1}|-e_k\big|=R_k$; if $E_{k-1}=0$ then $|E_k|=e_k=|0-e_k|=R_k$. Thus the chain value is $R_r=|E_r|=|\Sigma P-\Sigma N|$, which is $0$ in case (a) and $v$ in case (b). $\blacksquare$
