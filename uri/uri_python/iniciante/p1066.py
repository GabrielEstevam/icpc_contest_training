pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(5):
    entrada = int(input())
    if entrada % 2 == 0:
        pares += 1
    else:
        impares += 1
    if entrada > 0:
        positivos += 1
    elif entrada < 0:
        negativos += 1
print(str(pares)+" valor(es) par(es)")
print(str(impares)+" valor(es) impar(es)")
print(str(positivos)+" valor(es) positivo(s)")
print(str(negativos)+" valor(es) negativo(s)")