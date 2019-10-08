while True:
    try:
        dic = {}
        entry = input()
        for i in range(len(entry)):
            if entry[i] in dic:
                dic[entry[i]] += 1
            else:
                dic[entry[i]] = 1
        cont = -1
        for i in dic:
            if dic[i] % 2 == 1:
                cont += 1
        if cont == -1:
            cont += 1
        print(cont)
    except EOFError:
        break