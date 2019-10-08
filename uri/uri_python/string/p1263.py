while True:
	try:
		entry = input().split(" ")
		cont = 0
		aux = 0
		for i in range(1, len(entry)):
			if entry[i][0].lower() != entry[i-1][0].lower():
				if aux > 0:
					cont += 1
					aux = 0
			else:
				aux += 1
		if aux > 0:
			cont += 1
		print(cont)
	except EOFError:
		break
