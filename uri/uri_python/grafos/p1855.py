x = int(input())
y = int(input())
entry = []
mapa = []
for i in range(y):
    entry.append(input())
    mapa.append([])
    for j in range(x):
        mapa[i].append('.')
i = 0
j = 0
direcao = 'C'
while True:
    if mapa[j][i] == '!':
        print('!')
        break
    if entry[j][i] == '>':
        direcao = 'L'
        mapa[j][i] = '!'
    elif entry[j][i] == '<':
        direcao = 'O'
        mapa[j][i] = '!'
    elif entry[j][i] == '^':
        direcao = 'S'
        mapa[j][i] = '!'
    elif entry[j][i] == 'v':
        direcao = 'N'
        mapa[j][i] = '!'
    elif entry[j][i] == '*':
        print('*')
        break
    if direcao == 'L' and  i + 1 < x:
        i += 1
    elif direcao == 'O' and i - 1 >= 0:
        i -= 1
    elif direcao == 'N' and j + 1 < y:
        j += 1
    elif direcao == 'S' and j - 1 >= 0:
        j -= 1