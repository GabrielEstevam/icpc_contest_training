flag = True
while True:
	try:
		lista = []
		for i in range(96):
			lista.append([0, i+32])
		entry = input()
		for i in entry:
			lista[ord(i)-32][0] += 1
		from operator import itemgetter, attrgetter
		lista.sort(key=itemgetter(1), reverse=True)
		lista.sort(key=itemgetter(0))
		if flag:
			flag = False
		else:
			print("")
		for i in lista:
			if i[0] > 0:
				print(i[1], i[0])
	except EOFError:
		break
