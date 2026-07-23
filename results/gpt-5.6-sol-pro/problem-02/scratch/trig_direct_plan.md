# Direct r,v trigonometric plan

We have key complex equation
r b + v d - rv bd = R := p e^{-ix}+q e^{ix}-pq,
where b=e^{-i(x+y)}, d=e^{i(x+z)}.
Explicit real/imag:
r cos(x+y)+v cos(x+z)-rv cos(z-y)=p cosx+q cosx-pq
-r sin(x+y)+v sin(x+z)-rv sin(z-y)= -p sinx+q sinx.
Definitions p,q satisfy
2p sin(x+z)=sin z, 2q sin(x+y)=sin y.
Could perhaps manipulate T in r,v to factor exactly these two equations. Do direct hand-friendly coordinate setup from outset with rays and use trig identities.
Coordinates:
K=(1-p cosx, p sinx).
L=(1-r cos(x+y), r sin(x+y)). [since 1-r e^{-i...}: imag + r sin]
C=K/(1-v e^{i(x+z)}), messy denominator. Alternatively C=L/D. Use C=L/D, no v/d/z in target! Indeed target T depends C,K,L,D and BL representation. Since C=L/D. K independent p,z, D q,y. Does target perhaps follow from CK condition only; substitute C=L/D and L=1-rb, then T as function r, p,q,x,y. CK condition says direction C->K angle etc, but z tied p. Target could factor the single CK ray angle condition. This is less variables.

Set c=l/D with l=1-rb. Compute target E purely x,y,z through p and q, r. CK condition c-k direction equivalent angle x+z from CA: (k-c)/(-c) = 1-k/c? Actually k=c(1-vd), so k/c=1-vd, hence (1-k/c)/d=v real. Since k/c=kD/l. Thus [d,1-kD/l]=0 => [d,l-kD]=0 after division by l complicates angle due /l: 1-k/c=1-kD/l=(l-kD)/l, direction d. Equation l-kD=v d l, not simply fixed line.
But original compatibility equation is l(1-vd)=kD.
For given r, CK angle gives one real equation but also v. Eliminating v: (1-kD/l)/d real. This should be quadratic in r. Target after c=l/D likely also quadratic-ish in r and factors this angle condition! This likely yields smaller factor.

Derive target E after c=l/D. Use abstract formula perhaps then substitute l line. CK condition:
H := (1-kD/l)/d real
=> (l-kD)/(ld) = (L-KE)/(L/dbar?) conjugate.
Since unit d: ((l-kD)/(l d)) - conjugate =0.
Multiply l L:
L(l-kD)/d - l(L-KE)*d =0 (since conjugate denominator L/d? conj(ld)=L/d, conjugate fraction=(L-KE)/(L/d)=d(L-KE)/L; multiply? Equation (l-kD)/(ld)= d(L-KE)/L. times l d L: L(l-kD)=l d^2(L-KE).)
So CK polynomial condition:
G = L(l-kD)-l d^2(L-KE)=0.
Here L=bar l,E=bar D,K=bar k.
Target E with c=l/D may be proportional to G using trig relation among k,D,d,b. This is the exact small lemma to seek. Compute quotient abstract/specialized.
