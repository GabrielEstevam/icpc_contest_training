entry = input().split(' ')
x = int(entry[0])
y = int(entry[1])
if x < 0 or x > 432 or y < 0 or y > 468:
	print('fora')
else:
	print('dentro')