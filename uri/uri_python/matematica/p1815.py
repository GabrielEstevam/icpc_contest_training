k = 1
while True:
	entry = input().split(" ")
	if len(entry) == 1:
		break
	N = int(entry[0])
	T = int(entry[1]) - 1
	K = int(entry[2]) - 1
	M = int(entry[3])
	P = []
	for i in range(N):
		entry = input().split(" ")
		P.append([])
		for j in range(N):
			P[i].append(float(entry[j]))
	Prob = []
	aux = []
	for i in range(N):
		Prob.append(P[T][i])
		aux.append(0)
	for m in range(M-1):
		for i in range(N):		
			if i != K:		
				for j in range(N):
					aux[j] += Prob[i]*P[i][j]
		aux[K] += Prob[K]		
		for i in range(N):
			Prob[i] = aux[i]
			aux[i] = 0
	print("Instancia", k)
	k += 1
	print("%.6f" % (1 -Prob[K]))
	print("")
		
