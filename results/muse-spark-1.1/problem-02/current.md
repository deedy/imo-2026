# imo-2026-02 — tracking file
## Status
unsolved

## Problem
Let $ABC$ be a triangle and let points $M$ and $N$ be the midpoints of sides $AB$ and $AC$, respectively. Let points $K$ and $L$ be chosen inside triangles $BMC$ and $BNC$, respectively, such that $K$ lies inside the angle $LBA$, $L$ lies inside the angle $ACK$, and $\angle KBA = \angle ACL$, $\angle LBK = \angle LNC$, $\angle LCK = \angle BMK$. Let $O$ be the circumcentre of triangle $AKL$. Prove that $OM = ON$.

## Approaches tried
- Setup coordinate system with midpoints at (-1,0) and (1,0) to exploit symmetry about perpendicular bisector of MN (which is y-axis). In this system, OM=ON iff O's x-coordinate is 0. Goal reduces to proving circumcenter of AKL lies on y-axis / line perpendicular to MN.
- Let alpha = KBA = ACL, gamma = BMK = LCK, beta = LBK = LNC. Then angle LBA = alpha+beta, angle ACK = alpha+gamma. So lines determined. Parametrization leads to existence of K,L intersection. Trying to understand locus.
- Numeric search attempt: using triangle placing M=(-1,0), N=(1,0), A=(u,v) etc. Then B = (-2 -u, -v), C = (2 -u, -v). Write equations for intersection. Need to solve for gamma, beta given alpha such that K and L definitions consistent.

## Current best
Coordinate choice: M=(-1,0), N=(1,0), A=(u,v). Then B=(2M - A) = (-2 -u, -v), C = (2N - A) = (2 -u, -v). BC horizontal line y=-v, MN horizontal y=0, etc. Condition OM=ON equivalent to Ox=0 for circumcenter O of AKL. So need to prove Ox=0.

Let alpha = ∠KBA = ∠ACL.
Define gamma = ∠BMK = ∠LCK, beta = ∠LBK = ∠LNC.

Then geometry:
- At B: BA direction to BM etc. But BA vector is A - B. BK is BA rotated clockwise by alpha (if inside). BL is BA rotated clockwise by alpha+beta.
- At M: MB vector is B - M. MK is MB rotated CCW by gamma.
- At C: CA vector is A - C. CL is CA rotated??? Need orientation: ACL = alpha, with L inside angle ACK. So CL is inside angle between CA and CK. CA direction from C to A. CK is further? Since L lies inside ACK, ACL = alpha, and ACK = alpha + gamma? Let's deduce: LCK = gamma = BMK. And ACL = alpha, so ACK = ACL + LCK = alpha+gamma if L inside ACK (with CL between CA and CK). So CK is CA rotated clockwise by alpha+gamma (if CA as reference). Similarly at B: LBA? K inside angle LBA, KBA=alpha, LBK=beta, so LBA=alpha+beta. BA reference, BK is BA rotated (?) toward inside. So BL is further.
- At N: NC vector = C - N. NL is? LNC = beta, so angle between LN? Wait LNC vertex N between LN and CN. So angle between NL and NC is beta. So NL is NC rotated.

Thus K is intersection of ray from B at angle alpha from BA and ray from M at angle gamma from MB. So for each (alpha,gamma) there is a K; consistency requires that C,K, and direction CA rotated by alpha+gamma are collinear. That gives equation E1(alpha,gamma)=0.
Similarly L intersection of ray from C at angle alpha from CA and ray from N at angle beta from NC (?) gives condition that B,L, and BA rotated by alpha+beta collinear: E2(alpha,beta)=0.

Thus K is fully determined by alpha (since gamma solved from E1), L by alpha (beta solved from E2). Subsequently need to show Ox=0.

We numerically suspect this holds.

## Full proof
TBD.
