def multiplicacao(A, n):
	if n == 0:
		return [[1, 0], [0, 1]]
	else:
		m = multiplicacao(A, int(n/2))
		ms = [[0,0],[0,0]]

		ms[0][0] = (m[0][0]*m[0][0] + m[0][1]*m[1][0]) % 1000000
		ms[0][1] = (m[0][0]*m[0][1] + m[0][1]*m[1][1]) % 1000000
		ms[1][0] = (m[0][0]*m[1][0] + m[1][0]*m[1][1]) % 1000000
		ms[1][1] = (m[1][0]*m[0][1] + m[1][1]*m[1][1]) % 1000000
		if n % 2 == 1:
			m[0][0] = (A[0][0]*ms[0][0] + A[0][1]*ms[1][0]) % 1000000
			m[0][1] = (A[0][0]*ms[0][1] + A[0][1]*ms[1][1]) % 1000000
			m[1][0] = (A[0][0]*ms[1][0] + A[1][0]*ms[1][1]) % 1000000
			m[1][1] = (A[1][0]*ms[0][1] + A[1][1]*ms[1][1]) % 1000000
			return m
		else:
			return ms

while True:
	try:
		entry = input().split(' ')
		N = int(entry[0])
		K = int(entry[1])
		L = int(entry[2])
		n = int(N / 5)
		A = [[0, L],[1, K]]
		A = multiplicacao(A, n)
		print('%06d' % ((A[0][0] + K*A[1][0]) % 1000000))

	except EOFError:
		break