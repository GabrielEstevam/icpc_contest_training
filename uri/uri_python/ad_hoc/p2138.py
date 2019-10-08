while True:
	try:
		entry = input()
		v = []
		for i in range(10):
			v.append(0)
		for i in range(len(entry)):
			v[int(entry[i])] += 1
		m = 0
		for i in range(1, 10):
			if v[i] >= v[m]:
				m = i
		print(m)
	except EOFError:
		break