def buscaProfundidade(G):
	N = len(G)
	cor = []	
	for i in range(N):
		cor.append(-1) #pinta de branco
	flagLinha = False
	while True:
		x = 0
		i = 0
		while True:
			if G[x][i]:
				break
			i += 1
			if i == N:
				i = 0
				x += 1
				if x == N:
					break
		if x == N:
			break 		
		pilha = []		
		pilha.append([x, 1])
		cor[x] = 0 #pinta de azul
		while len(pilha) > 0:
			p = pilha[len(pilha) - 1]
			x = p[0]
			d = p[1]
			cor[x] = 0 #pinta de uma cor
			flag = True
			for i in range(N):
				if G[x][i]:
					if cor[i] == -1:
						cor[i] = 0 #pinta de azul
						pilha.append([i, d+1])
						if flagLinha:
							print("")
						saida = ""
						for j in range(d):
							saida += "  "
						flagLinha = False
						print(saida+str(x)+"-"+str(i), "pathR(G,"+str(i)+")")
						flag = False
						G[x][i] = 0
						break
					else:
						saida = ""
						for j in range(d):
							saida += "  "
						print(saida+str(x)+"-"+str(i))
						G[x][i] = 0
			if flag:
				pilha.pop()
		flagCor = True
		for i in cor:
			if i == -1:
				flagCor = False
				flagLinha = True
		if flagCor:
			break
	print("")

for n in range(int(input())):
	entry = input().split(" ")
	V = int(entry[0])
	E = int(entry[1])
	G = []
	for i in range(V):
		G.append([])
		for j in range(V):
			G[i].append(0)
	for i in range(E):
		entry = input().split(' ')
		x = int(entry[0])
		y = int(entry[1])
		G[x][y] = 1
	print("Caso", str(n+1)+":")
	buscaProfundidade(G)
	G.clear()

