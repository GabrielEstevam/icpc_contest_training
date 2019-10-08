while True:
	try:
		T = int(input())
		entry = input().split(" + ")
		saida = ""
		for i in range(T):
			entry[i] = entry[i].split('x')
			saida += str(int(entry[i][0])*int(entry[i][1]))+"x"
			if int(entry[i][1]) > 2:			
				saida += str(int(entry[i][1])-1)
			if i != T-1:
				saida += " + "
		print(saida)
	except EOFError:
		break
