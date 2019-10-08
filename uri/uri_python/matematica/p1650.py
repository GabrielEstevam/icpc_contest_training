import math
entry = input().split(' ')
x = int(entry[0])
while x != 0:
	y = int(entry[1])
	b = int(entry[2])
	print(math.floor(((x-7)*(y-7)+b)/2))

	entry = input().split(' ')
	x = int(entry[0])