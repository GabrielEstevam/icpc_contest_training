def testePrimalidade(Num):
    flagPrime = True
    for i in range(5):
        a = 2+i
        if a < Num:
            K = expModular(a, Num-1, Num)
            if K != 1:
                flagPrime = False
                break
        else:
            break
    if flagPrime:
        return 1
    else:
        return 0

def expModular (X, Y, MOD):
    if Y == 0:
        return 1
    W = expModular(X, int(Y/2), MOD)
    W = (W*W)%MOD
    if Y%2 == 1:
        W = (W*X)%MOD
    return W

def fatorial (X):
    if X == 0:
        return 1
    else:
        return X*fatorial(X-1)

N = int(input())

factors = []
flagPrime = True
i = 2
if N > 0:
    while N % i == 0:
        factors.append(i)
        N = int(N/i)
    i += 1

while N > 1:
    a = testePrimalidade(N)
    if a == 0:
        flagPrime = False
    if flagPrime:
        factors.append(int(N))
        break
    else:
        while N%i == 0:
            factors.append(i)
            N = int(N / i)
        i += 2
        flagPrime = True


if len(factors) != 0:
    n = 1
    k = factors[0]
    for i in range (1, len(factors)):
        if factors[i] != k:
            n += 1
            k = factors[i]

    despojados = 0
    if len(factors) > 2 and n >= 2:
        nFat = fatorial(n)
        for k in range (2, n+1):
            kFat = fatorial(k)
            nkFat = fatorial(n-k)
            result = nFat/(nkFat*kFat)
            despojados += int(result)

    print(despojados)
else:
    print(0)
