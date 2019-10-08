while True:
    try:
        entry = input().split(' ')
        N = int(entry[0])
        G = int(entry[1])
        
        vitorias = 0
        empates = 0
        derrotas = []
        for i in range(N):
            entry = input().split(' ')
            if int(entry[0]) > int(entry[1]):
                vitorias += 1
            elif int(entry[0]) == int(entry[1]):
                empates += 1
            else:
                derrotas.append(int(entry[1]) - int(entry[0]))

        derrotas.sort()
        pontos = vitorias*3
        if G > empates:
            pontos += empates*3
            G -= empates
            while len(derrotas) > 0 and G > 0:
                if derrotas[0] + 1 <= G:
                    pontos += 3
                    G -= derrotas[0] + 1
                    derrotas.remove(derrotas[0])
                else:
                    if derrotas[0] == G:
                        pontos += 1
                    break
        else:
            pontos += G*3 + (empates - G)
        print(pontos)
    except EOFError:
        break