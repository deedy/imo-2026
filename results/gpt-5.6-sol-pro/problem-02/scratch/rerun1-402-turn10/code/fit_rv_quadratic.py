# derive compatibility (1-rb)(1-vd)=kD, compare imaginary components.
# Expand: rb+vd-rv bd = 1-kD = p/e+qe-pq.
# Take bracket with possible directions to solve r in v.
# Imag eq: r Im b + v Im d-rv Im(bd)= RHS imag.
# Real similarly. Eliminate gives quadratic v.
# Target may simplify to that vector equation identically by direct trig.
import math,cmath
exec(open('code/explore_numeric.py').read().split("for xyz in")[0])
for xyz in [(.3,.2,.25),(.4,.35,.2),(.2,.3,.4)]:
 x,y,z=xyz;p=math.sin(z)/(2*math.sin(x+z));q=math.sin(y)/(2*math.sin(x+y));k,D,vals=configuration(*xyz)
 b=cmath.exp(-1j*(x+y));d=cmath.exp(1j*(x+z));R=1-k*D
 print('\n',xyz)
 for v,c,r in vals:
  # Calculate T for arbitrary r,v satisfying only imag compatibility r(v); test target relation perhaps real compat exactly polynomial
  print((r*b+v*d-r*v*b*d)-R)
