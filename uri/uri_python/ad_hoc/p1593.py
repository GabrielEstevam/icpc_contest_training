for n in range(int(input())):
	entry = str(bin(int(input())))
	cont = 0
	for i in range(2, len(entry)):
		if entry[i] == '1':
			cont += 1
	print(cont)