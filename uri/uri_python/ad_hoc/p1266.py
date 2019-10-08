N = int(input())
while N > 0:
	entry = input().split(' ')
	poste = []
	novos = 0
	for i in range(N):
		poste.append(int(entry[i]))
	if sum(poste) == 0:
		poste[0] = 1
		novos += 1
		
	i = 0
	while poste[i] == 0:
		i += 1
	pivo = i
	i += 1
	while i < N:
		if poste[i] == 0 and poste[i - 1] == 0:
			poste[i] = 1
			novos += 1
		i += 1
	if poste[N - 1] == 0 and poste[0] == 0:
		poste[0] = 1
		novos += 1
	i = 1
	while i < pivo:
		if poste[i] == 0 and poste[i - 1] == 0:
			poste[i] = 1
			novos += 1
		i += 1

	print(novos)

	N = int(input())