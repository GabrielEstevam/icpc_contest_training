import time
entrada = input()
lista = []
for i in range(len(entrada)):
    lista.append(ord(entrada[i])-96)

#print(len(lista))
timeInitial = time.time()
soma1 = [lista[0]]
soma2 = [lista[0]]
for i in range(1, len(lista)):
    tam = len(soma2)
    soma3 = []
    for j in range(tam):
        soma3.append(soma2[j]+lista[i])
    soma3.append(lista[i])
    soma1 = list(set(soma1 + soma2))
    soma2 = list(set(soma3))
soma1 = list(set(soma1 + soma2))
soma = list(set(soma1))
print(len(soma))
timeFinal = time.time()
#print("tempo: ", timeFinal-timeInitial)
'''
lista = [1, 1, 2]
lista = list(set(lista))
print(lista)
print(lista[0]*lista[1])
'''