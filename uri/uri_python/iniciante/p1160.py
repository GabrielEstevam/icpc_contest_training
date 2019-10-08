instancias = int(input())
for i in range(instancias):
    entrada = input().split()
    PA = int(entrada[0])
    PB = int(entrada[1])
    GA = float(entrada[2])
    GB = float(entrada[3])

    tempo = 0
    while PA <= PB:
        PA += int(PA*(GA/100))
        PB += int(PB*(GB/100))
        tempo += 1
        if tempo > 100:
            break

    if tempo > 100:
        print("Mais de 1 seculo.")
    else:
        print("%d anos." % tempo)
