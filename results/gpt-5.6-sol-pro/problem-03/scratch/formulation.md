# Exploratory formulation

Assume Liu uses exactly \(n\) cuts, with initial lengths \(a_1,\ldots,a_{n+1}\). If the final piece lengths, sorted decreasingly, are \(x_1\ge\cdots\ge x_m\), the draft payoff is
\[
F=\sum_{j\text{ odd}}x_j=\frac12\left(1+D\right),\qquad
D=x_1-x_2+x_3-x_4+\cdots.
\]
The layer-cake identity is
\[
D=\int_0^\infty \bigl(\#\{j:x_j\ge t\}\bmod 2\bigr)\,dt.
\]
Thus Xiang minimizes the measure of the XOR of vertical intervals \([0,x_j]\).

A cut replacing a piece of length \(a=x+y\), \(x\ge y\), replaces its parity profile \([0,a]\) by the band \((y,x]\). In particular, cutting an initial interval into two equal pieces cancels its parity profile entirely. With \(n\) cuts Xiang can internally halve-pair any \(n\) of Liu's \(n+1\) intervals, showing \(D\le \min_i a_i\).

Exact paired configurations can be represented by a weighted multigraph on the initial intervals: an edge of weight \(w\) between two vertices means one part of size \(w\) in each interval; a loop means two such parts in one interval. With \(2n+1\) final parts there are \(n\) pairs and one singleton; the alternating excess is then exactly the singleton length. This graph viewpoint may identify the extremal initial partition.
