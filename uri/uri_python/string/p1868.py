import math
N = int(input())
while N != 0:
    y = math.floor(N/2)
    x = y
    direcao = ">"
    cont1 = 0
    cont2 = 1
    cont3 = 0
    for k in range(N*N):
        for i in range(N):
            saida = ""
            for j in range(N):
                if i == y and j == x:
                    saida += "X"
                else:
                    saida += "O"
            print(saida)
        if direcao == '>' and x + 1 < N:
            x += 1
        elif direcao == '^' and y > 0:
            y -= 1
        elif direcao == '<' and x > 0:
            x -= 1
        elif direcao == 'v' and y + 1 < N:
            y += 1
        cont1 += 1
        if cont1 == cont2:
            if direcao == '>':
                direcao = '^'
            elif direcao == '^':
                direcao = '<'
            elif direcao == '<':
                direcao = 'v'
            elif direcao == 'v':
                direcao = '>'
            cont1 = 0
            cont3 += 1
            if cont3 == 2:
                cont2 += 1
                cont3 =0
        print('@')
    N = int(input())