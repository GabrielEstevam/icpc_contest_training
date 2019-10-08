N = int(input())
while N > 0:
	lista = []
	for i in range(N):
		entry = input().split(" ")
		lista.append(entry)
	M = int(input())
	falsos = 0
	for i in range(M):
		entry = input().split(" ")
		for j in range(N):
			aux = 0
			if entry[0] == lista[j][0]:
				if len(entry[1]) != len(lista[j][1]):
					falsos += 1
					break
				for k in range(len(entry[1])):
					if entry[1][k] != lista[j][1][k]:
						aux += 1
						if aux == 2:
							falsos += 1
							break
	print(falsos)
	N = int(input())
