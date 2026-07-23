"""Numerical sanity checks for imo-2026-05 (not part of the proof)."""

from __future__ import annotations

import math
import random


def check_translation(trials: int = 100_000) -> float:
    """Check f(t)=t+c on random logarithmic-scale inputs; return worst margin."""
    rng = random.Random(202605)
    worst = math.inf
    for _ in range(trials):
        x = 10 ** rng.uniform(-6, 6)
        y = 10 ** rng.uniform(-6, 6)
        c = 10 ** rng.uniform(-6, 6) if rng.random() < 0.9 else 0.0
        fx, fy = x + c, y + c
        upper_margin = math.sqrt((x * x + fy * fy) / 2.0) - (fx + y) / 2.0
        lower_margin = (fx + y) / 2.0 - math.sqrt(x * fy)
        # Floating-point cancellation can cause tiny relative errors near equality.
        scale = max(x, y, c, 1.0)
        assert upper_margin >= -1e-10 * scale
        assert lower_margin >= -1e-10 * scale
        worst = min(worst, upper_margin / scale, lower_margin / scale)
    return worst


def check_orbit_alignment() -> None:
    """Verify the floor alignment and decay of the rationalized RMS gap."""
    a, b, p, q = 0.73, 2.19, 1.37, 0.91
    previous_bound = math.inf
    for m in (10, 100, 1_000, 10_000, 100_000):
        x = a + m * p
        n = math.floor((x - (b + q)) / q)
        assert n >= 0
        v = b + (n + 1) * q
        assert -1e-12 <= x - v < q + 1e-12
        phi = (x - v) ** 2 / (math.sqrt(2 * (x * x + v * v)) + x + v)
        bound = q * q / (x + v)
        assert 0 <= phi <= bound * (1 + 1e-12)
        assert bound < previous_bound
        previous_bound = bound
    assert previous_bound < 1e-5


if __name__ == "__main__":
    worst = check_translation()
    check_orbit_alignment()
    print(f"all sanity checks passed; worst normalized floating margin = {worst:.3e}")
