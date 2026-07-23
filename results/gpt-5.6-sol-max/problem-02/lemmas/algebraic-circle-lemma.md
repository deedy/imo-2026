# Algebraic circle lemma

## Statement
Let $S,C,U,X,b,c,R,D$ be real numbers with $S,b,c>0$, and suppose
\[
C^2+S^2=X^2+U^2=1.
\]
Put
\[
V=SX+CU,\qquad W=CX-SU,
\]
\[
F(T)=V(T^2-2XT+2)-ST.
\]
Assume $V\ne0$ and
\[
2Ub=cF(R),\qquad 2Uc=bF(D). \tag{1}
\]
Define
\[
K=\left(c-\frac{cRX}{2},\frac{cRU}{2}\right),
\qquad
L=\left(bC-\frac{bDW}{2},bS-\frac{bDV}{2}\right). \tag{2}
\]
If $A=(0,0),K,L$ are noncollinear and their circle has equation
\[
\xi^2+\eta^2-P\xi-Q\eta=0,
\]
then
\[
b(CP+SQ)-cP=\frac{b^2-c^2}{2}. \tag{3}
\]

## Proof
Set
\[
\Delta=K_xL_y-K_yL_x,
\]
\[
P_0=|K|^2L_y-K_y|L|^2,
\qquad Q_0=K_x|L|^2-|K|^2L_x.
\]
As $A,K,L$ are noncollinear, $\Delta\ne0$. The two equations
\[
PK_x+QK_y=|K|^2,
\qquad PL_x+QL_y=|L|^2
\]
therefore give, by Cramer's rule,
\[
P=\frac{P_0}{\Delta},\qquad Q=\frac{Q_0}{\Delta}. \tag{4}
\]
Define
\[
\mathcal T=2\bigl(b(CP_0+SQ_0)-cP_0\bigr)-(b^2-c^2)\Delta.
\]
For brevity write
\[
E_R=2Ub-cF(R),\qquad E_D=2Uc-bF(D).
\]
Direct expansion gives the polynomial identity
\[
4V\mathcal T=A E_R+B E_D+(C^2+S^2-1)G+(X^2+U^2-1)H, \tag{5}
\]
where
\[
A=bc\bigl(C^2DUb-CDUc+DS^2Ub-DSXc+2Sc\bigr),
\]
\[
B=bc\bigl(CRUb+RSXb-RUc-2Sb\bigr),
\]
\[
G=Ubc^2\bigl(2CDRUXb-2CDUb+2DRSX^2b-DRSb-2DSXb-2RUc\bigr),
\]
\[
H=Sbc\bigl(CDRUb^2-CDRUc^2+DRSXb^2-DRSXc^2-2DSb^2+2RSc^2\bigr).
\]
Identity (5) is checked simply by substituting the definitions (2), expanding $|K|^2,|L|^2,\Delta,P_0,Q_0$, and collecting terms; both sides are polynomials in the displayed variables.

By (1), $E_R=E_D=0$, and the two unit identities make the last two terms in (5) zero. Since $V\ne0$, it follows that $\mathcal T=0$. Using (4) and dividing the equation $\mathcal T=0$ by $2\Delta$ yields (3).
