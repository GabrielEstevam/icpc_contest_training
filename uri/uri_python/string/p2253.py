while True:
    try:
        entry = input()
        maisculo = False
        minusculo = False
        digito = False
        flag = True
        for i in entry:
            if i.islower():
                minusculo = True
            if i.isupper():
                maisculo = True
            if i.isdigit():
                digito = True
            elif ord(i) < 65 or 90 < ord(i) < 97 or ord(i) > 122:
                flag = False
        if maisculo and minusculo and digito and flag and 6 <= len(entry) <= 32:
            print("Senha valida.")
        else:
            print("Senha invalida.")
    except EOFError:
        break