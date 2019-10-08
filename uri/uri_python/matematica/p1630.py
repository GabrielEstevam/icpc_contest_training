def euclides(a, b):
	if b == 0:
		return a
	else:
		return euclides(b, a % b)

while True:
	try:
		entry = input().split(' ')
		A = int(entry[0])
		B = int(entry[1])
		mdc = euclides(A, B)
		print(int(A/mdc * 2 + B/mdc* 2))
	except EOFError:
		break
