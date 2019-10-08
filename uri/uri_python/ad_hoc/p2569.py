entry = input().split(" ")
opr = entry[1]
a = ''
b = ''

for i in entry[0]:
	if i == '7':
		a += '0'
	else:
		a += i

for i in entry[2]:
	if i == '7':
		b += '0'
	else:
		b += i

if opr == '+':
	result = int(a) + int(b)
else:
	result = int(a) * int(b)

result = str(result)
saida = ''
for i in result:
	if i == '7':
		saida += '0'
	else:
		saida += i

print(int(saida))
 
