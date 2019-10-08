entry = input().split(' ')
P = int(entry[0])
N = int(entry[1])
C = int(entry[2])
while P != 0 and N != 0 and C != 0:
    aux = []
    cont = 0
    for i in range(P):
        aux.append(0)
    for i in range(N):
        entry = input().split(' ')
        for j in range(P):
            if entry[j] == '1':
                aux[j] += 1
            else:
                if aux[j] >= C:
                    cont += 1
                aux[j] = 0
    for i in range(P):
        if aux[i] >= C:
            cont += 1
    print(cont)

    entry = input().split(' ')
    P = int(entry[0])
    N = int(entry[1])
    C = int(entry[2])