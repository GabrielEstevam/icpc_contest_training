while True:
    try:
        entry = input()
        n = int(input())
        cont = 0
        ciclos = 0
        for i in entry:
            if i == 'W':
                ciclos += 1
                if cont > 0:
                    ciclos += 1
                cont = 0
            else:
                cont += 1
                if cont == n:
                    cont = 0
                    ciclos += 1
        if cont > 0:
            ciclos += 1
        print(ciclos)
    except EOFError:
        break