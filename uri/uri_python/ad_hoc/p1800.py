entry = input().split(' ')
Q = int(entry[0])
E = int(entry[1])
q = []
for i in range(10000):
	q.append(0)
entry = input().split(' ')
for i in range(E):
	q[int(entry[i])] = 1
for i in range(Q):
	entry = int(input())
	if q[int(entry)] == 1:
		print(0)
	else:
		print(1)
	q[int(entry)] = 1