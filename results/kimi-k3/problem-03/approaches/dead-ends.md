# Dead ends and false leads (recorded honestly)

- **NM (non-positive merge) induction for Part A.** Hope: in any subdivision of a super-increasing family, some two fragments of the same original piece can be merged without increasing $D$; then induct on cuts. **False**: family $\{1,3\}$ ($m=2$, margin $1$), one cut $3\to1.5+1.5$: $D$ drops from $2$ to $1$; the only same-parent merge raises $D$ back to $2$. (Merging can increase $D$; the statement "some merge doesn't" fails already for $m=2$.) Note $D$ never drops below $\delta$ here — but that is Theorem 3.1 itself, proved via matchings instead.

- **Dominance "min over subdivisions = min over halve/cancel sequences".** False on coarse integer grids (e.g. pool $(1,9)$, 1 cut: true subdiv min $=2$ since $4.5$ is off-grid, halve/cancel min $=1$). These are grid artifacts; and in any case Part B only needs that halve/cancel sequences are *valid* subdivisions (they are), so the inequality direction we use is unaffected.

- **Min signed sum = min chain value.** Tempting because the pigeonhole gives $|\sum\delta_i a_i|\le T_nS$ directly. **False** (`code/signed.py`): e.g. family $[3,7,7.75,9,11.33]$ has min signed sum $0.083\overline{3}$ but min chain value $0.41\overline{6}$. Part B instead realizes *adjacent* subset-sum gaps, which are always chain-realizable (realizability lemma).

- **Interval chains / prefix-suffix chains suffice.** Empirically true on random tests but not needed; subset chains via the chain theorem are cleaner and provably sufficient.

- **Direct induction on $m$ for the chain theorem** via $f(a_2..a_m)\le T_{m-2}(S-a_1)$: the bound $T_{m-2}(S-a_1)\le T_{m-1}S$ holds only when $a_1/S\ge2^{m-1}/(2^m-1)$, so induction through $f(a_2..a_m)$ alone cannot close; the cross terms $|{\rm chain}(B)-a_1|$ do not obviously interpolate. Superseded by the pigeonhole + realizability route.
