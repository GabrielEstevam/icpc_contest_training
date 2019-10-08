N = int(input())
for n in range(N):
    M = int(input())
    matriz = []
    for i in range(M):
        entry = input().split(" ")
        for j in range(M):
            entry[j] = str(pow(int(entry[j]), 2))
        matriz.append(entry)
    for i in range(M):
        tam = 0
        for j in range(M):
            if len(matriz[j][i]) > tam:
                tam = len(matriz[j][i])
        for j in range(M):
            while len(matriz[j][i]) < tam:
                matriz[j][i] = " " + matriz[j][i]
    if n > 0:
        print("")
    print("Quadrado da matriz #"+str(n+4)+":")
    for i in range(M):
        saida = matriz[i][0]
        for j in range(1, M, 1):
            saida += " " + matriz[i][j]
        print(saida)