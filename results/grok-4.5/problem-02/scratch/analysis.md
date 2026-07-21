# Angle chasing / setup

Triangle ABC.
M midpoint AB, N midpoint AC.

K ∈ int(△BMC)
L ∈ int(△BNC)

Conditions:
- K inside ∠LBA  (so ray BK is between BL and BA? ∠LBA is the angle at B between L,B,A so rays BL and BA. K inside that angle means ray BK is between BL and BA.)
- L inside ∠ACK (ray CL between CA and CK)
- ∠KBA = ∠ACL  := α
- ∠LBK = ∠LNC  := β
- ∠LCK = ∠BMK  := γ

Note ∠KBA is part of ∠ABC, since K inside ∠LBA which is inside ∠ABC (assuming L properly placed).

From B:
Rays from B: BA, then BK (since K in ∠LBA), then BL, then maybe BC?

K in △BMC: from B, BM is along BA but opposite? Wait no: M is between A and B, so point M is on AB, ray BM is from B through M to A, so ray BM = ray BA.

That's important! Points A-M-B collinear, M between A and B.
So AB from A to B: A, M, B.
From B, the side BA is B to A: B, M, A. So ray BA goes through M.
Triangle BMC has vertices B, M, C. Side BM is part of BA.
So interior of △BMC is the region between rays BM(=BA) and BC, but only up to the line MC, not the whole angle ABC; specifically the part "beyond" M towards C, but since M is on BA, △BMC is half-ish.

From point B, the directions into △BMC are directions between ray BM (along BA) and ray BC, and the points K in △BMC are seen from B in angles strictly between ∠MBC = ∠ABC.

So K is inside angle ABC, ray BK between BA and BC.

L in △BNC: N on AC, BNC has points B,N,C. From B, N is interior-ish, ray BN is inside angle ABC (or BAC?).

Anyway.

∠KBA: angle between BK and BA, so that's the angle from BA to BK, call it α.
So ∠ABK = α.

Then ∠LBK = β: angle between LB and BK is β.
So from BA to BK is α, then BK to BL is β, so from BA to BL is α+β, assuming the order BA, BK, BL (which matches K inside ∠LBA: order BA, BK, BL).

Then there is also from BL to BC some angle.

Now ∠LNC = β.
N mid AC, L in BNC, ∠LNC is angle at N in triangle LNC, between LN and NC.

NC is part of AC, since N mid AC, A-N-C, so ray NC is along AC away from A.

This is getting complex; points on different vertices.

∠ACL = α: C, angle between AC and CL is α. So ∠ACL = α, thus ray CL makes α with CA.

Order: L inside ∠ACK, so rays CA, CL, CK in that order? ∠ACK is between CA and CK, L inside means CL between CA and CK.
Yes, so ∠ACL = α, then ∠LCK = γ, so ∠ACK = α + γ.

Then ∠BMK = γ: at M, angle between BM and MK is γ? ∠BMK is angle at M in B,M,K: rays MB and MK.

Points: at M on AB.

Perhaps use trigonometry Ceva in some triangles, or barycentric coordinates, or trig form for angles.

Since we need OM=ON, and M,N midpoints, perhaps O lies on the A-median or rather on the perp bisector of MN, which is the set of points equidistant to M and N, i.e. the line through midpoint of MN perpendicular to MN, and since MN||BC, it's //.

Perhaps reflection over the angle bisector if isosceles, but general.

I could assume BC coordinates, use complex plane or cartesian.

Let me try to assume specific triangle to find possible K,L, to see if configuration is unique or what the locus is.

Perhaps the conditions determine a unique pair (K,L) up to something, or a family, but for any such, OM=ON.

Is there freedom? Three angle equalities relating K and L, and positions 4 degrees of freedom (2 each), plus the inside conditions, so perhaps 1-parameter or discrete.

2+2=4, three conditions, so possibly curves, but prove always OM=ON.

To understand better, let's use angle notation more carefully, introduce more angles.

Let ∠ABC = B, ∠ACB = C, ∠BAC = A.

Then ∠ABK = α, so remaining ∠KBC = B - α. But there's BL: ∠ABL = α + β, so ∠LBC = B - α - β.

At C: ∠ACL = α, so ∠LCB = C - α? No: ∠ACB = C = ∠ACL + ∠LCK + ∠KCB = α + γ + ∠KCB, so ∠KCB = C - α - γ.

L is in BNC, K in BMC, so CK crosses etc.

Also ∠BMK = γ.
At M: line AB is straight, M mid.
Points K from M: MK.

Triangle BMK: angles at M is γ = ∠BMK.
What is side: also there's point C, MC is a line (median? M mid AB, MC is from M to C, not a median usually, median would be from C to mid AB which is exactly CM! Yes, CM is a median.

Medians: from C to midpoint of AB which is M, yes CM median.

From B to N mid AC, BN median.

Etc.

In △BMC, we have K, angles.

Also ∠LNC = β at N in △LNC.

At N: AC straight A-N-C.
BN is median.
L from N: NL.

Perhaps use trigonometric identity for cevians.

I could use coordinate geometry with sympy to verify for a specific triangle if such K,L exist, and check OM=ON.

Let's try to place triangle in coordinates.