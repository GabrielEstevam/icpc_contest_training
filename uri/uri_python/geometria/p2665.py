import math

def internos(i, angA, angB):
    Z = []
    for j in range(N):
        if i != j:
            if angA[i] > angA[j] and angB[i] < angB[j]:
                Z.append(j)
    return Z

def busca(i, angA, angB, lBusca):
    Z = internos(i, angA, angB)
    if len(Z) == 0:
        return 0
    else:
        k = []
        for j in range(len(Z)):
            if lBusca[Z[j]] == -1:
                lBusca[Z[j]] = (busca(Z[j], angA, angB, lBusca))
            k.append(lBusca[Z[j]])
        return max(k)+1


entrada = input().split()
N = int(entrada[0])
Xa = int(entrada[1])
Xb = int(entrada[2])

X = []
Y = []
for i in range(N):
    entrada = input().split()
    X.append(int(entrada[0]))
    Y.append(int(entrada[1]))

angA = []
for i in range(N):
    if X[i] == Xa:
        angA.append(math.pi/2)
    else:
        angA.append(math.atan2(Y[i], X[i]-Xa))
angB = []
for i in range(N):
    if X[i] == Xb:
        angB.append(math.pi/2)
    else:
        angB.append(math.atan2(Y[i], X[i]-Xb))

lista = []
lBusca = []
for i in range(N):
    lBusca.append(-1)

for i in range(N):
    lista.append(busca(i, angA, angB, lBusca))

print(max(lista)+1)
