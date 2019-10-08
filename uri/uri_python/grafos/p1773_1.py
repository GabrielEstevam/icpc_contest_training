while True:
	try:
		entry = input().split(" ")
		N = int(entry[0])
		V = int(entry[1])
		E = []
		for v in range(V):
			entry = input().split(" ")
			E.append([int(entry[0]) - 1, int(entry[1]) - 1])
		entry = input().split(" ")
		keys = []
		for i in range(N - 1):
			keys.append(int(entry[i]) - 1)
		cor = []
		for i in range(N):
			cor.append(0)
		cor[0] = 1
		fila = []
		fila.append(0)
		while len(fila) > 0:
			print(fila)
			k = fila[0]
			fila.remove(fila[0])
			for i in range(len(keys)):
				if keys[i] == k:
					for j in range(V):
						if E[j][1] == (i + 1) and cor[E[j][0]] == 1:
							cor[i + 1] = 1
							fila.append(i + 1)
		flag = True
		for i in cor:
			if i == 0:
				flag = False
				break
		if flag:
			print("sim")
		else:
			print("nao")
	except EOFError:
		break
