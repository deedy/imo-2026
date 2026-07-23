import sympy as s
# Build target numerator and constraints in quotient ring, ask Groebner extended representation? Sympy doesn't track reps. Build linear ansatz multipliers based degrees and solve sparse linear system.
S,C,U,X,b,c,R,D=s.symbols('S C U X b c R D')
vars=(R,D,b,c,C,X,U,S)
V=S*X+C*U; W=C*X-S*U
F=lambda T:s.expand(V*(T**2-2*X*T+2)-S*T)
ER=s.expand(2*U*b-c*F(R));ED=s.expand(2*U*c-b*F(D))
IA=S**2+C**2-1;Ix=U**2+X**2-1;Is=b**2+c**2-2*C*b*c-S**2
# direct target numerator recalc
r=c*R/2;d=b*D/2;kx=c-r*X;ky=r*U;lx=b*C-d*W;ly=b*S-d*V
K2=c*c-2*c*r*X+r*r;L2=b*b-2*b*d*X+d*d
det=kx*ly-ky*lx
P=(K2*ly-ky*L2);Q=(kx*L2-K2*lx) # actual coefficients /det
T=s.expand(2*(b*(C*P+S*Q)-c*P)-(b*b-c*c)*det) # target with denom, times 2
print('T terms/degree',len(s.Poly(T,*vars).terms()),s.Poly(T,*vars).total_degree())
# First obtain quotient representation via custom Buchberger with module reps? use sage unavailable. Sympy groebner fglm no reps.
# Ansatz guided: T degrees R,D <=2? target determinant likely <=2 each, constraints ER R² and ED D².
print('degrees',[(v,s.degree(T,v)) for v in vars])
# multipliers A ER + B ED + basic identity multipliers. Set monomial ansatz constrained multidegrees and total degree.
def monomials(maxdeg, caps):
 out=[]
 # recursive exponent products with total <= maxdeg and cap dictionary
 def rec(i,left,m):
  if i==len(vars):out.append(m);return
  v=vars[i]
  for e in range(min(caps.get(v,left),left)+1):rec(i+1,left-e,m*v**e)
 rec(0,maxdeg,s.Integer(1));return list(dict.fromkeys(out))
# Try staged degrees. T total degree likely 9. constraints degree 5. multipliers degree4 etc huge. exploit homogeneity b,c.
# Print target and constraints degrees multivariate
for name,e in [('ER',ER),('ED',ED),('IA',IA),('Ix',Ix),('Is',Is)]:print(name,'terms',len(s.Poly(e,*vars).terms()),'deg',s.Poly(e,*vars).total_degree(),[(v,s.degree(e,v)) for v in vars])
# use groebner division to get quotients from G then express G via originals difficult. Could implement extended Buchberger over QQ tracking vector representations, likely manageable 5 polynomials 8 vars and chosen order.
