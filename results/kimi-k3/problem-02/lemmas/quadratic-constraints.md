# Lemma: the quadratic constraints

**Statement.** Under the problem's hypotheses, with $\varphi=\angle KBA=\angle ACL$, $p=BK$, $q=CL$, $b=CA$, $c=AB$:
$$2\sin(A+\varphi)p^2-(2\sin A+\sin(A+2\varphi))cp+c^2\sin(A+\varphi)-bc\sin\varphi=0,$$
$$2\sin(A+\varphi)q^2-(2\sin A+\sin(A+2\varphi))bq+b^2\sin(A+\varphi)-bc\sin\varphi=0.$$

**Proof.** See current.md Steps 2–3. Law of sines in $\triangle BMK$ and $\triangle BKC$ gives
(R1) $2p\sin(\varphi+\gamma)=c\sin\gamma$ and (EqC) $p\sin(A+\gamma+2\varphi)=c\sin(A+\gamma+\varphi)-b\sin(\gamma+\varphi)$
(the latter via the auxiliary identity $c\sin(A+x)=b\sin x+a\sin(C-x)$, proved there).
Expanding both as linear equations in $\cos\gamma,\sin\gamma$ and eliminating yields the first quadratic; the second is the symmetric argument with (R2),(R4).

**Verification.** `code/verify_power_formulas.py`: the elimination polynomial equals ConsP exactly (`elim - ConsP = 0`); ConsP/ConsQ vanish at the geometric $(p,q)$ in all numeric tests (`code/explore.py`, `code/symbolic.py`).

**Remark.** ConsP's two roots are exactly $BK$ and $BX$ ($X$ = second intersection of line $BK$ with $\omega$); their product $\frac{c^2\sin(A+\varphi)-bc\sin\varphi}{2\sin(A+\varphi)}$ is precisely $\operatorname{pow}(B)$, which is the content of identity (4) in current.md.
