P = []
for i in range(101):
	P.append(0)
entry = input().split(' ')
N = int(entry[0])
K = int(entry[1])
while N != 0 or K != 0:
	entry = input().split()
	for i in range(N):
		P[int(entry[i])] += 1
	cont = 0
	for i in range(len(P)):
		if P[i] >= K:
			cont += 1
	print(cont)
	entry = input().split(' ')
	N = int(entry[0])
	K = int(entry[1])
	for i in range(101):
		P[i] = 0