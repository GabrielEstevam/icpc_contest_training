entry = input().split(' ')
while entry[0] != '0':
	N = int(entry[0])
	k = int(entry[1])
	m = int(entry[2])
	v = []
	for i in range(N):
		v.append(1)
	x = N-1
	y = 0
	out = ""
	while sum(v) > 0:
		ks = 0
		while ks < k:
			x += 1
			if x >= N:
				x = 0
			ks += v[x]
		ms = 0
		while ms < m:
			y -= 1
			if y < 0:
				y = N-1
			ms += v[y]
		v[x] = 0
		v[y] = 0
		if x+1 >= 10:
			out += " " + str(x+1)
		else:
			out += "  " + str(x+1)
		if x != y:
			if y+1 >= 10:
				out += " " + str(y+1)
			else:
				out += "  " + str(y+1)
		if sum(v) > 0:
			out += ","
	print(out) 
	entry = input().split(' ')