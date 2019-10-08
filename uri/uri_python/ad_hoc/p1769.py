while True:
	try:
		entry = input()
		a = []
		for i in entry:
			if i != '.' and i != '-':
				a.append(int(i))
		b1 = 0
		for i in range(9):
			b1 += a[i]*(i+1)
		b2 = 0
		for i in range(9):
			b2 += a[i]*(9-i)
		
		b1 = b1 % 11
		if b1 == 10:
			b1 = 0

		b2 = b2 % 11
		if b2 == 10:
			b2 = 0

		if b1 == a[9] and b2 == a[10]:
			print("CPF valido")
		else:
			print("CPF invalido")
	except EOFError:
		break
