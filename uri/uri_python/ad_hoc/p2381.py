entry = input().split(' ')
N = int(entry[0])
K = int(entry[1])
lista = []
for i in range(N):
	lista.append(input())
lista.sort()
print(lista[K-1])