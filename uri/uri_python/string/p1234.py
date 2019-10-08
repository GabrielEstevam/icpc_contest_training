while True:
    try:
        entry = input()
        flag = True
        saida = ""
        for i in entry:
            if i.isalpha():
                if flag:
                    saida += i.upper()
                    flag = False
                else:
                    saida += i.lower()
                    flag = True
            else:
                saida += i
        print(saida)
    except EOFError:
        break