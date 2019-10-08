N = int(input())
while N != 0:
    saida = "1"
    for i in range(2, N+1):
        saida += " "+str(i)
    print(saida)
    N = int(input())