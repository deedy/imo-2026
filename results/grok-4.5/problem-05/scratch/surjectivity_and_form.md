# Proving properties of f

## Goal: show f(x)=x for all x, or find all possible f.

### From earlier:
We always have for all x,y >0:
f(y) ≤ (f(x) + y)² / (4x)

And from (L):
(f(x) + y)² ≤ 2(x² + f(y)²)

### Let's consider the possibility that im(f) is not all of R>0.

Suppose some value a >0 is missed by f, i.e. a ∉ im(f).

Then we never have the forced equality case for that.

But still inequalities.

### Lower bound for f from (L) or (R)

From (R) swapped version: x + f(y) ≥ 2 √(y f(x))
Perhaps solve for lower bound of f(y).

Consider g(t) = √t or something.

### Suppose we assume f continuous, or even differentiable, to find candidates.

Candidates: f(x)=x works, as RMS-AM-GM.

Is f(x)=c/x ? We saw no.
f(x)=c²/x : no.
f(x)=k-x no positively.
f(x)=x^k : try k=1 only.

Let me test f(x)=x^k with code later.

Or f(x)=c x : 
Plug in.
(R): (c x + y)/2 ≥ √(x * c y) = √c √(x y)
Multiply 2: c x + y ≥ 2√c √(x y)
Set √x =u, √y=v: c u² + v
² ≥ 2√c u v
(√c u - v)² + c u² - c u
² + v² - v² wait:
c u
² + v² - 2√c u v ≥ 0
(√c u - v)² + c u² - c u² ? (√c u - v)² = c u² - 2√c u v + v²
So left - that = (c - c)u
² + (1-1)v²=0? Wait our is c u² + v² -2√c uv = (√c u - v)² + c u² - c u² = (√c u - v)² ≥0.
c u² + v² - 2√c uv = [c u
² - 2√c u v + v
²] + (c-c? wait no: the c vs 1 for u²? 

(√c u - v)² = c u² - 2√c uv + v²
So c u² + v² - 2√c uv = (√c u - v)² + (c u² - c u²)? It's equal to (√c u - v)² + c u² - c u² = wait:

c u² + v² - 2√c = [c u² - 2√c uv + v²] + (c - c) no:

Difference: (c u² + v² - 2√c) - (c u² - 2√c + v
²) = 0. So yes = (√c u - v)² ≥0 always!
So (R) holds for f(x)=c x for ANY c>0 !!!!!

Wow! I miscalculated earlier. The AM-GM-like holds with the √c weights.

(√c √x - √y) related, yes it holds with equality when √y = √c √x i.e. y = c x = f(x).

Great, so linear works for (R).

Now check (L) for f(x)=c x:
√((x
² + (c y)²)/2) ≥ (c x + y)/2

Square*2: x² + c² y² ≥ (1/2) (c x + y)²
2x² + 2 c
² y² ≥ c
² x² + 2 c x y + y²
(2 - c²) x² - 2 c x y + (2 c
² - 1) y² ≥ 0 for all x,y>0.

This quadratic form in (x,y) must be positive semidefinite (or ≥0 on first quadrant, but since homogeneous and can scale, and for all ratios, need the quadratic form ≥0 everywhere, or check discriminant).

Let t = x/y >0, divide by y²:
(2-c
²) t² - 2 c t + (2 c
² -1) ≥0 ∀ t>0.

Let p(t) = A t² - 2c t + B with A=2-c², B=2c²-1.

Need p(t)≥0 ∀t>0.

Cases on c.

If A>0 i.e. c < √2, then parabola opens up, need either disc≤0 or if disc>0 the roots not making negative in (0,∞).

Disc D = 4c² - 4 A B = 4[ c
² - A B ]

A B = (2-c²)(2c²-1) = 2·2c² -2·1 -c²·2c² +c
² = 4c
² -2 -2 c^4 + c² = -2c^4 +5c² -2

Wait: (2-c²)(2c²-1)= 2*(2c
²) +2*(-1) + (-c
²)*(2c
²) + (-c
²)*(-1) = 4c² -2 -2 c^4 + c² = -2c^4 +5c² -2

Yes. So A B = -2c^4 +5c² -2
c² - AB = c
² - (-2c^4 +5c² -2) = c
² +2c^4 -5c² +2 = 2c^4 -4c² +2
= 2(c^4 -2c² +1)= 2(c
²-1)²

Nice! D/4 = 2(c²-1)² ≥0 always.
D= 8 (c²-1)²

So roots exist when c≠1: actually always disc≥0, =0 iff c=1.

When c=1, A=2-1=1>0, B=2-1=1, p(t)=(t-1)²≥0 perfect.

When c≠1, roots: [2c ± √D ] / (2A) = [2c ± √8 |c²-1| ] /(2A)= [ c ± √2 |c
²-1| ] / A

Since D=8(c²-1)², √D= √8 |c²-1|= 2√2 |c
²-1|

Yes roots [2c ± 2√2 |c²-1| ] / 2A = [ c ± √2 |c²-1| ] / A

For p≥0 on (0,∞), since opens up only if A>0 i.e. c√2, if A=0 i.e c=√2, then p becomes linear: -2√2 t + (2*2 -1)= -2√2 t +3 , which for large t →-∞, fails.

If A<0 (c>√2), opens down, →-∞ as t→∞, fails.

So only possible c<√2. Now A>0, p has two roots (if c≠1), and p≥0 outside the roots. So for p≥0 on all (0,∞), we need no root in (0,∞), or the interval between roots doesn't intersect (0,∞) positively -- but since opens up, p negative between roots, so we need the open interval (root-, root+) disjoint from (0,∞), meaning both roots ≤0, or... impossible to cover all (0,∞) if both roots real and A>0 unless the negative dip is left of 0 i.e. larger root ≤0.

So need larger root ≤0.

Let's compute.

Let δ = |c²-1|

Note if c>1, |c²-1|=c
²-1; if c<1, 1-c².

Case 1: 0<c<1. Then A=2-c²>2-1=1>0, B=2c²-1 which may be neg if c<1/√2.

Larger root = [ c + √2 (1-c²) ] / A   since | |=1-c
²
Is this >0? Numerator c + √2(1-c
²)>0 always, A>0 so larger root >0. Thus p dips below in (0,∞). Fail!

For example c=0.5, we expect failure.

Case 2: c>1, c<√2. Then |c²-1|=c²-1
Larger root = [c + √2 (c²-1) ] / A
Num >0, A=2-c²>0, so larger>0. Fail!

Both cases larger root positive?? So only when disc=0 i.e. c=1 ??

Is smaller root negative large positive?

But yes when disc>0 both cases larger root >0, so p takes negative values. Thus ONLY c=1 works for f(x)=c x !!

Confirm calculation of larger root for c>1 always >0 yes. For c<1 yes.

Is there possibility larger ≤0? Only if num ≤0 but num = c + √2 |c
²-1| ≥c >0. Always! So always larger root >0 when A>0 and c≠1.

Hence the ONLY homogeneous linear is f(x)=x.

Great, confirms f(x)=x is a candidate, and only among ray multiples.

Now, are there others?

Perhaps f(x)=1/x ? Check (R): (1/x + y)/2 ≥ √(x * 1/y)= √(x/y)
Fails for large x: left~y/2 right large.

Or f=x^k no.

Back to analysis.