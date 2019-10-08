import math
pi = 3.142
while True:
	try:
		entry = input().split(' ')
		A = float(entry[0])
		D = float(entry[1])
		R = float(entry[2])
		a = D*math.cos(R*(pi/180))
		print("{:.4f}".format(A-a))
	except EOFError:
		break