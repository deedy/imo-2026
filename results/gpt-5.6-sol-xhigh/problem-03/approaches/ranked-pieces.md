# Ranked-pieces reduction

## Idea
After all cuts, let the piece lengths in nonincreasing order be $x_1\ge x_2\ge\cdots\ge x_m$. The claiming game is a draft of independent nonnegative values. At every turn, claiming a currently largest piece is optimal: an exchange/backward-induction argument shows there is a subgame-perfect outcome in sorted order. Thus Liu Bang's total is
\[
F(x_1,\dots,x_m)=x_1+x_3+x_5+\cdots.
\]
The marking game is therefore a max-min problem for this odd-rank sum.

## Status
Valid reduction; exact minimax value remains to be found.
