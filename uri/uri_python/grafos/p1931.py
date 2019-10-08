def Dijkstra(G):
	N = len(G)
	D = []
	Flag = []
	for i in range(N):
		D.append(10001) #atribui infinito
		Flag.append(True)
	D[0] = 0
	lenFila = N
	while lenFila > 0:
		u = 0
		while Flag[u] == 0:
			u += 1
		for i in range(N):
			if Flag[i] and D[i] < D[u]:
				u = i
		Flag[u] = False
		lenFila -= 1
		for v in range(N):
			if G[u][v] > 0:
				for j in range(N):
					if G[v][j] > 0 and D[j] > D[u] + G[u][v] + G[v][j]:
						D[j] = D[u] + G[u][v] + G[v][j]
	return D

# Main
grafo = []
c = []
entry = input().split(" ")
N = int(entry[0])
V = int(entry[1])
for n in range(N):
	grafo.append([])
	for i in range(N):
		grafo[n].append(0)

for v in range(V):
	entry = input().split(" ")
	x = int(entry[0]) - 1
	y = int(entry[1]) - 1
	z = int(entry[2])
	grafo[x][y] = z
	grafo[y][x] = z
D = Dijkstra(grafo)
if D[N-1] != 10001:
	print(D[N-1])
else:
	print(-1)
