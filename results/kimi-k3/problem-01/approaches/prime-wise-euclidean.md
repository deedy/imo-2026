# Approach: prime-wise reduction to a subtractive Euclidean game (equivalent viewpoint)

**Idea.** The move $(m,n) \mapsto (\gcd(m,n), \operatorname{lcm}(m,n)/\gcd(m,n))$ acts on the
$p$-adic valuations of the two chosen entries independently for each prime $p$:
$$(\alpha,\beta) \longmapsto \big(\min(\alpha,\beta),\ \max(\alpha,\beta)-\min(\alpha,\beta)\big)
= \big(\min(\alpha,\beta),\ |\alpha-\beta|\big).$$
So the whole process projects, for each prime $p$, onto the 1-dimensional game:
a multiset of nonnegative integers; a move picks two positive entries $a,b$ and replaces them
by $\min(a,b)$ and $|a-b|$ (if one of them is $0$ the multiset is unchanged). For two numbers
this is exactly the subtractive Euclidean algorithm, which ends at $(\gcd(a,b), 0)$; the
analogous invariant in general is the gcd of the whole multiset.

**What it gives.** The same invariant $G_p = \gcd_i v_p(a_i)$ and the same conclusion.
This viewpoint is excellent for *discovering* the answer (simulate the 1-D game; guess the
gcd invariant; e.g. $(4,6) \mapsto (4,2) \mapsto (2,2) \mapsto (2,0)$ on the 2-adic
valuations). For the write-up the direct global invariant (see
`approaches/invariant-valuations.md`) is shorter: one does not need to prove that the
projected games terminate independently — termination is global (product argument), and the
invariant is checked prime by prime.

**Caveat handled.** Different primes are coupled (one physical move acts on all primes at
once), but for part (b) we only need that in the *actual* terminal position
$(1,\dots,1,M)$ the valuation at each prime equals the invariant $G_p$; no decoupling
argument is required.

**Status.** Equivalent reformulation; superseded by the direct invariant proof.
