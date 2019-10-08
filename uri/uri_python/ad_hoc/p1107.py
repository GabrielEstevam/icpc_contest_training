entry = input().split(' ')
A = int(entry[0])
C = int(entry[1])
while A != 0:
	entry = input().split(' ')
	k = int(entry[0])
	cont = A - int(entry[0])
	for i in range(1, C):
		if int(entry[i]) < k:
			cont += (k - int(entry[i]))
		k = int(entry[i])
	print(cont)
	entry = input().split(' ')
	A = int(entry[0])
	C = int(entry[1])