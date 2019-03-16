''' (PARA) Problema da Mochila 0-1 '''
N = int(input())
while N > 0:
	c = int(input())
	P = []
	Pi = []
	Pf = []
	for i in range(N):
		entry = input().split(" ")
		P.append([int(entry[0]), int(entry[1])])
	for i in range(c + 1):
		Pi.append(0)
		Pf.append(0)
	for i in range(N):
		if i % 2 == 0:
			for j in range(c + 1):
				if P[i][1] > j:
					Pf[j] = Pi[j]
				else:
					if Pi[j-P[i][1]] + P[i][0] > Pi[j]:
						Pf[j] = Pi[j-P[i][1]] + P[i][0]
					else:
						Pf[j] = Pi[j]
		else:
			for j in range(c + 1):
				if P[i][1] > j:
					Pi[j] = Pf[j]
				else:
					if Pf[j-P[i][1]] + P[i][0] > Pf[j]:
						Pi[j] = Pf[j-P[i][1]] + P[i][0]
					else:
						Pi[j] = Pf[j]

	if N % 2 == 0:
		print(Pi[c], 'min.')
	else:
		print(Pf[c], 'min.')
	N = int(input())
