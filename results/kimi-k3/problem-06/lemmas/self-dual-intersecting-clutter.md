# Lemma: finiteness of self-dual intersecting clutters

**Definitions.** A *clutter* is a family of finite sets, none containing another (antichain). A *transversal* of a family $\mathcal F$ is a set meeting every member of $\mathcal F$. A transversal is *minimal* if no proper subset is a transversal.

**Theorem.** Let $\mathcal C$ be a family of finite subsets of a countable ground set such that

1. *(antichain)* no member of $\mathcal C$ contains another member;
2. *(intersecting)* any two members of $\mathcal C$ have nonempty intersection;
3. *(self-dual)* every minimal transversal of $\mathcal C$ is a member of $\mathcal C$.

Then $\mathcal C$ is finite.

**Remarks (both hypotheses are needed).**
- The infinite "star" $\mathcal C=\{\{0,i\}:i\ge1\}$ satisfies (1) and (2) but not (3): $\{0\}$ is a minimal transversal that is not a member. So (3) is indispensable.
- Families satisfying (1),(2),(3) exist and can have more than one member, e.g. the triangle $\{\{1,2\},\{1,3\},\{2,3\}\}$ or the Fano lines; they are all finite, as the theorem asserts.

**Proof.** Suppose for contradiction that $\mathcal C$ is infinite.

**(a) Every transversal $W$ of $\mathcal C$ contains a minimal transversal.**
Order the transversals contained in $W$ by reverse inclusion $\supseteq$. Every chain $(T_\alpha)$ in this poset has an upper bound: let $T:=\bigcap_\alpha T_\alpha\subseteq W$; for each $e\in\mathcal C$, the family $\{e\cap T_\alpha\}$ consists of nonempty subsets of the finite set $e$ and is totally ordered by inclusion, hence has a smallest element; that smallest element is nonempty and equals $e\cap T$. Thus $T$ is a transversal contained in every $T_\alpha$. By Zorn's lemma the poset has a maximal element, i.e. a transversal $T\subseteq W$ that is minimal under inclusion; it is minimal among all transversals, since any smaller transversal would also be contained in $W$. $\square$

Fix a member $t\in\mathcal C$. By (2) every member meets the finite set $t$, so
$$\mathcal C=\bigsqcup_{\emptyset\neq I\subseteq t}\mathcal C_I,\qquad \mathcal C_I:=\{e\in\mathcal C:e\cap t=I\},$$
a finite union. Since $\mathcal C$ is infinite, $\mathcal C_I$ is infinite for some $I$; fix such an $I$.

**(b) Key observation.** If $g\in\mathcal C$ is disjoint from $I$, then $g$ meets every member of $\mathcal C_I$ at a point outside $t$. Indeed, $g\cap e\neq\emptyset$ by (2), and
$$g\cap e\cap t=(g\cap t)\cap(e\cap t)=(g\cap t)\cap I=\emptyset,$$
because $g\cap I=\emptyset$.

Fix an enumeration of the countable family $\mathcal C$. We inductively construct distinct points $z_1,z_2,\dots$ outside $t$ and infinite subfamilies
$$\mathcal F_s=\{e\in\mathcal C_I:e\supseteq Z_s\},\qquad Z_s:=\{z_1,\dots,z_s\},$$
starting from $\mathcal F_0:=\mathcal C_I$ (infinite).

**Stage $s+1$** ($s\ge0$). Suppose $\mathcal F_s$ is infinite.

*Case A: no member of $\mathcal C$ is disjoint from $I\cup Z_s$.* Then $I\cup Z_s$ is a transversal of $\mathcal C$; by (a) it contains a minimal transversal $T$, and $T\in\mathcal C$ by (3). Every $e\in\mathcal F_s$ satisfies $e\supseteq I\cup Z_s\supseteq T$, so by (1) $e=T$. Hence $\mathcal F_s\subseteq\{T\}$, contradicting that $\mathcal F_s$ is infinite. So Case A never occurs.

*Case B: some member is disjoint from $I\cup Z_s$.* Let $g_s$ be the disjoint member of smallest index. Since $g_s\cap I=\emptyset$, observation (b) says $g_s$ meets every $e\in\mathcal F_s$ outside $t$. The set $g_s\setminus t$ is finite and $\mathcal F_s$ is infinite, so by the pigeonhole principle some point $r\in g_s\setminus t$ belongs to infinitely many members of $\mathcal F_s$. Set $z_{s+1}:=r$ (then $r\notin Z_s$, since $g_s\cap Z_s=\emptyset$) and $\mathcal F_{s+1}:=\{e\in\mathcal F_s:z_{s+1}\in e\}$, which is infinite.

Since Case A never occurs, the process never stops and produces the infinite set $Z_\omega:=\{z_1,z_2,\dots\}$.

**(c) Every member of $\mathcal C$ meets $I\cup Z_\omega$.** Suppose instead that $g\in\mathcal C$ is disjoint from $I\cup Z_\omega$. Then $g$ is disjoint from $I\cup Z_s$ for every $s$, so $g$ is eligible at every stage: $\mathrm{index}(g)\ge\mathrm{index}(g_s)$ for all $s$. But at stage $s+1$ the least eligible member $g_s$ receives the point $z_{s+1}\in g_s$, so $g_s$ is not eligible at any later stage; and $g_{s+1}$, being disjoint from $I\cup Z_{s+1}\supseteq I\cup Z_s$, was already eligible at stage $s+1$, whence $\mathrm{index}(g_{s+1})\ge\mathrm{index}(g_s)$, with equality impossible because $z_{s+1}\in g_s\setminus g_{s+1}$. Thus $(\mathrm{index}(g_s))_{s\ge1}$ is a strictly increasing sequence of positive integers bounded above by $\mathrm{index}(g)$ — contradiction. $\square$

Hence $I\cup Z_\omega$ is a transversal of $\mathcal C$. By (a) it contains a minimal transversal $T$, and $T\in\mathcal C$ by (3). Since $T$ is finite and $Z_\omega=\bigcup_{s<\omega}Z_s$, there is a finite $s$ with $T\subseteq I\cup Z_s$. The family $\mathcal F_{s+1}$ is infinite; choose $e\in\mathcal F_{s+1}$ with $e\neq T$. Then
$$e\supseteq I\cup Z_{s+1}\supseteq I\cup Z_s\supseteq T,$$
so $e\supsetneq T$, contradicting (1). $\blacksquare$
