"""Retrograde analysis of the discretized triangle-cutting game.

Angles are integer multiples of a unit; the triangle's angles are positive
integers (a,b,c) with a+b+c = N (N=180 means unit = 1 degree). Theta = t units.

State: sorted triple (a,b,c), a<=b<=c.
Move (Mulan): pick cut-vertex value A in {a,b,c}, pick ordered (B,C) = remaining,
pick integer alpha in [1, A-1]:
    half1 = sort(B, alpha, N-B-alpha)
    half2 = sort(C, A-alpha, B+alpha)
Shan-Yu keeps one half. Mulan wins when a state has a coordinate == t.

We compute the least fixed point W (Mulan's winning region).
"""
import sys
import numpy as np


def build(N):
    states = []
    for a in range(1, N // 3 + 1):
        for b in range(a, (N - a) // 2 + 1):
            c = N - a - b
            if c >= b:
                states.append((a, b, c))
    idx = {s: i for i, s in enumerate(states)}
    H1, H2, counts = [], [], []
    for s in states:
        a, b, c = s
        mv = set()
        seen_A = set()
        for A in (a, b, c):
            if A in seen_A:
                continue
            seen_A.add(A)
            rem = [a, b, c]
            rem.remove(A)
            for (B, C) in ((rem[0], rem[1]), (rem[1], rem[0])):
                for al in range(1, A):
                    h1 = tuple(sorted((B, al, N - B - al)))
                    h2 = tuple(sorted((C, A - al, B + al)))
                    mv.add((h1, h2))
        for (h1, h2) in mv:
            H1.append(idx[h1])
            H2.append(idx[h2])
        counts.append(len(mv))
    return (states,
            np.array(H1, dtype=np.int32),
            np.array(H2, dtype=np.int32),
            np.array(counts, dtype=np.int64))


def attractor(t, states, H1, H2, counts, max_rounds=10000):
    W = np.array([(t in s) for s in states], dtype=bool)
    starts = np.concatenate(([0], np.cumsum(counts)))[:-1]
    rounds = 0
    while True:
        good = W[H1] & W[H2]
        winmove = np.maximum.reduceat(good.view(np.int8), starts).astype(bool)
        new = W | winmove
        rounds += 1
        if new.sum() == W.sum() or rounds >= max_rounds:
            W = new
            break
        W = new
    return W, rounds


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 180
    t_lo = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    t_hi = int(sys.argv[3]) if len(sys.argv) > 3 else N - 1
    states, H1, H2, counts = build(N)
    nstates = len(states)
    print(f"N={N}: {nstates} states, {len(H1)} moves", flush=True)
    for t in range(t_lo, t_hi + 1):
        W, rounds = attractor(t, states, H1, H2, counts)
        nwin = int(W.sum())
        allwin = nwin == nstates
        line = f"t={t:3d} (theta={180.0*t/N:8.3f} deg): " \
               f"{'ALL WIN ' if allwin else 'losesome'} " \
               f"win={nwin}/{nstates} rounds={rounds}"
        if not allwin:
            losers = [states[i] for i in range(nstates) if not W[i]]
            line += f"  #lose={len(losers)} ex={losers[:6]}"
        print(line, flush=True)


if __name__ == "__main__":
    main()
