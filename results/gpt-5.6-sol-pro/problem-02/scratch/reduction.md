# Current algebraic parametrization

Let A=0, B=1, C=c. Angles x,y,z are equal pairs. Define
P = sin z/(2 sin(x+z)), Q=sin y/(2 sin(x+y)),
a=e^{-ix}, b=e^{-i(x+y)}, d=e^{i(x+z)}.
Then
K=k=1-Pa,
L=l=c(1-Q/a)=cD, D=1-Qe^{ix},
and ray equations l=1-rb, k=c(1-vd), r,v>0.
Thus c=k/(1-vd) and cD=1-rb. Eliminating r says Im((cD-1)/b)=0; this is a quadratic condition in v. There are generally two algebraic roots, of which geometry/interiority may select one (numeric experiments show two ray-compatible roots but likely only one has K,L inside required triangles).

Target: circle through 0,k,l. For circle coefficient u with |w|^2=2 Re(u conjugate(w)), target F(1/2)=F(c/2), equivalently
2 Re(u(1-conj(c))) = (1-|c|^2)/2 [check convention carefully]. Better multiply by 4: F(1/2)=(1/4)-Re(u), F(c/2)=|c|^2/4-Re(u conj(c)); equality iff 4 Re(u(conj(c)-1))=|c|^2-1.

Could directly compute u from k,l:
If cross(a,b)=Im(conj(a)b), and equations dot(u,k)=|k|^2/2, dot(u,l)=|l|^2/2, then dot(u,c-1) determinant expression. Need show
2[ |k|^2 cross(c-1,l)+|l|^2 cross(k,c-1)] / cross(k,l) = |c|^2-1 (sign verify).
This may factor by compatibility.
