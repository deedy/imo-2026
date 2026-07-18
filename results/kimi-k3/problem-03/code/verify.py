"""Focused checks for the conjectured value c_n = 2^n/(2^{n+1}-1)."""
from game import xy_min, lb_value, multisets, alt_sum

Tn = {1: 1/3, 2: 1/7, 3: 1/15}

print("=== Check 1: geometric pieces give min-D exactly T_n*K on grid ===")
for n, K in [(1, 3), (1, 12), (2, 7), (2, 14), (3, 15)]:
    m = K // (2**(n+1) - 1)
    geo = tuple(m * 2**i for i in range(n + 1))
    v = xy_min(geo, n)
    print(f"n={n} K={K} geo={geo}: min D = {v} (target {m} = T_n*K), match={v==m}")

print()
print("=== Check 2: lb_value on grids divisible by 2^{n+1}-1 ===")
for n, K in [(1, 12), (2, 7), (2, 14), (3, 15)]:
    best, arg = lb_value(K, n)
    m = K // (2**(n+1) - 1)
    print(f"  -> D={best}, target {m}, match={best==m}")

print()
print("=== Check 3: trend over K (n=2) ===")
for K in [7, 8, 9, 10, 11, 12, 13, 14]:
    best, arg = lb_value(K, 2, verbose=False)
    print(f"K={K}: D={best}, c={(K+best)/2/K:.4f} (target 0.5714), arg={arg}")
