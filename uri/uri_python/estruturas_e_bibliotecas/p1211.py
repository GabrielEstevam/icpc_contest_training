while True:
	try:
		entry = []
		count = 0
		n = int(input())
		for i in range(n):
			entry.append(input())
		entry.sort()
		m = len(entry[0])
		for i in range(1, n):
			for j in range(m):
				if (entry[i-1][j] == entry[i][j]):
					count += 1
				else:
					break
		print(count)
	except EOFError:
		break
