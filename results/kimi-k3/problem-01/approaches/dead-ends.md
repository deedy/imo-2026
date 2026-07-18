# Dead ends / rejected ideas (honest log)

- **Sum of entries as a potential.** False: for $(m,n) = (6,10)$ the move gives
  $(g,\ell) = (2,15)$, and the sum *increases* $16 \to 17$. So the sum is not monotone;
  the product (equivalently $\sum_i \Omega(a_i)$, total number of prime factors with
  multiplicity) is the right first component of the potential.

- **Plain gcd of all entries as the invariant for (b).** False: starting from $(4,6)$ the
  final value is $M = 6$, while $\gcd(4,6) = 2$. The correct invariant is prime-wise and
  uses the *gcd of the exponents*, not the *minimum*: $v_p(M) = \gcd_i v_p(a_i)$, whereas
  $v_p(\gcd_i a_i) = \min_i v_p(a_i)$. (For $(4,6)$: $v_2 : \gcd(2,1)=1$, $v_3 :
  \gcd(0,1)=1$, so $M = 2\cdot 3 = 6$.)

- **Associative "star product" viewpoint.** One can check that the operation
  $x \star y = \prod_p p^{\gcd(v_p(x),v_p(y))}$ is associative and commutative, and the
  final answer is $M = a_1 \star \dots \star a_N$. This is a nice reformulation but proving
  that the game computes the star product requires essentially the same invariant argument,
  so it was not used in the final write-up. (Note: $M$ is the greatest common
  *exponential* divisor of the initial numbers, in the sense of exponential divisibility:
  $v_p(M) \mid v_p(a_i)$ for all $p, i$, and $M$ is maximal with this property.)

- **Induction on $N$.** No clean inductive step was found: after one move the remaining
  configuration is not of the same type with a known final value unless one already knows
  the invariant. The invariant argument makes induction unnecessary.
