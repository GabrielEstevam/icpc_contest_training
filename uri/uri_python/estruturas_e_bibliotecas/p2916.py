while True:
	try:
		entry = input().split(' ')
		N = int(entry[0])
		K = int(entry[1])
		entry = input().split(' ')
		for i in range(N):
			entry[i] = int(entry[i])
		entry.sort()
		soma = 0
		for i in range(K):
			soma += entry[N-1-i]
		print(soma)
	except EOFError:
		break