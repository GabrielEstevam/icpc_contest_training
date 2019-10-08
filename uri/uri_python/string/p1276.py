while True:
    try:
        entry = input()
        v = []
        for i in range(26):
            v.append(0)
        for i in entry:
            if ord(i) >= 97 and ord(i) <= 122:
                v[ord(i)-97] = 1
        pivo = -1
        out = ""
        for i in range(0, 26):
            if v[i] == 1:
                if pivo == -1:
                    pivo = i
            elif v[i] == 0 and pivo != -1:
                if len(out) == 0:
                    out = chr(pivo+97)+':'+chr(i-1+97)
                else:
                    out += ", " + chr(pivo+97)+':'+chr(i-1+97)
                pivo = -1
        if v[25] == 1:
            if len(out) == 0:
                out = chr(pivo+97)+':'+chr(i+97)
            else:
                out += ", " + chr(pivo+97)+':'+chr(i+97)
        print(out)
        
    except EOFError:
        break