for n in range(int(input())):
    entry = input()
    k = 1
    cont = 0
    for i in range(len(entry)-1, -1, -1):
        if entry[i].isdigit():
            cont += k*int(entry[i])
            k *= 10
        else:
            k = 1
    print(cont)