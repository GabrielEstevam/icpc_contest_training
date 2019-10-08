entry = input().split(' ')
N = int(entry[0])
while N != 0:
    M = int(entry[1])
    S = int(entry[2])
    v = []
    f = []
    x = 0
    y = 0
    D = ''
    for i in range(N):
        row = input()
        rowF = []
        for j in range(M):
            if row[j] != '.' and row[j] != '*' and row[j] != '#':
                D = row[j]
                x = j
                y = i
            rowF.append(0)
        v.append(row)
        f.append(rowF)
    cont = 0
    entry = input()
    for i in range(S):
        if entry[i] == 'D':
            if D == 'N':
                D = 'L'
            elif D == 'L':
                D = 'S'
            elif D == 'S':
                D = 'O'
            else:
                D = 'N'
        elif entry[i] == 'E':
            if D == 'N':
                D = 'O'
            elif D == 'L':
                D = 'N'
            elif D == 'S':
                D = 'L'
            else:
                D = 'S'
        else:
            if D == 'N':
                if y > 0:
                    if v[y-1][x] != '#':
                        y -= 1
            elif D == 'L':
                if x < M-1:
                    if v[y][x+1] != '#':
                        x += 1
            elif D == 'S':
                if y < N-1:
                    if v[y+1][x] != '#':
                        y += 1
            else:
                if x > 0:
                    if v[y][x-1] != '#':
                        x -= 1
        if v[y][x] == '*' and f[y][x] == 0:
            cont += 1
            f[y][x] = 1
    print(cont)
    entry = input().split(' ')
    N = int(entry[0])