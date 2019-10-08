for N in range(int(input())):
    n = int(input())
    lista = []
    for i in range(n):
        lista.append(input())
    flag = True
    for i in range(len(lista)):
        if lista[i] != lista[0]:
            flag = False
            break
    if flag:
        print(lista[0])
    else:
        print("ingles")