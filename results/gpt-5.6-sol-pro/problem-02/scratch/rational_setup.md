# Rational coordinate setup

Normalize $A=(0,0),B=(1,0)$ and orient $C=(u,v)$ with $v>0$. Put
$$X=\cot x,\quad Y=\cot y,\quad Z=\cot z.$$
Directly intersecting the appropriate rays in triangles $BMK,CNL$ gives
$$K=(r,s)=\left(\frac{X+2Z}{2(X+Z)},\frac1{2(X+Z)}\right),$$
while, in complex notation,
$$L=(a-ib)C,\qquad a=\frac{X+2Y}{2(X+Y)},\quad b=\frac1{2(X+Y)}.$$
The condition $\angle LBK=y$ and ray order says $BL$ has direction $\pi-(x+y)$. If
$$T=\cot(x+y)=\frac{XY-1}{X+Y},$$
this is the linear equation
$$au+bv-1+T(av-bu)=0.$$
The condition at $C$ says $CK$ is obtained by turning $CA$ counterclockwise through $x+z$. Hence, for
$$W=\cot(x+z)=\frac{XZ-1}{X+Z},$$
one has
$$u^2+v^2-ur-vs=W(rv-su).$$
These two equations are the entire remaining geometry. If the circle through $0,K,L$ is
$$q_x^2+q_y^2-Uq_x-Vq_y=0,$$
then $Ur+Vs=r^2+s^2$, $U(au+bv)+V(av-bu)=|L|^2=(a^2+b^2)(u^2+v^2)$. The target is
$$1-(u^2+v^2)+2U(u-1)+2Vv=0.$$
Goal: prove the target polynomial is a scalar multiple (after use of the linear equation) of the angle-at-$C$ quadratic.
