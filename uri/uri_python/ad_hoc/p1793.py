N = int(input())
while N > 0:
	entry = input().split(' ')
	t = 10
	for i in range(1, N):
		if int(entry[i]) >= int(entry[i-1]) + 10:
			t += 10
		else:
			t += (int(entry[i]) - int(entry[i-1]))
	print(t)
	N = int(input())