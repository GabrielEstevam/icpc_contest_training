entry = input().split(' ')
N = int(entry[0])
M = int(entry[1])

player = []
for i in range(N):
	player.append(1)

for i in range(N):
	entry = input().split(' ')
	for j in range(M):
		if int(entry[j]) == 0:
			player[i] = 0

cont = 0
for i in range(N):
	if player[i] > 0:
		cont += 1

print(cont)