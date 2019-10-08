entry = []
for i in range(4):
	entry.append(input())
num = []
for i in range(len(entry[0])):
	n = 0
	for j in range(4):
		n = n*10 + int(entry[j][i])
	num.append(n)
F = num[0]
L = num[len(num)-1]
out = ""
for i in range(1, len(num)-1):
	out += chr((F*num[i] + L) % 257)
print(out)