entry = input().split(" ")
N = int(entry[0])
M = int(entry[1])
mapa = []

for i in range(N):
    entry = input().split(" ")
    mapa.append([])
    for j in range(M):
        mapa[i].append(int(entry[j]))

flag = True
for i in range(1, N-1, 1):
    for j in range(1, M-1, 1):
        if mapa[i][j] == 42:
            if mapa[i - 1][j - 1] == 7 and mapa[i - 1][j] == 7 and mapa[i - 1][j + 1] == 7 and mapa[i][j - 1] == 7 and mapa[i][j + 1] == 7 and mapa[i + 1][j - 1] == 7 and mapa[i + 1][j] == 7 and mapa[i + 1][j + 1] == 7:
                    print(i+1, j+1)
                    flag = False
                    break
if flag:
    print('0 0')