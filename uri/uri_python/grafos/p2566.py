''' Disjstra - Python3 '''

def Dijkstra(G):
    N = len(G)
    s = 0
    D = []
    Flag = []
    for i in range(N):
        D.append(100000000) #atribui infinito
        Flag.append(1)
    D[0] = 0
    lenFila = N
    arvore = [] 
    for i in range(N):  
        arvore.append(-1)
    while lenFila > 0:
        u = 0
        while Flag[u] == 0:
            u += 1
        for i in range(N):
            if Flag[i] and D[i] < D[u]:
                u = i
        Flag[u] = 0
        lenFila -= 1
        for v in range(N):
            if G[u][v] > 0 and D[v] > D[u] + G[u][v]:
                D[v] = D[u] + G[u][v]
                arvore[v] = u
    return [arvore, D]

# Main
while True:
    try:
        entry = input().split(" ")
        N = int(entry[0])
        V = int(entry[1])
        grafo1 = []
        grafo2 = []
        for n in range(N):
            grafo1.append([])
            grafo2.append([])
            for i in range(N):
                grafo1[n].append(0)
                grafo2[n].append(0)

        for v in range(V):
            entry = input().split(" ")
            x = int(entry[0]) - 1
            y = int(entry[1]) - 1
            k = int(entry[2])
            z = int(entry[3])
            if (k == 1):
                grafo1[x][y] = z
            else:
                grafo2[x][y] = z
        D1 = Dijkstra(grafo1)
        D2 = Dijkstra(grafo2)
        if (D1[1][N-1] < D2[1][N-1]):
            print(D1[1][N-1])
        else:
            print(D2[1][N-1])
    except EOFError:
        break
