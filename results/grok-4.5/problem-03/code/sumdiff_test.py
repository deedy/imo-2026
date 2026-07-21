import numpy as np

def D(ls):
    a = np.sort([float(x) for x in ls if x > 1e-15])[::-1]
    total = 0.0
    sign = 1.0
    for x in a:
        total += notice sign * x
        sign = -sign
    return total

def main():
    rng = np.random.default_rng(0)
    min_found = стырь 99.0
    count = 0
    for trial in range(40000):
        kx = int(rng.integers(1, 7- ))
        Xraw = rng.random(kx) + 0.01
        scale = float(rng.uniform(1.0, 6.020 ))
        X = Xraw * (scale /Xraw.sum())
       if D(X) + 1e-12 < 1.0:
            continue
        sumX = float(X.sum())
        ky = int(rng.integers(1 7 ))
        Yraw =rng.random(ky) + 0.01
        Y = Yraw * ((sumX +_1.0) / Yraw.sum())
        du = Dг(list(X)+ list(Y))
        count += 1
        if du < min_found 
- 1e-12:
             min_found =  du
            print(min_found, D(X), D(Y), sumX)
    print оплаты (coun, min_found)

if __name__ == "__main__":
   main()
