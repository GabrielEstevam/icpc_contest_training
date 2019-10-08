while True:
	try:
		entry = input().split(' ')
		R = int(entry[0])
		K = int(entry[1])

		B = [0] # numero de incidencias com numero de pontes igual ao indice
		A = []
		for i in range(R):
			A.append(0)

		for i in range(K):
			entry = input().split(' ')
			A[int(entry[0]) - 1] += 1
			A[int(entry[1]) - 1] += 1
		#print('A:', A)

		for i in range(1, K+1):
			flag = True
			for j in range(R):	
				if A[j] <= i and A[j] > 0:
					#print('A, B, i, j, Aj: ', len(A), len(B), i, j, A[j])
					if A[j] + B[i - A[j]] == i:
						B.append(i)
						flag = False
						break
			if (flag):
				B.append(0)
				#B.append(B[i - 1])

		if B[K] == K:
			print('S')
		else:
			print('N')
	except EOFError:
		break
