# imo-2026-06 — tracking file
## Status
solved

## Problem
Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i)>1$ for every $i=1,2,\ldots,n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T}=a_n+L$ for every positive integer $n$. (Note that $\gcd(x,y)$ denotes the greatest common divisor of positive integers $x$ and $y$.)

## Approaches tried
- Recast the recurrence as a greedy scan of all integers from $a_1$ onward. An integer is accepted precisely when it is noncoprime to every previously accepted integer; rejected integers have smaller accepted coprime witnesses.
- Passed to finite sets of prime divisors. Acceptance depends only on the prime support, and the family $\mathcal F$ of accepted supports is self-dual: $S\in\mathcal F$ exactly when $S$ meets every member of $\mathcal F$.
- Considered projection to the finitely many primes dividing $a_1$. This gave restrictions on support types but did not by itself control auxiliary primes.
- Considered proving eventual periodicity from the descending periodic conditions imposed by finite prefixes. Such conditions need not visibly stabilize, so this route did not resolve the core issue.
- Used the inclusion-minimal accepted supports $\mathcal C$ and multiplicative weight $w(S)=\prod_{p\in S}p$. Removing one prime from a minimal support produces a rejected support; its smaller coprime witness yields a strict weight descent to a bounded-size minimal support containing the chosen prime.
- Proved, via the infinite sunflower lemma and self-duality, that there are only finitely many minimal supports of any fixed bounded size. The descent then shows that only finitely many primes occur in all minimal supports, so acceptance is periodic modulo their product.

## Current best
The sequence is globally translation-periodic. Let $\mathcal C$ be the family of inclusion-minimal prime supports of accepted integers. The proof below shows that $\mathcal C$ is finite. If $P=\bigcup_{C\in\mathcal C}C$ and $L=\prod_{p\in P}p$, then an integer $m\ge a_1$ is a term of the sequence exactly when its prime support contains some $C\in\mathcal C$; hence this status is periodic modulo $L$. Taking $T$ to be the number of accepted residue classes modulo $L$ gives $a_{n+T}=a_n+L$ for every $n$.

## Full proof
We first reinterpret the construction. Starting with $a_1$, scan the integers $a_1+1,a_1+2,\ldots$ in increasing order, accepting an integer if and only if it has greatest common divisor greater than $1$ with every integer accepted earlier. The accepted integers, in increasing order, are exactly $a_1,a_2,\ldots$. Indeed, this is precisely the minimality condition in the definition of $a_{n+1}$.

Consequently:

1. any two accepted integers are noncoprime; and
2. every rejected integer $x>a_1$ has a smaller accepted integer coprime to it.

For a positive integer $x>1$, write
\[
\operatorname{supp}(x)=\{p:p\text{ is prime and }p\mid x\}.
\]
We claim that, among integers at least $a_1$, acceptance depends only on the support. Suppose $a_1\le x<y$ and $\operatorname{supp}(x)=\operatorname{supp}(y)$. If $x$ is rejected, it has a smaller accepted coprime witness, which is then also coprime to $y$; hence $y$ is rejected. If $x$ is accepted, every accepted integer smaller than $y$ is noncoprime to $x$, because accepted integers are pairwise noncoprime. Having the same support as $x$, the integer $y$ is therefore noncoprime to every earlier accepted integer, so $y$ is accepted. This proves the claim.

Every nonempty finite set of primes is the support of arbitrarily large integers. We may therefore define $\mathcal F$ to be the family of nonempty finite prime sets whose integers of sufficiently large size (equivalently, all such integers at least $a_1$) are accepted. We have the following self-duality property:
\[
S\in\mathcal F
\quad\Longleftrightarrow\quad
S\cap R\ne\varnothing\text{ for every }R\in\mathcal F.
\tag{1}
\]
For the forward implication, choose accepted integers with supports $S$ and $R$ and use pairwise noncoprimality. Conversely, if $S$ meets every member of $\mathcal F$, choose an integer $x\ge a_1$ with support $S$. Every accepted integer smaller than $x$ has support in $\mathcal F$, and thus is noncoprime to $x$. Hence the greedy scan accepts $x$, proving $S\in\mathcal F$.

Let $\mathcal C$ be the collection of inclusion-minimal members of $\mathcal F$. Every member of $\mathcal F$ contains a member of $\mathcal C$, because it is a finite set. Thus $\mathcal C$ is an intersecting antichain, and
\[
S\in\mathcal F
\quad\Longleftrightarrow\quad
S\text{ contains some }C\in\mathcal C.
\tag{2}
\]
We will prove that $\mathcal C$ is finite.

We need first a bounded-size finiteness lemma.

**Lemma 1.** For every positive integer $K$, there are only finitely many $C\in\mathcal C$ such that $|C|\le K$.

**Proof.** Suppose instead that there are infinitely many such members. We use the following elementary infinite sunflower fact: every infinite family of distinct sets of cardinality at most $K$ has an infinite subfamily $C_1,C_2,\ldots$ for which there is a fixed set $R$ satisfying
\[
C_i\cap C_j=R\qquad(i\ne j).
\tag{3}
\]
For completeness, this fact follows by induction on $K$. If some element occurs in infinitely many sets, restrict to those sets, delete that element, and apply the induction hypothesis. If every element occurs only finitely many times, one can greedily choose infinitely many pairwise disjoint sets, giving $R=\varnothing$.

Apply the fact to the assumed infinite bounded-size subfamily of $\mathcal C$. The petals $C_i\setminus R$ are pairwise disjoint. Fix any $H\in\mathcal C$. Since $\mathcal C$ is intersecting, $H$ meets every $C_i$. If $H$ were disjoint from $R$, the finite set $H$ would have to meet every one of the infinitely many pairwise disjoint petals, which is impossible. Thus every $H\in\mathcal C$ meets $R$. Since $\mathcal C$ is nonempty, this also shows that $R$ is nonempty.

Every member of $\mathcal F$ contains a member of $\mathcal C$, so $R$ meets every member of $\mathcal F$. By (1), $R\in\mathcal F$. Hence $R$ contains some $H_0\in\mathcal C$. But
\[
H_0\subseteq R\subseteq C_i
\]
for every $i$. Since $H_0$ and $C_i$ belong to the antichain $\mathcal C$, this forces $H_0=C_i$ for every $i$, contradicting the distinctness of the $C_i$. This proves Lemma 1. $\square$

For a finite set $S$ of primes, define
\[
w(S)=\prod_{p\in S}p,
\]
with $w(\varnothing)=1$.

**Lemma 2.** If $C\in\mathcal C$ and $p\in C$, then there is a $D\in\mathcal C$ such that
\[
p\in D
\qquad\text{and}\qquad
w(D\setminus\{p\})<a_1.
\tag{4}
\]

**Proof.** We first establish a descent step. Let $E\in\mathcal C$, let $p\in E$, and suppose
\[
w(E\setminus\{p\})\ge a_1.
\]
Set $S=E\setminus\{p\}$. By the inclusion-minimality of $E$, we have $S\notin\mathcal F$. The squarefree integer $w(S)$ has support $S$, is at least $a_1$, and is therefore rejected. In fact it is greater than $a_1$, since $a_1$ itself is accepted. Hence there exists an accepted integer $y<w(S)$ coprime to $w(S)$. The support of $y$ lies in $\mathcal F$, so it contains some $H\in\mathcal C$.

We have $H\cap S=\varnothing$. Since $H,E\in\mathcal C$ and $\mathcal C$ is intersecting, $H\cap E\ne\varnothing$. As $E=S\cup\{p\}$, it follows that $p\in H$. Moreover,
\[
w(H)\le \prod_{q\mid y}q\le y<w(S)=w(E\setminus\{p\}).
\tag{5}
\]
This is the required descent step.

Starting from $C$, repeatedly perform this step as long as the current set $E$ satisfies $w(E\setminus\{p\})\ge a_1$. Every resulting member of $\mathcal C$ contains $p$, and (5) shows that its weight is strictly smaller than the weight of the preceding member. Since these weights are positive integers, the process must terminate. At termination we obtain a set $D$ satisfying (4). This proves Lemma 2. $\square$

Call a member $D\in\mathcal C$ terminal if (4) holds for at least one $p\in D$. Every terminal member has bounded cardinality. Indeed, since all primes are at least $2$,
\[
2^{|D|-1}\le w(D\setminus\{p\})<a_1
\]
for the corresponding $p$. In particular, $|D|\le a_1$, so Lemma 1 shows that there are only finitely many terminal members.

Let $P$ be the union of all terminal members. It is a finite set of primes. If a prime $p$ occurs in any $C\in\mathcal C$, Lemma 2 supplies a terminal $D\in\mathcal C$ containing $p$. Therefore every prime occurring in any member of $\mathcal C$ belongs to $P$. It follows that every member of $\mathcal C$ is a subset of the finite set $P$, and hence $\mathcal C$ itself is finite, as desired.

Now set
\[
L=\prod_{p\in P}p.
\]
The set $P$ is nonempty: $\mathcal F$ contains the support of $a_1$, so $\mathcal C$ is nonempty. By (2), an integer $m\ge a_1$ is accepted exactly when $\operatorname{supp}(m)$ contains at least one member of $\mathcal C$. For each $p\in P$, we have
\[
p\mid m\quad\Longleftrightarrow\quad p\mid m+L.
\]
It follows that
\[
m\text{ is accepted}\quad\Longleftrightarrow\quad m+L\text{ is accepted}
\qquad(m\ge a_1).
\tag{6}
\]

Let $T$ be the number of residue classes modulo $L$ whose integers at least $a_1$ are accepted. This is positive because $a_1$ is accepted. Every half-open interval $(x,x+L]$ contains exactly one representative of each residue class modulo $L$, and therefore contains exactly $T$ accepted integers. Taking $x=a_n$ and using (6), the endpoint $a_n+L$ is accepted. It is consequently the $T$-th accepted integer after $a_n$, so
\[
a_{n+T}=a_n+L
\]
for every positive integer $n$. This completes the proof.
