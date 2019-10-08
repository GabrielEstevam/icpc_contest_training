for i in range(int(input())):
    notas = []
    n = int(input())
    entry = input().split(" ")
    for j in range(n):
        notas.append(int(entry[j]))
    maior = max(notas)
    sequencia = 1
    sequenciaMaior = 1
    for j in range(1, len(notas)):  
        if notas[j] == maior and notas[j-1] == maior:
            sequencia += 1
        else:
            if sequencia > sequenciaMaior:
                sequenciaMaior = sequencia
            sequencia = 1
    if sequencia > sequenciaMaior:
        sequenciaMaior = sequencia
    print("Caso #"+str(i+1)+":", sequenciaMaior)