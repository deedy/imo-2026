# Analysis for small n

## n=1
LB marks at 1/3. Always gets exactly 2/3 (or at least).
c_1 = 2/3.

## n=2 conjecture
LB can mark 2 points. Total cuts up to 4, up to 5 pieces.
LB picks 3 pieces if 5, or 2 if 4/3/2 etc.

Strategy for LB: create equal pieces of strategic sizes.

Perhaps think in terms of the final multiset of lengths. XY wants to minimize the alternating sum of sorted lengths.

Let S be sorted lengths descending l1 ≥ l2 ≥ ... ≥ lk.
LB gets l1+l3+l5+...

XY goes second in marking and wants to minimize this.

Perhaps LB should aim for pieces all of size 1/(2n+1) or something?
For n=1: 1/3, gets two of them effectively → 2/3 = 2/(2*1+1)

For n=2: if all equal 1/5, 5 pieces, LB gets 3/5.
Can LB force 3/5?

If LB marks at 1/5 and 2/5:
Pieces initially: 1/5,1/5,3/5.
XY can mark twice in the large piece to split 3/5 into three 1/5 → all 1/5 → LB gets 3/5.
Or XY could mark elsewhere maliciously.

If XY marks both in the 3/5 to make pieces a,b,c with a+b+c=3/5, and two 1/5 outside.
Sorted: depends. Max LB can be forced down?
Total LB gets (total - middle picks of XY).
With 5 pieces LB gets 3, XY 2. Sum of all half + half of leftover if odd number.

Generally LB gets at least half, but with advantage of first pick and possible odd count.

If XY leaves large pieces that he can also claim...

Suppose LB marks two points at 1/5, 2/5.
XY places y1,y2 in (2/5,1).
The three pieces in (2/5,1) sum to 3/5. Plus two 1/5.
If the three are each ≤1/5, then all ≤1/5, five pieces, LB gets three largest summing ≥3/5 (actually = if equal).
If one is >1/5, say largest overall is M >1/5, then XY as second picker...

Actually LB first takes M, then XY takes next, etc.
LB's total = sum odd positions.

It's known that with k pieces, LB gets at least ceil(k/2) of the averages etc., but RHS can force.

Let me compute worst case for this strategy.
