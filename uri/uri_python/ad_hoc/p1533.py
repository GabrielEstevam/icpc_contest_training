N = int(input())
while N > 0:
	entry = input().split(" ")
	for i in range(N):
		entry[i] = int(entry[i])
	i = entry.index(max(entry))
	entry[i] = 0
	print(entry.index(max(entry)) + 1)
	N = int(input())
