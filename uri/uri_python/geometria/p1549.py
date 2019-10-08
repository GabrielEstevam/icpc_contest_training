import math
for n in range(int(input())):
	entry = input().split(' ')
	N = int(entry[0])
	V = int(entry[1])	
	entry = input().split(' ')
	b = int(entry[0])
	B = int(entry[1])
	H = int(entry[2])

	delta = H
	h = H
	r = b
	while (True):
		R = (B - b)*h/H + b
		v_s = math.pi*h/3 * (R*R + R*r + r*r)
		if (round(v_s*N, 2) == V):
			break
		else:
			if (v_s*N > V):
				h -= delta
			else:
				h += delta
			delta /= 2

	print("{:.2f}".format(round(h, 2)))