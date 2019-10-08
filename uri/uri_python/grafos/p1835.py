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

for N in range(int(input())):
	entry = input().split(" ")
	if len(entry) > 1:
		V = int(entry[0])
		E = int(entry[1])
	else:
		V = int(entry[0])
		E = int(input())
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
	if (len(floresta) == 1):
		print("Caso #" + str(N+1) + ": a promessa foi cumprida")
	else:
		print("Caso #" + str(N+1) + ": ainda falta(m) " + str(len(floresta) - 1) + " estrada(s)")

