positivos = 0
soma = 0
for i in range(6):
    entrada = float(input())
    if entrada > 0:
        positivos += 1
        soma += entrada
print(str(positivos)+" valores positivos")
media = soma/positivos
print(round(media, 1))