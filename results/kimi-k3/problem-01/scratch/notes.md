# Scratch notes

Hand simulations (verifying the conjecture $M = \prod_p p^{\gcd_i v_p(a_i)}$):

- $(4,6)$: $(4,6) \to (2,6) \to (2,3) \to (1,6)$. $M = 6$.
  Formula: $v_2: \gcd(2,1)=1$; $v_3: \gcd(0,1)=1$; $M = 2\cdot 3 = 6$. OK.
- $(2,3) \to (1,6)$. Formula: $v_2:\gcd(1,0)=1$, $v_3:\gcd(0,1)=1$, $M=6$. OK.
- $(2,4,8)$: $(2,4,8)\to(2,2,8)\to(2,1,8)\to(2,1,4)\to(2,1,2)\to(2,1,1)$. $M = 2$.
  Formula: only prime 2, $\gcd(1,2,3) = 1$, $M = 2$. OK.
- $(6,10,15)$: formula gives $v_2:\gcd(1,1,0)=1$, $v_3:\gcd(0,1,1)=1$, $v_5:\gcd(0,0,1)=1$,
  $M = 30$. One playout: $(6,10,15)\to(4,6,15)\to(2,4,15)\to(2,2,15)\to(2,0,15)$
  $\to \dots$ ends at $30$ (checked by code). OK.
- $(12,18) \to (6,6) \to (6,1)$. $M = 6$; formula: $v_2:\gcd(2,1)=1$, $v_3:\gcd(1,2)=1$. OK.
- All equal $(c,\dots,c)$: every move is $(c,c)\mapsto(c,1)$, reducing the count of $c$'s
  by one; final $M = c$. Formula: $\gcd(c,\dots,c)$-valuations $= v_p(c)$, so $M=c$. OK.
- Pairwise coprime inputs: each $v_p$-tuple has at most one nonzero entry, and
  $\gcd(0,\dots,0,e) = e$, so $M$ = product of all entries. Matches the fact that coprime
  moves $(m,n)\mapsto(1,mn)$ just merge entries into one big product.

Key algebraic identity behind everything:
$(\alpha,\beta) \mapsto (\min(\alpha,\beta), |\alpha-\beta|)$ preserves the gcd of the pair
(because $\gcd(a,b) = \gcd(a, b-a)$ for $a \le b$) — this is one step of the subtractive
Euclidean algorithm on the *exponents*.

Termination counting: moves of type B ($\gcd=1$) $\le N$ total (each creates a new $1$, and
$1$'s are never destroyed); moves of type A ($\gcd\ge 2$) $\le \log_2 P_0$ (each at least
halves the product). Total $\le N + \lfloor\log_2 P_0\rfloor < \infty$.
