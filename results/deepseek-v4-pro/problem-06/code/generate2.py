import math
import sys

def gen(a1, max_terms=200):
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

# Test more interesting a1 values
test_vals = [15, 21, 33, 35, 39, 45, 51, 55, 57, 63, 65, 69, 75, 77, 85, 87, 91, 93, 95, 99, 105, 111, 115, 117, 119, 121, 123, 125, 129, 133, 135, 141, 143, 145, 147, 153, 155, 159, 161, 165, 169, 171, 175, 177, 183, 185, 187, 189, 195, 201, 203, 205, 207, 209, 213, 215, 217, 219, 221, 225, 231, 235, 237, 245, 247, 249, 253, 255, 259, 261, 265, 267, 273, 275, 279, 285, 287, 289, 291, 295, 297, 299, 301, 303, 305, 309, 315, 319, 321, 323, 325, 327, 329, 333, 335, 339, 341, 343, 345, 351, 355, 357, 361, 363, 365, 369, 371, 375, 377, 381, 385, 387, 391, 393, 395, 399]

for a1 in test_vals:
    seq = gen(a1, 80)
    d = diffs(seq)
    print(f"a1={a1}: first 40 seq: {seq[:40]}")
    # Try to detect period in diffs
    diff_str = ','.join(str(x) for x in d)
    # find eventual period
    # Just print diffs up to 50
    # Check if eventually constant
    # Also check if periodic
    # Let's see
