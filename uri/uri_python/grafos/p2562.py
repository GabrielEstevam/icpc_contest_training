while True:
	try:
		entry = input().split(' ')
		V = int(entry[0])
		A = int(entry[1])
		G = []
		cor = []
		for i in range(V):
			G.append([])
			cor.append(1)
		for i in range(A):
			entry = input().split(' ')
			G[int(entry[0])-1].append(int(entry[1])-1)
			G[int(entry[1])-1].append(int(entry[0])-1)
		E = int(input()) - 1
		pilha = [E]
		cor[E] = 0
		cont = 1
		while len(pilha) > 0:
			topo = pilha.pop()
			for i in range(len(G[topo])):
				if cor[G[topo][i]]:
					pilha.append(G[topo][i])
					cor[G[topo][i]] = 0
					cont += 1
			
		print(cont)
	except EOFError:
		break