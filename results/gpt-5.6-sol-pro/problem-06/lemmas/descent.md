# Multiplicative descent for minimal accepted supports

## Statement
Let $\mathcal F$ be the accepted support family and $\mathcal C$ its inclusion-minimal members. For a finite prime set $S$, put $w(S)=\prod_{q\in S}q$, with $w(\varnothing)=1$. If $E\in\mathcal C$, $p\in E$, and $w(E\setminus\{p\})\ge a_1$, then there exists $H\in\mathcal C$ such that
\[
p\in H,\qquad w(H)<w(E\setminus\{p\}).
\]
Consequently, for every $E\in\mathcal C$ and every $p\in E$, there is a $D\in\mathcal C$ containing $p$ such that $w(D\setminus\{p\})<a_1$.

## Proof
Set $S=E\setminus\{p\}$. Since $E$ is inclusion-minimal in $\mathcal F$, we have $S\notin\mathcal F$. The squarefree integer $w(S)$ is at least $a_1$ and has support $S$, so it was rejected in the greedy scan. Hence some accepted integer $y<w(S)$ is coprime to $w(S)$. Its support belongs to $\mathcal F$ and therefore contains some $H\in\mathcal C$.

Now $H\cap S=\varnothing$. On the other hand, $H$ and $E$ are two members of the intersecting family $\mathcal C$, so $H\cap E\ne\varnothing$. As $E=S\cup\{p\}$, this forces $p\in H$. Moreover,
\[
w(H)\le \prod_{q\mid y}q\le y<w(S),
\]
as required.

Starting with $E$ and repeatedly applying the first part while the product obtained by removing $p$ is at least $a_1$ produces members of $\mathcal C$ that all contain $p$ and whose positive integer weights strictly decrease. Thus the process terminates, and its terminal member $D$ has $w(D\setminus\{p\})<a_1$.
