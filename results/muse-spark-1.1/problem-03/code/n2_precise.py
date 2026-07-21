import random, math
import itertools

def f_of_pieces(pieces):
    q = sorted(pieces, reverse=True)
    s = 0.0
    for i in range(0, len(q), 2):
        s += q[i]
    return s

def best_Xiang_n2(a, grid=401, random_samples=8000):
    # a list of 3
    # ensure list
    best = 1.0
    # option 0 cuts
    best = min(best, f_of_pieces(a))
    # 1-cut options
    for i in range(3):
        ai = a[i]
        others = [a[j] for j in range(3) if j != i]
        # dense grid over r
        for k in range(1, grid):  # avoid 0,1
            r = k / grid
            pieces = [r*ai, (1-r)*ai] + others
            fv = f_of_pieces(pieces)
            if fv < best:
                best = fv
        # also random refinement around critical points
        # random samples
        for _ in range(2000):
            r = random.random()
            if r==0 or r==1:
                continue
            pieces = [r*ai, (1-r)*ai] + others
            fv = f_of_pieces(pieces)
            if fv < best:
                best = fv

    # 2-cut: case single piece into 3 (ti=2)
    for i in range(3):
        ai = a[i]
        others = [a[j] for j in range(3) if j != i]
        # grid over r1,r2 for simplex
        # parameterize by two cut positions c1<c2 in (0,1)
        steps = 31
        for k in range(1, steps):
            c1 = k / steps
            for l in range(k+1, steps):
                c2 = l / steps
                r1 = c1
                r2 = c2 - c1
                r3 = 1 - c2
                pieces = [r1*ai, r2*ai, r3*ai] + others
                fv = f_of_pieces(pieces)
                if fv < best:
                    best = fv
        for _ in range(random_samples):
            c1 = random.random()
            c2 = random.random()
            if c1 > c2:
                c1, c2 = c2, c1
            if c1 == 0 or c2 == 1 or c1 == c2:
                continue
            r1 = c1
            r2 = c2 - c1
            r3 = 1 - c2
            pieces = [r1*ai, r2*ai, r3*ai] + others
            fv = f_of_pieces(pieces)
            if fv < best:
                best = fv

    # 2-cut: split two distinct pieces each into 2 (ti=1, tj=1)
    for i in range(3):
        for j in range(i+1, 3):
            ai = a[i]; aj = a[j]
            k = [x for x in range(3) if x != i and x != j][0]
            ak = a[k]
            steps = 51
            for ri in range(1, steps):
                r_i = ri / steps
                for rj in range(1, steps):
                    r_j = rj / steps
                    pieces = [r_i*ai, (1-r_i)*ai, r_j*aj, (1-r_j)*aj, ak]
                    fv = f_of_pieces(pieces)
                    if fv < best:
                        best = fv
            for _ in range(random_samples):
                r_i = random.random()
                r_j = random.random()
                pieces = [r_i*ai, (1-r_i)*ai, r_j*aj, (1-r_j)*aj, ak]
                fv = f_of_pieces(pieces)
                if fv < best:
                    best = fv

    return best

def test_a(a):
    best = best_Xiang_n2(a)
    print(f"a={a} best Xiang={best:.6f}")

# test known
for a in [[0.4,0.4,0.2],[0.6,0.2,0.2],[0.6,0.3,0.1],[1/3,1/3,1/3]]:
    test_a(a)

def outer_search_n2(iterations=500, refine_steps=200):
    best_L = -1
    best_a = None
    best_val = None
    for it in range(iterations):
        # sample a from dirichlet random
        # Use uniform simplex via sorting random points
        # Use exponentials
        exps = [-math.log(random.random()+1e-12) for _ in range(3)]
        s = sum(exps)
        a = [e/s for e in exps]
        # sort descending for convenience (does not affect best Xiang since pieces symmetric? But for evaluation it's symmetric anyway because Xiang can choose which piece to split, so sorted order doesn't matter)
        # But keep as is; best Xiang already searches over all i, so permutation invariant.
        val = best_Xiang_n2(a, grid=81, random_samples=2000)  # coarser for fast search
        if val > best_L:
            best_L = val
            best_a = list(a)
            print(f"[outer {it}] new best {best_L:.6f} a {best_a}")
    # refine around best
    if best_a is not None:
        print(f"\nRefining around {best_a} with best {best_L}")
        cur_a = best_a[:]
        cur_best = best_L
        for step in range(refine_steps):
            # perturb cur_a
            # Gaussian perturbation with decreasing variance
            sigma = 0.05 * (0.98 ** step)
            new_a = [max(1e-6, x + random.gauss(0, sigma)) for x in cur_a]
            s = sum(new_a)
            new_a = [x/s for x in new_a]
            val = best_Xiang_n2(new_a, grid=201, random_samples=4000)
            if val > cur_best:
                cur_best = val
                cur_a = new_a
                print(f" refine {step} improved to {cur_best:.6f} a {cur_a}")
        # final precise evaluation
        final_val = best_Xiang_n2(cur_a, grid=401, random_samples=20000)
        print(f"FINAL refined: {final_val:.6f} a {cur_a}")
        return final_val, cur_a
    return best_L, best_a

outer_search_n2(iterations=300)
