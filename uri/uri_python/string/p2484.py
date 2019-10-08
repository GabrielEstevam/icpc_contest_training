while True:
    try:
        entry = input()
        tam = len(entry)
        for i in range(tam):
            saida = ""
            for j in range(i):
                saida += " "
            for j in range(tam - i):
                if j > 0:
                    saida += " "
                saida += entry[j]
            print(saida)
        print("")
    except EOFError:
        break