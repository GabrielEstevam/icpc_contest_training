for n in range(int(input())):
	p = []
	for i in range(9):
		row = []
		for j in range(1+i):
			row.append(0)
		p.append(row)

	for i in range(5):
		entry = input().split(' ')
		for j in range(i+1):
			p[2*i][j*2] = int(entry[j])

	i = 2
	while i < 9:
		for j in range(int(i/2)):
			p[i][2*j+1] = int((p[i-2][2*j] - p[i][2*j] - p[i][2*j+2])/2)
		i += 2
	i = 1
	while i < 8:
		for j in range(len(p[i])):
			p[i][j] = p[i+1][j] + p[i+1][j+1]
		i += 2

	for i in range(9):
		out = str(p[i][0])
		for j in range(1, len(p[i])):
			out += ' '
			out += str(p[i][j])
		print(out)
