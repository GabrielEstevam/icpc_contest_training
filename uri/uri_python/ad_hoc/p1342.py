entry = input().split(' ')
P = int(entry[0])
S = int(entry[1])
while P > 0 and S > 0:
	entry = input().split(' ')
	arm = [int(entry[0]), int(entry[1]), int(entry[2])]
	p = []
	f = []
	for i in range(P):
		p.append(0)
		f.append(1)
	k = 0
	for i in range(int(input())):
		entry = input().split(' ')
		dados = int(entry[0]) + int(entry[1])
		while f[k] == 0:
			f[k] = 1
			k += 1
			if k == P:
				k = 0
		p[k] += dados
		if p[k] == arm[0] or p[k] == arm[1] or p[k] == arm[2]:
			f[k] = 0
		if p[k] > S:
			print(k+1)
			break
		k += 1
		if k == P:
			k = 0

	entry = input().split(' ')
	P = int(entry[0])
	S = int(entry[1])
