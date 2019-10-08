for n in range(int(input())):
	N = int(input())
	H = input().split(' ')
	J = input()
	cont = 0
	for i in range(N):
		if (int(H[i]) >= 3 and J[i] == 'J') or (int(H[i]) <= 2 and J[i] == 'S'):
			cont += 1
	print(cont)