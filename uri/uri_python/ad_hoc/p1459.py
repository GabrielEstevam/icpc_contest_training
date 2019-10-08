while True:
	try:
		N = int(input())
		p = []
		for i in range(N):
			entry = input().split()
			p.append([int(entry[0]), 0])
			p.append([int(entry[1]), 1])
		p.sort()
		print(p)
		aux = 0
		cont = 1
		for i in range(2*N):
			if p[i][1] != aux:
				cont += 1
				aux = p[i][1]
		print(int(cont/2))

	except EOFError:
		break