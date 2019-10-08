r = []
for i in range(181):
	r.append(0)

for i in range(31):
	r[i*6] = 1

while True:
	try:
		i = int(input())
		if r[i]:
			print('Y')
		else:
			print('N')
	except EOFError:
		break