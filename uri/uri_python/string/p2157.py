for c in range(int(input())):
    entry = input().split()
    saida = ""
    for i in range(int(entry[0]), int(entry[1]) + 1, 1):
        saida += str(i)
    tam = len(saida)
    for i in range(tam):
        saida += saida[tam - 1 - i]
    print(saida)