entry = input().split(' ')
A = int(entry[0])
B = int(entry[1])
while A != 0 and  B != 0:
	entry = input().split(' ')
	atacantes = []
	for i in range(A):
		atacantes.append(int(entry[i]))
	entry = input().split(' ')
	defensores = []
	for i in range(B):
		defensores.append(int(entry[i]))
	defensores.sort()

	flag = False
	for i in range(A):
		if (atacantes[i] < defensores[1]):
			flag = True
			break

	if flag:
		print('Y')
	else:
		print('N')

	entry = input().split(' ')
	A = int(entry[0])
	B = int(entry[1])