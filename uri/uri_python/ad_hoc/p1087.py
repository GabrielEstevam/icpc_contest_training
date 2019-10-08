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
    x1 = entrada[0]
    y1 = entrada[1]
    x2 = entrada[2]
    y2 = entrada[3]
    if x1 == x2 and y1 == y2:
        print(0)
    elif x1 == x2 or y1 == y2 or (x1-y1)==(x2-y2) or (x1+y1)==(x2+y2):
        print(1)
    else:
        print(2)
    entrada = leitura()
