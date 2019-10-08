import time
import math
entrada = input().split(" ")
N = int(entrada[0])
T = int(entrada[1])
tam = []
values = []
for i in range(N):
    entrada = input().split(" ")
    tam.append(int(entrada[0]))
    values.append(int(entrada[1]))

tempo = time.time()
corte = []
lucro = []
for i in range(T+1):
    corte.append(i)
    lucro.append(0)
for i in range(N):
    lucro[tam[i]] = values[i]

for i in range(1, T+1):
    for j in range(1, math.ceil(i/2)):
        if lucro[j] + lucro[i-j] > lucro[i]:
            lucro[i] = lucro[j] + lucro[i-j]

#for i in range(1, T+1):
#    print("i: ", corte[i], lucro[i])

print(max(lucro))
print("t: ", time.time() - tempo)