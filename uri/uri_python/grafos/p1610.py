for T in range(int(input())):
	entry = input().split(' ')
	V = int(entry[0])
	A = int(entry[1])
	G = []
	cor = []
	for i in range(V):
		G.append([])
		cor.append(0)
	for i in range(A):
		entry = input().split(' ')
		G[int(entry[0])-1].append(int(entry[1])-1)
	for i in range(V):
		G[i] = list(set(G[i]))
	flag = False
	for i in range(V):
		if cor[i] == 0:
			pilha = [i]
			cor[i] = 1
			while len(pilha) > 0:
				topo = pilha[len(pilha) - 1]
				flag2 = True
				for j in range(len(G[topo])):
					if cor[G[topo][j]] == 0:
						pilha.append(G[topo][j])
						cor[G[topo][j]] = 1
						flag2 = False
						break
					elif cor[G[topo][j]] == 1:
						flag = True
						break
				if flag2:
					cor[pilha.pop()] = 2
				if flag:
					break
		if flag:
			break
	if flag:
		print('SIM')
	else:
		print('NAO')
