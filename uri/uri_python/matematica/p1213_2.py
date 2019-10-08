N = 10000
lista = []
fila = []
for i in range(N):
	lista.append(0)
	if i % 2 != 0 and i % 5 != 0:
		fila.append(i)
mult = "1"
cont = 0
while len(fila) > 0:
	i = 0
	while i < len(fila):
		if int(mult) % fila[i] == 0:
			lista[fila[i]] = len(mult)
			fila.remove(fila[i])
		else:
			i+=1
	mult += "1"
	print(len(fila))

#print(lista)
print("oi")
while True:
    try:
        print(lista[int(input())])

    except EOFError:
        break
