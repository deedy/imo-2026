# Lemma: value of the claiming phase

## Statement
Let the lengths of the available pieces, in nonincreasing order, be
\(x_1\ge x_2\ge\cdots\ge x_m\ge0\). If two players alternately claim one
piece, with the first player moving first and both maximizing their own total
length, then the first player's value is
\[
F=x_1+x_3+x_5+\cdots.
\]
Consequently, since \(\sum_i x_i=1\),
\[
F=\frac{1+D}{2},\qquad
D=x_1-x_2+x_3-x_4+\cdots.
\]

## Proof
If the first player always takes a largest remaining piece, then immediately
before their \(j\)-th move at most \(2j-2\) pieces have disappeared. Hence a
remaining largest piece has length at least \(x_{2j-1}\), and this strategy
guarantees at least \(\sum_jx_{2j-1}\).

Conversely, suppose the second player always takes a largest remaining piece.
Immediately before their \(j\)-th move at most \(2j-1\) pieces have
disappeared. Thus the piece they take has length at least \(x_{2j}\). They
therefore obtain at least \(\sum_jx_{2j}\), leaving the first player at most
\(1-\sum_jx_{2j}=\sum_jx_{2j-1}\). The two bounds agree, proving the value.
The displayed formula for \(F\) follows by adding
\(\sum_i x_i=1\) and \(D\).
