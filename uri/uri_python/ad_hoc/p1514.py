entry = input().split(" ")
N = int(entry[0])
M = int(entry[1])
while N != 0 and M != 0:
	linhas = []
	colunas = []
	for i in range(N):
		linhas.append(0)
	for i in range(M):
		colunas.append(0)
	for i in range(N):
		entry = input().split(" ")
		for j in range(M):
			linhas[i] += int(entry[j])
			colunas[j] += int(entry[j])
	
	um = True
	dois = True
	tres = True
	quatro = True
	count = 0
	for i in range(N):
		if linhas[i] == M:
			um = False
		if linhas[i] == 0:
			quatro = False
	for i in range(M):
		if colunas[i] == N:
			tres = False
		if colunas[i] == 0:
			dois = False
	if um:
		count += 1
	if dois:
		count += 1
	if tres:
		count += 1
	if quatro:
		count += 1
	print(count)
	entry = input().split(" ")
	N = int(entry[0])
	M = int(entry[1])
