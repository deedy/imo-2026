# Approach: specialization and forcing equality

## Status
in progress

## Idea
The two sides look like RMS and GM of certain pairs. Force cases where equality must hold in classical inequalities, or take limits / specific substitutions to pin down f.

## Details

Write the inequalities again:

(L)  √((x² + f(y)²)/2) ≥ (f(x) + y)/2

(R)  (f(x) + y)/2 ≥ √(x f(y))

All positive so we can square freely.

### Setting y = f(x)

Not sure what that gives.

### Contemplating equality case of AM-GM / RMS-AM

For (R) to hold for all, and if we ever have equality in AM-GM for the pair (f(x), y), i.e., when y = f(x), then
(f(x) + f(x))/2 = f(x) ≥ √(x f(f(x)))
so f(x)² ≥ x f(f(x))

For (L), when f(y) = x, then left is x, so x ≥ (f(x) + y)/2, etc.

### Perhaps f is involution or f(f(x))=x or f=id.

Assume f is bijective or continuous later; first find candidates.

### Take x → 0+ or x → ∞ for fixed y

Fix y > 0. Let a = f(y) > 0 fixed.

(R): (f(x) + y)/2 ≥ √(x a) = √a √x

So f(x) ≥ 2√a √x - y

For small x this is automatic (right side negative eventually). For large x, f(x) ≳ C √x, so f cannot grow slower than √x asymptotically in some sense—but this must hold for every a=f(y), so for all a in the image of f. If image of f is unbounded, f grows at least like √x; if image bounded... we already saw constants fail.

Actually for EVERY fixed y, f(x) + y ≥ 2 √(x f(y)), so
f(x) ≥ 2 √(f(y)) √x - y  for all x large enough that RHS>0.

If I pick y with f(y) large, the coefficient is large. So if im(f) unbounded above, then the lower bound coefficient can be arbitrary large: f(x)/√x is unbounded below... wait no: for each fixed y it's a lower bound, but y also appears subtracted. For each fixed y the liminf f(x)/√x ≥ 2√f(y). If sup f = ∞ then liminf f(x)/√x = ∞, so f(x)/√x → ∞.

On the other hand from (L):
√((x² + a²)/2) ≥ (f(x)+y)/2
so f(x) + y ≤ √2 √(x² + a²) ≤ √2 (x + a)
f(x) ≤ √2 x + √2 a - y

So f(x) = O(x) as x→∞, uniformly in the sense that for each y we have an upper bound linear.

More precisely limsup f(x)/x ≤ √2.

If I can take a→0 if 0 is limit point of im(f), tighter.

Also f(x) ≤ √2 x + C_y.

### From (R) squared or rearrange as quadratic

Consider the right inequality as saying that for all x,y:
y + f(x) ≥ 2 √(x) √f(y)

Think of this as a relation between f(x) and f(y).

Swap x and y?
(R) with swapped: (f(y)+x)/2 ≥ √(y f(x))

So we have both:
f(x) + y ≥ 2 √(x f(y))
f(y) + x ≥ 2 √(y f(x))

Interesting.

Also left inequalities similarly.

### Set x = y

Then √((x² + f(x)²)/2) ≥ (f(x)+x)/2 ≥ √(x f(x))

The right part and left part together sandwich the AM of x and f(x) between RMS of (x,f(x)) and GM of (x,f(x)).

But RMS ≥ AM ≥ GM always holds, with eq throughout iff x = f(x).

Here the middle is AM of (f(x), x) which is same, left is RMS of (x, f(x)), right is GM of (x, f(x)). So when x=y the inequality is AUTOMATICALLY true for any f! It gives no information.

Nice: x=y is free.

### Set y = 1, let c = f(1)

Then √((x² + c²)/2) ≥ (f(x)+1)/2 ≥ √(x c)

So  √2 √(x²+cI²) ≥ f(x)+1 ≥ 2√(c x)

And f(x) ≤ √2 √(x²+c²) - 1

### Try to force f(x) = x

Suppose I want equality in both for some pairs.

From (R): equality in AM-GM would require f(x)=y and also √(x f(y))=y so √(x f(f(x)))=f(x) i.e. x f(f(x)) = f(x)².

If f invertible or something.

### Consider the composition of both inequalities

From (L) and (R), the leftmost ≥ rightmost:
√((x² + f(y)²)/2) ≥ √(x f(y))
⇒ (x
² + f(y)²)/2 ≥ x f(y)
⇒ x² + f(y)² ≥ 2 x f(y)
⇒ (x - f(y))² ≥ 0 always true!

Again automatic. So the outer inequality is free; the two must "meet in the middle".

### Key idea: the only way the chain holds for all x,y is if the middle term is both ≤ RMS and ≥ GM in a compatible way, perhaps forcing f(x)=x, and middle = AM.

Suppose that for every x,y the value m = (f(x)+y)/2 lies between GM=√(x f(y)) and RMS=√((x²+f(y)²)/2).

This must hold universally.

### Let's try to prove f is injective, or surjective, or monotone.

From upper bound f(x) ≤ √2 x + C, lower bound f(x) ≥ k√x - C or better.

Let me try taking y very small.

As y→0+, what happens to f(y)?

From (R) with fixed x: (f(x)+y)/2 ≥ √(x f(y)), so √(x f(y)) ≤ (f(x)+y)/2 → f(x)/2, so f(y) ≤ (f(x)+y)² /(4x) 

As y→0 this gives f(y) bounded (for each fixed x). Since x arbitrary, take x large?

f(y) ≤ (f(x)+y)²/(4x) for all x. Let x→∞: if f(x)=o(√x) wait no we have f(x)=O(x), so (O(x))²/x = O(x) not helpful to force f(y)→0.

If limsup f(x)/x = L ≤√2, then (f(x)+y)²/(4x) ~ (L² x)/4 , still O(x).

From left ineq: as y→0, √((x² + f(y)²)/2) ≥ (f(x)+y)/2 ≈ f(x)/2

so √((x
² + f(y)²)/2) ≥ f(x)/2 roughly, so f(y) can be small.

Not conclusive yet.

### Let's rearrange (R) to bound f(y)

From (R): 4 x f(y) ≤ (f(x)+y)²
f(y) ≤ (f(x)+y)² /(4x)  for all x>0.

This upper bound on f(y) must hold for every x. So
f(y) ≤ inf_{x>0} (f(x)+y)² /(4x)

Similarly from swapped: f(x) ≤ inf_y (f(y)+x)²/(4y)

From the left inequality we can get lower bounds on f.

(L): 2(x² + f(y)²) ≥ (f(x)+y)²
2 f(y)² - 2 y f(x) wait expand:
2x² + 2 f(y)² ≥ f(x)² + 2 f(x) y + y
²
2 f(y)² ≥ f(x)
² + 2 f(x) y + y² - 2x²

Not always positive RHS, so only useful when RHS>0.

Perhaps better to think differently.

### Consider equality cases by choosing y so that GM = RMS of (x, f(y)), which only when x = f(y), then middle must equal that value x.

Yes!!!! When x = f(y), then √((x² + x
²)/2) = x and √(x · x)=x, so both ends equal x, hence equality throughout:
the middle must equal x:
(f(x) + y)/2 = x
so f(x) + y = 2x
y = 2x - f(x)

But x = f(y), so y is such that f(y)=x, i.e. y ∈ f^{-1}(x) (if nonempty).

If f is surjective, then for every x there is y with f(y)=x, and then we must have
(f(x) + y)/2 = x, i.e. y = 2x - f(x)

Moreover this y must be positive, so f(x) < 2x.

And since f(y)=x, we have f(2x - f(x)) = x

This is very promising!

Is f surjective?

### Is f surjective?

Let me prove that f is onto R>0.
