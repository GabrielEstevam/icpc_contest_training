entry = input().split(' ')
saldo = int(entry[1])
minimo = saldo
for i in range(int(entry[0])):
	entry = int(input())
	saldo += entry
	if saldo < minimo:
		minimo = saldo
print(minimo)