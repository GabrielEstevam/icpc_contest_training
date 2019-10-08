k = 0
flag = False
while True:
	try:
		F = 0
		M = 0
		n = int(input())
		entry = input().split(' ')
		for i in range(int(len(entry)/2)):
			if int(entry[i*2]) == n:
				if entry[i*2 + 1] == 'F':
					F += 1
				else:
					M += 1

		if flag:
			print('')
		else:
			flag = True
		k += 1
		print('Caso', str(k)+':')
		print('Pares Iguais:', F+M)
		print('F:', F)
		print('M:', M)

	except EOFError:
		break