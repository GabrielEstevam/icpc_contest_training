pares = 0
for i in range(5):
    entrada = int(input())
    if entrada % 2 == 0:
        pares += 1
print(str(pares)+" valores pares")