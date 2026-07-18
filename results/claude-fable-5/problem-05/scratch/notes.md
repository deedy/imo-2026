# Scratch notes imo-2026-05

Inequalities (squared, equivalent since everything positive):
(1) 2x^2 + 2 f(y)^2 >= (f(x)+y)^2
(2) (f(x)+y)^2 >= 4 x f(y)

Key trick: x = f(y) makes (1) give 2f(y) >= f(f(y)) + y and (2) give f(f(y)) + y >= 2 f(y).
=> f(f(y)) = 2 f(y) - y  (equality in BOTH at x = f(y)).

Orbits y_{n+1} = f(y_n) satisfy y_{n+2} = 2y_{n+1} - y_n => arithmetic progression
y_n = y + n(f(y)-y) > 0 for all n => f(y) >= y. g(y) := f(y)-y >= 0.
Also f(y + n g(y)) = y + (n+1) g(y).

Candidate check: f(x) = x + c, c >= 0: with u = x, v = y + c,
sqrt((u^2+v^2)/2) >= (u+v)/2 >= sqrt(uv): QM-AM-GM. Works!

Rigidity: gap d>0 at a => orbit a+nd has gap exactly d. Using orbit points as y in
(1),(2), with t = a+(n+1)d = x + eps, |eps| <= d/2:
lower (from (2)): f(x) >= 2 sqrt(x(x+eps)) - (x+eps-d) >= x + d - eps^2/x >= x+d - d^2/(4x)
upper (from (1)): f(x) <= sqrt((2x+eps)^2 + eps^2) - (x+eps-d) <= x + d + eps^2/(2(2x+eps))
=> for x >= a+d:  d - d^2/(4x) <= g(x) <= d + d^2/(16x-4d).

=> all positive gaps equal (sandwich as x->infty); lower bound > 0 for x >= a+d
=> g(x) = d for x >= a+d.

Downward bootstrap: if f = id + d on [T,inf), then for y>0 with y+d>=T take x=y+d:
(1): 2(y+d)^2 + 2f(y)^2 >= (y+2d+y)^2 = 4(y+d)^2 => f(y) >= y+d.
(2): 4(y+d)^2 >= 4(y+d) f(y) => f(y) <= y+d.
Induct down; covers all y > 0.

sqrt estimates needed:
- sqrt(1+u) >= 1 + u/2 - u^2/2 for -1 <= u <= 3  (squares to -(u^2/4)(u-3)(u+1) >= 0)
- sqrt(A^2+B) <= A + B/(2A) for A>0, B>=0.

ANSWER: f(x) = x + c for a constant c >= 0.
