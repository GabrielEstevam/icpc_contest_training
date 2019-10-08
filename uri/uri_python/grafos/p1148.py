def Dijkstra(G, v):
	N = len(G)
	s = 0
	D = []
	cor = []
	for i in range(N):
		D.append(100000000) #atribui infinito
		cor.append(1)
	D[v] = 0
	cor[v] = 0
	fila = [v]
	while len(fila) > 0:
		u = fila[0]
		fila.remove(u)
		for i in range(N):
			if G[u][i] > -1:
				if D[i] > D[u] + G[u][i]:
					D[i] = D[u] + G[u][i]
					if cor[i]:
						fila.append(i)
						cor[i] = 0
		if len(fila) == 0:
			for i in range(N):
				if cor[i]:
					fila.append(i)
					cor[i] = 0
					break
	return D

# Main
grafo = []
buscas = []
entry = input().split(" ")
N = int(entry[0])
V = int(entry[1])
while (N != 0 or V != 0):
	for i in range(N):
		grafo.append([])
		buscas.append([])
		for j in range(N):
			grafo[i].append(-1)		

	for v in range(V):
		entry = input().split(" ")
		if (grafo[int(entry[1])-1][int(entry[0])-1] > -1):
			grafo[int(entry[1])-1][int(entry[0])-1] = 0
			grafo[int(entry[0])-1][int(entry[1])-1] = 0
		else:
			grafo[int(entry[0])-1][int(entry[1])-1] = int(entry[2])


	for k in range(int(input())):
		entry = input().split(" ")
		if (len(buscas[int(entry[0])-1]) > 0):
			D = buscas[int(entry[0])-1]
		else:
			D = Dijkstra(grafo, int(entry[0])-1)
			buscas[int(entry[0])-1] = D
		if D[int(entry[1])-1] == 100000000:
			print('Nao e possivel entregar a carta')
		else:
			print(D[int(entry[1])-1])
	print("")
	entry = input().split(" ")
	N = int(entry[0])
	V = int(entry[1])
	grafo.clear()
	buscas.clear()
