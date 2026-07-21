# Lemma: properties of the alternating-sum functional \(D\)

## Definition
For a finite list (multiset) \(L\) of nonnegative real numbers, write the nonincreasing rearrangement \(a_1\ge a_2\ge\cdots\ge a_k\) and set
\[
D(L)\,:=\,\sum_{i=1}^{k}(-1)^{i-1}a_i
\]
(with \(D(\emptyset)=0\)).

If the two players alternately select pieces, always taking a currently longest remaining piece, with Liu Bang first, then Liu Bang’s total length equals \(\frac12\bigl(\sum L + D(L)\bigr)\) and Xiang Yu’s total equals \(\frac12\bigl(\sum L - D(L)\bigr)\). (In the actual game the players may pick any piece, but an optimal opponent will never leave a longer piece than necessary; the value of the game on a fixed multiset is exactly the greedy alternating sum above.)

## Lemma A
For any two finite multisets \(X,Y\) of nonnegative reals,
\begin{align}
D(X\cup Y)&\le D(X)+D(Y),\tag{sub}\\
D(X\cup Y)&\ge\bigl|D(X)-D(Y)\bigr|.\tag{rev}
\end{align}

## Proof
Both statements are proved simultaneously by induction on \(m:=|X|+|Y|\).

If \(m=0\) both sides are zero. Assume $m\ge 1$ and the claim holds for all pairs of smaller total cardinality. Let \(U=X\cup Y\) and let \(\mu=\max U\). Without loss of generality at least one copy of \(\mu\) lies in \(X\). Write \(X'=X\setminus\{\mu\}\) (remove one copy). Then the sorted list of \(U\) begins with \(\mu\), so
\[
D(U)=\mu-D(X'\cup Y).
\]
(The same formula holds in the presence of ties because equal leading terms merely continue the alternating pattern.)

**Subadditivity.**  
By the reverse-triangle inequality already known for the smaller instance \((X',Y)\),
\[
D(X'\cup Y)\ge\bigl|D(X')-D(Y)\bigr|\ge D(X')-D(Y).
\]
Hence
\[
D(U)=\mu-D(X'\cup Y)\le\mu-\bigl(D(X')-D(Y)\bigr)=\bigl(\mu-D(X')\bigr)+D(Y).
\]
But \(\mu=\max X\) (it is a global maximum), so \(D(X)=\mu-D(X')\). Therefore \(D(U)\le D(X)+D(Y)\).

**Reverse triangle.**  
By subadditivity already known for the smaller instance,
\[
D(X'\cup Y)\le D(X')+D(Y),
\]
hence
\[
D(U)=\mu-D(X'\cup Y)\ge\mu-D(X')-D(Y)=D(X)-D(Y).
\]
Symmetrically (swap the labels of \(X\) and \(Y\), or repeat the argument if the global max belongs to \(Y\)) one obtains \(D(U)\ge D(Y)-D(X)\). Consequently
\[
D(U)\ge\bigl|D(X)-D(Y)\bigr|.
\]

This completes the inductive step.

## Immediate corollaries
1. If \(D(Y)\le 0\) then \(D(X\cup Y)\ge D(X)\).  
2. \(D\) is continuous with respect to the elements (for fixed cardinality) and invariant under adding zero elements.  
3. For a single part of length \(S\), \(D(\{S\})=S\). After any subdivision into smaller parts the resulting \(D\) is at most \(S\).
