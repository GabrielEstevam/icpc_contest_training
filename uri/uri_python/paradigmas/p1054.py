for t in range(int(input())):
	entry = input().split(' ')
	N = int(entry[0])
	D = int(entry[1])
	if N == 0:
		print("Case " + str(t+1) + ": " + str(D))
	else:
		entry = []
		entry.append(['B', 0])
		entr = input().split(' ')
		for i in range(N):
			entr[i] = entr[i].split('-')
		for i in range(N):
			entry.append([entr[i][0], int(entr[i][1])])
		entry.append(['B', D])
		pivo = 0
		pivoProx = 0
		dist = []
		for i in range(N+2):
			if entry[i][0] == 'B':
				dist.append(entry[i][1] - entry[pivo][1])
				pivo = i
				pivoProx = i
			else:
				dist.append(entry[i][1] - entry[pivo][1])
				pivo = pivoProx
				pivoProx = i
		dist.sort()
		print("Case " + str(t+1) + ": " + str(max(dist)))