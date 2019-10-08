def subset(B, k, n, A, soma, r):
	if soma == r:
		return 1
	else:
		if k+1 < n:
			B[k] = True		
			r1 = subset(B, k+1, n, A, soma + A[k], r)
			B[k]= False
			r2 = subset(B, k+1, n, A, soma, r)
			return r1 or r2	
		else:
			return 0

while True:
	try:
		entry = input().split(' ')
		R = int(entry[0])
		K = int(entry[1])

		B = []
		A = []
		for i in range(R):
			B.append(False)
			A.append(0)

		for i in range(K):
			entry = input().split(' ')
			A[int(entry[0]) - 1] += 1
			A[int(entry[1]) - 1] += 1
		#print('A:', A)

		if subset(B, 0, R, A, 0, K):
			print('S')
		else:
			print('N')
	except EOFError:
		break
