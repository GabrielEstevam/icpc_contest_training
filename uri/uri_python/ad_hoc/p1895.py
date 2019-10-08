entry = input().split(" ")
N = int(entry[0])
T = int(entry[1])
L = int(entry[2])
a = 0
b = 0
for i in range(N-1):
	entry = int(input())
	if abs(T-entry) <= L:
		if i % 2 == 0:
			a += abs(T-entry)
		else:
			b += abs(T-entry)
		T = entry
print(a, b)
