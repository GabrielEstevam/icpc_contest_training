positivos = 0
for i in range(6):
    entrada = float(input())
    if entrada > 0:
        positivos += 1
print(str(positivos)+" valores positivos")