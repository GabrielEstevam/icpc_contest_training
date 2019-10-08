# Functions
def leitura ():
    linha = input().split(" ")
    entrada = [0, 0, 0, 0]
    for i in range(4):
        entrada[i] = int(linha[i])
    return  entrada

# Main
entrada = leitura()
while entrada[0]+entrada[1]+entrada[2]+entrada[3] != 0:
    h1 = entrada[0]
    m1 = entrada[1]
    h2 = entrada[2]
    m2 = entrada[3]
    calc = (h2-h1)*60-m1+m2
    if calc <= 0:
        print(calc+1440)
    else:
        print(calc)
    entrada = leitura()
