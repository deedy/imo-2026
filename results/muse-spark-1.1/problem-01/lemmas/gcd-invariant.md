# Lemma: gcd of valuations invariant

**Statement:** For nonnegative integers a,b, let a' = min(a,b), b' = |a-b|. Then gcd(a,b)=gcd(a',b'). Consequently for any multiset a_1,...,a_N, replacing a_i,a_j by a'_i,a'_j preserves gcd of whole multiset.

**Proof:** If a≤b, then a'=a, b'=b-a, and gcd(a,b)=gcd(a,b-a) standard Euclid. Similarly if b<a. If a=b, a'=a, b'=0, gcd(a,a)=a=gcd(a,0). Edge case a=0 or b=0: say a=0≤b, then a'=0, b'=b, gcd preserved. For multiset, gcd_total = gcd(gcd(a_i,a_j), rest) = gcd(gcd(a'_i,a'_j), rest) = new total. ∎

**Application:** v_p board exponents G_p invariant.
