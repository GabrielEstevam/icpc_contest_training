v = []
N = 10001
for i in range(N):
	v.append(False)
i = 0
j = 0
pi = 0
pj = 0
while True:
	v[pi+pj] = True
	i += 1
	pi = i*i
	if (pi+pj) >= N:
		j += 1
		pj = j*j
		i = j
		pi = i*i
		if (pi+pj) >= N:
			break

#print(v)

while True:
	try:
		entry = int(input())
		if entry < 0:
			print("NO")
		else:
			if v[entry]:
				print("YES")
			else:
				print("NO")
	except EOFError:
		break
