# Direct bounding of prime factors

## Idea
Try to prove directly that the prime divisors of all sequence terms lie in a fixed finite set.

## Status
Abandoned; the claim is false and stronger than needed.

## Details
Even when selection is controlled by a small prime (for example, if all selected integers are even), selected terms can acquire arbitrarily large extra prime factors. These extra factors do not influence eligibility. Thus one must distinguish *relevant* primes from incidental factors.

This led to considering inclusion-minimal prime supports. An arbitrary support may contain unbounded incidental primes, but every selected support contains a minimal support, and it is enough to prove that the union of those minimal supports is finite.