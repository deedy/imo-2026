# Approach: power-of-a-point reduction + trig constraints (successful)

## Idea
$OM=ON \iff \operatorname{pow}(M)=\operatorname{pow}(N)$ wrt $\omega=(AKL)$. By Apollonius in $\triangle OAB,\triangle OAC$ (using $OA=R$):
$\operatorname{pow}(M)=\frac{\operatorname{pow}(B)}2-\frac{c^2}4$, $\operatorname{pow}(N)=\frac{\operatorname{pow}(C)}2-\frac{b^2}4$.
So target: $\operatorname{pow}(B)-\operatorname{pow}(C)=\frac{c^2-b^2}2$.

## Key structural facts (all verified numerically and symbolically)
1. Law of sines in $\triangle BMK,\triangle CNL,\triangle BKC,\triangle BCL$ gives relations R1–R4 for $p=BK$, $q=CL$.
2. Eliminating $\beta,\gamma$: $p,q$ satisfy **quadratics** ConsP, ConsQ (see current.md Step 3). Derivation verified exactly by sympy.
3. Coordinates $A=0,B=c,C=be^{iA}$: $K=c-pe^{-i\varphi}$, $L=e^{iA}(b-qe^{i\varphi})$; power formulas (2),(3).
4. The power formulas minus their target values are *linear combinations of ConsP, ConsQ* (identities (4),(5)), so they vanish. Verified: coefficient comparison in $p,q$ reduces everything to one trig identity, proved by hand (see current.md Step 5).

## Status: complete success — full proof in current.md.
