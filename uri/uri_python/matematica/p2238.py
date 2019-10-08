import math
entry = input().split(" ")
A = int(entry[0])
B = int(entry[1])
C = int(entry[2])
D = int(entry[3])
n = 0
for i in range(1, C):
	aux = C / i
	if aux % 1 == 0:
		if i % A == 0 and i % B != 0 and D % i != 0:
			print(i)
			break

