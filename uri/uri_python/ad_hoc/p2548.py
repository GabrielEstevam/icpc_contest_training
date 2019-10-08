while True:
	try:
		entrada = input().split(" ")
		N = int(entrada[0])
		M = int(entrada[1])
		entry = input().split(" ")
		lista = []
		for i in range(N):
			lista.append(int(entry[i]))
		#print(lista)
		soma = 0
		entry.sort()
		for i in range(M):
			soma += lista[N-i-1]
		print(soma)
	except EOFError:
		break
