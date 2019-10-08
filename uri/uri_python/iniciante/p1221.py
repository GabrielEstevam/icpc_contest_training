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

instancias = int(input())
for i in range(instancias):
    N = int(input())

    if testePrimalidade(N):
        print('Prime')
    else:
        print('Not Prime')