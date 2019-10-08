k = 0
while True:
    try:
        N1 = input()
        N2 = input()
        k += 1
        cont = 0
        pos1 = 0
        pos2 = 0
        pos_anterior = 0
        aux = ""
        for i in range(len(N1)):
            aux += '-'
        while True:
            pos1 = N2.find(N1)
            pos2 = N2.find(N1[0])
            if pos1 == -1:
                break
            if pos1 == pos2:
                pos_anterior = pos1
                cont += 1
            N2 = N2.replace(N1[0], '-', 1)
        print("Caso #" + str(k) + ":")
        if cont > 0:
            print("Qtd.Subsequencias:", cont)
            print("Pos:", pos_anterior + 1)
        else:
            print("Nao existe subsequencia")
        print("")
    except EOFError:
        break