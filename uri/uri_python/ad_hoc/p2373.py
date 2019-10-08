cont = 0
for n in range(int(input())):
	entry = input().split();
	l = int(entry[0])
	c = int(entry[1])
	if l > c:
		cont += c
print(cont)