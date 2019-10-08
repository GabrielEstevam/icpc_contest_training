while True:
	try:
		N = int(input())
		largada = input().split(" ")
		chegada = input().split(" ")
		ptr = []
		for i in range(N):
			ptr.append(0)
		for i in range(N):
			largada[i] = int(largada[i]) - 1
			chegada[i] = int(chegada[i]) - 1
			ptr[largada[i]] = i
		for i in range(N):
			largada[ptr[chegada[i]]] = i
		ult = 0
		while True:
			flag = True
			for i in range(1, N):
				if largada[i - 1] > largada[i]:
					aux = largada[i - 1]
					largada[i - 1] = largada[i]
					largada[i] = aux
					ult += 1
					flag = False
			if flag:
				break
		print(ult)
	except EOFError:
		break
