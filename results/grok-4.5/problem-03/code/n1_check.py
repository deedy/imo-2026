"""Verify n=1: c should be 2/3."""
import numpy as np
from itertools import combinations

def pieces_from_cuts(cuts):
    pts = np.sort(np.concatenate(([0.], np.unique(cuts), [1.])))
    return np.diff(pts)

def lb_share(lengths):
    lengths = np.sort(lengths)[::-1]
    return lengths[0::2].sum()

def evaluate_xy_best(lb_cuts, grid):
    """Min share LB gets over XY's choices of 0 or 1 cut from grid (not coinciding)."""
    best_for_xy = 1.0  # min LB share
    # 0 cuts
    lens = pieces_from_cuts(lb_cuts)
    best_for_xy = min(best_for_xy, lb_share(lens))
    # 1 cut
    for y in grid:
        if np.any(np.isclose(y, lb_cuts, atol=1e-12)):
            continue
        lens = pieces_from_cuts(np.append(lb_cuts, y))
        best_for_xy = min(best_for_xy, lb_share(lens))
    return best_for_xy

def main():
    grid = np.linspace(0.01, 0.99, 99)
    best_c = 0
    best_x = None
    for x in grid:
        c = evaluate_xy_best(np.array([x]), grid)
        if c > best_c:
            best_c = c
            best_x = x
    print("Best approx c", best_c, "at x", best_x)
    # specifically at 1/3
    print("At 1/3:", evaluate_xy_best(np.array([1/3]), grid))
    print("At 0.5:", evaluate_xy_best(np.array([0.5]), grid))

if __name__ == "__main__":
    main()
