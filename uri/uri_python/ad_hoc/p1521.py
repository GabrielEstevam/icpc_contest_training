N = int(input())
while N > 0:
    entry = input().split(' ')
    lista = []
    for i in range(N):
        lista.append(int(entry[i]) - 1)
    k = int(input()) - 1
    while True:
        if lista[k] == k:
            break
        else:
            k = lista[k]
    print(k+1)

    N = int(input())