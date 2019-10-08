import math
entry = input().split(' ')
n = int(entry[0])
m = int(entry[1])
u = int(entry[2])
A = []
for i in range(n):
	A.append(int(input()))
for i in range(m):
	entry = input().split(' ')
	L = int(entry[0])
	R = int(entry[1])
	v = int(entry[2])
	p = int(entry[3])
	k = 0
	for j in range(L-1, R):
		if A[j] < v:
			k += 1
	A[p-1] = math.floor((u*k)/(R-L+1))
for i in range(n):
	print(A[i])

