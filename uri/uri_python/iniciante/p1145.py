entry = input().split(" ")
x = int(entry[0])
y = int(entry[1])
i = 0
while (i*x) < y:
    j = 1
    saida = str(i*x+j)
    while j < x and i*x+j < y:
        j += 1
        saida += " "+str(i*x+j)
    print(saida)
    i += 1