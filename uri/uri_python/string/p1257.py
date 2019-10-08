for N in range(int(input())):
    lista = []
    for n in range(int(input())):
        lista.append(input())
    soma = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            soma += ord(lista[i][j]) - 65 + i + j
    print(soma)