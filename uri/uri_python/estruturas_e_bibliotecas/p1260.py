N = int(input())
input()
for i in range(N):
	entry = input()
	v = []
	while len(entry) > 0:
		v.append(entry)
		try:
			entry = input()
		except EOFError:
			break

	v.sort()
	p = 100/len(v)
	cont = 1
	for j in range(1, len(v)):
		if v[j] != v[j-1]:
			print(v[j-1], '{:.4f}'.format(p*cont))
			cont = 0
		cont += 1
	print(v[len(v)-1], '{:.4f}'.format(p*cont))
	if i+1 < N:
		print()
