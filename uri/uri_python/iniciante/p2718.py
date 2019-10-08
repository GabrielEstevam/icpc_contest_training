for i in range(int(input())):
    X = int(input())
    binary = str("{0:b}".format(X))
    maior = 0
    sequencia = 0
    for j in binary:
        if int(j) == 1:
            sequencia += 1
        else:
            if sequencia > maior:
                maior = sequencia
            sequencia = 0
    if sequencia > maior:
        maior = sequencia
    print(maior)