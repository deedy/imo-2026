# Approach: Angle-triple game and multiples invariant

Idea: Model triangle by angles (p,q,D). Cut splits D = x + (D-x) producing children (p,x,q+D-x) and (q,D-x,p+x).

Define W0 = contains θ, Wn+1 = triangles from which Mulan can move to make both children in Wn.

First step: W1\W0 contains 2θ if 2θ<180, else empty (except θ=90 where W1 = all).

Observation: If s and s' are universally winning (every triangle containing them is in Wk), then s+s' <180 is universally winning at level k+1 by cutting s+s' into s and s'.

Hence all multiples kθ <180 become universally winning, at level k-1.

If 180 = nθ integral, then any triangle with no multiple can be moved into multiplicity: pick minimal angle p, let r = next multiple minus p, 0<r<θ ≤60. Split maximal angle D into r and D-r, yielding both children containing multiples. Hence all triangles winning in ≤ n-1 moves.

If 180 not multiple, set I = triangles with no angle kθ. For T in I, any split has at least one child in I (four cases). Indeed assuming both children contain multiples leads to either D multiple, p multiple, q multiple, or 180 multiple, contradiction. So adversary can stay in I forever, avoiding θ.

Thus characterization 180/θ ∈ N.

Status: complete.
