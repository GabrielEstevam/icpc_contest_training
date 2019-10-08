while True:
    try:
        entry = input().split(" ")
        N = int(entry[0])
        R = int(entry[1])
        entry = input().split(" ")
        if R == N:
            print("*")
        else:
            lista = []
            for i in range(N):
                lista.append(1)
            for i in range(R):
                lista[int(entry[i])-1] = 0
            saida = ""
            for i in range(N):
                if lista[i] == 1:
                    saida += str(i+1)+ " "
            print(saida)
    except EOFError:
        break