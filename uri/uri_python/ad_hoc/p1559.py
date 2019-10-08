for n in range(int(input())):
    v = []
    for i in range(4):
        v.append(input().split(' '))
    #DOWN
    flagD = False
    for i in range(4):
        for j in range(3):
            if (v[j][i] == v[j+1][i] and v[j][i] != '0') or (v[j][i] != '0' and v[j+1][i] == '0'):
                flagD = True
                break
    #LEFT
    flagL = False
    for i in range(4):
        for j in range(3):
            if (v[i][j] == v[i][j+1] and v[i][j] != '0') or (v[i][j] == '0' and v[i][j+1] != '0'):
                flagL = True
                break
    #RIGHT
    flagR = False
    for i in range(4):
        for j in range(3):
            if (v[i][j] == v[i][j+1] and v[i][j] != '0') or (v[i][j] != '0' and v[i][j+1] == '0'):
                flagR = True
                break
    #UP
    flagU = False
    for i in range(4):
        for j in range(3):
            if (v[j][i] == v[j+1][i] and v[j][i] != '0') or (v[j][i] == '0' and v[j+1][i] != '0'):
                flagU = True
                break
    out = ""
    if flagD:
        out = "DOWN"
    if flagL:
        if len(out) == 0:
            out = "LEFT"
        else:
            out += " LEFT"
    if flagR:
        if len(out) == 0:
            out = "RIGHT"
        else:
            out += " RIGHT"
    if flagU:
        if len(out) == 0:
            out = "UP"
        else:
            out += " UP"
    if len(out) == 0:
        out = "NONE"
    flag = True
    for i in range(4):
        for j in range(4):
            if v[i][j] == '2048':
                flag = False
                break
    if flag:
        print(out)
    else:
        print("NONE")  