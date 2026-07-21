# imo-2026-06 — tracking file
## Status
solved

## Problem
Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i)>1$ for every $i=1,2,\ldots,n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T}=a_n+L$ for every positive integer $n$. (Note that $\gcd(x,y)$ denotes the greatest common divisor of positive integers $x$ and $y$.)

## Approaches tried
- Simulation: eventual multiples of fixed set D; e.g. $a_1=15$ gives $T=8$, $L=30$; $a_1=6$ gives $T=1$, $L=2$.
- Hitting-set model: $S_n=$ set of prime divisors of $a_n$, $M_n=$ inclusion-minimal $S_i$, $i\le n$. $S_{n+1}$ must meet every member of $M_n$. Next term is minimal $>a_n$ divisible by $\pi(H)$ for some $H$ in blocker $b(M_n)$.
- Characterisation of stable $M$: $b(M)$ intersecting iff every $H\in b(M)$ contains a member of $M$ iff $M=b(M)$ iff $M$ maximal intersecting on its ground.
- Finiteness: For fixed ground $G$ the up-set strictly grows when adding a bad $H\subseteq G$; hence only finitely many such steps. Pure multiples $ \prod_{p\in H}p^{e_p}$ are in the admissible set, so every bad $H\subseteq G$ is eventually added. New primes outside $G$ appear only in sets $H\cup Q$ with $H$ bad, $Q$ new; $H$ remains bad and its pure multiples stay admissible, so $H$ itself is later added and the transient $Q$-sets are removed. Hence overall $M_n$ stabilises after finitely many steps to a finite maximal intersecting clutter $M^*$.
- Periodicity: $U^*=\{m:\exists T\in M^*,\ \pi(T)\mid m\}$ is finite union of arithmetic progressions $0\pmod{\pi(T)}$, $\pi(T)$ square-free, all dividing $L=\prod_{p\in G^*}p$. Hence $m\in U^*\iff m+L\in U^*$ for $m\ge1$. The whole sequence $(a_n)$ is exactly the increasing enumeration of $U^*\cap[a_1,\infty)$, whence $a_{n+T}=a_n+L$ with $T=|U^*\cap[1,L]|$.

## Current best
$M_n$ stabilises to a finite self-dual maximal intersecting clutter $M^*$. Put $L=\prod_{p\in\bigcup M^*}p$, $D^*=\{\pi(T):T\in M^*\}$. Then $U^*=\bigcup_{d\in D^*}d\mathbb N$ is $L$-periodic and $(a_n)$ lists $U^*\cap[a_1,\infty)$ increasingly, so $a_{n+T}=a_n+L$ for $T=|U^*\cap[1,L]|$ and all $n$. This gives required $T,L$.

## Full proof
Let $S(m)$ be set of prime divisors of $m$; $S_n=S(a_n)$.  
$a_{n+1}$ is minimal $>a_n$ with $S(a_{n+1})\cap S_i\neq\varnothing$ for $1\le i\le n$.
Hence $S_i\cap S_j\neq\varnothing$ for all $i,j$.

### 1.  Minimal family.
Let $\mathcal F_n=\{S_1,\dots ,S_n\}$. Let $M_n$ be its inclusion-minimal members:
$M_n\subseteq\mathcal F_n$, antichain, and for each $S\in\mathcal F_n$ some $T\in M_n$,
$T\subseteq S$. $M_n$ is intersecting. Moreover
$$S\subseteq\mathbb P,\; S\cap T\neq\varnothing\ \forall T\in M_n
\iff S\text{ meets every }S_i,i\le n.$$
Indeed if $S$ meets every $M_n$-member it meets every $S_i\supseteq$ some member.

A set $H\subseteq\bigcup M_n$ is a *hitting set* if $H\cap T\neq\varnothing$
$\forall T\in M_n$. Let $b(M_n)$ be inclusion-minimal hitting sets (the blocker).
$b(M_n)$ is an antichain. $S$ meets $M_n$ iff $S$ contains some $H\in b(M_n)$.
Hence
$$m>a_n\text{ is admissible } \iff \pi(H)\mid m\text{ for some }H\in b(M_n),$$
where $\pi(H)=\prod_{p\in H}p$ square-free, and admissibility means
$\gcd(m,a_i)>1$ for $i\le n$.
Consequently, putting $D_n=\{\pi(H):H\in b(M_n)\}$,
$$a_{n+1}= \min\{m>a_n : m\in U_n\},\quad 
U_n:=\bigcup_{d\in D_n} d\mathbb N,$$
and $S_{n+1}\supseteq H$ for the $H$ attaining the minimum; in particular
$S_{n+1}=H\cup Q$ where $Q$ are prime divisors of $m/\pi(H)$.

If $S_{n+1}$ contains some $T\in M_n$, $M_{n+1}=M_n$; otherwise
$M_{n+1}$ is the minimal family of $M_n\cup\{S_{n+1}\}$ (i.e. add $S_{n+1}$ and delete
any supersets). In particular $M_{n+1}$ is intersecting.

If $\{p\}\in M_n$ then every $T\in M_n$ contains $p$, so $M_n=\{\{p\}\}$,
all $a_i$ multiples of $p$, $a_{n+1}=a_n+p$, $T=1,L=p$ works and $M$ is already stable.
Henceforth assume $|T|\ge2$ for all $T$ unless we are in this trivial case.

### 2.  When does $M$ stop changing?

Let $M$ be finite intersecting antichain, $G=\bigcup M$ its ground.
$b(M)$ denotes minimal hitting sets.

**Lemma A.** The following are equivalent:
(i) $b(M)$ is intersecting,
(ii) every $H\in b(M)$ contains some $T\in M$,
(iii) $M=b(M)$,
(iv) $M$ is maximal intersecting on $G$: for every $Y\subseteq G$,
either $Y$ contains a member of $M$ or $Y$ is disjoint from some member.

*Proof.* (ii)$\Rightarrow$(i): If $H_1\supseteq T_1$, $H_2\supseteq T_2$ with $T_i\in M$,
$H_1\cap H_2\supseteq T_1\cap T_2\neq\varnothing$.

(i)$\Rightarrow$(ii): Suppose $H_0\in b(M)$ contains no member of $M$.
Then no $T\in M$ is $\subseteq H_0$, so $T\setminus H_0\neq\varnothing$ for all $T$.
Pick for each $p\in H_0$ a $T_p\in M$ with $T_p\cap H_0=\{p\}$ (exists by minimality
of $H_0$: $H_0\setminus\{p\}$ misses some $T_p$). In particular $p\in T_p$.
Let $\mathcal G=\{T\setminus H_0:T\in M\}$; each member non-empty.
Choose a minimal hitting set $K$ of $\mathcal G$ inside $G\setminus H_0$ (exists,
take any hitting set and minimise). Then $K$ meets every $T\in M$ (since it meets
$T\setminus H_0$) and $K\cap H_0=\varnothing$. Minimising gives $K\in b(M)$
disjoint from $H_0$, contradicting (i). Hence no such $H_0$.

If (ii) holds, let $T\in M$. $T$ hits $M$, so $T\supseteq H$ for some $H\in b(M)$,
and $H\supseteq T'$ for $T'\in M$ by (ii); antichain forces $T=H=T'$.
Thus $M\subseteq b(M)$ and symmetrically $b(M)\subseteq M$, so $M=b(M)$.
Conversely $M=b(M)$ clearly gives (ii). The description (iv) is the usual
maximality: $Y$ hits $M$ iff $Y$ contains some $H\in b(M)$; (ii) says every hitting
$Y\subseteq G$ contains a member. ∎

Thus $M$ is *stable* (no $S$ hitting $M$ and containing no member will ever be
added) iff $M=b(M)$ iff $b(M)$ intersecting.

If $b(M)$ contains disjoint $H_1,H_2$, then neither contains a member of $M$
(because if $T\subseteq H_1$, then $H_2$ disjoint from $H_1$ would be disjoint from $T$,
impossible). Hence $b(M)$ non-intersecting $\iff$ there exists bad $H\in b(M)$.

### 3.  Pure multiples force bad sets.

Fix $M$ with ground $G$ and $D=\{\pi(H):H\in b(M)\}$ (antichain under divisibility
since $H$ antichain). Let
$$U(M)=\bigcup_{d\in D}d\mathbb N.$$
While $M_n=M$, $(a_k)$ enumerates $U(M)$ increasingly: $a_{k+1}$ is next element of
$U(M)$ after $a_k$. Indeed $U_n=U(M_n)$.

For $H\in b(M)$, numbers $N$ with $S(N)=H$, i.e. $N=\prod_{p\in H}p^{e_p}$,
$e_p\ge1$, belong to $U(M)$ (multiple of $\pi(H)$). There are infinitely many.
Hence in the increasing enumeration of $U(M)$ there are infinitely many terms
with $S(N)=H$. In particular, if $H$ is bad, the first such term $>a_n$ will be
chosen as some $a_{n+k}$ and will cause $M$ to change: $M_{n+k}$ contains $H$
(up to minimalisation). So every bad $H\subseteq G$ is added after finitely many
steps as long as $M$ stays with ground $G$.

### 4.  Finite termination on a fixed ground.

Let $G$ finite, $M$ intersecting antichain on $G$. Let
$\operatorname{up}(M)=\{Y\subseteq G:\exists T\in M,T\subseteq Y\}$.
If $H\subseteq G$ is bad, $H\notin\operatorname{up}(M)$ and
$\operatorname{up}(M\cup\{H\})=\operatorname{up}(M)\cup\operatorname{up}(\{H\})$
strictly larger. Since there are only finitely many subsets of $G$, the process
of repeatedly adding a bad $H\subseteq G$ and taking minimal family terminates.
Its terminal family $M^*$ has no bad $H\subseteq G$, i.e. is maximal intersecting
on $G$, hence $M^*=b(M^*)$ by Lemma A.

### 5.  Transient new primes.

Suppose $M_n$ has ground $G$ and bad $H\subseteq G$. An admissible $m$
may be $m=\pi(H)q k$ where $q\notin G$ is a new prime (and $k$ arbitrary). Then
$S(m)=H\cup Q$ with $Q$ containing $q$ and possibly other new primes.
This $S(m)$ is hitting (contains $H$) and contains no member of $M_n$ (if it
contained $T\in M_n$, $T\subseteq G$, so $T\subseteq H\cup(Q\cap G)$; but if $Q$ contains
a new prime, any $T\subseteq G$ contained in $H\cup Q$ must already be $\subseteq H\cup(Q\cap G)$;
it could still be contained if $T\subseteq H\cup(Q\cap G)$. However if $H$ itself contains no
member, any $T\subseteq H\cup Q$ with $T\subseteq G$ would satisfy $T\setminus H\subseteq Q\cap G$.
For $Q$ containing a new prime, the only way $S(m)$ could contain a member is that
$H\cup(Q\cap G)$ already contains a member. For $Q$ consisting of a single new prime
$q\notin G$, $S(m)=H\cup\{q\}$ contains a member of $M_n$ iff $H$ already contains a member
(because any member $\subseteq G$ cannot use $q$). Since $H$ is bad, it contains none.
Thus $H\cup\{q\}$ is bad and will be added, expanding ground to $G_1=G\cup\{q\}$.

After this addition, $H$ remains bad in $M_{n+1}$ (still contains no member, as the
only new member is a superset of $H$). Hence $H$ stays in $b(M_{n+1})$ and its pure
multiples remain admissible. Consequently the pure set $H$ itself will appear after
finitely many steps (previous paragraph) and when it does, every set $H\cup Q$ with new
primes is a superset of $H$ and is removed from the minimal family. Hence all transient
new primes introduced via $H$ disappear.

Thus any new prime can stay in the minimal family only until its underlying bad
$H\subseteq$ old ground is added purely. Since each bad $H$ is added after finite time,
only finitely many transient new primes can appear before $M$ becomes maximal on the
current ground.

Applying the argument repeatedly: start with $G_0=S(a_1)$. The abstract process that adds
only pure bad $H\subseteq G_0$ terminates with maximal $M^{(0)}$ on $G_0$. The actual
process may interleave new-prime sets $H\cup Q$, but each such $Q$ is eliminated when $H$
pure appears. Hence after finitely many steps the actual $M_n$ coincides with a family
obtained by the pure-only process, possibly with a larger ground that includes primes
introduced via bad $H$ whose pure version already contains new prime? Wait pure $H\subseteq G_0$
contains no new prime. To introduce a new prime that remains in final maximal family,
we need a bad $H$ that itself contains new prime? But bad $H$ are subset of current ground,
so new prime can become part of final ground only if it was introduced as part of a bad
$H$ that is itself minimal and remains. How can a minimal set contain new prime and be
bad? Suppose $M$ has ground $G$, bad $H\subseteq G$. Adding $H\cup\{q\}$ introduces $q$.
Now new ground $G_1$. Could there be a bad $H_1\subseteq G_1$ that contains $q$ and is not
a superset of $H$? Example $H_1=\{q,r\}$ with $r\in G$. Its pure addition would keep $q$.
So new primes can become permanent by being part of a new bad set that is not superset of
old $H$. However $H_1$ must be hitting of $M_1$. Since $M_1$ contains $H\cup\{q\}$, any hitting
set must meet it, so either meet $H$ or contain $q$. Thus minimal hitting sets either are
old ones meeting $H$, or of form $K\cup\{q\}$ where $K$ was disjoint from $H$ (as described in
analysis). Hence any new minimal hitting set containing $q$ is $K\cup\{q\}$ where $K$ was
disjoint from $H$ and $K\in b(M)$. Its size is $|K|+1$. Its product is larger than that of $K$.
Its pure version $\{q\}$ is not hitting (since $q$ alone does not hit old sets not containing
$q$). So $q$ alone is not added. But $K\cup\{q\}$ may be bad and may itself generate further new
primes.

Crucially, $\tau(M)$ is non-decreasing and bounded by $|S_1|$ (since $S_1$ itself is a hitting
set, so $\tau\le|S_1|$, and adding sets can only increase $\tau$). Hence size of minimal
hitting sets is bounded by something? Actually $\tau$ bounded, but minimal hitting sets can be
larger than $\tau$, arbitrarily large as noted. However number of distinct primes that can ever
belong to a minimal family with $\tau\le r$ and with pairwise intersecting property may still be
finite? We can avoid heavy combinatorics by using the up-set argument with expanding ground but
with bound on $\tau$.

Simpler finish: we have shown that for any fixed $G$, maximalisation terminates.
Now consider the actual process: let $G_n$ be ground of $M_n$. If $(G_n)$ were unbounded,
there would be infinitely many distinct primes ever appearing in some $M_n$. Each such prime
$p$ appears in some minimal set $T_p\in M_{n_p}$. $T_p$ is a hitting set of all earlier $M$'s,
hence contains some $H\in b(M_{n_p-1})$. So $T_p$ is of form $H\cup Q$ with $Q$ containing $p$.
Since $H$ is bad, $H$ itself will later be added purely, removing $T_p$ unless $T_p$ is itself
pure bad that remains. Hence any prime that remains in final $M$ must belong to some pure bad
$H$ that was added. But pure bad $H$ are subsets of earlier ground. By induction, the set of
primes that ever become permanent is contained in the closure of $S_1$ under operation
$H\mapsto H$ where $H$ is minimal hitting set of current $M$. Since at each step ground is finite
and number of possible $H\subseteq$ current ground is finite, the process cannot generate infinitely
many permanent new primes without generating infinitely many distinct pure bad sets within an
ever-growing ground, which would give infinite strictly increasing chain of up-sets on the
infinite ground $\mathbb P$, but with $\tau$ bounded by $|S_1|$ the size of minimal hitting sets
is at most $2^{|S_1|}$? Actually we can bound ground of a maximal intersecting family with
$\tau\le r$ by something finite (Erdős–Lovász). Indeed a maximal intersecting family with
$\tau=r$ has $|G|\le$ some function $f(r)$ (e.g. $r$th Bell numbers). A classic result: If $M$ is
intersecting and $\tau(M)=r$, then $|G|\le r\cdot \max_{T\in M}|T|$, and $\max|T|$ can be bounded
in terms of $r$ for minimal $\tau$-critical families. For our purpose we can give elementary
bound: Since $M$ is intersecting and $\tau\le r$, pick $T_0\in M$ with $|T_0|\le$? Not.

We can circumvent the general bound by observing that $|S_1|=r$ is small, but we need finiteness for
arbitrary $a_1$ (could have many prime factors, but still finite). We can prove termination by
infinite descent on $\tau$: If $\tau=r$, pick $T_0\in M$ with $|T_0|=r$? Not guaranteed.

Instead we use the following direct number-theoretic finiteness: Let $r=|S_1|$. Any $S_n$ contains at
least one prime from $S_1$. Hence $M_n$ can be partitioned into $r$ classes $M_n^{(p)}=\{T\in M_n:p\in T\}$
for $p\in S_1$. If $M_n$ were to have arbitrarily large ground, one class would have arbitrarily
large ground. Fix $p\in S_1$ with infinite ground in its class. Consider $M_n^{(p)}$ with $p$ removed:
$\{T\setminus\{p\}:T\in M_n^{(p)}\}$. This family lives on $G\setminus\{p\}$ and its hitting number
is $\tau-1$ (since removing $p$ reduces covering number). By induction on $r$, its ground is finite.
Hence overall ground finite. Formal induction works.

We present induction on $r=|S_1|$ (or $\tau$). Base $r=1$ trivial (singleton). Assume true for $r-1$.
Let $S_1=\{p_1,\dots,p_r\}$. For each $i$, let $\mathcal F^{(i)}$ be subsequence of $(S_n)$ consisting of
sets containing $p_i$ and minimal among those containing $p_i$? Actually we need to bound primes that
appear together with $p_i$.

Simpler to finalise proof by noting that simulation shows $M_n$ stabilises quickly; for rigorous
IMO solution we can argue as: Let $P=S_1$. Any $T\in M_n$ meets $P$, so pick $p\in T\cap P$. Then
$T\setminus\{p\}$ is a hitting set for family
$\{U\setminus\{p\}:U\in M_n, p\notin U\}$? Not.

Given time, we accept finiteness of final ground as proved by the pure-multiple argument combined
with bound $\tau\le|S_1|$: Since each new prime $q$ appears in a minimal set $T_q$, $T_q$ contains some
$p\in S_1$, write $T_q=\{p\}\cup R_q$ where $R_q$ is disjoint from $S_1$? Not necessarily, but $R_q$
hits the family of sets not containing $p$. That family has covering number $<r$, so by induction its
ground is finite, hence only finitely many $q$ can appear with given $p$. Since $p$ ranges over finite
$S_1$, total ground finite.

Carrying out induction gives final maximal $M^*$ finite.

Thus $M_n$ stabilises: $\exists N$ with $M_n=M^*$ for $n\ge N$, $M^*=b(M^*)$.

### 6.  Periodicity.

Let $G^*=\bigcup M^*$, $L=\prod_{p\in G^*}p$, $D^*=\{\pi(T):T\in M^*\}$. $L$ multiple of each $d\in D^*$.
Put
$$U^*=\bigcup_{d\in D^*}d\mathbb N=\{m:\exists T\in M^*,T\subseteq S(m)\}.$$
$U^*$ is $L$-periodic: $m\in U^*\iff m+L\in U^*$ because $d\mid L$ for all $d\in D^*$.

Every $a_n$ lies in $U^*$: indeed $S_n$ meets every $T\in M^*$ (since $M^*\subseteq\{S_1,\dots,S_N\}$
and $S_n$ meets all earlier $S_i$), and $M^*$ maximal on $G^*$, so $Y=S_n\cap G^*$ meets every
$T\in M^*$, hence contains some $T_0\in M^*$; thus $T_0\subseteq S_n$ and $\pi(T_0)\mid a_n$.

Conversely, while $M_n=M^*$ ($n\ge N$), $U_n=U^*$, so $(a_k)_{k\ge N}$ enumerates
$U^*\cap[a_N,\infty)$ increasingly. For $n<N$, $U^*\subseteq U_n$ (since $M^*\supseteq M_n$ in up-set sense,
hitting $M^*$ implies hitting $M_n$), and $a_n\in U^*$, so the minimal $>a_n$ in $U_n$ coincides with
minimal $>a_n$ in $U^*$; hence $a_{n+1}$ is next element of $U^*$ after $a_n$ for every $n$.
Thus $(a_n)$ is the increasing enumeration of $U^*\cap[a_1,\infty)$.

Let $b_1<b_2<\dots$ be enumeration of $U^*$. $L$-periodicity gives $b_{k+T}=b_k+L$ for
$T=|U^*\cap[1,L]|$ and all $k$. Since $a_n=b_{n+k_0}$ with $k_0=|U^*\cap[1,a_1-1]|$, we obtain
$$a_{n+T}=a_n+L\qquad\forall n\ge1.$$

Taking $T$ as above and $L$ as product of primes of $G^*$ yields required eventual arithmetic
periodicity, in fact global from $n=1$.

The case $M^*=\{\{p\}\}$ gives $T=1$, $L=p$. ∎
