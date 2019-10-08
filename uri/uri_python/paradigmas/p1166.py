import math
C = []
for i in range(1, 51):
	A = []
	for j in range(i):
		A.append(0)
	k = 1
	while True:
		flag = True
		for j in range(i):
			if math.sqrt(A[j]+k) % 1 == 0 or A[j] == 0:
				A[j] = k
				flag = False
				break
		if flag:
			C.append(k-1)
			break
		k += 1
	A.clear()

for t in range(int(input())):
	print(C[int(input())-1])
