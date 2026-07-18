"""Random sanity checks for the integer-entry cut and its child angles."""
import random
import math

for N in range(2, 30):
    for _ in range(10000):
        xs = [random.expovariate(1.0) for _ in range(3)]
        a0, b0, c0 = [N*x/sum(xs) for x in xs]
        if any(abs(x-round(x)) < 1e-10 for x in (a0,b0,c0)):
            continue
        found = None
        vals = (a0,b0,c0)
        # a is split; b,c are endpoint angles in their two possible orders.
        for i in range(3):
            a = vals[i]
            b = vals[(i+1)%3]
            c = vals[(i+2)%3]
            for k in range(1, N):
                if b < k < a+b:
                    found = (a,b,c,k)
                    break
            if found:
                break
        assert found, (N, vals)
        a,b,c,k = found
        x = k-b
        assert 0 < x < a
        # Child triples: (b,x,N-b-x), (c,a-x,N-c-a+x)
        left = (b, x, N-b-x)
        right = (c, a-x, N-c-a+x)
        assert abs(left[2]-(N-k)) < 1e-9
        assert abs(right[2]-k) < 1e-9
        assert all(y > 0 for y in left+right)
print("random checks passed")
