instancias = int(input())

for i in range(instancias):
    partida1 = input().split(" ")
    M = int(partida1[0])
    V = int(partida1[2])

    if M > V:
        pontosTime1 = 3
        pontosTime2 = 0
    elif V > M:
        pontosTime1 = 0
        pontosTime2 = 3
    else:
        pontosTime1 = 1
        pontosTime2 = 1

    saldo1Time1 = M
    saldo1Time2 = V

    partida2 = input().split(" ")
    M = int(partida2[0])
    V = int(partida2[2])

    if M > V:
        pontosTime2 += 3
    elif V > M:
        pontosTime1 += 3
    else:
        pontosTime1 += 1
        pontosTime2 += 1

    saldo2Time1 = V
    saldo2Time2 = M

    if pontosTime1 > pontosTime2:
        print("Time 1")
    elif pontosTime2 > pontosTime1:
        print("Time 2")
    elif saldo1Time1+saldo2Time1 > saldo1Time2+saldo2Time2:
        print("Time 1")
    elif saldo1Time1+saldo2Time1 < saldo1Time2+saldo2Time2:
        print("Time 2")
    elif saldo2Time1 > saldo1Time2:
        print("Time 1")
    elif saldo1Time2 > saldo2Time1:
        print("Time 2")
    else:
        print("Penaltis")