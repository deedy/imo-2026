# Findings so far

## Setup / notation
- $A, B, C$ = angles of triangle; $a = BC, b = CA, c = AB$.
- $\varphi = \angle KBA = \angle ACL$; $\beta = \angle LBK = \angle LNC$; $\gamma = \angle LCK = \angle BMK$.
- $K$ inside $\angle LBA$ ⇒ $\angle LBA = \beta+\varphi$; $L$ inside $\angle ACK$ ⇒ $\angle ACK = \gamma+\varphi$.
- $p = BK$, $q = CL$.

## Key relations (verified numerically)
1. From $\triangle BMK$ ($\angle KBM=\varphi$, $\angle BMK=\gamma$, $BM=c/2$): $p=\frac{c\sin\gamma}{2\sin(\varphi+\gamma)}$, and $\cot\angle BAK = \cot\varphi+2\cot\gamma$.
2. From $\triangle CNL$: $q=\frac{b\sin\beta}{2\sin(\varphi+\beta)}$, $\cot\angle CAL = \cot\varphi+2\cot\beta$.
3. Coupling conditions give (via law of sines matches), equivalently:
   - EqB: $c\sin(\beta+\varphi)=b\sin(A+\beta+\varphi)-q\sin(A+\beta+2\varphi)$  [=$\angle LBK=\beta$]
   - EqC: $b\sin(\gamma+\varphi)=c\sin(A+\gamma+\varphi)-p\sin(A+\gamma+2\varphi)$  [=$\angle LCK=\gamma$]
4. ELIMINATING $\beta,\gamma$: get QUADRATICS (verified numerically!):
   - ConsP: $2s_{A+\varphi}p^2-(2s_A+s_{A+2\varphi})cp+c^2s_{A+\varphi}-bcs_\varphi=0$
   - ConsQ: $2s_{A+\varphi}q^2-(2s_A+s_{A+2\varphi})bq+b^2s_{A+\varphi}-bcs_\varphi=0$

## Target reformulations
- $OM=ON \iff \operatorname{pow}(M)=\operatorname{pow}(N)$ wrt circle $AKL$
- $\iff \operatorname{pow}(B)-\operatorname{pow}(C)=\frac{c^2-b^2}{2}$
- $\iff O_x = \frac a2 + \frac{c^2-b^2}{4a}$ in coords $B=(0,0),C=(a,0)$.

## Coordinates (A at origin)
- $A=0$, $B=c$ (real), $C=be^{iA}$.
- $K=c-pe^{-i\varphi}$, $L=e^{iA}(b-qe^{i\varphi})$.
- $|K|^2=c^2-2cp\cos\varphi+p^2$; $|L|^2=b^2-2bq\cos\varphi+q^2$.
- $\Delta:=\Im(\bar KL)=bc\sin A-(bp+cq)\sin(A+\varphi)+pq\sin(A+2\varphi)=2[AKL]$.
- FACTORIZATION: $\bar KL = e^{iA}(b-qe^{i\varphi})(c-pe^{i\varphi})$.

## Power formulas (verified numerically)
- $\operatorname{pow}(B)=c^2+\frac{c[|L|^2 p\sin\varphi-|K|^2\Im L]}{\Delta}$, $\Im L=b\sin A-q\sin(A+\varphi)$.
- $\operatorname{pow}(C)=b^2+\frac{b[|L|^2(p\sin(A+\varphi)-c\sin A)+|K|^2 q\sin\varphi]}{\Delta}$.
- Also $\operatorname{pow}(B)=pc[\cos\varphi+\sin\varphi\cot\angle ALK]$, $\operatorname{pow}(C)=qb[\cos\varphi+\sin\varphi\cot\angle AKL]$.

## Final algebraic identity to prove ($\star$)
$$2\big[|L|^2W+|K|^2Z\big]=(c^2-b^2)\Delta$$
where $W=pc\sin\varphi-bp\sin(A+\varphi)+bc\sin A$, $Z=cq\sin(A+\varphi)-bq\sin\varphi-bc\sin A$.

This should follow from ConsP, ConsQ. Check: $(\star)=X\cdot$ConsP$+Y\cdot$ConsQ with $X,Y$ linear in $p,q$.
