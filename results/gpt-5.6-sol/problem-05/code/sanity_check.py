import math
import random


def check_translation(c, trials=100000):
    worst_upper = float("inf")
    worst_lower = float("inf")
    for _ in range(trials):
        x = 10 ** random.uniform(-6, 6)
        y = 10 ** random.uniform(-6, 6)
        fx, fy = x + c, y + c
        left = math.sqrt((x*x + fy*fy) / 2)
        mid = (fx + y) / 2
        right = math.sqrt(x * fy)
        worst_upper = min(worst_upper, left-mid)
        worst_lower = min(worst_lower, mid-right)
        assert left + 1e-9 * max(1, left) >= mid
        assert mid + 1e-9 * max(1, mid) >= right
    return worst_upper, worst_lower


for c in [0.0, 1e-6, 0.3, 7.0, 1e6]:
    print(c, check_translation(c, 20000))
