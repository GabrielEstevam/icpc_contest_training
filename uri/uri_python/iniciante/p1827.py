import math
while True:
    try:
        N = int(input())
        M = []
        interno = math.floor(N/3)
        for i in range(N):
            M.append([])
            for j in range(N):
                if interno <= i <= N-interno-1 and interno <= j <= N-interno-1:
                    if i == j and i+j == N-1:
                        M[i].append(4)
                    else:
                        M[i].append(1)
                else:
                    if i == j:
                        M[i].append(2)
                    elif i+j == N-1:
                        M[i].append(3)
                    else:
                        M[i].append(0)
        for i in range(N):
            saida = ""
            for j in range(N):
                saida += str(M[i][j])
            print(saida)
        print("")
    except EOFError:
        break
