''' Floidwarshall (Probabilidade)- Python3 '''
entry = input().split(' ')
while len(entry) > 1:
	N = int(entry[0])
	M = int(entry[1])
	G = []
	for i in range(N):
	    G.append([])
	    for j in range(N):
	    	G[i].append(0)
	for i in range(N):
		G[i][i] = 1
	for i in range(M):
		entry = input().split(' ')
		G[int(entry[0])-1][int(entry[1])-1] = int(entry[2])/100
		G[int(entry[1])-1][int(entry[0])-1] = int(entry[2])/100

	for i in range(N):
		for j in range(N):
			for k in range(N):
				if G[i][k] < G[i][j] * G[j][k]:
					G[i][k] = G[i][j] * G[j][k]
					G[k][i] = G[i][j] * G[j][k]
	print('{:.6f} percent'.format(G[0][N-1]*100))
	entry = input().split(' ')