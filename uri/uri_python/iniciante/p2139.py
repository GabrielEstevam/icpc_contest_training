while True:
    try:
        entry = input().split()
        mes = int(entry[0])
        dia = int(entry[1])
        Natal = dia
        for i in range(1, mes):
            if i == 1 or i == 3 or i == 5 or i == 7 \
                    or i == 8 or i == 10 or i == 12:
                Natal += 31
            elif i == 2:
                Natal += 29
            else:
                Natal += 30
        if Natal == 359:
            print("E vespera de natal!")
        elif Natal == 360:
            print("E natal!")
        elif Natal > 360:
            print("Ja passou!")
        else:
            print("Faltam", str(360-Natal), "dias para o natal!")
    except EOFError:
        break