entry = input()
cont = 0
for i in entry:
	if i == '1':
		cont += 1
if cont % 2 == 0:
	entry += '0'
else:
	entry += '1'
print(entry)
