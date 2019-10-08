import math
N = int(input())
while N > 0:
    M = []
    for i in range(N):
        M.append([])
        for j in range(N):
            if j >= i:
                M[i].append(j+1-i)
            else:
                M[i].append(i+1-j)
    for i in range(N):
        saida = ""
        for j in range(N):
            saida += ""
            if M[i][j] < 10:
                saida += "  "
            elif M[i][j] < 100:
                saida += " "
            if j == N-1:
                saida += str(M[i][j])
            else:
                saida += str(M[i][j])+" "
        print(saida)
    print("")
    N = int(input())