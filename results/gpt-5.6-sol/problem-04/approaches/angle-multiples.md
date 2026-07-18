# Angle-multiple strategy

**Idea.** Normalize angles by \(\theta\). If \(180^\circ=N\theta\) for an integer \(N\ge2\), every positive integral multiple of \(\theta\) below \(180^\circ\) is a winning angle: split \(k\theta\) into \(\theta\) and \((k-1)\theta\), and induct.

To enter this winning set, for normalized triangle angles \(a+b+c=N\), seek an integer \(k\) with \(b<k<N-c=a+b\). Cutting the angle \(a\) so that one part is \(k-b\) makes the two angles at the cut point equal to \(N-k\) and \(k\), respectively. Thus either retained triangle has an integral angle.

The interval existence follows unless an angle was integral already. If one angle exceeds 1, use it as \(a\). Otherwise all three are in \((0,1)\), forcing \(N=2\), and the two largest have sum greater than 1.

**Status:** Complete; proves sufficiency.