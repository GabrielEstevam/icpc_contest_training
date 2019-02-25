''' Dyjkstra Python3 '''

def Dijkstra(G):
	N = len(G)
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
print(D)
