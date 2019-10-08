import math
N = int(input())
while N > 0:
    M = []
    for i in range(N):
        M.append([])
        for j in range(N):
            M[i].append(int(math.pow(2, i+j)))
    tam = len(str(M[N - 1][N - 1]))
    for i in range(N):
        saida = ""
        for j in range(N):
            saida_aux = str(M[i][j])
            while len(saida_aux) < tam:
                saida_aux = " " +saida_aux
            if j != N-1:
                saida_aux += " "
            saida += saida_aux
        print(saida)
    print("")
    N = int(input())