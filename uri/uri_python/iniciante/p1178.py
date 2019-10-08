vetor = []
n = float(input())
for i in range(100):
    vetor.append(n)
    n /= 2
for i in range(100):
    print("N["+str(i)+"] =", "{0:.4f}".format(vetor[i]))
