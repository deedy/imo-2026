"""Sanity checks for imo-2026-05.

This script verifies the candidate family numerically and checks the algebraic
expansions used in the proof with exact polynomial arithmetic via SymPy when
available. The proof itself does not depend on this computation.
"""

import math
import random


def check_candidate(x: float, y: float, c: float) -> None:
    f_x = x + c
    f_y = y + c
    left = math.sqrt((x * x + f_y * f_y) / 2.0)
    middle = (f_x + y) / 2.0
    right = math.sqrt(x * f_y)
    scale = max(1.0, left, middle, right)
    tol = 2e-12 * scale
    assert left + tol >= middle
    assert middle + tol >= right


def numeric_trials() -> None:
    rng = random.Random(202605)
    for _ in range(100_000):
        # Log-uniform positive test data over several orders of magnitude.
        x = 10.0 ** rng.uniform(-4.0, 4.0)
        y = 10.0 ** rng.uniform(-4.0, 4.0)
        c = 10.0 ** rng.uniform(-4.0, 4.0) if rng.random() < 0.9 else 0.0
        check_candidate(x, y, c)


def symbolic_checks() -> None:
    try:
        import sympy as sp
    except ImportError:
        print("SymPy unavailable; skipped symbolic checks")
        return

    x, y, a, b, c = sp.symbols("x y a b c")

    # Four times the squared upper-inequality gap.
    raw_upper = 2 * x**2 + 2 * (y + b) ** 2 - (x + a + y) ** 2
    expanded_upper = (x - y) ** 2 + 4 * y * b + 2 * b**2 - 2 * a * (x + y) - a**2
    assert sp.expand(raw_upper - expanded_upper) == 0

    # For f(t)=t+c, the squared RMS-AM and AM-GM gaps are the same square.
    rms_am_gap_times_4 = 2 * x**2 + 2 * (y + c) ** 2 - (x + y + c) ** 2
    am_gm_gap_times_4 = (x + y + c) ** 2 - 4 * x * (y + c)
    expected = (x - y - c) ** 2
    assert sp.expand(rms_am_gap_times_4 - expected) == 0
    assert sp.expand(am_gm_gap_times_4 - expected) == 0


if __name__ == "__main__":
    numeric_trials()
    symbolic_checks()
    print("All sanity checks passed.")
