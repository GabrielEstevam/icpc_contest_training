entry = input().split(' ')
A = int(entry[0])
B = int(entry[1])
C = int(entry[2])
while A != 0 or B != 0 or C != 0:
	print(int(pow(A*B*C, 1/3)))

	entry = input().split(' ')
	A = int(entry[0])
	B = int(entry[1])
	C = int(entry[2])