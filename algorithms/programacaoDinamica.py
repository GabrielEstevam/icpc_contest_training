''' (PARA) Cortando Canos - Programacao Dinamica '''
entrada = input().split(" ")
N = int(entrada[0])
T = int(entrada[1])
tam = []
values = []
for i in range(N):
    entrada = input().split(" ")
    tam.append(int(entrada[0]))
    values.append(int(entrada[1]))

lucro = []

for i in range(T+1):
    lucro.append(0)

for i in range(1, T+1):
	for j in range(N):
		if tam[j] <= i:
			if values[j] + lucro[i-tam[j]] > lucro[i]:
				lucro[i] = values[j] + lucro[i-tam[j]]

print(lucro[T])
