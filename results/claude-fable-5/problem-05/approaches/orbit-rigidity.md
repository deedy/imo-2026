# Approach: equality at x = f(y), arithmetic orbits, asymptotic sandwich

**Status: successful — this is the approach used in the final proof (`current.md`).**

## Idea
Square both inequalities:
(1) `2x^2 + 2 f(y)^2 >= (f(x)+y)^2`, (2) `(f(x)+y)^2 >= 4 x f(y)`.
The middle quantity `(f(x)+y)^2` is squeezed between `4x f(y)` and `2x^2+2f(y)^2`,
and these two bounds coincide exactly when `x = f(y)` (their difference is `2(x-f(y))^2`).
So `x = f(y)` forces **equality in both**, giving the exact identity
`f(f(y)) = 2 f(y) - y`.

## Consequences
- Orbits `y_{n+1} = f(y_n)` satisfy `y_{n+2} = 2y_{n+1} - y_n`, hence are arithmetic
  progressions `y_n = y + n g(y)` with `g = f - id`. Positivity of the range forces
  `g >= 0`, i.e. `f(y) >= y`, and `f(y + n g(y)) = y + (n+1) g(y)`.
- If `g(a) = d > 0`, use the orbit points `y = a + nd` (where `f(y) = y + d`) in (1),(2),
  picking the orbit point with `y + d = x + eps`, `|eps| <= d/2`. Elementary sqrt
  estimates give, for all `x >= a + d`:
  `d - d^2/(4x) <= g(x) <= d + d^2/(16x - 4d)`.
- Sandwich as `x -> oo`: all positive values of `g` coincide (call it `d`); and the lower
  bound is `> 0` for `x >= a+d`, so `g(x) = d` exactly on `[a+d, oo)`.
- Downward bootstrap: if `f = id + d` on `[T, oo)`, take `x = y + d >= T` in (1),(2):
  (1) gives `f(y) >= y+d`, (2) gives `f(y) <= y+d`. Induct down by steps of `d` to cover
  all of `R_{>0}`.

## Answer
`f(x) = x + c` for a constant `c >= 0` (sufficiency = QM-AM-GM for the pair `x`, `y+c`).

## Dead ends noted along the way
- Setting `x = y` in either squared inequality gives `(f(x)-x)^2 >= 0` — vacuous.
- Trying `f(x) = kx`: forces `(k-1)^2 <= 0`, so only `k=1`; linear ansatz alone doesn't
  reveal the `+c` family — needed to test affine maps.
- Trying to derive a contradiction from a *single* positive gap fails: `f = id + d`
  actually IS a solution, so the rigidity must aim at "gap is globally constant",
  not "gap is zero".
- Local analysis around a fixed point `b` (`f(b)=b`) gives only bounds like
  `f(y) <= (b+y)^2/(4b)`, too weak far from `b`; the asymptotic sandwich + downward
  bootstrap circumvents this entirely.
