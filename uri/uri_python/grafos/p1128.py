entry = input().split(' ')
N = int(entry[0])
M = int(entry[1])
while N != 0:
	G = []
	low = []
	pai = []
	stack = []
	k = [] # marca aonde parou a busca em i-esimo
	for i in range(N):
		low.append(-1)
		k.append(0)
		pai.append(-1)
		row = []
		for j in range(N):
			row.append(0)
		G.append(row)
	for i in range(M):
		entry = input().split(' ')
		G[int(entry[0])-1][int(entry[1])-1] = 1
		if int(entry[2]) == 2:
			G[int(entry[1])-1][int(entry[0])-1] = 1
	
	stack.append(0)
	low[0] = 0
	cont = 1
	while (len(stack) > 0):
		top = stack[len(stack)-1]
		i = k[top]
		if i <= N-1:
			k[top] += 1
			if G[top][i] == 1:
				if low[i] == -1:
					stack.append(i)
					low[i] = cont
					cont += 1
					pai[i] = top
				else:
					low[top] = min([low[top], low[i]])
		elif i == N:
			stack.pop()
			if pai[top] != -1:
				low[pai[top]] = min(low[pai[top]], low[top])
	print(low)
	print(pai)
	if len(set(low)) > 1:
		print(0)
	else:
		print(1)
	entry = input().split(' ')
	N = int(entry[0])
	M = int(entry[1])

