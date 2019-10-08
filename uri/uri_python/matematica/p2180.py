import math

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

N = int(input())

k = 0;
primes = []
n = N

while k < 10:
    if testePrimalidade(n):
        primes.append(n)
        k += 1
    n += 1

vel = sum(primes)
print(vel, "km/h")
horas = int(60000000/vel)
dias = int(horas/24)
print(horas,"h /", dias,"d")