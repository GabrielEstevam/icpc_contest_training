n = input()
n = int(n)
'''
import math
for a in range(n):
    presentes = []
    peso = []
    for i in range(int(input())):
        presentes.append(input())
        peso.append(float(input()))
    capacidade = float(input())
    entry = input()
    n = int(input())
    carga = 0
    naoListados = []
    while entry != '-':
        flag = True
        for j in range(len(presentes)):
            if entry == presentes[j]:
                carga += n*peso[j]
                flag = False
        if flag:
            naoListados.append(entry)
        entry = input()
        n = int(input())
    for i in range(len(naoListados)):
        print("NAO LISTADO:", naoListados[i])
    print("Peso total:","{0:.2f}".format(carga),"kg")
    print("Numero de trenos:",math.ceil(carga/capacidade))
    print("")
'''