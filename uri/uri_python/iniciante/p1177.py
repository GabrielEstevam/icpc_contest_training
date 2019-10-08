vetor = []
n = int(input())
aux = -1
for i in range(1000):
    aux += 1
    if aux == n:
        aux = 0
    vetor.append(aux)
for i in range(1000):
    print("N["+str(i)+"] = "+str(vetor[i]))
