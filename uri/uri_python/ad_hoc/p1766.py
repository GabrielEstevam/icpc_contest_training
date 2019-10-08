def ordena(t):
    return t[1]*-1, t[2], t[3], t[0]
T = int(input())
for i in range(T):
    renas = []
    entry = input().split(" ")
    N = int(entry[0])
    M = int(entry[1])
    for j in range(N):
        entry = input().split(" ")
        tupla = (str(entry[0]), int(entry[1]), int(entry[2]), float(entry[3]))
        renas.append(tupla)
    renas = sorted(renas, key=ordena)
    print("CENARIO {"+str(i+1)+"}")
    for j in range(M):
        print(str(j+1)+" - "+renas[j][0])
