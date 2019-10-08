vetor = []
for i in range(100):
    vetor.append(float(input()))
for i in range(100):
    if vetor[i] <= 10:
        print("A["+str(i)+"] =", "{0:.1f}".format(vetor[i]))