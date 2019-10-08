def buscaLargura(G):
	N = len(G)
	cor = []	
	for i in range(N):
		cor.append(-1) #pinta de branco
	k = 1
	floresta = []
	while True:
		x = 0
		while cor[x] != -1:
			x += 1		
		fila = []		
		fila.append(x)
		cor[x] = 0 #pinta de azul
		arvore = []
		while len(fila) > 0:
			x = fila[0]
			fila.remove(fila[0])
			cor[x] = k #pinta de uma cor
			arvore.append(x)
			for i in range(N):
				if G[x][i] and cor[i] == -1:
					cor[i] = 0 #pinta de azul
					fila.append(i)
		floresta.append(arvore)
		flagCor = True
		for i in cor:
			if i == -1:
				flagCor = False
		if flagCor:
			break
		k += 1
	return floresta

# Main
entry = input().split(' ')
V = int(entry[0])
E = int(entry[1])
G = []
for i in range(V):
	G.append([])
	for j in range(V):
		if i == j:
			G[i].append(1)
		else:
			G[i].append(0)
for i in range(E):
	entry = input().split(' ')
	x = int(entry[0]) - 1
	y = int(entry[1]) - 1
	G[x][y] = 1
	G[y][x] = 1
floresta = buscaLargura(G)
print(len(floresta))

