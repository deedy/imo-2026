# Lemma: finitely many primes occur in minimal supports

## Statement
In the notation of the self-blocking support-family lemma, let $m=a_1$ and let $\mathcal H$ be the inclusion-minimal members of $\mathcal F$. Then
\[
\bigcup_{H\in\mathcal H}H
\]
is finite.

## Proof
First note the scanning property: if $x>m$ is not a term, then some earlier term is coprime to $x$. Indeed, place $x$ strictly between two consecutive terms and use the minimality of the latter.

Fix $p\in H\in\mathcal H$ and define
\[
c(H,p)=\prod_{q\in H\setminus\{p\}}q.
\]
If $c(H,p)>m$, put $D=H\setminus\{p\}$ and $x=c(H,p)$. Since $D$ is a proper subset of the minimal member $H$, it is not in $\mathcal F$ and hence, by $\mathcal F=\mathcal G$, $x$ is not a term. There is an earlier term $y<x$ with $P(y)\cap D=\varnothing$. Choose a minimal member $K\in\mathcal H$ contained in $P(y)$. Since $K$ and $H$ intersect but $K$ is disjoint from $D$, we have $p\in K$. Also
\[
c(K,p)\le y/p<x=c(H,p).
\]
Integer descent therefore yields, for every relevant $p$, some $H\ni p$ with $c(H,p)\le m$.

Only finitely many prime sets $C$ satisfy $\prod_{q\in C}q\le m$. Every relevant $p$ has $C\cup\{p\}\in\mathcal H$ for one such $C$, with $p\notin C$. Fix $C$. If it occurs, then $C\notin\mathcal F$ by minimality. Self-blocking gives a finite $F_C\in\mathcal F$ disjoint from $C$. Whenever $C\cup\{p\}\in\mathcal H$, intersection of this set with $F_C$ forces $p\in F_C$. Hence only finitely many $p$ correspond to each $C$. Since there are finitely many $C$, the union of the minimal members is finite. ∎