n = int(input())
for i in range(n):
    saida = ""
    for j in range(1, 5):
        if j % 4 == 0:
            saida += "PUM"
        else:
            saida += str(j+4*i)+" "
    print(saida)