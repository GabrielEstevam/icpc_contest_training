instancias = int(input())
for i in range(instancias):
    entrada = input().split(" ")
    n = int(entrada[0])
    notas = []
    for j in range(1, n+1):
        notas.append(int(entrada[j]))
    media = round(sum(notas)/n, 3)
    k = 0
    for j in range(n):
        if notas[j] > media:
            k += 1
    k = k/n
    resultado = "{0:.3f}".format(k*100)+"%"
    print(resultado)