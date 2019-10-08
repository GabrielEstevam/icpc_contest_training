N = int(input())
flag = True
while N > 0:
    if flag:
        flag = False
    else:
        print("")
    lista = []
    maior = 0
    for i in range(N):
        lista.append(input())
        if len(lista[i]) > len(lista[maior]):
            maior = i
    for i in range(N):
        while len(lista[i]) < len(lista[maior]):
            lista[i] = " "+lista[i]
        print(lista[i])
    N = int(input())