# imo-2026-02 — tracking file
## Status
partial

## Problem
Let $ABC$ be a triangle and let points $M$ and $N$ be the midpoints of sides $AB$ and $AC$, respectively. Let points $K$ and $L$ be chosen inside triangles $BMC$ and $BNC$, respectively, such that $K$ lies inside the angle $LBA$, $L$ lies inside the angle $ACK$, and $\angle KBA = \angle ACL$, $\angle LBK = \angle LNC$, $\angle LCK = \angle BMK$. Let $O$ be the circumcentre of triangle $AKL$. Prove that $OM = ON$.

## Approaches tried
- **Angle/trigonometric parametrization (active).** Four compact complex equations encode all hypotheses.
- **Circle-equation reduction (active).** The goal is determinant identity (T).
- **Exact symbolic factorization.** A custom Laurent-polynomial script verifies the implication exactly, but the initial quotient is too large.
- **Reduced compatibility factorization (active).** After $c=l/D$, $l=1-rb$, the target $T_0$ and CK compatibility $G$ satisfy $T_0/G=A+rB$ numerically. Further probing found $A$ has exactly the direction $e^{-i(x+z)}=1/d$: $A/(p/d)$ is real. An explicit formula for its real magnitude and for $B/A$ is still being identified.
- **Coefficient expansion.** `code/coeff_abstract.py` now gives a compact abstract cubic-in-$r$ expansion of the target numerator after clearing $|D|^2$. Its $r^3$ coefficient is particularly simple and should permit coefficient-by-coefficient comparison with $(A+rB)G$.
- **Ray-length and synthetic approaches.** Recorded, but incomplete.

## Current best
Let
\[
p=\frac{\sin z}{2\sin(x+z)},\ q=\frac{\sin y}{2\sin(x+y)},\quad
k=1-pe^{-ix},\ D=1-qe^{ix},\ b=e^{-i(x+y)},\ d=e^{i(x+z)}.
\]
Then $l=1-rb$, $c=l/D$, and
\[
G:=\bar l(l-kD)-ld^2(\bar l-\bar k\bar D)=0. \tag{G}
\]
With $\langle a,b\rangle=\bar a b-a\bar b$, the desired identity is $T_0=0$, where
\[
T_0=2\{|k|^2\langle c-1,l\rangle+|l|^2\langle k,c-1\rangle\}
-(|c|^2-1)\langle k,l\rangle.
\]
After multiplying by $|D|^2$, direct expansion gives the relatively manageable form
\[
S=2|k|^2\bigl(|l|^2(D-\bar D)+D\bar D(\bar l-l)\bigr)
+2|l|^2\bigl(\bar k l\bar D-k\bar lD+D\bar D(k-\bar k)\bigr)
-(|l|^2-|D|^2)(\bar k l-k\bar l), \tag{S}
\]
where $S=|D|^2T_0$. The planned finish is to factor (S) as a linear factor times (G), using $l=1-rb$ and the elementary sine identities.

## Full proof
A complete proof has not yet been obtained. The established reduction follows.

Let
\[
x=\angle KBA=\angle ACL,\quad y=\angle LBK=\angle LNC,
\quad z=\angle LCK=\angle BMK.
\]
Put $A=0,B=1,C=c$. Ray order and the sine rule in $BMK,CNL$ give
\[
k=1-pe^{-ix},\qquad l=cD,
\]
where
\[
p=\frac{\sin z}{2\sin(x+z)},\qquad D=1-qe^{ix},\qquad
q=\frac{\sin y}{2\sin(x+y)}.
\]
The directions of $BL,CK$ give positive $r,v$ such that
\[
l=1-re^{-i(x+y)}=1-rb,
\qquad k=c(1-ve^{i(x+z)})=c(1-vd).
\]
Thus $c=l/D$ and $(1-kD/l)/d=v\in\mathbb R$. Equating this to its conjugate gives (G).

For vectors $a,w$, write $[a,w]=\operatorname{Im}(\bar a w)$. If $u$ represents $O$, then
\[
u\cdot k=\frac{|k|^2}{2},\qquad u\cdot l=\frac{|l|^2}{2}.
\]
Resolving $w$ in the basis $k,l$ gives
\[
u\cdot w=\frac{|k|^2[w,l]+|l|^2[k,w]}{2[k,l]}.
\]
Hence
\[
2\bigl(|k|^2[c-1,l]+|l|^2[k,c-1]\bigr)=(|c|^2-1)[k,l] \tag{T}
\]
is equivalent to $4u\cdot(c-1)=|c|^2-1$, i.e.
\[
|u-1/2|^2=|u-c/2|^2.
\]
This is $OM=ON$.

Substituting $c=l/D$ into the doubled-bracket version of (T), then multiplying by $|D|^2$, gives (S) by direct expansion. Available simplifications are
\[
kD-k-D=pq-1\in\mathbb R,
\]
\[
b^2=e^{-2ix}\frac{2D-1}{2\bar D-1},\qquad
d^2=e^{2ix}\frac{2k-1}{2\bar k-1}.
\]
The sole gap is the concise factorization of (S) by (G).
