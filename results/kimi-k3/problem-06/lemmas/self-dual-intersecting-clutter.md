# Lemma: finiteness of intersecting antichains with finite self-duality and compactness

**Definitions.** A family of sets is an *antichain* (clutter) if no member contains another. A *transversal* of a family $\mathcal F$ is a set meeting every member of $\mathcal F$; it is *minimal* if no proper subset is a transversal.

**Theorem.** Let $\mathcal C$ be a family of finite subsets of a countable ground set such that

1. *(antichain)* no member of $\mathcal C$ contains another member;
2. *(intersecting)* any two members of $\mathcal C$ have nonempty intersection;
3. *(finite self-duality)* every FINITE minimal transversal of $\mathcal C$ is a member of $\mathcal C$;
4. *(compactness)* every transversal of $\mathcal C$ contains a finite transversal.

Then $\mathcal C$ is finite.

**Remark on hypotheses.** In the application (`sequence-framework.md` + `compactness.md`), (1),(2),(3) are proved for the permanent family, and (4) is the Compactness Theorem, proved from the killing property (K′) — the number-theoretic input. Hypothesis (3) alone does NOT give (4): the star $\mathcal C=\{\{0,i\}:i\ge1\}$ satisfies (1),(2) but fails (3); and without (K′)-type input, an infinite minimal transversal (e.g. $\{1,2,3,\dots\}$ for the star) can exist. This theorem therefore cannot be strengthened to drop (4); an earlier version of this file erroneously applied (3) to infinite minimal transversals.

**Proof.** Suppose for contradiction that $\mathcal C$ is infinite.

Fix a member $t\in\mathcal C$. By (2) every member meets the finite set $t$, so
$$\mathcal C=\bigsqcup_{\emptyset\neq I\subseteq t}\mathcal C_I,\qquad \mathcal C_I:=\{e\in\mathcal C:e\cap t=I\},$$
a finite union. Since $\mathcal C$ is infinite, $\mathcal C_I$ is infinite for some $I$; fix such an $I$.

**(b) Key observation.** If $g\in\mathcal C$ is disjoint from $I$, then $g$ meets every member of $\mathcal C_I$ at a point outside $t$. Indeed, $g\cap e\neq\emptyset$ by (2), and
$$g\cap e\cap t\subseteq g\cap(e\cap t)=g\cap I=\emptyset.$$

Fix an enumeration of the countable family $\mathcal C$. Set $Z_0:=\emptyset$, $\mathcal F_0:=\mathcal C_I$ (infinite). For $s=0,1,2,\dots$, assuming $\mathcal F_s:=\{e\in\mathcal C_I:e\supseteq Z_s\}$ infinite, perform stage $s+1$:

*Case A: no member of $\mathcal C$ is disjoint from $I\cup Z_s$.* Then $I\cup Z_s$ is a transversal of $\mathcal C$; being finite, deleting redundant elements yields a finite minimal transversal $U\subseteq I\cup Z_s$, and $U\in\mathcal C$ by (3). Every $e\in\mathcal F_s$ satisfies $e\supseteq I\cup Z_s\supseteq U$, so by (1), $e=U$; hence $\mathcal F_s\subseteq\{U\}$, contradicting $\mathcal F_s$ infinite. **Case A cannot occur.**

*Case B: some member is disjoint from $I\cup Z_s$.* Let $g_s$ be such a member of least index. Since $g_s\cap I=\emptyset$, observation (b) says $g_s$ meets every $e\in\mathcal F_s$ outside $t$. The set $g_s\setminus t$ is finite and $\mathcal F_s$ is infinite, so by pigeonhole some $r\in g_s\setminus t$ lies in infinitely many members of $\mathcal F_s$. Set $z_{s+1}:=r$ (then $r\notin Z_s$, since $g_s\cap Z_s=\emptyset$; and $r\notin t$) and $\mathcal F_{s+1}:=\{e\in\mathcal F_s:z_{s+1}\in e\}$, infinite.

Since Case A never occurs, the process runs forever and produces distinct points $Z_\omega:=\{z_1,z_2,\dots\}$, all outside $t$.

**(c) $W:=I\cup Z_\omega$ is a transversal of $\mathcal C$ with no finite sub-transversal.** Suppose $g\in\mathcal C$ is disjoint from $W$. Then $g$ is disjoint from $I\cup Z_s$ for every $s$, hence eligible at every stage: $\mathrm{index}(g_s)\le\mathrm{index}(g)$ for all $s$. But $g_{s+1}$, disjoint from $I\cup Z_{s+1}\supseteq I\cup Z_s$, was already eligible at stage $s+1$, so $\mathrm{index}(g_{s+1})\ge\mathrm{index}(g_s)$; equality would force $g_{s+1}=g_s$, impossible since $z_{s+1}\in g_s$ while $g_{s+1}\cap Z_{s+1}=\emptyset$. Thus $(\mathrm{index}(g_s))$ is a strictly increasing sequence of positive integers bounded by $\mathrm{index}(g)$ — contradiction. So $W$ is a transversal. Any finite $F\subseteq W$ lies in some $I\cup Z_s$, and the member $g_s$ is disjoint from $I\cup Z_s\supseteq F$; so no finite subset of $W$ is a transversal. $\square$

But (c) contradicts hypothesis (4) (compactness). Hence $\mathcal C$ is finite. $\blacksquare$

**Remarks (sharpness).**
- The star $\{\{0,i\}:i\ge1\}$ satisfies (1),(2) but not (3); its transversal $\{1,2,3,\dots\}$ has no finite sub-transversal, so (4) fails too.
- Finite families satisfying (1),(2),(3),(4) abound: singletons, the triangle $\{\{1,2\},\{1,3\},\{2,3\}\}$, Fano lines, etc.
