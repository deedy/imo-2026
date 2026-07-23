import sympy as s
X,Y,Z,D=s.symbols('X Y Z D', real=True, nonzero=True)
i=s.I
k=(2*X+Z+i*X*Z)/(2*(X+Z))
g=(2*X+Y-i*X*Y)/(2*(X+Y))
E=(1-i*X)*(1-i*Y)
l=1-D*E
w=s.factor(l/g)
# C constraint
Em=(1-i*X)*(1-i*Z)
CC=s.factor(s.im(s.expand_complex((w-k)*s.conjugate(w)*Em)))
print('CC=',s.factor(s.together(CC)))
# circle determinant target
row1=[s.expand(k*s.conjugate(k)),k,s.conjugate(k)]
row2=[s.expand(l*s.conjugate(l)),l,s.conjugate(l)]
row3=[(1-w*s.conjugate(w))/4,(1-w)/2,(1-s.conjugate(w))/2]
DD=s.factor(s.simplify(s.expand_complex(s.det(s.Matrix([row1,row2,row3])))/i))
print('target=',s.factor(s.together(DD)))
print('ratio=',s.factor(s.cancel(DD/CC)))
