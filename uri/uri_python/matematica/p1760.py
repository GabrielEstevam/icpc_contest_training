import math
Area = 0
parcela = 1
n = 3
m = 9
while parcela > 0.00000000001:
    Area += parcela
    parcela = n / m
    n *= 4
    m *= 9
while True:
    try:
        L = int(input())
        AreaInicial = math.pow(L, 2)*math.sqrt(3)/4
        print("{0:.2f}".format(Area*AreaInicial))
    except EOFError:
        break