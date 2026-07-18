# Computational exploration

## Idea
Generate initial terms for small starting values to identify the likely structure.

## Status
Completed as a sanity check; not used as proof.

## Details
The script `code/sim.py` checks each successive integer until it finds one non-coprime to every earlier term. For prime-power starts the observed sequence is an arithmetic progression (step the underlying prime). For \(a_1=15\), the first terms are
\[
15,18,20,24,30,36,40,42,45,48,50,54,60,\ldots,
\]
and the differences have period 8 with total 30. This matches the proof's periodic-set mechanism: here admissibility is divisibility by 6, 10, or 15, a union periodic modulo 30 with 8 occupied residue classes.
