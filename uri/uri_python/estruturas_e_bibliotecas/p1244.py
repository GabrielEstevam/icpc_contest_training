for N in range(int(input())):
	entry = input().split(" ")	
	entry = sorted(entry, key=lambda x:(-1*len(x)))
	saida = entry[0]
	for i in range(1, len(entry), 1):
		saida += " " + entry[i]	
	print(saida)
