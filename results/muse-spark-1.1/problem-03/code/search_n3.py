import random, math, itertools

def f_val(pieces):
    # pieces is list of floats
    # sort descending
    q = sorted(pieces, reverse=True)
    s = 0.0
    for i in range(0, len(q), 2):
        s += q[i]
    return s

def best_Xiang_for_a(a, n, grid_res=41, random_extra=5000, verbose=False):
    m = len(a)
    # generate t tuples sum <= n
    def gen_tuples(idx, rem, cur):
        if idx == m:
            yield tuple(cur)
            return
        for ti in range(rem+1):
            cur.append(ti)
            yield from gen_tuples(idx+1, rem-ti, cur)
            cur.pop()
    t_list = list(gen_tuples(0, n, []))
    best overall = 1.0
    best_cfg = None
    # for each t, we need to optimize over splits
    for t in t_list:
        total_cuts = sum(t)
        # skip if total cuts <0 etc.
        # quick lower bound: if we already have best <= 0.5 maybe cannot go below 0.5, but we keep
        # optimization
        # If total_cuts ==0: just evaluate
        if total_cuts == 0:
            fv = f_val(a)
            if fv < best_overall:
                best_overall = fv
                best_cfg = (t, list(a))
            continue
        # For each i, we need to generate fragment options
        # We'll do two-phase: grid search + random refinement
        # For grid search, we need to handle up to n=3, so total continuous vars = total_cuts
        # We'll generate all combinations via product of per-interval grids if feasible

        # Build per-interval option lists for grid search
        per_interval_grid = []
        feasible = True
        total_combos = 1
        for ai, ti in zip(a, t):
            if ti == 0:
                per_interval_grid.append([[ai]])
            elif ti == 1:
                # r in (0,1)
                opts = []
                for k in range(1, grid_res):
                    r = k / grid_res
                    opts.append([r*ai, (1-r)*ai])
                per_interval_grid.append(opts)
                total_combos *= len(opts)
            elif ti == 2:
                opts = []
                # c1 < c2 in (0,1)
                # Use grid_res for 2D: step = grid_res//2 maybe
                # To keep combos manageable, use smaller resolution for ti=2
                res = max(5, grid_res//2)
                for k in range(1, res):
                    for l in range(k+1, res+1):
                        if l == res:
                            c1 = k/res
                            c2 = 1.0  # actually c2 <1, need <1
                            # skip
                            continue
                        c1 = k/res
                        c2 = l/res
                        opts.append([c1*ai, (c2-c1)*ai, (1-c2)*ai])
                per_interval_grid.append(opts)
                total_combos *= len(opts)
            elif ti == 3:
                opts = []
                res = max(4, grid_res//3)
                # generate combinations of 3 cuts: c1<c2<c3
                # For simplicity generate random for grid phase
                for _ in range(200):
                    c = sorted([random.random() for __ in range(3)])
                    opts.append([c[0]*ai, (c[1]-c[0])*ai, (c[2]-c[1])*ai, (1-c[2])*ai])
                per_interval_grid.append(opts)
                total_combos *= len(opts)
            else:
                feasible = False
                break
        # If feasible and total_combos is not huge, enumerate product
        if feasible and total_combos <= 200000:
            # enumerate product
            for combo in itertools.product(*per_interval_grid):
                pieces = []
                for frags in combo:
                    pieces.extend(frags)
                fv = f_val(pieces)
                if fv < best_overall:
                    best_overall = fv
                    best_cfg = (t, pieces)
        else:
            # random sampling for this t
            # We'll do random_extra samples
            for _ in range(random_extra):
                pieces = []
                for ai, ti in zip(a, t):
                    if ti == 0:
                        pieces.append(ai)
                    else:
                        cuts = sorted([random.random() for __ in range(ti)])
                        prev = 0.0
                        for c in cuts:
                            pieces.append((c-prev)*ai)
                            prev = c
                        pieces.append((1-prev)*ai)
                fv = f_val(pieces)
                if fv < best_overall:
                    best_overall = fv
                    best_cfg = (t, pieces)
        # After grid/product, also do some random extra refinement for this t
        for _ in range(random_extra//2):
            pieces = []
            for ai, ti in zip(a, t):
                if ti == 0:
                    pieces.append(ai)
                else:
                    cuts = sorted([random.random() for __ in range(ti)])
                    prev = 0.0
                    for c in cuts:
                        pieces.append((c-prev)*ai)
                        prev = c
                    pieces.append((1-prev)*ai)
            fv = f_val(pieces)
            if fv < best_overall:
                best_overall = fv
                best_cfg = (t, pieces)

    return best_overall, best_cfg

def evaluate_Liu_a(a, n):
    # a list sum 1
    best, cfg = best_Xiang_for_a(a, n, grid_res=31, random_extra=3000)
    return best, cfg

# Test geometric for n=3
S = 15
a_geom = [1/S, 2/S, 4/S, 8/S]
best, cfg = best_Xiang_for_a(a_geom, 3, grid_res=41, random_extra=8000)
print(f"Geometric n=3 a={a_geom} best Xiang {best:.6f} target 8/15={8/15:.6f} cfg t={cfg[0] if cfg else None}")

# Test some random a for n=3
for _ in range(5):
    exps = [-math.log(random.random()+1e-12) for __ in range(4)]
    s = sum(exps)
    a = [e/s for e in exps]
    best, cfg = best_Xiang_for_a(a, 3, grid_res=21, random_extra=2000)
    print(f"Random a {[f'{x:.3f}' for x in a]} best {best:.4f}")

def search_best_Liu(n, outer_iters=200):
    best_Liu_val = -1
    best_a = None
    best_cfg = None
    for it in range(outer_iters):
        exps = [-math.log(random.random()+1e-12) for __ in range(n+1)]
        s = sum(exps)
        a = [e/s for e in exps]
        # quick coarse eval
        val, cfg = best_Xiang_for_a(a, n, grid_res=21, random_extra=2000)
        if val > best_Liu_val:
            # refine with higher res
            val_refined, cfg_refined = best_Xiang_for_a(a, n, grid_res=41, random_extra=5000)
            if val_refined > best_Liu_val:
                best_Liu_val = val_refined
                best_a = a[:]
                best_cfg = cfg_refined
                print(f"[outer {it}] new best Liu {best_Liu_val:.6f} a {[f'{x:.4f}' for x in a]} cfg t={cfg_refined[0] if cfg_refined else None}")
    # final refinement around best_a
    if best_a is not None:
        print(f"\nFinal best coarse {best_Liu_val:.6f} a {best_a}")
        # local search
        cur_a = best_a[:]
        cur_val = best_Liu_val
        cur_cfg = best_cfg
        for step in range(100):
            # perturb
            sigma = 0.05
            new_a = [max(1e-6, x + random.gauss(0, sigma)) for x in cur_a]
            s = sum(new_a)
            new_a = [x/s for x in new_a]
            val, cfg = best_Xiang_for_a(new_a, n, grid_res=21, random_extra=2000)
            if val > cur_val:
                # refine
                val2, cfg2 = best_Xiang_for_a(new_a, n, grid_res=41, random_extra=5000)
                if val2 > cur_val:
                    cur_val = val2
                    cur_a = new_a[:]
                    cur_cfg = cfg2
                    print(f"  local {step} improved to {cur_val:.6f} a {[f'{x:.4f}' for x in cur_a]}")
        # final precise eval
        final_val, final_cfg = best_Xiang_for_a(cur_a, n, grid_res=61, random_extra=10000)
        print(f"\nFINAL n={n} best approx {final_val:.6f} a {[f'{x:.6f}' for x in cur_a]} cfg t={final_cfg[0] if final_cfg else None}")
        return final_val, cur_a
    return best_Liu_val, best_a

print("\n=== Searching best Liu for n=3 ===")
search_best_Liu(3, outer_iters=100)
