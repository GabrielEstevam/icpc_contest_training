N = int(input())
while (N!= 0):
	entry = input().split(" ")
	while (int(entry[0]) != 0):		
		for i in range(N):
			entry[i] = int(entry[i])		
		pilha = []
		k = 1
		flag = True
		while len(entry) > 0:
			if len(pilha) > 0:
				if pilha[0] == entry[0]:
					pilha.remove(pilha[0])
					entry.remove(entry[0])
				elif k <= N:
					pilha.insert(0, k)
					k += 1
				else:
					flag = False
					break
			elif k <= N:
				pilha.insert(0, k)
				k += 1
			else:
				flag = False
				break
		if flag:
			print('Yes')
		else:
			print('No')
		entry = input().split(" ")
	print("")
	N = int(input())
