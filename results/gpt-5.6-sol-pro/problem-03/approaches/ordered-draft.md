# Ordered-draft reduction

## Idea
For a fixed multiset of final piece lengths, the claiming phase should reduce to taking pieces in nonincreasing order. Thus Liu's total is the sum of odd-ranked lengths. The cutting game is then a refinement extremal problem.

## Status
Active.

## Details
Write the final lengths as
\[
x_1\ge x_2\ge\cdots\ge x_m>0.
\]
Since both players value every piece by its length and the game is constant-sum, taking a currently longest piece is optimal: this will be proved rigorously by backward induction/exchange. The resulting Liu payoff is
\[
F(x_1,\dots,x_m)=x_1+x_3+x_5+\cdots.
\]
Equivalently, if \(A=x_1-x_2+x_3-x_4+\cdots\), then
\[
F=\frac{1+A}{2}.
\]
For odd \(m\), the alternating excess also has the layer-cake form
\[
A=\int_0^\infty \mathbf 1_{\{\#\{i:x_i\ge t\}\text{ is odd}\}}\,dt.
\]
Xiang's cuts refine the initial multiset of interval lengths chosen by Liu.

Small case \(n=1\): if Liu's two lengths are \(a\ge 1-a\), Xiang's largest achievable middle final piece has supremum \(1-a\) for \(a\le2/3\), and \(a/2\) for \(a\ge2/3\). Thus Liu's worst-case payoff is \(a\) in the first range and \(1-a/2\) in the second; it is maximized at \(a=2/3\), giving \(c=2/3\).
