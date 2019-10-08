for N in range(int(input())):
    entry = input()
    saida = ""
    for i in range(len(entry)):
        if i < len(entry)/2:
            saida += str(entry[int(len(entry)/2-i-1)])
        else:
            saida += str(entry[int(len(entry)*(3/2)-i-1)])
    print(saida)