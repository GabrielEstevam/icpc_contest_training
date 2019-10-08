entry = input().split(' ')
N = int(entry[0])
M = int(entry[1])
l = []
c = []
for i in range(N):
	l.append(0)
for i in range(M):
	c.append(0)
for i in range(N):
	entry = input().split(' ')
	for j in range(M):
		r = int(entry[j])
		l[i] += r
		c[j] += r
cmax = max(c)
lmax = max(l)
print(max([cmax, lmax]))