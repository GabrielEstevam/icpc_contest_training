while True:
	try:
		N = int(input())
		epr = 0
		ehd = 0
		intrusos = 0
		for i in range(N):
			entry = input().split(' ')
			if entry[1] == 'EPR':
				epr += 1
			elif entry[1] == 'EHD':
				ehd += 1
			else:
				intrusos += 1
		print('EPR:', epr)
		print('EHD:', ehd)
		print('INTRUSOS:', intrusos)
	except EOFError:
		break
