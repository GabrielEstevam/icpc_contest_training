instancias = int(input())
lista = []
for i in range(instancias):
    lista.append(int(input()))
lista.sort()
numero = [lista[0]]
qtd = [1]
k = 0
for i in range(1, instancias):
    if lista[i] != numero[k]:
        numero.append(lista[i])
        qtd.append(1)
        k += 1
    else:
        qtd[k] += 1
for i in range(len(numero)):
    print(numero[i], "aparece", qtd[i], "vez(es)")