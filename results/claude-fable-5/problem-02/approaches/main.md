# Main approach (successful): auxiliary points X, Y + affine power identity

## Idea
1. $Y := $ ray $BK \cap$ segment $AC$ (interior), $X := $ ray $CL \cap$ segment $AB$ (interior). Exist by crossbar since $K,L$ are strictly inside angles $ABC$, $ACB$.
2. Directed-angle translations of the hypotheses (with ABC counterclockwise WLOG):
   - $\angle KBA=\angle ACL=\theta$: $\measuredangle(BA\to BK)=-\theta$, $\measuredangle(CA\to CL)=+\theta$ ⇒ mod 180°: $\angle(BX,BY)=\angle(CX,CY)$ ⇒ $B,X,Y,C$ concyclic ($\omega_1$).
   - $\angle LCK=\angle BMK=\psi$: $\measuredangle(CL\to CK)=+\psi$ and $\measuredangle(MB\to MK)=+\psi$ ⇒ $C,M,K,X$ concyclic ($\omega_K$); if $X=M$, $AB$ is tangent to $(CMK)$ at $M$ (tangent–chord).
   - $\angle LBK=\angle LNC=\varphi$: $\measuredangle(BK\to BL)=-\varphi$ and $\measuredangle(NC\to NL)=-\varphi$ ⇒ $B,N,L,Y$ concyclic ($\omega_L$); if $Y=N$, $AC$ tangent to $(BNL)$ at $N$.
   Sign facts used: $K,L$ strictly inside triangle $ABC$ (on $C$-side of $AB$, $B$-side of $AC$, $A$-side of $BC$); "K inside angle LBA" gives $\angle ABL=\angle ABK+\angle KBL$; "L inside angle ACK" gives $\angle ACK=\angle ACL+\angle LCK$.
3. Let $\omega=(AKL)$. Define $F(Z):=\mathrm{pow}(Z,\omega)-\mathrm{pow}(Z,\omega_K)-\mathrm{pow}(Z,\omega_L)+\mathrm{pow}(Z,\omega_1)$. The $|Z|^2$ terms cancel, so $F$ is affine.
   - $F(A)= 0 - \tfrac{c}{2}x - \tfrac{b}{2}y + cx = 0$ using $cx=by$ (power of $A$ wrt $\omega_1$ along the two chords $XB$, $YC$), where $x=AX$, $y=AY$, $c=AB$, $b=AC$.
   - $F(K)=0-0-KB\cdot KY+KB\cdot KY=0$ ($B,Y$ lie on both $\omega_1$ and $\omega_L$; $K\in BY$).
   - $F(L)=0-LC\cdot LX-0+LC\cdot LX=0$ ($C,X$ lie on both $\omega_1$ and $\omega_K$; $L\in CX$).
   $A,K,L$ non-collinear ⇒ $F\equiv 0$.
4. $F(B)=0$: $\mathrm{pow}(B,\omega)=\mathrm{pow}(B,\omega_K)=BM\cdot BX=\tfrac{c}{2}(c-x)$ (as $B\in\omega_1\cap\omega_L$). $F(C)=0$: $\mathrm{pow}(C,\omega)=CN\cdot CY=\tfrac{b}{2}(b-y)$.
5. Median formula: $4(OM^2-ON^2)=2OB^2-2OC^2-c^2+b^2 = 2(\mathrm{pow}(B,\omega)-\mathrm{pow}(C,\omega))-c^2+b^2 = c(c-x)-b(b-y)-c^2+b^2 = by-cx=0$.

## Status
Complete; verified numerically (`code/verify.py`), including the $X=M$ tangency case.

## Dead ends / notes
- First tried to find the second common points $K^*,L^*$ of $\omega$ with $\omega_K,\omega_L$ and show radical axes are $BY$, $CX$; works but tangency cases are awkward. The affine function $F$ avoids all of that.
- Also checked: $\mathrm{pow}(A,\omega_K)=\mathrm{pow}(A,\omega_L)$ (so the radical axis of $\omega_K,\omega_L$ passes through $A$ and the radical centre $R=BY\cap CX$) — true but not needed.
