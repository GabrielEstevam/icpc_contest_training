N = int(input())
while N != 0:
	pares = 0
	for i in range(N):
		entry = input().split(' ')
		pares += int(int(entry[1])/2)
	print(int(pares/2))
	N = int(input())