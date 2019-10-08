instancias = int(input())
for i in range(instancias):
    N = int(input())
    k = N-1
    j = 2
    while j*j <= N:
        k -= 1
        j += 1
    print(k)