# Lemma: an integer-entry cut

## Statement
Let \(N\ge2\) be an integer and let \(a,b,c>0\) satisfy \(a+b+c=N\). If none of \(a,b,c\) is an integer, then, after possibly permuting them, there is an integer \(k\) such that
\[
b<k<a+b=N-c.
\]

## Proof
If one of \(a,b,c\), say \(a\), is greater than \(1\), choose either of the other two numbers as \(b\). Since \(b\notin\mathbb Z\), the number \(k=\lceil b\rceil\) satisfies
\[
b<k<b+1<b+a.
\]

It remains to consider the case in which all three numbers are at most \(1\). As none is an integer, all three are strictly less than \(1\). Hence \(N=a+b+c<3\). Also \(N\ge2\), so \(N=2\). Let \(a,b\) be the two largest of the three numbers. The remaining number \(c\) is less than \(2/3\), for otherwise all three would be at least \(2/3\), with equality throughout forced by their sum, contrary to their being ordered if strict; more directly, \(a+b=2-c>1\) since \(c<1\). Taking \(k=1\), and ordering the chosen pair so that \(b<1\), gives
\[
b<1<a+b.
\]
This proves the lemma. \(\square\)
