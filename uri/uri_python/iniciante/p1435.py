import math
N = int(input())
while N > 0:
    M = []
    for i in range(N):
        linha = []
        if i <= math.ceil(N/2)-1:
            for j in range(N):
                if j <= math.ceil(N/2)-1:
                    if j < i:
                        linha.append(j+1)
                    else:
                        linha.append(i+1)
                else:
                    linha.append(linha[N-j-1])
            M.append(linha)
        else:
            linha = M[N-i-1]
            M.append(linha)
    for i in range(N):
        saida = ""
        for j in range(N):
            saida += " "
            if M[i][j] < 10:
                saida += " "
            if j == N-1:
                saida += str(M[i][j])
            else:
                saida += str(M[i][j])+" "
        print(saida)
    print("")
    N = int(input())