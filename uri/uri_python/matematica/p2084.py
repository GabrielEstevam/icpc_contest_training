N = int(input())
entry = input().split(' ')
for i in range(N):
	entry[i] = int(entry[i])
maior = entry.index(max(entry))
soma = sum(entry)
for i in range(N):
	entry[i] /= soma
if entry[maior] >= 0.45:
	print(1)
else:
	flag = False
	if entry[maior] >= 0.4:
		flag = True
		for i in range(N):
			if i != maior and entry[maior] - 0.1 < entry[i]:
				flag = False
	if flag:
		print(1)
	else:
		print(2)
