for n in range(int(input())):
	N = int(input())
	lista = []
	posicao = 0
	for i in range(N):
		entry = input().split(" ")
		if entry[0] == 'LEFT':
			posicao -= 1
			lista.append(-1)
		elif entry[0] == 'RIGHT':
			posicao += 1
			lista.append(1)
		else:
			lista.append(lista[int(entry[2])-1])
			posicao += lista[len(lista)-1]
	print(posicao)
