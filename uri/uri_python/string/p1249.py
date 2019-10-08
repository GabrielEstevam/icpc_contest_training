while True:
    try:
        entry = input()
        saida = ""
        for i in entry:
            if i.isalpha():
                num = ord(i)
                num += 13
                if i.islower():
                    if num > 122:
                        num -= 26
                else:
                    if num > 90:
                        num -= 26
                saida += chr(num)
            else:
                saida += i

        print(saida)
    except EOFError:
        break