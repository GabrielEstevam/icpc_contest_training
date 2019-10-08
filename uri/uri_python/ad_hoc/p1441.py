N = int(input())
while N != 0:
    lista = [N]
    while N > 1:
        if N % 2 == 0:
            N /= 2
        else:
            N = N*3 + 1
        lista.append(N)
    print(int(max(lista)))
    N = int(input())