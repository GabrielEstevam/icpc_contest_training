import math
while True:
    try:
        N = int(input())
        if N % 2 != 0:
            for i in range(math.ceil(N/2)):
                saida = ""
                for j in range(math.floor(N/2)-i):
                    saida += " "
                for j in range(2*i+1):
                    saida += "*"
                print(saida)
            saida = ""
            for i in range(math.floor(N/2)):
                saida += " "
            saida += "*"
            print(saida)
            saida = ""
            for i in range(math.floor(N/2-1)):
                saida += " "
            saida += "***"
            print(saida)
            print("")

    except EOFError:
        break