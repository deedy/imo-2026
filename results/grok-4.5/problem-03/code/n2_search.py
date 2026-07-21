"""Brute force / grid search for n=2 LB strategy."""
import numpy as np

def pieces(cuts):
    pts = np.sort(np.unique(np.concatenate(([0.0], cuts, [1.0]))))
    # remove near-duplicates
    keep = [pts[0]]
    for p in pts[1:]:
        if p - keep[-1] > 1e-12:
            keep.append(p)
    return np.diff(keep)

def lb_get(lengths):
    a = np.sort(lengths)[::-1]
    return a[0::2].sum()

def worst_xy(lb_cuts, y_grid):
    """Min over XY choosing 0,1,2 distinct points from grid not coinciding with LB."""
    m = 1.0
    # combine choices: all subsets of size 0,1,2 from grid, filtered
    # For 2 points we enumerate pairs + singles + empty
    cand = []
    lb_cuts = np.asarray(lb_cuts, dtype=float)
    # empty
    cand.append(lb_cuts.copy())
    for y in y_grid:
        if np.any(np.abs(y - lb_cuts) < 1e-10):
            continue
        cand.append(np.append(lb_cuts, y))
    for i, y1 in enumerate(y_grid):
        if np.any(np.abs(y1 - lb_cuts) < 1e-10):
            continue
        for y2 in y_grid[i+1:]:
            if np.any(np.abs(y2 - lb_cuts) < 1e-10):
                continue
            if abs(y1-y2)<1e-10:
                continue
            cand.append(np.concatenate([lb_cuts, [y1,y2]]))
    for c in cand:
        val = lb_get(pieces(c))
        if val < m:
            m = val
    return m

def main():
    # Coarse grid for LB two points
    g = np.linspace(0.05, 0.95, 37)
    ygrid = np.linspace(0.02, 0.98, 49)
    best = 0
    best_xy = None
    results = []
    for i,x1 in enumerate(g):
        for x2 in g[i+1:]:
            c = worst_xy([x1,x2], ygrid)
            results.append((c, x1, x2))
            if c > best:
                best = c
                best_xy = (x1,x2)
    results.sort(reverse=True)
    print("Top 10:")
    for r in results[:10]:
        print(r)
    print("Best found", best, best_xy)
    # special candidates
    for cand in [(1/5,2/5),(1/4,1/2),(1/3,2/3),(1/5,3/5),(2/5,3/5),(1/4,1/2),(1/5,2/5)]:
        c = worst_xy(cand, ygrid)
        print(cand, "->", c)
    # denser around 1/5,2/5
    print("At exact 0.2,0.4")
    yg2 = np.linspace(0.01,0.99,99)
    print(worst_xy([0.2,0.4], yg2))
    print("At 1/5,2/5", worst_xy([1/5,2/5], yg2))
    print("At 1/5,3/5", worst_xy([1/5,3/5], yg2))
    print("At 1/4,1/2", worst_xy([0.25,0.5], yg2))
    print("At 1/3,1/2", worst_xy([1/3,0.5], yg2))

if __name__ == "__main__":
    main()
