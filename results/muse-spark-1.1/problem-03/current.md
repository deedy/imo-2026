# imo-2026-03 — tracking file
## Status
partial
## Problem
Let $n$ be a positive integer. Liu Bang and Xiang Yu have a stick of length $1$ and want to divide it between themselves. Liu Bang marks at most $n$ points on the stick, and then Xiang Yu marks at most $n$ points on the stick. The marked points are distinct. Then, the stick is cut at all marked points, creating a number of pieces. Afterwards, they take turns claiming any unclaimed piece of the stick, with Liu Bang going first. Each player's goal is to maximise the total length of their own pieces. For each $n$, determine the largest value $c$ such that Liu Bang may guarantee a total length of at least $c$, regardless of Xiang Yu's play.

## Approaches tried
- analyzed n=1 case: optimal a = 2/3,1/3 gives c=2/3 = (n+1)/(2n+1)
- hypothesize general c = (n+1)/(2n+1)
- need to brute small n to test.

## Current best
Conjecture c = (n+1)/(2n+1). For n=1 proven. For general n, strategy for Liu: cut at k/(2n+1)?? Actually need n cuts, not 2n. Maybe need uneven.

If Liu cuts at positions k/(2n+1) for k=1..n (or some n of them), then Xiang can at most complete to equal partition? Let's see: if Liu chooses n equally spaced points? Suppose he chooses positions i/(2n+1) *? Let's test: full equal partition needs cuts at 1/(2n+1),2/(2n+1),...,2n/(2n+1). Liu can place n of them. Then Xiang can place remaining n, making all pieces equal 1/(2n+1). So Liu gets (n+1)/(2n+1). That's a baseline guarantee if Xiang cooperates to equalize. But Xiang might choose different cuts to try to reduce Liu's share below that, not to equalize. So we need to show that with clever Liu choice, any deviation by Xiang from equalizing does not reduce Liu below (n+1)/(2n+1). Or maybe Liu chooses a different set of cuts not equally spaced.

For n=1, Liu cuts at 2/3 = 2/(2n+1)=2/3 matches pattern of cutting at 2/(2n+1),4/(2n+1)...? Actually n=1, positions multiples of 1/3: cut at 2/3 (which is 2/(3)). That's one of the equal partition points (1/3 and 2/3). He chooses one of them (2/3). So after Xiang's choice, if Xiang places at 1/3, equal partition results. If Xiang deviates, Liu still gets at least 2/3. So choosing equal partition points as candidates seems optimal for Liu.

Generalize: Liu places cuts at positions 2/(2n+1),4/(2n+1),...,2n/(2n+1) i.e., even multiples. Then the intervals are: first piece 2/(2n+1), then pieces 2/(2n+1), ..., last piece 1/(2n+1). Actually let's compute: cuts at 2k/(2n+1) for k=1..n. Then sorted cuts: 2/(2n+1),4/(2n+1),...,2n/(2n+1). Pieces: sizes 2/(2n+1) repeated n times, plus final piece 1/(2n+1). So a_i = 2/(2n+1) for i=1..n, and a_{n+1}=1/(2n+1). Then if Xiang completes to equal partition, he cuts each big piece into two equal pieces 1/(2n+1) each, using n cuts (one per big piece). Then all 2n+1 equal pieces. Liu gets (n+1)/(2n+1). Could Xiang do better by cutting not equally? Suppose a_i=2/(2n+1). If Xiang splits it into unequal pieces x and 2/(2n+1)-x, with x <= 1/(2n+1) <= other? The larger piece >1/(2n+1). That would make a larger piece available to Liu maybe increasing his share? We need to analyze.

This construction seems promising to guarantee (n+1)/(2n+1). Let's test lower bound: with this Liu choice, can Xiang reduce Liu's f below (n+1)/(2n+1)?

We need to evaluate.

General Liu's pieces: n pieces of size 2d where d=1/(2n+1), and one piece size d.

M after Xiang splits each 2d piece into at most (t_i+1) pieces. Since total t sum <=n, and there are n big pieces, best use likely to split each big piece once (t_i=1 for each i=1..n) requiring n cuts, leaving small piece d untouched. That's exactly equal partition. If Xiang splits a piece into more than 2 pieces, he'd have to leave some other big piece unsplit (since limited cuts). That would create a piece of size 2d untouched, which is larger than d, maybe increasing Liu's share (since Liu gets large pieces). So seems optimal for Xiang to split each 2d piece exactly in half (or at least into two pieces). Could splitting into unequal halves give less f?

Consider final pieces after Xiang splits each 2d into y_i and 2d - y_i, with y_i <= d <= 2d - y_i? Actually if he splits evenly, both =d. If unequal, one piece <d, one >d.

Sorted final multiset consists of n pieces of sizes > =d (the larger halves) and n pieces <=d (smaller halves) plus the original small d.

We need to compute f for such configuration.

We can attempt to compute f minimal over y_i.

Suppose we have 2n+1 pieces: L_i = 2d - y_i (big half), S_i = y_i (small half), plus d.

Order: L_i >= d >=? S_i may be <=d.

So sorted descending: L's are top n (since > d). Among them, maybe d is next, then S's? But some S_i could be close to d, but still <=d, so after d, top S's come.

So ordering: L_{(1)} >= ... >= L_{(n)} >= d >= S_{(n)} >= ...? Actually S sorted descending.

Now M=2n+1 pieces odd, Liu gets n+1 pieces: positions 1,3,5,...2n+1.

What sum does he get? We need to consider alternating picks.

We can attempt to compute worst case for Liu.

If all L_i = d + δ_i, S_i = d - δ_i where δ_i = d - y_i >=0? Wait if y_i <=d, then L_i =2d - y_i = d + (d - y_i)= d+δ_i, S_i = d - δ_i.

So δ_i >=0, < =d.

Then multiset is d+δ_i (n pieces) and d-δ_i (n pieces) plus d.

Sorted decreasing among L_i: larger δ_i first, etc. For S_i, smaller δ_i (i.e., larger S) first.

So f = sum of Liu's picks.

We can compute bound: maybe f = (n+1)d + something *δ ?

Let's compute for n=1 case we did: d=1/3, L =2d - y =2/3 - y, S=y. Then δ = d - y. L = d+δ, S = d-δ. Final pieces: d+δ, d, d-δ. Sorted: d+δ, d, d-δ. Liu picks 1st and 3rd: d+δ + d-δ =2d =2/3 independent of δ! Interesting! So any split gives same sum 2d! So equal split not necessary, any split gives same Liu sum! That matches earlier calculation where we found with Liu (2/3,1/3) any split of big piece yields f =2/3 regardless of δ? Let's verify: earlier we calculated f for splitting big piece could be up to 0.8, but with this specific Liu configuration a1=2/3 =2d, splitting it into y and 2d-y gave final pieces y,2d-y,d. We computed f = max+min. Let's compute: pieces: L=2d-y, S=y, d. If y <=d, then L >=d >=S, sorted L,d,S, f = L+S =2d =2/3. If y >d, then roles swap: then S big? Actually then S = y is >d but still <2d? Could still be up to 2d. Then ordering changes but f still 2d? Let's test y =0.5 (>d=0.333): L=0.166..., S=0.5, d=0.333. Sorted: 0.5,0.333,0.166 => f=0.666 =2d. So indeed f constant! Nice.

So for n=1, this Liu construction makes f invariant under split of big piece, guaranteeing 2d.

For general n, perhaps similar invariance holds: With n big pieces 2d and one small d, splitting each big piece arbitrarily into two pieces (any y_i) yields total Liu share exactly (n+1)d? Let's test.

We have 2n+1 pieces: for each i, sum L_i+S_i =2d. Plus d.

We want sum of pieces at odd positions after sorting. Is it always (n+1)d ?

Let's conjecture that for any choice of δ_i in [0,d], the sorted order interleaves such that Liu's sum equals (n+1)d.

Let's test with small n=2 computationally with random δ_i to see.

d=1/5=0.2. Liu pieces: three? Actually n=2, we have 2 pieces of 0.4 and one 0.2. Pieces after Xiang splits each 0.4 into two arbitrary. So final 5 pieces: for i=1,2: L_i =0.4 - y_i, S_i =y_i, plus 0.2. Choose y1=0.1, y2=0.05: pieces =0.3,0.1,0.35,0.05,0.2 => sorted 0.35,0.3,0.2,0.1,0.05 => Liu picks positions 1,3,5 =0.35+0.2+0.05=0.6 = (n+1)d =3*0.2=0.6 matches! Try y1=0.35,y2=0.35: pieces 0.05,0.35,0.05,0.35,0.2 => sorted 0.35,0.35,0.2,0.05,0.05 => sum 0.35+0.2+0.05=0.6 matches! Try y1=0.39,y2=0.01: pieces 0.01,0.39,0.39? Wait 0.4-0.01=0.39, pieces:0.39,0.01,0.01,0.39,0.2 sorted 0.39,0.39,0.2,0.01,0.01 sum=0.6 matches! So seems invariant!

Let's test with random where splits not just two pieces per big piece but maybe Xiang uses fewer cuts or splits one piece into more than two and leaves another unsplit. Would that still guarantee at least 0.6?

Suppose n=2, Liu same. Xiang could split one big piece into 3 pieces and leave the other big untouched (using 2 cuts on one piece). Then final pieces: big untouched 0.4, plus three pieces summing to 0.4, plus 0.2. Total 5 pieces again. Example split 0.4 into 0.1,0.1,0.2: pieces 0.4,0.1,0.1,0.2,0.2 sorted 0.4,0.2,0.2,0.1,0.1 sum odd =0.4+0.2+0.1=0.7 >0.6, so Liu gets more! So Xiang wouldn't do that.

What if Xiang uses only 1 cut (not all), splitting one big piece into 0.2+0.2, others untouched 0.4 and 0.2: pieces 0.2,0.2,0.4,0.2 => actually 4 pieces: 0.4,0.2,0.2,0.2 sorted 0.4,0.2,0.2,0.2 Liu picks 1st and 3rd =0.6 again! Classic.

So seems this construction guarantees at least 3/5.

Let's test n=3: d=1/7≈0.142857, Liu pieces: three pieces 2d and one d? Wait n=3 => Liu should have n pieces of 2d = 3 pieces 2d, plus one d? Actually there are n+1=4 pieces initially if Liu uses n cuts: n pieces 2d and one d gives total n*2d + d = (2n+1)d=1 correct. So for n=3, 3*0.2857+0.1428=1. Good. Then Xiang has 3 cuts. To make equal, split each big into two d's using 3 cuts. Final 7 equal pieces => Liu gets 4d=4/7≈0.5714. If Xiang splits unequally, does Liu still get 4/7? Let's test with random quick mental? Let's brute with code quick mental for invariance: we have 3 pairs summing to 2d each plus d. Total 7 pieces. We claim sum of odd positions always =4d? Might be true due to pairing argument similar to "splitting 2d into two parts does not affect alternating sum when d present". Let's attempt to prove.

This resembles classic "balancing" lemma: If you have multiset where each of n pairs sums to 2d and one singleton d, then irrespective of distribution within pairs, the sum of elements in odd positions after sorting descending is (n+1)d.

Is that always true? Let's test counterexample: Suppose d=1, n=2, pairs: (1.9,0.1) and (1.9,0.1) plus 1. Pieces: 1.9,1.9,1,0.1,0.1 sorted 1.9,1.9,1,0.1,0.1 f=1.9+1+0.1=3.0 =3d=3, matches. Another pair: (2,0) and (0,2)? but 0 would be distinct points not allowed zero length but limit? (2,0) approx. Pieces: 2,0,2,0,1 sorted 2,2,1,0,0 f=3 again.

What about pairs like (1.5,0.5) and (1.5,0.5): pieces 1.5,1.5,1,0.5,0.5 sorted 1.5,1.5,1,0.5,0.5 f=3 again.

Seems plausible invariant.

Let's try to prove: Suppose we have numbers x_i = d+δ_i, y_i = d-δ_i for i=1..n, where δ_i can be positive or negative but |δ_i| <= d (since each piece positive, but δ_i could be negative if we label opposite but wlog |δ| <d). Plus central d_0 = d. Sorted descending, the largest pieces are those with largest δ. Since pairs symmetric around d, there might be a combinatorial argument that for any ordering consistent with δ, the sum of odd positions sums to (n+1)d.

Is there known combinatorial identity? This is reminiscent of "draft" game where splitting 2d into pair symmetric around d keeps total sum of alternating picks same.

Let's attempt proof for general n under this specific construction.

Let multiset S = {d+δ_i, d-δ_i : i=1..n} ∪ {d}. Assume ordering δ_i >=0 for definition but we can allow negative? Actually define δ_i = L_i - d >=0 if we enforce L_i >= d (i.e., split with one part >=d). But if y_i > d, then both parts? Wait if y_i > d, then the larger part? Actually 2d = y_i + (2d - y_i). If y_i > d, then y_i = d+δ, other = d-δ with δ>0 still. So we can always write larger = d+|δ|, smaller = d-|δ|. So δ_i >=0.

Thus we have pairs symmetric.

Now sort δ_i descending: δ_(1) >= δ_(2) >= ... >= δ_(n) >=0.

Then sorted list of all pieces descending:

Top n pieces are d+δ_(1)...d+δ_(n) in that order (since δ positive, bigger than d). Actually there might be interleaving with d if δ small, but still d+δ_i >= d.

Next piece is d (the original small piece). Then after that come d-δ_(n) <= ... <=? Since smallest δ gives largest small piece: d-δ_(n) is largest among small pieces (closest to d). So after d, we have pieces d-δ_(n), d-δ_(n-1),..., d-δ_(1) ascending??? Wait descending order among small pieces means larger small pieces first: Since δ larger => d-δ smaller. So smallest δ gives largest small piece. So order after d is d-δ_(n), d-δ_(n-1),..., d-δ_(1).

Thus sorted order is exactly:

Positions:
1: d+δ_1
2: d+δ_2
...
n: d+δ_n
n+1: d
n+2: d-δ_n
n+3: d-δ_{n-1}
...
2n+1: d-δ_1

If this sorted order holds (requires that d+δ_n >= d and d >= d-δ_n which true), no interleaving between large and small beyond central d. Since all larges >= d >= all smalls, ordering is as described (though among larges and among smalls order by δ). Indeed since d+δ_i >= d for all i, and d >= d-δ_i, so all larges before d and d before all smalls. So sorted order is as above.

Now compute Liu's sum (odd positions). For M=2n+1 odd, odd positions are 1,3,5,...,2n+1.

Sum odd = ?

Case n even or odd changes parity of inclusion of central d? For M=2n+1, position n+1 has parity = (n+1) odd/even depending on n. If n even, n+1 odd, so central d included in Liu's sum; if n odd, n+1 even, central d goes to Xiang? But final sum may still be (n+1)d? Let's compute formula.

Compute sum_{k odd} ?

We need to sum:

If i from 1..n, piece d+δ_i at position i. Its contribution to Liu if i odd.

Central d at position n+1 contributes if n even (since n+1 odd).

Small pieces: positions n+2..2n+1. Piece d-δ_{n+1 - (pos - (n+1))}? Actually at position n+1+j (j=1..n), piece is d-δ_{n+1 - j}? Let's index more cleanly:

Let j=1 corresponds to pos=n+2 piece = d-δ_n (largest small). So pos=n+1+j piece = d-δ_{n+1-j}. Contribution if pos odd.

So total f = sum_{i odd,1≤i≤n} (d+δ_i) + [n even? d :0] + sum_{j: n+1+j odd} (d-δ_{n+1-j}).

Now count number of d terms: Number of odd positions total is n+1 (since M=2n+1 -> ceil =n+1). So sum of d terms across all pieces contributes (n+1)d. Plus contributions of δ_i with signs: each δ_i appears either with + coefficient if its large piece in odd position, and - coefficient if its small piece counterpart in odd position.

Specifically, for each i, we have large piece at pos i with +δ_i if i odd, and small piece at pos n+1 + (n+1 - i) =2n+2 - i. Let's compute its position: small piece corresponding to δ_i is at position p_i = 2n+2 - i. Since mapping: large δ_i position i, small δ_i position 2n+2 - i. Indeed for i=1, small position =2n+1, matches. For i=n, small position = n+2. Good.

So small piece at pos p_i =2n+2 - i. It contains -δ_i.

Now i and p_i have opposite parity? Since p_i =2n+2 - i -> parity = same as i (since 2n+2 even). So parity of large and small positions for same i is same! Therefore if i is odd, both large and small pieces are in odd positions (both counted for Liu), giving contribution δ_i - δ_i =0. If i is even, both pieces are in even positions (not counted for Liu). Hence net δ cancellation! Thus total f = (n+1)d regardless of δ_i values.

Great! So invariant holds.

Thus Liu with that construction guarantees that if Xiang splits each big piece once, Liu gets (n+1)d exactly, independent of how he splits.

But we also need to consider other Xiang strategies that do not split each big piece exactly once. We argued they give Liu at least as much. Need to prove best response for Xiang among all allowed splits is indeed to split each big once (any way). We tested n=2 case where splitting one big into 3 gave larger Liu share. Is it always at least (n+1)d?

We need to show that with Liu's initial partition (n pieces size 2d, one size d), Xiang cannot force Liu below (n+1)d.

This is lower bound for Liu: c >= (n+1)/(2n+1).

What about upper bound? Can Liu guarantee more than (n+1)/(2n+1)? Suppose Liu chooses a different partition, could he get more? For n=1, we saw max is exactly 2/3 = (n+1)/(2n+1). For general n, we suspect this is optimal, i.e., Xiang can respond to any Liu partition to hold Liu to at most (n+1)/(2n+1). So c = (n+1)/(2n+1).

Upper bound proof: Need to show for any Liu partition into ≤n+1 pieces (since at most n cuts), Xiang can achieve final partition where Liu's draft sum ≤ (n+1)/(2n+1). Ideally Xiang can complete to equal partition of 2n+1 pieces of size 1/(2n+1)?? But Liu's pieces may not align to allow that exactly; Xiang can only refine, not move Liu's cuts. However to get equal pieces, Liu's cuts must be subset of equal partition cuts. Since Liu can choose arbitrary positions, not necessarily aligned with equal grid, Xiang cannot necessarily make equal pieces.

But Xiang's goal is to hold Liu to at most (n+1)/(2n+1). He doesn't need equal pieces necessarily; he can aim for something else to keep Liu's share low.

Classic bound: With total cuts 2n, the minimal possible maximal f over any partition into ≤2n+1 pieces that refines Liu's is at most (n+1)/(2n+1)?? Is there strategy for Xiang to ensure that after his cuts, all pieces are ≤1/(2n+1) ??? No, because Liu's pieces might be larger than that, but Xiang can split them to ensure no piece larger than 1/(2n+1)? Can he?

Liu's biggest piece could be >1/(n+1). Since Xiang has n cuts, he can split a piece of size a into at most n+1 subpieces if he puts all cuts into it. The minimal possible maximal subpiece size after splitting a into k parts minimal max is at least a/k. So to ensure all final pieces ≤1/(2n+1), we need to split each a_i into at least ceiling(a_i*(2n+1)) pieces. Sum of required extra pieces (k_i-1) sum may exceed n. Does it always exceed? For arbitrary Liu, perhaps some piece too large requires many cuts. Since Liu has only n+1 pieces, average size 1/(n+1) ~2/(2n+2) ~ >1/(2n+1). So to make all pieces ≤1/(2n+1), each piece a_i would need at least 2 parts if a_i >1/(2n+1). If a_i >2/(2n+1), need at least 3 parts etc. Might require more than n cuts.

So Xiang may not be able to make all pieces ≤1/(2n+1). Therefore equal partition upper bound not straightforward.

However we can maybe prove upper bound using "strategy stealing" or pairing argument: Show Xiang can always ensure Liu's total ≤ (n+1)/(2n+1) regardless of Liu's initial cuts.

How could Xiang do that? He can aim to adopt a strategy that after his cuts, when pieces sorted, the sum of pieces at odd positions ≤ (n+1)/(2n+1).

Maybe Xiang can ensure final pieces can be paired such that...

Alternate viewpoint: The draft game outcome f can be bounded above by something like? For any final partition into M pieces, f ≤? Not helpful.

We need to design Xiang's response to arbitrary Liu partition to limit f.

We have Liu partition a_1,...,a_m (m≤n+1). Xiang can choose to place his cuts to make final pieces as balanced as possible. Approach: He can try to ensure that for any threshold t, number of pieces larger than t is limited?

Another method: Think of the dual game where Xiang wants to minimize Liu's share, equivalent to maximizing his own. Could Xiang use a strategy of "mirroring" Liu's cuts around 1/2? Not.

Maybe we can prove upper bound by showing Liu cannot guarantee more than (n+1)/(2n+1) because Xiang can use a specific counter-strategy: After Liu's cuts, consider the 2n+1 equal-length intervals of size d=1/(2n+1). Liu's cuts are at n positions; they occupy n of the 2n interior grid points possibly not exactly at grid points. But we can think of intervals.

Xiang's strategy to limit to (n+1)d: He can place his cuts at grid points not occupied by Liu, but near them? However Liu's cuts are arbitrary real numbers, not aligned to grid. So Xiang can still place cuts at grid positions? Wait if Liu cut at x, he blocks that exact point, but Xiang can cut arbitrarily close to it? Points must be distinct, but can be arbitrarily close. So he could approximate grid points.

But if Liu's cut is at e.g., 0.4 and grid points at 0.2,0.4,0.6,0.8 (for n=2, grid 0.2,0.4,0.6,0.8). If Liu cuts at 0.4 exactly, that's already a grid point. If Liu cuts at 0.41, Xiang could cut at 0.4 (if not used) which is distinct, so final pieces would be not exactly equal but close. The draft sum would be close to (n+1)d. So maybe Xiang can get arbitrarily close to (n+1)d, ensuring Liu cannot exceed (n+1)d + epsilon. But since points must be distinct, and Liu could place cut exactly at grid point, blocking that grid point, forcing Xiang to place elsewhere. However then Liu's cuts already occupy some grid points; the remaining grid points are n points (since total 2n grid points). So Xiang can place at remaining grid points, exactly completing equal partition! So if Liu places his n cuts exactly at n of the 2n grid points, Xiang completes equal partition. If Liu places cuts elsewhere, not at grid points, then Xiang cannot make all pieces exactly d, but can make pieces slightly over? Could that increase Liu's share beyond (n+1)d? We need to analyze.

Wait grid model: equal partition into 2n+1 pieces requires cuts at d,2d,...,2nd. That's 2n cuts. Liu has n cuts; if he places them exactly at n of these positions, Xiang can place the other n and get equal. Then Liu gets exactly (n+1)d. That's the construction we used for lower bound (Liu placed at even multiples). If Liu places his cuts not on grid points, then Xiang could still try to get as close as possible to equal, but final piece sizes will not be all equal. Could that lead to Liu getting more than (n+1)d? Perhaps; but Xiang could choose different strategy not aiming for equal grid; maybe he can still limit to (n+1)d even when Liu's cuts off-grid.

We need to show for any Liu cuts, Xiang can ensure Liu ≤ (n+1)d + epsilon (?) Actually we need upper bound: Liu cannot guarantee > (n+1)d. So we need to exhibit for any Liu strategy, a Xiang response that keeps Liu ≤ (n+1)d (or at most (n+1)/(2n+1)). So need to show such response exists.

Potential Xiang counter-strategy: Use the same grid. Suppose Liu's cuts are arbitrary. Consider the 2n+1 intervals of length d. Count how many of Liu's cuts lie in each interval? No cuts are points, not intervals.

Alternative viewpoint: Sorting all possible cut positions: Let Liu's cuts be L. Let G = {d,2d,...,2nd} be ideal equal cut positions. If L intersects G at k positions, then those cuts are already good. Xiang could place his cuts at the remaining G\L positions, except those overlapping with L? But L may contain points not in G. The combined set L ∪ (G\L) includes all G plus extra points from L\G (n - k extra). So total pieces would be 2n+1 + (n - k) extra pieces due to off-grid Liu cuts. That would be more than 2n+1 pieces, splitting some d intervals into smaller pieces. Would that increase Liu's total beyond (n+1)d? Let's see.

If Liu's cuts are off-grid, then combined set includes all grid points (2n) plus extra (n - k) off-grid points inside intervals. So final partition is refinement of equal partition, with some d-intervals split into two pieces. How many extra pieces? Each off-grid Liu cut splits one d-interval into two. So total pieces = (2n+1) + (n - k). That's up to 2n+1 + n =3n+1 if k=0, but Xiang only has n cuts, not enough to cover all grid points if Liu cuts are off-grid? Wait we only have n Xiang cuts, not 2n. Our earlier assumption Xiang can place all remaining grid points (2n - k) needs 2n - k cuts, but he has only n cuts. So if L has k intersections with G, Xiang needs 2n - k cuts to complete G, but he has only n. So if k < n, he cannot complete full equal grid. So previous plan fails.

Thus Xiang cannot always complete equal partition unless Liu's cuts are exactly n of the grid points. Since Liu can avoid grid points, Xiang cannot necessarily achieve equal partition.

So need different Xiang strategy to upper bound.

Maybe better to think differently: The value (n+1)/(2n+1) may be optimal but upper bound proof must be clever.

Let's attempt to search computationally for n=2 to see what Liu can guarantee best. Our earlier heuristic that c=3/5=0.6. Let's test via brute search with deeper optimization for Xiang using random + local search to approximate worst case for Liu given best Liu.

We attempted earlier but not yet run due to code path issues. Let's attempt to run new brute code in environment. We'll need to find workspace path. The tool bash previous had path issue because of working directory. Let's use relative path.

