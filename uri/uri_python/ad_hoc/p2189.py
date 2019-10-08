N = int(input())
k = 1
while N > 0:
	entry = input().split(' ')
	win = 0
	for i in range(N):
		if int(entry[i]) == i + 1:
			win = i + 1
			break
	print('Teste', k)
	k += 1
	print(win)
	print('')

	N = int(input())