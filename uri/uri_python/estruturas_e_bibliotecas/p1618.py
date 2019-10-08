for n in range(int(input())):
	entry = input().split(" ")
	ax = int(entry[0])
	ay = int(entry[1])
	bx = int(entry[2])
	by = int(entry[3])
	cx = int(entry[4])
	cy = int(entry[5])
	dx = int(entry[6])
	dy = int(entry[7])
	rx = int(entry[8])
	ry = int(entry[9])

	if (ax <= bx):
		x1 = ax
		x2 = bx
	else:
		x1 = bx
		x2 = ax
	if (ay <= dy):
		y1 = ay
		y2 = dy
	else:
		y1 = dy
		y2 = ay
	
	'''if (rx > x1 and rx < x2 and ry > y1 and ry < y2):
		print(1)
	else:
		print(0)'''

	if (rx <= x1 or rx >= x2 or ry <= y1 or ry >= y2):
		print(0)
	else:
		print(1)
