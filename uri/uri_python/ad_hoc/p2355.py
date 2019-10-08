import math
entry = int(input())
while entry > 0:
	b = math.floor(entry/90)
	a = math.ceil(entry/90*7)
	print('Brasil', b, 'x Alemanha', a)
	entry = int(input())