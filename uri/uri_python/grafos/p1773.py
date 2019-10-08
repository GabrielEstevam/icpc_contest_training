def buscaLargura(G):
	N = len(G)
	cor = []
	arvore = []
	for i in range(N):
		cor.append(-1) #pinta de branco
		arvore.append(-1)
	x = 0
	y = 0
	flag = False
	for i in range(N):
		for j in range(N):
			if G[i][j]:
				x = i
				y = j
				flag = True
				break
		if flag:
			break
	fila = []		
	fila.append(x)
	cor[x] = 0 #pinta de azul
	while len(fila) > 0:
			x = fila[0]
			fila.remove(fila[0])
			cor[x] = 1 #pinta de preto
			for i in range(N):
				if G[x][i] and cor[i] == -1:
					cor[i] = 0 #pinta de azul
					fila.append(i)
					arvore[i] = x
	return arvore

# Main
grafo = []
entry = input().split(" ") 
N = int(entry[0])
V = int(entry[1])
for n in range(N):
	grafo.append([])
	for i in range(N):
		grafo[n].append(0)
for v in range(V):
	entry = input().split(" ")
	i = int(entry[0]) - 1
	j = int(entry[1]) - 1
	grafo[i][j] = 1
	grafo[j][i] = 1

arvore = buscaLargura(grafo)
print(arvore)
