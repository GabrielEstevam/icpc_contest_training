N = int(input())
Matriz = []
for i in range(N):
    entry = input().split(" ")
    for j in range(N):
        entry[j] = int(entry[j])
    Matriz.append(entry)
Lista = []
for i in range(2*N):
    entry = input().split()
    Lista.append(Matriz[int(entry[0])-1][int(entry[1])-1])
Lista.sort()
ListaDistinct = [Lista[0]]
for i in range(1, len(Lista)):
    if Lista[i] != Lista[i-1]:
        ListaDistinct.append(Lista[i])
print(len(ListaDistinct))