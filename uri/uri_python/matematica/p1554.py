import math
for c in range(int(input())):
    N = int(input())
    bolao = input().split(" ")
    bolao[0] = int(bolao[0])
    bolao[1] = int(bolao[1])
    bola = []
    for i in range(N):
        bola.append(input().split(" "))
    iDistancia = 0
    distancia = math.sqrt(pow(int(bola[0][0]) - bolao[0], 2) + pow(int(bola[0][1]) - bolao[1], 2))
    for i in range(1, N, 1):
        d = math.sqrt(pow(int(bola[i][0]) - bolao[0], 2) + pow(int(bola[i][1]) - bolao[1], 2))
        if d < distancia:
            distancia = d
            iDistancia = i
    print(iDistancia + 1)