entry = input().split(" ")
N = int(entry[0])
K = int(entry[1])
while N != 0 or K != 0:
	pilha = []
	flag = True
	for i in range(N):
		#print('p:', pilha)
		entry = input().split(" ")
		if flag:
			ci = int(entry[0])
			cs = int(entry[1])		
			while True:
				if len(pilha) == 0:
					break
				if pilha[len(pilha) - 1][1] <= ci:
					pilha.pop()
				else:
					break
			if len(pilha) > 0:
				if pilha[len(pilha) - 1][1] < cs:
					flag = False
			pilha.append([ci, cs])
			if len(pilha) > K:
				flag = False
	#print(pilha)
	while len(pilha) > 1:
		#print('w:', pilha)
		if pilha[len(pilha) - 2][1] < pilha[len(pilha) - 1][1]:
			flag = False
			break
		pilha.pop()
	if flag:
		print("Sim")
	else:
		print("Nao")
	entry = input().split(" ")
	N = int(entry[0])
	K = int(entry[1])
