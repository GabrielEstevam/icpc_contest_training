while True:
	try:
		N = int(input())
		entry = input().split(" ")
		media = 0
		for i in range(N):
			entry[i] = int(entry[i])
			media += entry[i]
		media /= N
		if media % 1 != 0:
			print(-1)
		else:
			soma = 0
			for i in range(len(entry)):
				soma += abs(entry[i] - media)
			print(int(soma/2 + 1))
	except EOFError:
		break
