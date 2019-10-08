for T in range(int(input())):
	N = int(input())
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
		G[int(entry[0])].append(int(entry[1]))
		G[int(entry[1])].append(int(entry[0]))
	pilha = [N]
	cor[N] = 0
	cont = 0
	while len(pilha) > 0:
		topo = pilha[len(pilha) - 1]
		flag = True
		for i in range(len(G[topo])):
			if cor[G[topo][i]]:
				pilha.append(G[topo][i])
				cor[G[topo][i]] = 0
				flag = False
				break
		if flag:
			pilha.pop()
		cont += 1
	print(cont-1)
