entry = input().split(" ")
N = int(entry[0])
M = int(entry[1])
K = int(entry[2])
board = []
for i in range(N):
	row = []
	for j in range(M):
		row.append("")
	board.append(row)
player = 0
for k in range(K):
	entry = input().split(" ")
	if entry[0] == 'L':
		x = int(entry[1]) - 1
		for j in range(M):
			board[x][j] = player
	else:
		y = int(entry[1]) - 1
		for i in range(N):
			board[i][y] = player
	player += 1
	player = player % 4
R = 0
H = 0
C = 0
P = 0
for i in range(N):
	for j in range(M):
		if board[i][j] == 0:
			R += 1
		elif board[i][j] == 1:
			H += 1
		elif board[i][j] == 2:
			C += 1
		elif board [i][j] == 3:
			P += 1

print('R' + str(R) + ' H' + str(H) + ' C' + str(C) + ' P' + str(P))
