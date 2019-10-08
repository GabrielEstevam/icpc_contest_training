N = int(input())
for i in range(N):
    entrada1 = input().split(" ")
    QT = int(entrada1[0])
    S = int(entrada1[1])
    entrada2 = input().split(" ")
    indice = 0
    for j in range(QT):
        if abs(S - int(entrada2[j])) < abs(S - int(entrada2[indice])):
            indice = j
    print(indice+1)