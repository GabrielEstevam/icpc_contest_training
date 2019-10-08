while True:
    try:
        quantidade = int(input())
        peDireito = []
        peEsquerdo = []
        for i in range(31):
            peDireito.append(0)
            peEsquerdo.append(0)
        for i in range(quantidade):
            entrada = input().split(" ")
            if entrada[1] == 'E':
                peEsquerdo[int(entrada[0]) - 30] += 1
            else:
                peDireito[int(entrada[0]) - 30] += 1
        soma = 0
        for i in range(31):
            if peDireito[i] < peEsquerdo[i]:
                soma += peDireito[i]
            else:
                soma += peEsquerdo[i]
        print(soma)
    except EOFError:
        break