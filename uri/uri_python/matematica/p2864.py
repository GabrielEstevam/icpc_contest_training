import math
for n in range(int(input())):
	entry = input().split(' ')
	a = int(entry[0])
	b = int(entry[1])
	c = int(entry[2])
	print("{:.2f}".format(-1*(math.sqrt(b*b-4*a*c)-b)/(2*a)))