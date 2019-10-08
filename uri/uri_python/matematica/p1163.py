import math
g = 9.80665
pi = 3.14159
while True:
	try:
		h = float(input())
		entry = input().split(' ')
		p1 = int(entry[0])
		p2 = int(entry[1])
		for i in range(int(input())):
			entry = input().split(' ')
			a = float(entry[0])
			v = float(entry[1])
			vx = v*math.cos((a*pi)/180.0)
			vy = v*math.sin((a*pi)/180.0)
			ts = vy/g
			hmax = vy*ts - (1/2)*g*ts*ts
			td = math.sqrt(((h+hmax)*2)/g)
			d = vx*(td+ts)
			if d >= p1 and d <= p2:
				print("{:.5f}".format(d), "-> DUCK")
			else:
				print("{:.5f}".format(d), "-> NUCK")
	except EOFError:
		break