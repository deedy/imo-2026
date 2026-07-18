# imo-2026-06 — tracking file
## Status
solved

## Problem
Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i)>1$ for every $i=1,2,\ldots,n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T}=a_n+L$ for every positive integer $n$. (Note that $\gcd(x,y)$ denotes the greatest common divisor of positive integers $x$ and $y$.)

## Approaches tried
- Reformulated the sequence as the result of scanning all integers above $a_1$ and retaining exactly those non-coprime to every previously retained integer.
- A direct attempt to bound all prime divisors of the terms fails: terms can have arbitrarily large irrelevant prime factors.
- The successful route is instead to consider the inclusion-minimal prime supports of retained integers. They form a self-blocking intersecting family. An arithmetic descent shows that every prime occurring in a minimal support also occurs in a minimal support whose remaining radical is at most $a_1$. There are only finitely many such small cores, and a disjoint witness shows that each core can be paired with only finitely many primes. Hence the set of relevant primes is finite.

## Current best
Let $\mathcal H$ be the family of inclusion-minimal prime supports of sequence terms. The proof establishes that $U=\bigcup\mathcal H$ is finite. Consequently the sequence is exactly the increasing enumeration, beginning at $a_1$, of integers divisible by $\prod_{p\in H}p$ for at least one $H\in\mathcal H$. This condition is periodic modulo $L=\prod_{p\in U}p$. If $T$ is the number of admissible residue classes modulo $L$, then $a_{n+T}=a_n+L$ for every $n$.

## Full proof
Put $m=a_1$, and for every integer $x>1$ let $P(x)$ denote the finite set of prime divisors of $x$.

### 1. The self-blocking family of prime supports

The terms $a_n$ are strictly increasing, so the sequence is unbounded. We first record the following consequence of the defining rule:

> **Scanning property.** If an integer $x>m$ is not a term of the sequence, then there is a term $a_i<x$ such that $\gcd(x,a_i)=1$.

Indeed, choose $n$ such that
\[
a_n<x<a_{n+1}.
\]
If $x$ had a common prime divisor with each of $a_1,\ldots,a_n$, it would be an eligible choice after $a_n$, contradicting the fact that $a_{n+1}$ is the smallest eligible integer. This proves the scanning property.

Let
\[
\mathcal G=\{P(a_n):n\geq 1\}
\]
and define its *blocker* (among finite sets of primes) by
\[
\mathcal F=\{S:S\text{ is a finite set of primes and }S\cap G\ne\varnothing
                  \text{ for every }G\in\mathcal G\}.
\]
Any two terms of the sequence have gcd greater than $1$, so any two members of $\mathcal G$ intersect. It follows that $\mathcal G\subseteq\mathcal F$.

In fact,
\[
\boxed{\mathcal G=\mathcal F.}\tag{1}
\]
To prove the reverse inclusion, take $S\in\mathcal F$. The set $S$ is nonempty, because it must intersect $P(a_1)$. Choose an integer $x>m$ with $P(x)=S$; for example, a sufficiently large power of $\prod_{p\in S}p$ has these properties. Since $S$ intersects every member of $\mathcal G$, the integer $x$ has gcd greater than $1$ with every term of the sequence. As the sequence is unbounded, we may choose $n$ such that
\[
a_n<x\leq a_{n+1}.
\]
Then $x$ is eligible after $a_n$, so the minimality in the recurrence gives $a_{n+1}\leq x$. Hence $x=a_{n+1}$, and therefore $S=P(x)\in\mathcal G$. This proves (1).

Thus $\mathcal F$ has the following properties:

1. it is **upward-closed**: if $S\in\mathcal F$ and $S\subseteq S'$, where $S'$ is finite, then $S'\in\mathcal F$;
2. it is **intersecting**: any two of its members intersect;
3. it is **self-blocking**:
   \[
   S\in\mathcal F\quad\Longleftrightarrow\quad
   S\cap F\ne\varnothing\text{ for every }F\in\mathcal F.\tag{2}
   \]

Here (2) follows from the definition of $\mathcal F$ and (1). In particular, whenever a finite set $S$ does not belong to $\mathcal F$, there exists $F\in\mathcal F$ disjoint from $S$.

Let $\mathcal H$ be the family of inclusion-minimal members of $\mathcal F$. Every member $F$ of $\mathcal F$ contains a member of $\mathcal H$: among the finitely many subsets of $F$ which belong to $\mathcal F$, choose an inclusion-minimal one.

### 2. Finiteness of the relevant primes

Call the primes in
\[
U=\bigcup_{H\in\mathcal H}H
\]
the **relevant primes**. We prove that $U$ is finite.

Fix $p\in U$, and choose $H\in\mathcal H$ containing $p$. Set
\[
c(H,p)=\prod_{q\in H\setminus\{p\}}q,
\]
where an empty product is $1$. We first prove that, after possibly replacing $H$ by another member of $\mathcal H$ which still contains $p$, we may arrange that
\[
c(H,p)\leq m.\tag{3}
\]

Suppose that the present $H$ does not satisfy (3), and put
\[
D=H\setminus\{p\},\qquad x=c(H,p)>m.
\]
The minimality of $H$ gives $D\notin\mathcal F$. By (1), no term of the sequence has prime support $D$; in particular, $x$ is not a term. By the scanning property there is a term $y=a_j<x$ with
\[
P(y)\cap D=\varnothing.
\]
The set $P(y)$ belongs to $\mathcal F$, so it contains some $K\in\mathcal H$. Hence $K\cap D=\varnothing$. On the other hand, $K,H\in\mathcal F$, and $\mathcal F$ is intersecting. Since $H=D\cup\{p\}$, these two facts force $p\in K$. Moreover, the squarefree number $p\,c(K,p)$ divides $y$, and therefore
\[
c(K,p)\leq \frac{y}{p}<x=c(H,p).\tag{4}
\]
Thus replacing $H$ by $K$ strictly decreases the positive integer $c(H,p)$ while preserving both $H\in\mathcal H$ and $p\in H$. Repeating this operation must terminate, and it can terminate only with (3). This proves the claim.

There are only finitely many finite sets $C$ of primes satisfying
\[
\prod_{q\in C}q\leq m,\tag{5}
\]
because every prime in such a set is at most $m$. By (3), every $p\in U$ admits at least one such set $C$ for which
\[
C\cup\{p\}\in\mathcal H,
\qquad p\notin C.\tag{6}
\]
We show that each fixed $C$ satisfying (5) can occur in (6) for only finitely many primes $p$.

If (6) holds, the inclusion-minimality of $C\cup\{p\}$ implies that $C\notin\mathcal F$. By (2), we may therefore fix some $F_C\in\mathcal F$ with
\[
F_C\cap C=\varnothing.
\]
For every prime $p$ satisfying (6), the two members $F_C$ and $C\cup\{p\}$ of the intersecting family $\mathcal F$ must intersect. Since $F_C$ is disjoint from $C$, this forces $p\in F_C$. The set $F_C$ is finite, so only finitely many such $p$ exist.

There are finitely many possible $C$, and each yields only finitely many possible $p$. Hence $U$ is finite. Since every $H\in\mathcal H$ is a subset of the finite set $U$, the family $\mathcal H$ itself is finite as well.

### 3. Periodicity

For every finite set $S$ of primes, upward-closure and the definition of $\mathcal H$ give
\[
S\in\mathcal F
\quad\Longleftrightarrow\quad
H\subseteq S\text{ for some }H\in\mathcal H.\tag{7}
\]
We now characterize the terms of the sequence. For every integer $x\geq m$,
\[
x\text{ is a term of the sequence}
\quad\Longleftrightarrow\quad
H\subseteq P(x)\text{ for some }H\in\mathcal H.\tag{8}
\]
The forward implication follows from $P(x)\in\mathcal G=\mathcal F$ and (7). Conversely, suppose the right-hand side holds. Then $P(x)\in\mathcal F$, so $x$ has gcd greater than $1$ with every term of the sequence. If $x=m$, it is already the first term. If $x>m$ and were not a term, the scanning property would supply an earlier term coprime to $x$, a contradiction. This proves (8).

The set $U$ is nonempty because $\mathcal F$ contains $P(m)$ and hence $\mathcal H$ is nonempty. Define
\[
L=\prod_{p\in U}p.
\]
For any positive integer $x$ and any $H\in\mathcal H$, all primes of $H$ divide $L$, so
\[
H\subseteq P(x)
\quad\Longleftrightarrow\quad
H\subseteq P(x+L).
\]
Thus the condition on the right of (8) is periodic modulo $L$.

Let $T$ be the number of integers $r\in\{1,2,\ldots,L\}$ satisfying that condition. This is positive: the integer $L$ itself satisfies it because it is divisible by every prime in every $H\in\mathcal H$. By periodicity, every interval of $L$ consecutive integers contains exactly $T$ integers satisfying the condition.

Fix $n\geq1$. By (8), among the integers
\[
a_n+1,a_n+2,\ldots,a_n+L
\]
there are exactly $T$ terms of the sequence. Also $a_n+L$ is one of them, since $a_n$ is a term and the condition in (8) is periodic modulo $L$. Therefore $a_n+L$ is precisely the $T$-th term after $a_n$, that is,
\[
\boxed{a_{n+T}=a_n+L}
\]
for every positive integer $n$. Both $T$ and $L$ are positive, completing the proof.
