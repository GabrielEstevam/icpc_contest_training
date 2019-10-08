entry = input().split(' ')
A = int(entry[0])
B = int(entry[1])
while A != 0 or B != 0:
	print(A*2 - B)
	entry = input().split(' ')
	A = int(entry[0])
	B = int(entry[1])