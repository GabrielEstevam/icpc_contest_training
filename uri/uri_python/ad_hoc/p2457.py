letra = input()
cont = 0
entry = input().split(' ')
for i in range(len(entry)):
	for j in range(len(entry[i])):
		if str(entry[i][j]) == str(letra):
			cont += 1
			break
print('{:.1f}'.format(100*cont/len(entry)))