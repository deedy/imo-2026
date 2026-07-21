# Lemma: Closure of universally winning angles under addition

Statement: Let θ with 0<θ<180, θ≠90. Define a set S_k of angles such that every triangle containing an angle from S_k is in W_k. If s,s'∈S_k and s+s'<180 then s+s'∈S_{k+1}.

Proof: Let T = (p,q,s+s') ∈ all triangles containing s+s'. Mulan can choose donor D=s+s' and split x=s, D-x=s'. Then child1 = (p,s,q+s') contains s, child2 = (q,s',p+s) contains s'. Both are in W_k, so T ∈ W_{k+1}. Hence s+s' is universally winning at level k+1.

Corollary: If θ∈S0 then kθ∈S_{k-1} for all k with kθ<180.

Status: proved.
