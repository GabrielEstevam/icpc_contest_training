e = input()
maior = ""
while e != '0':
	entry = e.split(" ")
	saida = str(len(entry[0]))
	if len(entry[0]) >= len(maior):
		maior = entry[0]
	for i in range(1, len(entry)):
		saida += "-" + str(len(entry[i]))
		if len(entry[i]) >= len(maior):
			maior = entry[i]
	print(saida)
	e = input()
print("")
print("The biggest word:", maior)
