for N in range(int(input())):
	entry = input().split(" ")
	X = int(entry[0])
	Y = int(entry[1])
	mapa = []
	soma = 0
	for i in range(X):
		entry = input().split(" ")
		mapa.append([])		
		for j in range(Y):
			k = int(entry[j])
			mapa[i].append(k)
			if (k == 1):
				soma += 1
	fila = []
	entry = input().split(" ")
	x = int(entry[0]) - 1
	y = int(entry[1]) - 1
	fila.append([x, y, 0])
	mapa[x][y] = 2
	count = 1
	while (len(fila) > 0):
		x = fila[0][0]
		y = fila[0][1]
		depth = fila[0][2]
		#print(mapa)
		fila.pop(0)
		if (x > 0):
			if mapa[x - 1][y] == 1:
				fila.append([x - 1, y, depth + 1])
				mapa[x - 1][y] = mapa[x][y] + 1
				count += 1
			if (y > 0):
				if mapa[x - 1][y - 1] == 1:
					fila.append([x - 1, y - 1, depth + 1])
					mapa[x - 1][y - 1] = mapa[x][y] + 1
					count += 1
			if (y + 1 < Y):
				if mapa[x - 1][y + 1] == 1:
					fila.append([x - 1, y + 1, depth + 1])
					mapa[x - 1][y + 1] = mapa[x][y] + 1
					count += 1
		if (x + 1 < X):
			if mapa[x + 1][y] == 1:
				fila.append([x + 1, y, depth + 1])
				mapa[x + 1][y] = mapa[x][y] + 1
				count += 1
			if (y > 0):
				if mapa[x + 1][y - 1] == 1:
					fila.append([x + 1, y - 1, depth + 1])
					mapa[x + 1][y - 1] = mapa[x][y] + 1
					count += 1
			if (y + 1 < Y):
				if mapa[x + 1][y + 1] == 1:
					fila.append([x + 1, y + 1, depth + 1])
					mapa[x + 1][y + 1] = mapa[x][y] + 1
					count += 1
		if (y > 0):
			if mapa[x][y - 1] == 1:
				fila.append([x, y - 1, depth + 1])
				mapa[x][y - 1] = mapa[x][y] + 1
				count += 1
		if (y + 1 < Y):
			if mapa[x][y + 1] == 1:
				fila.append([x, y + 1, depth + 1])
				mapa[x][y + 1] = mapa[x][y] + 1
				count += 1
		if count == soma:
			break
	depth = 0
	for i in range(X):
		for j in range(Y):
			if mapa[i][j] > depth:
				depth = mapa[i][j]
	print(depth - 2)
