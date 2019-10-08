lista = []
while True:
    try:
        entry = input()
        lista.append(entry)
    except EOFError:
        break
original = []
for i in range(len(lista)):
    original.append(lista[i])
    lista[i] = lista[i].lower()
lista.sort()
nome = lista[len(lista) - 1]
for i in original:
    if nome == i.lower():
        print(i)