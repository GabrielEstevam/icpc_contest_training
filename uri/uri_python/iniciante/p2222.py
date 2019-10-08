instacias = int(input())
nConjuntos = int(input())
conjuntos = []
for i in range (nConjuntos):
    entrada = input().split(" ")
    elementos = [int(entrada[0])]
    for j in range (1, elementos[0]+1):
        elementos.append(int(entrada[j]))
    conjuntos.append(elementos)

for i in range(nConjuntos):
    print(conjuntos[i])

nOperacoes = int(input())
for i in range(nOperacoes):
    entrada = input().split(" ")
    operacao = int(entrada[0])
    X = int(entrada[1])
    Y = int(entrada[2])
    if operacao:
        Z = conjuntos[X] + conjuntos[Y]
        Z.sort()
        j = 0
        while j < (len(Z)-1):
            if Z[j] == Z[j+1]:
                del Z[j]
            j += 1
        print("z: ", Z)