# Finite-blocker lemma

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

