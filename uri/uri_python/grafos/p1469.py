while True:
	try:
		entry = input().split(' ')
		N = int(entry[0])
		M = int(entry[1])
		I = int(entry[2])
		entry = input().split(' ')
		idade = []
		pos = []
		for i in range(N):
			idade.append(int(entry[i]))
			pos.append(i)
		gerente = []
		for i in range(N):
			gerente.append([])
		for i in range(M):
			entry = input().split(' ')
			gerente[int(entry[1])-1].append(int(entry[0])-1)
		for i in range(I):
			entry = input().split(' ')
			if len(entry) == 3:
				x = int(entry[1]) - 1
				y = int(entry[2]) - 1
				aux = idade[pos[x]]
				idade[pos[x]] = idade[pos[y]]
				idade[pos[y]] = aux
				aux = pos[x]
				pos[x] = pos[y]
				pos[y] = aux
			else:
				fila = set()
				menor = -1
				for j in range(len(gerente[pos[int(entry[1])-1]])):
					fila.add(gerente[pos[int(entry[1])-1]][j])
				while len(fila) > 0:
					k = fila.pop()
					if idade[k] < menor or menor == -1:
						menor = idade[k]
					for j in range(len(gerente[k])):
						fila.add(gerente[k][j])
				if menor == -1:
					print('*')
				else:
					print(menor)


	except EOFError:
		break