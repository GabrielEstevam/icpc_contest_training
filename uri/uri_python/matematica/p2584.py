import math
t = math.tan(54*math.pi/180)*5/4
for n in range(int(input())):
	l = int(input())
	print("{:.3f}".format(l*l*t))