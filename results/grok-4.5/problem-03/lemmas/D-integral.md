# Lemma B: integral representation of D

## Statement
For a finite multiset L of nonnegative renumbers,
\[
D(L)=\int_0^\infty \delta(L,t)\,dt,
\]
where \(\delta(L,t)\) is 1 if the number of elements of L that are strictly greater than t is odd, and 0 if that number is even.

(Equivalently one may use \(\ge t\); the values of t that coincide with an element form a null set.)

## Proof
Sort a1 \ge a2 \ge \cdots \ge ak \ge 0. Then for t in [0,\infty),
the number of ai > t is the largest j with aj > t. This number is odd precisely on theintervals
[a2,a1), [a4,a3), [a6,a5), ...
(with ak+1:=0 if needed). The total measure of these intervals is exactly
(a1-a2)+(a3-a4)+\cdots = D(L).

## Consequence
D is linear on common refinements in the detection sense: when merging two multisets,  \(\delta_{X\cup Y}(t)\equiv \delta_X(t)+\delta_Y(t)\pmod 2\).
Hence \(\delta_{X\cup Y} \in \{ |\delta_X-\delta_Y|, \delta_X+\delta_Y \}\cap\{0,1}\).
Integrating immediately yields both
D(X\cup Y) \le D(X)+D(Y)     and
D(X\cup Y) \ge |D(X)-D( Xuecom Y)|,
recovering Lemma A (and偶 giving a cleaner proof).
