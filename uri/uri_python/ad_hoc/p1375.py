N = int(input())
while N != 0:
	v = []
	for i in range(N):
		entry = input().split(' ')
		v.append([i+int(entry[1]), entry[0]])
	v.sort()
	f = True
	for i in range(N):
		if v[i][0] != i:
			print(-1)
			f = False
			break
	out = v[0][1]
	if f:
		for i in range(1, N):
			out += " " + v[i][1]
		print(out)
	N = int(input())