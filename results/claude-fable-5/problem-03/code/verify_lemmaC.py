# Monte Carlo check: any refinement of geometric config (2^n,...,2,1)*u with <= n cuts
# has alternating sum D >= u.  Random cut allocations and random real positions,
# plus adversarial-ish special positions (equal to other pieces, halves, etc.)
import random

def D(parts):
    s = sorted(parts, reverse=True)
    d = 0.0; sg = 1
    for x in s: d += sg*x; sg = -sg
    return d

random.seed(2)
for n in range(1, 8):
    u = 1.0/(2**(n+1)-1)
    pieces = [2**(n-i)*u for i in range(n+1)]
    worst = 10.0
    for trial in range(40000):
        K = random.randint(0, n)
        alloc = [0]*(n+1)
        for _ in range(K): alloc[random.randrange(n+1)] += 1
        parts = []
        for i,(b,c) in enumerate(zip(pieces, alloc)):
            if c == 0:
                parts.append(b); continue
            # random cut positions; sometimes snap to "nice" values
            cuts = []
            for _ in range(c):
                r = random.random()
                if random.random() < 0.5:
                    # snap to multiple of u
                    r = round(r*b/u)*u/b
                cuts.append(r*b)
            cuts = sorted(set(x for x in cuts if 0 < x < b))
            pos = [0]+cuts+[b]
            parts += [pos[j+1]-pos[j] for j in range(len(pos)-1)]
        d = D(parts)
        worst = min(worst, d)
        assert d >= u - 1e-9, (n, parts, d, u)
    print(f"n={n}: min D found = {worst:.6f}, u = {u:.6f}  (ratio {worst/u:.3f})")
print("Lemma C Monte Carlo passed")
