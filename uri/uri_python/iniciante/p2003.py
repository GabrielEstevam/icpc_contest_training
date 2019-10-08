while True:
    try:
        entry = input().split(":")
        tempo = (8-int(entry[0]))*60
        tempo -= int(entry[1])
        tempo -= 60
        if tempo <= 0:
            print("Atraso maximo:", tempo*-1)
        else:
            print("Atraso maximo: 0")
    except EOFError:
        break