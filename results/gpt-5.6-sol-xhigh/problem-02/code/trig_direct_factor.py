import sympy as S
x,y,z,t=S.symbols('x y z t', real=True)
a,b,c,d,e,f=S.symbols('a b c d e f', real=True)
# derive cleaner trigonometric coordinates perhaps simplify N using trig identities manually.
# Lambda modulus square: lambda=1+ sx/sxy e^-iy.
# = (sxy+sx cy -i sx sy)/sxy = (2sx cy+cx sy - i sx sy)/sxy.
# N=l/lambda. Maybe avoid explicit N in lemma: state abstract coordinates and expansion identity coefficient sinx(sinx*t+siny)/(sin(x+y)sin(x+z)) because c2+d2=1.
# homogeneous ratio above = a*(a*t+c)/ (sinxy sinxz).
print('ratio simple: sinx*(t*sinx+siny)/(sin(x+y)*sin(x+z))')
