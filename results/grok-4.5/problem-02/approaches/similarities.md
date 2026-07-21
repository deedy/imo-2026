# Approach: similar triangles and spiral similarities

## From angles

△BMK: ∠MBK=α, ∠BMK=γ ⇒ ∠BKM = 180-α-γ

△CNL: ∠NCL=α, ∠CNL=β ⇒ ∠CLN = 180-α-β

△ACL: ∠ACL=α, ∠ at A = ∠CAL (part of A), unknown.

Perhaps consider directed angles or inversion, but overkill for IMO.

Since M,N midpoints, vectorially O M = O N in length ⇒ (O-M)·(O-M) = (O-N)·(O-N) ⇒ |O|^2 -2O·M +|M|^2 = |O|^2 -2O·N +|N|^2 ⇒ 2O·(N-M) = |N|^2 - |M|^2
If we place A origin, M=B/2, N=C/2, then 2O·(C-B)/2 = (|C|^2 - |B|^2)/4 ⇒ O·(C-B) = (|C|^2 - |B|^2)/4
But the perp bisector of MN: mid of M N is (B+C)/4, dir MN=(C-B)/2, so perp is vectors X with (X - (B+C)/4 ) · (C-B) =0
I.e. X·(C-B) = (B+C)·(C-B)/4 = (|C|^2 - |B|^2)/4
Yes exactly: O lies on that line iff O·(C-B) = (|C|^2-|B|^2)/4. So if A=0, the condition OM=ON is equivalent to O being on the perpendicular bisector of BC? No of MN, and note mid of BC is (B+C)/2, perp bisector of BC is X·(C-B)= (|C|^2-|B|^2)/2 , different. It's the line parallel to the perp-bisector of BC but shifted, actually it's the Newton line or something? Anyway, since A=0 is origin, this means the projection of O onto (C-B) matches that of midline.

Since O is circumcenter of AKL, with A=0, O is such that |O|=|O-K|=|O-L|, so |O|^2 = |O-K|^2 ⇒ 0 = |K|^2 -2 O·K ⇒ O·K = |K|^2 /2
Similarly O·L = |L|^2 /2
So O is intersection of the perp bisector of AK (which is {X | X·K = |K|^2/2}) and of AL.

To have O·(C-B) = (|C|^2 - |B|^2)/4
We need to show that the solution O to O·K = |K|^2/2 , O·L = |L|^2/2 satisfies that.

If I can find expressions for K, L in terms of vectors.

Perhaps use complex plane with A=0, represent.

Or use area coordinates or bary, but angles suggest using cotangents for ray slopes, or arg.

In complex: let points be complex numbers a=0, b, c.
Then directions.

Perhaps better: use the law of sines to express positions of K,L as.

From earlier:
In △BMK: BM = |b|/2 (A=0), 
BK / sin γ = BM / sin(∠BKM) = ( |b|/2 ) / sin(α+γ)
∠ at K is 180-α-γ so sin=sin(α+γ)
Thus BK = ( |b|/2 ) * sin γ / sin(α+γ)
MK = ( |b|/2 ) * sin α / sin(α+γ)

Direction of BK: the ray from B making angle α with BA.
Since A=0, BA = a-b = -b, so direction from B to A is -b.
Then rotate that by ±α to get direction to K.

Yes, in complex, multiply by e^{i θ} where θ = signed α.

Assume orientation: assume triangle positively oriented (ccw A B C), then at B, from BA to BC is clockwise actually? Wait standard ccw ABC, at B interior angle is turning from BA to BC clockwise, signed negative if standard arg ccw.
Anyway we can take directed angles.

This might get messy but sympy can handle symbolic if we assume.

Perhaps there's better: notice possible isosceles or rotation by 2 something that maps M to N or etc, but since OM=ON, perhaps reflection over the A-aperture bisector if AB=AC, let's check isosceles case has symmetry.

If AB=AC, then by symmetry probably β=γ, K and L symmetric, O on altitude=median which is also midperp of MN, yes holds by sym.

Not new.

Let me try Ceva-like.

Consider triangle BMC? But L not in it.
Note BL is a line from B through to ? L may not on MC.
MC has K? K not on MC generally.

From construction, MK is a ray from M at γ to BK.

Perhaps use trigonometric form of Ceva in △ABC for concurrent, but what concurrent? AK, but K not related to A necessarily, wait we have AK which is line from A to K, AL to L, but they already with O of AKL, but for concurrent need third.
The lines BK (known angle), CL (known), and perhaps something.

BK makes α with BA so angle with sides known: BK divides ∠B into α and B-α.
CL divides ∠C into α and C-α.
If we had a cevian from A dividing, by Ceva (sin) : (sin ∠BAK / sin ∠KAC) * (sin ∠CBL /sin ∠LBA) * (sin ∠ACM /sinuples) wait not.

For BK and CL, they intersect? BK and CL intersect say at P, then etc, but K is not that, K is on BK, L on CL but not their intersection (their intersection would be if concurrent with something).

Perhaps introduce the intersection of BK and CL, call it P, then K on BP, L with other.

But conditions with M N involve MK, NL which are not through P.

Let's calculate angles in other triangles.

For example, look at △CKL or △BKL to chase more equal angles.

We have ∠LCK=γ, ∠BKM=180-α-γ so at K in BMK.

Perhaps ♠ perhaps use directed angles for munitions or use T2 theorem, isogonal conjugate.

Another idea: the condition OM=ON with M N midpoints means that O lies on the perpendicular bisector of MN, and since MN is midline || BC and half, the perp bisector of MN is the line joining the midpoint of MN (which is centroid of A B C? mid MN = (M+N)/2 = (A/2 +B/2 +A/2 +C/2)/2 wait A= ? mid MN = (B+C)/4 +A/2 /? Anyway it is known that the perp bisector of the midline MN is the line starting from the mid of BC? No.

Perhaps use vector geometry or properties that AKperp or.

Since O A = O K = O L =R say (circum R of AKL), so A,K,L on circle centerневе O.

To show |O-M|=|O-N|.

Perhaps find that M and N are related by inversion in the circle or have equal power, or isogonal, or that said and MN is seen under angles or chord. Quiet.

If power or if angle OMA =ONA or something, but if I show triangle OMA congruent ONA or isosceles with base MN  and O on midperp. 

Perhaps use coord symbolically withAngles. 

Let's try to use law ofsines in больше triangles to find relations between α,β,γ first: find the relation that α,β,γ must satisfy.

There should be oneṡ relation.f(α,β,γorigB,C)=0. 

From earlier numeric, almost mio any ratioウンザリ, but from various sols, let's see if there's simple relation like β/γ = something, or α +β +γ = (B+C)/2 =90 MED-A/2, or β+γ=B or.

Let’s check with one sol: for our triangle angB=45, angC~63.43, angA~71.57
One sol α~12.35, β~20.28, γ~35.05 ; α+β~32.63 जाता <45,α+γ~47.4 <63.6
β+γ~55.33,a α+β+γ~67.68 not special.
Another sol α~29.15, β~11.72, γ~28.67 ; sum~69.54
 يبدو not constant. Perhaps 1/α or tan.

Use tan of half or just derive the relation with sine law on the whole. 
