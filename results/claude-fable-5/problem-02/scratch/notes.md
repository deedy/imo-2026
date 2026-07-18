# Exploration notes (imo-2026-02)

Chronology of the discovery:

1. $OM=ON \iff \operatorname{pow}(M,\omega)=\operatorname{pow}(N,\omega)$ ($M,N$ at equal... no —
   actually via median formula: $4(OM^2-ON^2)=2(\operatorname{pow}(B,\omega)-\operatorname{pow}(C,\omega))-c^2+b^2$).
2. Angle condition $\angle LBK=\angle LNC$ smells like a concyclicity where a point of line $BK$
   meets line $NC=AC$. Define $Y=$ ray $BK\cap AC$: then $\angle LBY=\angle LNY$ gives $B,N,L,Y$ concyclic.
   Similarly $X=$ ray $CL\cap AB$ with $\angle KCX=\angle KMX$ gives $C,M,K,X$ concyclic, and
   $\angle KBA=\angle ACL$ gives $B,X,Y,C$ concyclic (equal angles subtending $XY$).
3. Observations found numerically before proving:
   - $\operatorname{pow}(A,\omega_K)=\operatorname{pow}(A,\omega_L)$ (radical axis of $\omega_K,\omega_L$ passes through $A$ and through $R=BY\cap CX$).
   - rad axis of $(\omega_1,\omega_L)$ is $BY$; of $(\omega_1,\omega_K)$ is $CX$.
   - KEY: $\operatorname{pow}(B,\omega)=BM\cdot BX$ and $\operatorname{pow}(C,\omega)=CN\cdot CY$ — then everything closes since $AB\cdot AX=AC\cdot AY$.
4. First proof attempt: define $K^*$ = second point of $\omega_K$ on $BY$, show $A,K,K^*,L$ concyclic
   via two radical-axis coincidences. Works, but tangency subcases ($BY$ tangent to $\omega_K$ etc.) get messy.
5. Final clean mechanism: $F=\operatorname{pow}(\cdot,\omega)-\operatorname{pow}(\cdot,\omega_K)-\operatorname{pow}(\cdot,\omega_L)+\operatorname{pow}(\cdot,\omega_1)$
   is affine and vanishes at $A$ (uses $cx=by$), at $K$ (both $\omega_1,\omega_L$ contain chord $BY\ni K$),
   at $L$ (both $\omega_1,\omega_K$ contain chord $CX\ni L$). Hence $F\equiv0$; evaluate at $B$, $C$. No radical axes needed.
6. Only genuine configuration work: unsigned→directed angle translation (signs pinned by
   $K,L$ interior to $ABC$ + the two "inside angle" hypotheses), crossbar for existence of $X,Y$,
   and the degenerate chords $X=M$ / $Y=N$ (handled as tangencies via directed tangent–chord).

Sign conventions verified numerically in code/check_signs.py; everything else in code/verify.py, code/verify2.py.
