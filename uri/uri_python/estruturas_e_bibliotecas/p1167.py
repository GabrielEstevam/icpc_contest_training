N = int(input())
while N != 0:
	v = []
	for i in range(N):
		entry = input().split(' ')
		v.append([entry[0], int(entry[1])])
	j = 0
	k = v[0][1]
	if k % 2 == 0:
		k = N-1
	while True:
		if k % 2 == 1:
			j += k
		else:
			j -= (k - 1)
		while j < 0:
			j += N
		while j >= N:
			j -= N
		k = v[j][1]
		del v[j]
		j -= 1
		N -= 1
		if len(v) == 1:
			break
	print("Vencedor(a):", v[0][0])
	N = int(input())