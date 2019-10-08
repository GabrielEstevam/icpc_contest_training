import math
while True:
    try:
        n = input()
        entry = input().split(" ")
        for i in range(len(entry)):
            entry[i] = int(entry[i])
        entry.sort()
        soma = 0
        tam = len(entry)
        for i in range(math.floor(tam/2)):
            soma += entry[tam-i-1] - entry[i]
        print(soma)
    except EOFError:
        break