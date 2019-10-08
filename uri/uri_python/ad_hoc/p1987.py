while True:
	try:
		entry = input().split(' ')
		soma = 0
		for i in entry[1]:
			soma += int(i)
		if (soma % 3 == 0):
			print(soma, 'sim')
		else:
			print(soma, 'nao')	

	except EOFError:
		break