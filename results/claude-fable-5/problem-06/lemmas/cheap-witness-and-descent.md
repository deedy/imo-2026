# Lemmas: cheap witness and the no-big-prime descent

(Notation as in `members-structure.md`.)

## Lemma 6 (cheap witness)
Let $Q\in\mathcal M$, $|Q|\ge2$, $t\in Q$. Then there is $Q'\in\mathcal M$ with
$$Q'\cap Q=\{t\},\qquad d_{Q'}<\frac{a_1 d_Q}{t}.$$

*Proof.* $X:=Q\setminus\{t\}\ne\emptyset$, $\pi(X)=d_Q/t\ge2$. No member is $\subseteq X$ (it would be a transversal properly inside the member $Q$). Let $e\ge1$ be least with $m:=\pi(X)^e>a_1$; then $m\le a_1\pi(X)$ (if $e\ge2$, $\pi(X)^{e-1}\le a_1$; if $e=1$, trivial). $P(m)=X$ contains no member, so $m\notin S$ (Lemma 4). By the downward-witness Lemma 3, some $s\in S$, $s<m$, $\gcd(s,m)=1$, i.e. $P(s)\cap X=\emptyset$. Take a member $Q'\subseteq P(s)$ (Lemma 4): $Q'\cap X=\emptyset$ and $d_{Q'}\mid s$, so $d_{Q'}\le s<m\le a_1\pi(X)=a_1d_Q/t$. Members intersect (Lemma 5), and $Q=X\cup\{t\}$, so $Q'\cap Q=\{t\}$. $\square$

## Lemma 7 (no member contains a prime $>a_1$)
*Proof.* If some member is a singleton $\{p\}$: every member $M$ meets $\{p\}$ (Lemma 5), so $p\in M$, and minimality of $M$ with the transversal $\{p\}\subseteq M$ forces $M=\{p\}$; thus $\mathcal M=\{\{p\}\}$ and Lemma 4 applied to $a_1\in S$ gives $p\mid a_1$, so $p\le a_1$ — claim holds.

Otherwise all members have $\ge2$ elements. Suppose $q>a_1$ is a prime in a member $Q_0$. Recursively let $Q_{i+1}$ be the Lemma 6 witness for $(Q_i,t=q)$; inductively $q\in Q_i$ and $|Q_i|\ge2$, and
$$d_{Q_{i+1}}<\tfrac{a_1}{q}d_{Q_i}\ \Rightarrow\ d_{Q_i}<\bigl(\tfrac{a_1}{q}\bigr)^i d_{Q_0}\to0,$$
contradicting $d_{Q_i}\ge q\ge2$. $\square$

## Corollary (finiteness)
$\mathcal M\subseteq 2^{\{p\ \mathrm{prime}:\ p\le a_1\}}$ is finite and nonempty, and every $d_Q$ divides $M=\prod_{p\le a_1}p$.
