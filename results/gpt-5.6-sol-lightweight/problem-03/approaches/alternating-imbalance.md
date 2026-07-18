# Alternating-imbalance approach

## Idea
Sort the final pieces decreasingly. Optimal claiming gives Liu the odd-indexed pieces. If their sum is $O$ and the even-indexed sum is $E$, introduce the imbalance $\Delta=O-E$. Since $O+E=1$, Liu gets $(1+\Delta)/2$.

The marking game is therefore exactly a problem about how much $n$ splits can alter the alternating imbalance. The relevant refinement lemma has matching extremal statements: every collection of at most $n+1$ pieces of total $1$ can be refined using $n$ splits until $\Delta\le(2^{n+1}-1)^{-1}$, while the geometric collection proportional to $1,2,\ldots,2^n$ retains imbalance at least its smallest member after any $n$ splits.

## Status
Successful. It gives
\[
c_n=\frac12\left(1+\frac1{2^{n+1}-1}\right)=\frac{2^n}{2^{n+1}-1}.
\]

## Details
Liu marks the stick so that the initial interval lengths, in any spatial order, are
\[
\frac1{2^{n+1}-1},\frac2{2^{n+1}-1},\ldots,
\frac{2^n}{2^{n+1}-1}.
\]
The lower half of the refinement lemma ensures that Xiang's at most $n$ further cuts cannot reduce $\Delta$ below $1/(2^{n+1}-1)$. Conversely, whatever initial partition Liu makes has at most $n+1$ members, and the upper half of the lemma supplies Xiang with at most $n$ cuts reducing $\Delta$ to this same bound. This proves both guarantee and optimality.
