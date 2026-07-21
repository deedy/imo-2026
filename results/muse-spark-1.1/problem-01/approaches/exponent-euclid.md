# Approach: Prime exponent Euclidean algorithm

Idea: translate operation to exponent pair transform.

For each prime p independently track valuations a_i = v_p(x_i).
gcd(m,n) -> min(a,b)
lcm(m,n)/gcd(m,n) -> max(a,b)-min(a,b)=|a-b|

So operation on pair (a,b) -> (min(a,b), |a-b|) up to swap.

This is exactly subtraction step of Euclidean algorithm.

Observation:
- Number of entries >1: corresponds to existence of some p with a_i>0.
- Product per prime sum? Not directly.

Key invariants/per variants:
- Let G_p = gcd_i a_i. Invariant because gcd(a,b)=gcd(min,|a-b|).
- Sum S_p = sum_i a_i? Transform: min + |a-b| = max, so sum after = sum before - min + max? Wait original sum = a+b, new sum = max. So sum decreases by min unless min=0. So total p-adic total valuation summed over board is nonincreasing, strictly decreasing when both a,b >0.
That implies total log product sum_p sum_i a_i decreases when operation is on pair sharing a common prime factor. This connects to product measure.

Termination proof using product or sum: product P = prod m_i satisfies P' = P / gcd(m,n). So integer decreasing when overlapping.

Counting of >1 entries: if gcd=1, we lose one >1 entry; if m=n we lose one; otherwise count preserved.

Thus any infinite run would eventually stabilize k and then cause infinite strict decrease of P, impossible.

Terminal characterization: only one >1 left, say M, then G_p = v_p(M). So final M = prod p^{G_p}.

This approach succeeds for both (a) and (b).

Status: successful, forms core proof.
