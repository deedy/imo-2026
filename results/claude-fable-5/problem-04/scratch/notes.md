# Initial exploration

Cut parametrization: triangle with angles A,B,C at vertices; cut from vertex A to P on BC,
let alpha = angle BAP in (0,A). Children:
- T1 = ABP: angles {B, alpha, 180-B-alpha}   (angle at P is 180-B-alpha)
- T2 = APC: angles {C, A-alpha, B+alpha}     (angle at P is B+alpha)

Key observations:
- The two P-angles sum to 180.
- If some angle = k*theta (k>=2), Mulan cuts alpha=theta: T1 contains theta (Shan-Yu must discard),
  T2 contains (k-1)theta. Chain down to theta. => any triangle with an angle in theta*N is a Mulan win.
- Double threat in one cut needs BOTH children to contain a multiple of theta. With generic B, C the
  only ways: alpha=k*theta & A-alpha=m*theta => A in theta*N; or both P-angles multiples => 180 in theta*N.

Conjecture: Mulan wins iff 180/theta is an integer (theta = 180/n, n>=2).

Mulan side (theta=180/n): if no angle in theta*N, cut at largest angle A, choose P-angle = k*theta
in (C, 180-B) (interval has length A > theta for n>=3 since A>=60>=theta and A != theta; for n=2 use 90 in
(C,180-B) since B,C<90). Then T1 has k*theta, T2 has P-angle 180-k*theta=(n-k)*theta. Both children winning.

Shan-Yu side (180 not in theta*N): invariant = all three angles not in theta*N.
Both children unsafe leads to 4 cases, each forcing A, B, C or 180 into theta*N. Contradiction.
