for n in range(int(input())):
    entry = input().split(' ')
    for i in range(len(entry)):
        if len(entry[i]) == 10:
            aux = 'J'
            for j in range(1, 9):
                aux += entry[i][j]
            aux += 'i'
            if aux == "Joulupukki":
                entry[i] = aux
        if len(entry[i]) == 11:
            if entry[i][10] == '.':
                aux = 'J'
                for j in range(1, 9):
                    aux += entry[i][j]
                aux += 'i'
                aux += '.'
                if aux == "Joulupukki.":
                    entry[i] = aux
    out = ""
    for i in entry:
        if len(out) > 0:
            out += ' '
        out += i
    print(out)
