entradas = int(input())
classificados = int(input())

pontos = []
for i in range(entradas):
    pontos.append(int(input()))

pontos.sort(reverse=True)
if classificados > 0:
    i = classificados-1
    corte = pontos[i]

    while i+1 < entradas:
        if pontos[i+1] == corte:
            i += 1
        else:
            break
    print(i+1)
else:
    print(0)