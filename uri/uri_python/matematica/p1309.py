while True:
    try:
        A = input()
        B = input()
        saida = ""
        for i in range(len(B)):
            saida += B[len(B)-i-1]
        while len(saida) < 2:
            saida += "0"
        saida += "."
        for i in range(len(A)):
            if i%3 == 0 and i > 0:
                saida += ","
            saida += A[len(A)-i-1]
        resposta = "$"
        for i in range(len(saida)):
            resposta += saida[len(saida)-1-i]

        print(resposta)

    except EOFError:
        break