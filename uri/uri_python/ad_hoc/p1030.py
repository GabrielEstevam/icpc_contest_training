instancias = int(input())
for i in range(instancias):
    entrada = input().split(" ")
    NC = int(entrada[0])
    K = int(entrada[1])
    lista = []
    for j in range(NC):
        lista.append(j+1)
    h = 0
    while len(lista) > 1:
        h += K-1
        h = h % len(lista)
        del lista[h]
    res = "Case "+str(i+1)+":"
    print(res, lista[0])