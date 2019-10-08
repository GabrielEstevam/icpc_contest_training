for n in range(int(input())):
	M = int(input())
	lista = []
	for i in range(M):
		lista.append(input().split(" "))
	P = int(input())
	total = 0	
	for i in range(P):
		entry = input().split(" ")
		for j in range(M):
			if (entry[0] == lista[j][0]):
				total += int(entry[1]) * float(lista[j][1])
				break
	print("R$ %.2f" % total)
