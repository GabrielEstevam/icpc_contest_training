instancias = int(input())
lista = [2]
for i in range(instancias):
    N = int(input())
    while N > len(lista):
       lista.append(lista[len(lista)-1]+len(lista)+1)
    print(lista[N-1])