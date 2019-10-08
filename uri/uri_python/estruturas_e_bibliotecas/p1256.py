N = int(input())
flag = False
for n in range(N):
	if flag:
			print("")
	else:
		flag = True
	entry = input().split(" ")
	N = int(entry[0])
	M = int(entry[1])
	entry = input().split(" ")
	Hash = []
	for i in range(N):
		Hash.append([])	
	for i in range(M):
		Hash[int(entry[i]) % N].append(int(entry[i]))
	for i in range(N):
		saida = str(i) + ' -> '
		for j in range(len(Hash[i])):
			saida += str(Hash[i][j]) + ' -> '
		saida += '\\'
		print(saida)
	
	
