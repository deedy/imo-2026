import math

def gen(a1, max_terms=500):
    a = [a1]
    for n in range(1, max_terms):
        cand = a[-1] + 1
        while True:
            ok = True
            for prev in a:
                if math.gcd(cand, prev) == 1:
                    ok = False
                    break
            if ok:
                a.append(cand)
                break
            cand += 1
    return a

def diffs(seq):
    return [seq[i+1]-seq[i] for i in range(len(seq)-1)]

# Compute L for given T by checking a_{n+T} - a_n for several n
def find_T_L(a1, max_terms=500):
    seq = gen(a1, max_terms)
    d = diffs(seq)
    # Try to find period in sequence directly: a_{n+T} - a_n constant
    # We'll search for small T
    n = len(seq)
    for T in range(1, 200):
        L = seq[T] - seq[0]  # candidate L from n=1
        if L <= 0:
            continue
        ok = True
        for i in range(0, n - T):
            if seq[i+T] - seq[i] != L:
                ok = False
                break
        if ok:
            return T, L, seq[:T+1], d[:T]
    return None

# test some interesting cases
tests = [15, 35, 45, 65, 75, 77, 85, 91, 95, 99, 105, 115, 119, 121, 125, 133, 135, 143, 145, 147, 153, 155, 161, 165, 169, 175, 187, 189, 195, 203, 205, 207, 209, 215, 217, 219, 221, 225, 231, 235, 237, 245, 247, 249, 253, 255, 259, 261, 265, 267, 273, 275, 279, 285, 287, 289, 291, 295, 297, 299, 301, 303, 305, 309, 315, 319, 321, 323, 325, 327, 329, 333, 335, 339, 341, 343, 345, 351, 355, 357, 361, 363, 365, 369, 371, 375, 377, 381, 385, 387, 391, 393, 395, 399]
for a1 in tests:
    res = find_T_L(a1, 500)
    if res:
        T, L, init, d = res
        print(f"a1={a1}: T={T}, L={L}, period diffs: {d}")
    else:
        print(f"a1={a1}: not found")
