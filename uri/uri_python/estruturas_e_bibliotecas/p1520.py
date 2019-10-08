while True:
	try:
		N = input()
		if len(N) > 0:
			N = int(N)
			lista = []
			for i in range(N):
				entry = input().split(" ")
				for j in range(int(entry[0]), int(entry[1]) + 1):
					lista.append(j)
			lista.sort()
			a = -1
			b = -1
			entry = int(input())
			for i in range(len(lista)):
				if (lista[i] == entry):
					a = i
					break
			b = a
			if a >= 0:
				for i in range(a + 1, len(lista)):
					if (lista[i] != entry):
						break
					else:	
						b += 1
				print(entry, "found from", a, "to", b)
			else:
				print(entry, "not found")
	except EOFError:
		break
