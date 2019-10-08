entry = input().split(' ')
N = int(entry[0])
M = int(entry[1])
while N != 0 and M != 0:
	m = []
	fila = []
	for i in range(N):
		entry = input()
		row = []
		for j in range(M):
			if entry[j] == 'T':
				fila.append([i, j])
			row.append(entry[j])
		m.append(row)
	while len(fila) > 0:
		f = fila.pop(0)
		if f[0] + 1 < N:
			if m[f[0]+1][f[1]] == 'A':
				m[f[0]+1][f[1]] = 'T'
				fila.append([f[0]+1, f[1]])
		if f[0] - 1 >= 0:
			if m[f[0]-1][f[1]] == 'A':
				m[f[0]-1][f[1]] = 'T'
				fila.append([f[0]-1, f[1]])
		if f[1] + 1 < M:
			if m[f[0]][f[1]+1] == 'A':
				m[f[0]][f[1]+1] = 'T'
				fila.append([f[0], f[1]+1])
		if f[1] - 1 >= 0:
			if m[f[0]][f[1]-1] == 'A':
				m[f[0]][f[1]-1] = 'T'
				fila.append([f[0], f[1]-1])
	
	for i in range(N):
		out = ''
		for j in range(M):
			out += m[i][j]
		print(out)
	print('')
	entry = input().split(' ')
	N = int(entry[0])
	M = int(entry[1])
