N = int(input())
notas = []
afinacao = [0, 2, 4, 5, 7, 9, 11]
notasString = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]
for i in range(N):
    notas.append(int(input())%12)
flagDesafinacao = True
for nota in range(12):
    aux = []
    flagNota = True
    for i in range(N):
        aux.append(notas[i]-nota-1)
        if aux[i] < 0:
            aux[i] += 12
    for i in range(N):
        flag = False
        for j in range(7):
            if aux[i] == afinacao[j]:
                flag = True
                break
        if flag == 0:
            flagNota = False
            break
    if flagNota:
        print(notasString[nota])
        flagDesafinacao = False
        break
if flagDesafinacao:
    print("desafinado")