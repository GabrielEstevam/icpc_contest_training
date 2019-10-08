impar = [0,0,0,0,0]
par = [0,0,0,0,0]
nImpar = 0
nPar = 0
for i in range(15):
    N = int(input())
    if N % 2 == 0:
        par[nPar] = N
        nPar += 1
        if nPar == 5:
            for j in range(5):
                print("par["+str(j)+"] =", par[j])
            nPar = 0
    else:
        impar[nImpar] = N
        nImpar += 1
        if nImpar == 5:
            for j in range(5):
                print("impar[" + str(j) + "] =", impar[j])
            nImpar = 0
for i in range(nImpar):
    print("impar[" + str(i) + "] =", impar[i])
for i in range(nPar):
    print("par[" + str(i) + "] =", par[i])