# Finite-horizon backward winning sets

## Idea
Define $W_0$ as triangles already containing $\theta$, and let $W_{r+1}$ consist of triangles for which some legal cut has both children in $W_r$ (allowing the nested convention $W_r\subseteq W_{r+1}$).

## Status
Abandoned as a full set-classification method; it suggested the successful multiple-angle induction.

## Details
Trying to describe every $W_r$ produces complicated unions of line segments in the angle simplex. The tractable part is that the hyperplanes “one angle equals $m\theta$” enter successively: splitting $m\theta$ as $\theta+(m-1)\theta$ sends the two children to lower-rank winning classes. This observation became the multiple-angle forcing lemma. A full explicit computation of the sets $W_r$ was unnecessary once the complementary cut-point construction and safe invariant were found.
