N = int(input())
k = 1
while N > 0:
	a = 0
	b = 0
	for i in range(N):
		entry = input().split(' ')
		a += int(entry[0])
		b += int(entry[1])
	print('Teste', k)
	k += 1
	if a > b:
		print('Aldo')
	else:
		print('Beto')
	print('')

	N = int(input())