# imo-2026-06 — tracking file
## Status
solved

## Problem
Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i)>1$ for every $i=1,2,\ldots,n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T}=a_n+L$ for every positive integer $n$. (Note that $\gcd(x,y)$ denotes the greatest common divisor of positive integers $x$ and $y$.)

## Approaches tried
- Computed examples. Prime-power starts produce arithmetic progressions, while $a_1=15$ produces the periodic difference pattern of period $8$ and total increment $30$.
- Recast the sequence as the increasing enumeration of the integers non-coprime to every sequence term. This reduces the problem to proving that this set is periodic.
- Used prime-divisor sets and a finite-transversal lemma. The pairwise-intersecting family of prime-divisor sets has only finitely many necessary transversal patterns; consequently the admissible integers are a finite union of sets of multiples. This completes the proof.

## Current best
The assertion is proved. There exist squarefree integers $b_1,\ldots,b_s>1$ such that an integer is non-coprime to every term precisely when it is divisible by at least one $b_j$. Taking $L=\operatorname{lcm}(b_1,\ldots,b_s)$ and $T$ equal to the number of admissible residue classes modulo $L$ gives $a_{n+T}=a_n+L$ for every $n\ge1$.

## Full proof
For a positive integer $m>1$, denote by $P(m)$ the finite nonempty set of its prime divisors. We first prove the set-theoretic lemma that will provide the needed finiteness.

**Finite-transversal lemma.** Let $\mathcal F$ be a nonempty, possibly infinite family of nonempty finite subsets of a set $P$. If every two members of $\mathcal F$ intersect, then there are finitely many nonempty finite sets $B_1,\ldots,B_s\subseteq P$ such that, for every finite $X\subseteq P$,
\[
 X\cap F\ne\varnothing\quad\text{for every }F\in\mathcal F
 \quad\Longleftrightarrow\quad
 B_j\subseteq X\quad\text{for some }j.
\]

**Proof of the lemma.** Call a finite set meeting every member of $\mathcal F$ a transversal. Every finite transversal contains an inclusion-minimal finite transversal, by successively deleting dispensable elements. We use the following elementary ``finite blocker'' fact.

> If a family of finite sets is pairwise intersecting and has a member $C$ of size $r$, then it has only finitely many inclusion-minimal finite transversals.

For completeness, here is a proof. Construct a rooted search tree as follows. A node bears a finite set $D$. If $D$ is a transversal, stop. Otherwise choose a member $F_D$ disjoint from $D$, and attach the finitely many children $D\cup\{x\}$, $x\in F_D$. At the root first attach the $r$ one-element sets $\{c\}$, $c\in C$; this loses no transversal, since every transversal meets the member $C$. Retain at a node only those branches which can still be extended to an inclusion-minimal finite transversal, and contract a node whenever an earlier chosen element has become dispensable.

This pruned tree is finite. Indeed, if it were infinite, König's lemma would give an infinite branch $x_1,x_2,\ldots$. At stage $k$ the set $F_k$ selected there is disjoint from $\{x_1,\ldots,x_k\}$. Since every $F_k$ meets the fixed finite set $C$, one $c\in C$ belongs to infinitely many $F_k$. Insert $c$ at its first such occurrence. Until the next occurrence nothing changes; at that next occurrence the element selected there is dispensable, because that selected set is already met by $c$. Repeating between consecutive occurrences shows that the branch has a contracted node, contrary to the pruning rule. Thus the tree is finite. Every minimal finite transversal follows a branch (at each nonterminal node it must contain some element of the selected set), and minimality prevents contraction; hence it is a terminal label. The finite blocker fact follows.

Apply this fact to any chosen $C\in\mathcal F$, which is a transversal because the family is pairwise intersecting. Let $B_1,\ldots,B_s$ be all inclusion-minimal finite transversals. A finite $X$ is a transversal exactly when it contains one of them. None is empty because $\mathcal F$ is nonempty. This proves the lemma. $\square$

We apply the lemma to
\[
 \mathcal F=\{P(a_i):i\ge1\}.
\]
If $i<j$, then the definition of $a_j$ gives $\gcd(a_i,a_j)>1$. Hence $P(a_i)\cap P(a_j)\ne\varnothing$, so $\mathcal F$ is pairwise intersecting. Obtain finite nonempty prime sets $B_1,\ldots,B_s$ from the lemma, and put
\[
 b_j=\prod_{p\in B_j}p\qquad(1\le j\le s).
\]
For every positive integer $x>1$, the lemma gives
\[
\begin{aligned}
 \gcd(x,a_i)>1\text{ for every }i
 &\Longleftrightarrow P(x)\cap P(a_i)\ne\varnothing\text{ for every }i\\
 &\Longleftrightarrow B_j\subseteq P(x)\text{ for some }j\\
 &\Longleftrightarrow b_j\mid x\text{ for some }j.
\end{aligned}
\]
Let
\[
 S=\{x\in\mathbb Z_{>0}:b_j\mid x\text{ for some }j\}.
\]
Thus $S$ is precisely the set of positive integers having gcd greater than $1$ with every term $a_i$. In particular, every $a_i$ belongs to $S$.

We next show that $a_1,a_2,\ldots$ are exactly the members of $S$ that are at least $a_1$, in increasing order. Certainly all terms belong to $S$. Conversely, suppose $x>a_1$ belongs to $S$. Because the sequence is strictly increasing, it is unbounded. Choose the unique $n$ for which
\[
 a_n<x\le a_{n+1}.
\]
Since $x\in S$, it has gcd greater than $1$ with each of $a_1,\ldots,a_n$. The minimality in the definition of $a_{n+1}$ therefore gives $a_{n+1}\le x$. Hence $x=a_{n+1}$. Also $a_1\in S$, proving the claim.

Finally, set
\[
 L=\operatorname{lcm}(b_1,\ldots,b_s).
\]
Membership in $S$ depends only on the residue class modulo $L$, because each $b_j$ divides $L$. Let $T$ be the number of residue classes modulo $L$ which belong to $S$. This is a positive integer: for example, the residue class $0$ belongs to $S$.

For every integer $y$, each residue class modulo $L$ occurs exactly once among
\[
 y+1,y+2,\ldots,y+L.
\]
Consequently exactly $T$ of these integers lie in $S$. Moreover, $y\in S$ if and only if $y+L\in S$.

Take $y=a_n$. Then $a_n+L\in S$, and among the integers strictly greater than $a_n$ and at most $a_n+L$ there are exactly $T$ members of $S$. Since the terms of the sequence are the increasing enumeration of $S$ from $a_1$ onward, the $T$-th term after $a_n$ is therefore $a_n+L$. Thus
\[
 \boxed{a_{n+T}=a_n+L}
\]
for every positive integer $n$, as required.
