entry = input().split(" ")
a = int(entry[0])
b = int(entry[1])

if b <= 2:
	print('nova')
elif b <= 96:
	if a <= b:
		print('crescente')
	else:
		print('minguante')
else:
	print('cheia')
