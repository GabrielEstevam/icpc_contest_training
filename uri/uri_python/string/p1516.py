entry = input().split(" ")
N = int(entry[0])
M = int(entry[1])
while int(entry[0]) != 0 and int(entry[1]) != 0:
    lista = []
    for i in range(N):
        lista.append(input())
    entry = input().split(" ")
    A = int(int(entry[0])/N)
    B = int(int(entry[1])/M)
    for i in range(N):
        for a in range(A):
            saida = ""
            for j in range(M):
                for b in range(B):
                    saida += lista[i][j]
            print(saida)
    print("")
    entry = input().split(" ")
    N = int(entry[0])
    M = int(entry[1])