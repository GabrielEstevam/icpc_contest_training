while True:
    try:
        N = int(input())
        for i in range(N):
            saida = ""
            for j in range(N):
                if i+j == N-1:
                    saida += "2"
                elif i == j:
                    saida += "1"
                else:
                    saida += "3"
            print(saida)
    except EOFError:
        break