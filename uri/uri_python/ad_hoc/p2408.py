entry = input().split(' ')
a = int(entry[0])
b = int(entry[1])
c = int(entry[2])
if (a > b and a < c) or (a < b and a > c):
	print(a)
elif (b > a and b < c) or (b < a and b > c):
	print(b)
elif (c > a and c < b) or (c < a and c > b):
	print(c)