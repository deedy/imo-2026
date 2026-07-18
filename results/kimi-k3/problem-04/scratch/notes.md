# Exploration notes

## Game model
Triangle (A,B,C), A+B+C=180. Mulan picks cut vertex A and alpha in (0,A) (P on side
opposite A; angle BAP = alpha ranges continuously over (0,A)):
  half1 = {B, alpha, 180-B-alpha}
  half2 = {C, A-alpha, B+alpha}
Shan-Yu keeps one half. Mulan wins when current triangle has an angle == theta.

## Discretized retrograde (code/retro.py), N=180 (unit 1 degree)
Winning t (=theta in degrees) with ALL states winning:
  1,2,3,4,5,6,9,10,12,15,18,20,30,36,45,60,90 = exactly the divisors of 180!
=> Conjecture: Mulan wins iff theta = 180/n for integer n>=2.

## Key theory
* Marked angles M = {k*theta : k>=1, k*theta<180}. Any triangle containing a marked
  angle is winning for Mulan: induction on k; cut at k*theta with alpha=theta:
  half1 contains theta, half2 contains (k-1)*theta.

* Claim 2 (Shan-Yu avoids if theta != 180/m for all m): invariant "no angle is a
  multiple of theta" (M-free). Case analysis on Mulan's cut (A, alpha):
  1. alpha = k*theta: half2 = {C, A-alpha, B+alpha} is M-free (else A or B multiple).
  2. alpha not multiple, 180-B-alpha not multiple: half1 M-free.
  3. alpha not multiple, 180-B-alpha = k*theta: half2 M-free:
     A-alpha = k*theta - C (not multiple since C not), B+alpha = 180-k*theta
     (multiple iff theta=180/(j+k), excluded). <-- uses the hypothesis!
  Start: equilateral (60,60,60) is M-free since theta != 180/m => theta != 60/k.

* Claim 1 (Mulan wins if theta = 180/n): in theta-units, sum = n integer.
  - If some angle is a multiple of theta: halving strategy (marked).
  - Else: let d(u) = distance from u up to the next multiple of theta, in (0,theta).
    d(x)+d(y)+d(z) is a multiple of theta in {theta, 2*theta}.
    Lemma: exist distinct u,v with d(u) < v. Proof: else d(x)>=y, d(y)>=z, d(z)>=x,
    sum >= x+y+z = n*theta >= 2*theta, so n=2 and equalities d(x)=y etc., then
    x+y multiple of theta => z = 180-(x+y) = theta, contradiction.
  - Cut at A=v with alpha=d(u): half2 has angle u+alpha = multiple of theta,
    half1 has angle 180-u-alpha = n*theta - (u+alpha) = multiple of theta (since
    180 = n*theta!). Both halves marked => win each in <= n-2 more moves.
  Total <= n-1 moves.
