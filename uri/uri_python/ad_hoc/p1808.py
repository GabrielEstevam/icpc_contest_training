entry = input()
soma = 0
cont = 0
i = len(entry) - 1
while i >= 0:
	if entry[i] == '0':
		soma += 10
		cont += 1
		i -= 1
	else:
		soma += int(entry[i])
		cont += 1
	i -= 1
print('{:.2f}'.format(round(soma/cont, 2)))