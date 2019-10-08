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

import time
N = int(input())
inicio = time.time()
primes = [2]
for i in range(3, N, 2):
    if testePrimalidade(i):
        primes.append(i)
fim = time.time()
print(primes)
print(fim - inicio)

"""
entrada = int(input())

while entrada != 0:
    N = entrada

    factors = []
    i = 3
    k = 0
    while k < 2:
        if N%i == 0:
            factors.append(i)
            N /= i
            k += 1
        else:
            i += 2
    factors.append(N)

    print(int(entrada), "=", int(factors[0]), "x", int(factors[1]), "x", int(factors[2]))
    entrada = int(input())
"""