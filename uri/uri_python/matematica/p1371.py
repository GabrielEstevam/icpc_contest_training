p = [0]
i = 1
for i in range(1, 5002):
	p.append(i*i)

entry = int(input())
while entry != 0:
	out = "1"
	i = 2
	while p[i] <= entry:
		out += " " + str(p[i])
		i += 1
	print(out)
	entry = int(input())