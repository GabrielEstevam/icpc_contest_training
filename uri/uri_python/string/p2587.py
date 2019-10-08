for c in range(int(input())):
    palavras = [input(), input()]
    entry = input()
    i1 = -1
    i2 = -1
    for i in range(len(entry)):
        if entry[i] == '_':
            if i1 != -1:
                i2 = i
            else:
                i1 = i
    if palavras[0][i1] != palavras[0][i2] and palavras[1][i1] != palavras[1][i2]:
        if palavras[0][i1] == palavras[1][i2] or palavras[0][i2] == palavras[1][i1]:
            print('Y')
        else:
            print('N')
    else:
        print('N')