N = int(input())
#entry = input().split(" ")
entry = []
for i in range(999999):
    entry.append('999999')
entry.append('1000000')
for i in range(len(entry)):
    entry[i] = int(entry[i])
soma = sum(entry)
soma_aux = 0
roubadas = 0
for i in range(N):
    if entry[i] == 1:
        soma_aux += 1
    if entry[i] % 2 == 0:
        soma += soma_aux
        roubadas = i
        break
atacadas = i + 1
roubadas += atacadas
print(atacadas, soma - roubadas)