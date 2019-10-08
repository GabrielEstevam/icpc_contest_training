entry = []
for i in range(5):
	entry.append(input().split(' '))
	for j in range(len(entry[i])):
		entry[i][j] = int(entry[i][j])
K = int(input())
v = []
for p in range(1, entry[0][0]+1):
	for m in range(1, entry[1][0]+1):
		for f in range(1, entry[2][0]+1):
			for q in range(1, entry[3][0]+1):
				for b in range(1, entry[4][0]+1):
					v.append(entry[0][p]+entry[1][m]+entry[2][f]+entry[3][q]+entry[4][b])
v.sort()
cont = 0
for i in range(len(v)-1, len(v)-K-1, -1):
	cont += v[i]
print(cont)