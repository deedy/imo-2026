# Lemma: a positive integral angle is winning

## Statement
Measure angles in units of the target angle, so the target is $1$. If a current triangle has an angle equal to a positive integer $m$, then Mulan can force victory in at most $m-1$ further cuts.

## Proof
We induct on $m$. If $m=1$, victory has already occurred, requiring no cuts. Let $m\ge2$. Mulan cuts from the vertex of angle $m$ along the ray that splits this angle into $1$ and $m-1$. The two children respectively contain these two angles. If Shan-Yu keeps the child containing $1$, Mulan wins immediately. If he keeps the other child, it has the positive integral angle $m-1$, from which the induction hypothesis gives victory in at most $m-2$ additional cuts. Thus at most $m-1$ cuts suffice. $\square$
