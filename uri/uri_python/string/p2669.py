import time
entrada = input()
lista = []
for i in range(len(entrada)):
    lista.append(ord(entrada[i])-96)

#print(len(lista))
timeInitial = time.time()
soma = [lista[0]]
for i in range(1, len(lista)):
    soma.append(soma[i-1]+lista[i])

soma_aux1 = soma
for i in range(len(lista)-1):
    soma_aux2 = []
    for j in range(len(soma_aux1)):
        soma_aux2.append(soma_aux1[j]-lista[i])
    del soma_aux2[0]
    soma_aux1 = soma_aux2
    soma = list(set(soma + soma_aux1))

print(len(soma))
timeFinal = time.time()
#print("tempo: ", timeFinal-timeInitial)
'''
lista = [1, 1, 2]
lista = list(set(lista))
print(lista)
print(lista[0]*lista[1])
'''