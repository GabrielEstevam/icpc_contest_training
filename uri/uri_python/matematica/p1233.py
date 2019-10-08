while True:
	try:
		N = int(input())
		primos = [2, 3, 5]
		fila = []		
		for i in range(7, N):
			if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
				primos.append(i)
		print(primos)
		'''while (i < len(primos)):
			k = 0
			while (primos[i]*k < N):
				try:
					primos.remove(primos[i]*k)
				except ValueError:
					k += 0
				k += 1
			i += 1
		print(primos)'''
	except EOFError:
		break

'''def euclides_MDC(a, b):
    if b == 0:
        return a
    else:
        return euclides_MDC(b, a%b)

while True:
	try:
		N = int(input())
		cont = 1
		for i in range(2, int(N/2)):
			if euclides_MDC(i, N) == 1:
				cont += 1
			print(cont)
		print(cont)
	except EOFError:
		break'''
