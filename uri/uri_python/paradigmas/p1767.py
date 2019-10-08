for N in range(int(input())):
	n = int(input())
	c = 51
	P = []
	Pi = []
	Pf = []
	for i in range(n):
		entry = input().split(" ")
		P.append([int(entry[0]), int(entry[1])])
	for i in range(c):
		Pi.append([0, 0, 0])
		Pf.append([0, 0, 0])
	for i in range(n):
		if i % 2 == 0:
			for j in range(c):
				if P[i][1] > j:
					Pf[j] = Pi[j]
				else:
					if Pi[j-P[i][1]][0] + P[i][0] > Pi[j][0]:
						Pf[j] = [Pi[j-P[i][1]][0] + P[i][0], Pi[j-P[i][1]][1] + 1, Pi[j-P[i][1]][2] + P[i][1]] 
					else:
						Pf[j] = Pi[j]
		else:
			for j in range(c):
				if P[i][1] > j:
					Pi[j] = Pf[j]
				else:
					if Pf[j-P[i][1]][0] + P[i][0] > Pf[j][0]:
						Pi[j] = [Pf[j-P[i][1]][0] + P[i][0], Pf[j-P[i][1]][1] + 1, Pf[j-P[i][1]][2] + P[i][1]]
					else:
						Pi[j] = Pf[j]

	if n % 2 == 0:
		print(Pi[50][0], 'brinquedos')
		print('Peso:', Pi[50][2],'kg')
		print('sobra(m)', n - Pi[50][1], 'pacote(s)')
	else:
		print(Pf[50][0], 'brinquedos')
		print('Peso:', Pf[50][2],'kg')
		print('sobra(m)', n - Pf[50][1], 'pacote(s)')
	print('')
