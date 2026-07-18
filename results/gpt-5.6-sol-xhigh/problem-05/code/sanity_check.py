"""Numerical sanity checks for the characterized family f(x)=x+c.

These checks are evidence only; the proof is entirely analytic.
"""

import math
import random


def check_shift(c: float, trials: int = 100_000) -> None:
    worst_left = float("inf")
    worst_right = float("inf")
    for _ in range(trials):
        # Log-uniform samples over twelve orders of magnitude.
        x = 10.0 ** random.uniform(-6.0, 6.0)
        y = 10.0 ** random.uniform(-6.0, 6.0)
        fx = x + c
        fy = y + c
        left = math.sqrt((x * x + fy * fy) / 2.0)
        middle = (fx + y) / 2.0
        right = math.sqrt(x * fy)
        # Normalize because absolute floating-point errors grow with scale.
        scale = max(left, middle, right, 1.0)
        worst_left = min(worst_left, (left - middle) / scale)
        worst_right = min(worst_right, (middle - right) / scale)
    assert worst_left > -1e-12, (c, worst_left)
    assert worst_right > -1e-12, (c, worst_right)
    print(f"c={c:g}: min normalized margins {worst_left:.3e}, {worst_right:.3e}")


def verify_gap_identity(trials: int = 100_000) -> None:
    for _ in range(trials):
        p = 10.0 ** random.uniform(-4.0, 4.0)
        q = 10.0 ** random.uniform(-4.0, 4.0)
        lhs = math.sqrt(2.0 * (p * p + q * q)) - p - q
        rhs = (p - q) ** 2 / (math.sqrt(2.0 * (p * p + q * q)) + p + q)
        assert abs(lhs - rhs) <= 1e-9 * max(1.0, abs(lhs), abs(rhs))
    print("RMS-gap rationalization identity checked")


if __name__ == "__main__":
    random.seed(202605)
    for shift in (0.0, 1e-6, 0.1, 1.0, 1000.0):
        check_shift(shift)
    verify_gap_identity()
