horario_anterior = 0
velocidade = 0
distancia = 0
flag = False
while True:
    try:
        entry = input().split(" ")
        if len(entry) > 1:
            v = float(entry[1])
            entry = entry[0].split(":")
            h = int(entry[0]) * 3600 + int(entry[1]) * 60 + int(entry[2])
            if flag:
                distancia += ((h - horario_anterior) * velocidade) / 3600
            else:
                flag = True
            velocidade = v
            horario_anterior = h
        else:
            saida = entry[0]
            entry = entry[0].split(":")
            h = int(entry[0]) * 3600 + int(entry[1]) * 60 + int(entry[2])
            d = distancia + ((h - horario_anterior) * velocidade) / 3600
            print(saida, '{0:.2f}'.format(d), 'km')
    except EOFError:
        break