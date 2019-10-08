entry = input().split(" ")
a = int(entry[0])
b = int(entry[1])
c = int(entry[2])
d = int(entry[3])
e = int(entry[4])
if a < b and b < c and c < d and d < e:
	print('C')
elif a > b and b > c and c > d and d > e:
	print('D')
else:
	print('N') 