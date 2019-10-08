v = []
N = 1000003
for i in range(N):
	v.append(True)
v[0] = False
v[1] = False
for i in range(2, N):
	if v[i]:
		for j in range(i+i, N, i):
			v[j] = False
twin = [0, 0]
k = 0
for i in range(2, N-2):
	if v[i] and (v[i-2] or v[i+2]):
		k += 1
	twin.append(k)
for i in range(int(input())):
	entry = input().split(' ')
	print(abs(twin[int(entry[1])]-twin[int(entry[0])-1]))
