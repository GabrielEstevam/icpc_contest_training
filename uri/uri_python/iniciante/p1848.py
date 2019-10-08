flag = 0
cont = 0
while flag < 3:
    entry = input()
    if entry[0] == 'c':
        print(cont)
        cont = 0
        flag += 1
    else:
        if entry[0] == '*':
            cont += 4
        if entry[1] == '*':
            cont += 2
        if entry[2] == '*':
            cont += 1
