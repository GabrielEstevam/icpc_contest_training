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

	if rx < ax and rx < bx and rx < cx and rx < dx:
		print(0)
	elif rx > ax and rx > bx and rx > cx and rx > dx:
		print(0)
	elif ry < ay and ry < by and ry < cy and ry < dy:
		print(0)
	elif ry > ay and ry > by and ry > cy and ry > dy:
		print(0)
	else:
		print(1)