N = int(input())
k = 1
while N > 0:
	primeiro = input()
	segundo = input()
	print('Teste', k)
	k += 1
	for n in range(N):
		entry = input().split(' ')
		if (int(entry[0]) + int(entry[1])) % 2 == 0:
			print(primeiro)
		else:
			print(segundo)
	print('')
	N = int(input())