while True:
    try:
        entry = input()
        negrito = False
        italico = False
        out = ""
        for i in entry:
            if i == '*':
                if negrito:
                    out += "</b>"
                    negrito = False
                else:
                    out += "<b>"
                    negrito = True
            elif i == "_":
                if italico:
                    out += "</i>"
                    italico = False
                else:
                    out += "<i>"
                    italico = True
            else:
                out += i
        print(out)
    except EOFError:
        break