for i in range(int(input())):
    entry = input().split(" ")
    N = int(entry[0])
    M = int(entry[1])
    entry = input().split(" ")
    viagens = 0
    carga = 0
    for j in entry:
        if carga + int(j) <= M:
            carga += int(j)
        else:
            carga = int(j)
            viagens += 1
    if carga > 0:
        viagens += 1
    print(viagens)