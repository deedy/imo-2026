import sympy as s
X,Y,Z,u,v=s.symbols('X Y Z u v', real=True, nonzero=True)
i=s.I
k=(2*X+Z+i*X*Z)/(2*(X+Z))
g=(2*X+Y-i*X*Y)/(2*(X+Y))
w=u+i*v
# constraint at B: arg(1-wg)=-(x+y); multiply e^{i(x+y)} numerator factor
Ep=(1+i*X)*(1+i*Y)
CB=s.expand(s.im(s.expand_complex((1-w*g)*Ep)))
# constraint at C: arg((w-k)/w)=x+z; multiply e^{-i(x+z)}, clear |w|2
Em=(1-i*X)*(1-i*Z)
CC=s.expand(s.im(s.expand_complex((w-k)*s.conjugate(w)*Em)))
print('CB factor=',s.factor(CB))
print('CC factor=',s.factor(CC))
# Circle F difference determinant. Rows [|k|2,k,kbar], [|l|2,l,lbar], delta row
l=w*g
row1=[s.expand(k*s.conjugate(k)),k,s.conjugate(k)]
row2=[s.expand(l*s.conjugate(l)),l,s.conjugate(l)]
row3=[(1-w*s.conjugate(w))/4,(1-w)/2,(1-s.conjugate(w))/2]
D=s.det(s.Matrix([row1,row2,row3]))
D=s.factor(s.simplify(s.expand_complex(D)/s.I)) # determinant pure imaginary, divide i
print('D factor raw=',D)
# numerator together
num=s.factor(s.together(D)).as_numer_denom()[0]
print('num factor=',s.factor(num))
# remove constraints via groebner
cbnum=s.factor(s.together(CB)).as_numer_denom()[0]
ccnum=s.factor(s.together(CC)).as_numer_denom()[0]
print('cbnum',cbnum)
print('ccnum',ccnum)
G=s.groebner([cbnum,ccnum],v,u, order='lex')
print('G',G)
rem=G.reduce(num)[1]
print('remainder=',s.factor(rem))
