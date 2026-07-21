# Invariance of exponent-gcd under the move

## Statement
Let $S$ be a finite multiset of non‑negative integers. Suppose two elements $\alpha,\beta\in S$ are removed and replaced by $\min(\alpha,\beta)$ and $|\alpha-\beta|$, obtaining a new multiset $S'$. Then $\gcd(S') = \gcd(S)$.

(Here $\gcd(\varnothing)=0$ and $\gcd$ of a multiset is the greatest common divisor of its elements; if all elements are $0$ then $\gcd=0$.)

## Proof
Let $d = \gcd(S)$. Since $d\mid\alpha$ and $d\mid\beta$, we have $d\mid\min(\alpha,\beta)$ and $d\mid|\alpha-\beta|$. All other elements of $S'$ are the same as in $S$, so $d$ divides every element of $S'$. Hence $d \mid \gcd(S')$.

Conversely, let $d' = \gcd(S')$. Then $d'\mid\min(\alpha,\beta)$ and $d'\mid|\alpha-\beta|$. Without loss of generality, assume $\alpha \le \beta$. Then $\alpha = \min(\alpha,\beta)$ and $\beta = \alpha + |\alpha-\beta| = \min(\alpha,\beta) + |\alpha-\beta|$. Since $d'$ divides both summands, $d'\mid\beta$ as well. Thus $d'$ divides every element of $S$, so $d' \mid d$.

Therefore $d = d'$. ∎
