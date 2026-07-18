# Approach: discretized retrograde analysis (status: used for discovery, not for proof)

**Idea.** Discretize angles to integer multiples of a unit ($N$ units $=180^\circ$,
$\theta=t$ units), enumerate all $\sim N^2/12$ unordered triangle states and all
legal cuts, and compute Mulan's winning region as a least fixed point
(retrograde attractor): $W_0=\{$states containing $t\}$,
$W_{i+1}=W_i\cup\{s:\exists\text{ cut with both halves in }W_i\}$.
Mulan wins the discretized game iff $W$ is everything.

**Implementation.** `code/retro.py` (numpy vectorized). $N=180$: 2700 states,
~940k moves, <1s for all $t=1..179$. $N=360$: 10811 states, ~7.5M moves, ~11s.

**Findings.**
- $N=180$: the values of $t$ for which Mulan wins **every** state are exactly
  $t\in\{1,2,3,4,5,6,9,10,12,15,18,20,30,36,45,60,90\}$ — precisely the
  divisors of $180$, i.e. $\theta=180^\circ/n$.
- $N=360$: winning $t$ are exactly $\{360/n: n\mid 360,\ n\ge2\}$, again exactly
  $\theta=180^\circ/n$ (now including $22.5^\circ=180^\circ/8$, etc.). No
  false positives/negatives.

**Caveat.** The discretized game is not the real game (angles and cuts are
reals). It only served to guess the characterization; the proof is purely
mathematical (see `current.md`). The exact-arithmetic simulator
`code/verify.py` bridges the gap: it executes the *explicit* strategies from the
proof on rational triangles with `Fraction` arithmetic and confirms
(a) for $\theta=180^\circ/n$ Mulan's strategy always wins, with worst case
exactly $n-1$ moves ($n\le 60$ tested, exhaustive over Shan-Yu's choices);
(b) for $\theta\ne 180^\circ/m$ Shan-Yu's invariant survives $200\times300$
random cuts.
