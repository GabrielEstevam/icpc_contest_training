import math
for n in range(int(input())):
	entry = input().split(' ')
	print(math.ceil((int(entry[0]) - 2)/3)*math.ceil((int(entry[1]) - 2)/3))