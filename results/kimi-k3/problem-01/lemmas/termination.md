# Lemma: termination (every play is finite)

**Statement.** Let $N \ge 2$ and start from any $N$ integers $\ge 2$ on the board. Then every
sequence of legal moves is finite; in fact the number of moves is at most
$N + \lfloor \log_2 P_0 \rfloor$, where $P_0$ is the initial product of all numbers.

**Proof.** Let $a_1,\dots,a_N$ be the current entries, $P = a_1\cdots a_N \in \mathbb{Z}_{>0}$,
and let $z = \#\{i : a_i = 1\}$. Consider a move on $(m,n)$, and put $g = \gcd(m,n)$,
$\ell = \operatorname{lcm}(m,n)/g$. Both $g$ and $\ell$ are positive integers since
$g \mid \operatorname{lcm}(m,n)$. The two new entries have product
$$g\cdot \ell = \operatorname{lcm}(m,n) = \frac{mn}{g},$$
so the total product $P$ becomes $P/g$.

*Monotonicity of $z$.* A move never destroys an entry equal to $1$: the two replaced entries
are $>1$ (only entries $>1$ may be chosen), and the two new entries are $\ge 1$. Hence $z$ is
non-decreasing during the whole process; also $z \le N$ always.

*Type A moves: $g \ge 2$.* Then $P$ is multiplied by $1/g \le 1/2$.

*Type B moves: $g = 1$.* Then $\ell = mn \ge 4$, so the pair $(m,n)$ (both entries $>1$) is
replaced by $(1, mn)$: the product $P$ is unchanged and $z$ increases by exactly $1$.

Bounding the two types: since $z$ is non-decreasing, takes values in $\{0,1,\dots,N\}$, and
increases by $1$ at each type B move, there are at most $N$ type B moves in the whole play.
Since $P$ is always a positive integer and each type A move at least halves it, if there were
$t$ type A moves then $1 \le P_0/2^{t}$, i.e. $t \le \lfloor \log_2 P_0 \rfloor$.

Hence every play has at most $N + \lfloor \log_2 P_0 \rfloor$ moves. $\blacksquare$

**Remark.** Equivalently, the lexicographic pair $(P,\, N - z) \in \mathbb{N}^2$ strictly
decreases at every move, and $\mathbb{N}^2$ with lexicographic order is well-ordered.
