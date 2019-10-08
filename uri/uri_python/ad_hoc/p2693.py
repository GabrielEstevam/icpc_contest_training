def ordena(t):
    return  int(t[2]), t[1], t[0]
while True:
    try:
        lista = []
        N = int(input())
        for n in range(N):
            lista.append(input().split(" "))
        lista = sorted(lista, key=ordena)
        for i in lista:
            print(i[0])
    except EOFError:
        break