vetor = []
n = int(input())
vetor.append(n)
for i in range(9):
    vetor.append(vetor[i]*2)
for i in range(10):
    print("N["+str(i)+"] = "+str(vetor[i]))