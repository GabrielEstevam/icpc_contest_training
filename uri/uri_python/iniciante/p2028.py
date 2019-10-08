k = 0
while True:
    try:
        k += 1
        N = int(input())
        saida = "0"
        cont = 1
        for i in range(N):
            for j in range(i+1):
                saida += " "+str(i+1)
                cont += 1
        if cont > 1:
            print("Caso", str(k)+str(':'), cont, 'numeros')
        else:
            print("Caso", str(k) + str(':'), cont, 'numero')
        print(saida)
        print("")
    except EOFError:
        break