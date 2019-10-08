entry = input().split(' ')
G = int(entry[0])
P = int(entry[1])
while G != 0 or P != 0:
    gp = []
    for i in range(G):
        entry = input().split(' ')
        gps = []
        for j in range(P):
            gps.append(0)
        for j in range(P):
            gps[int(entry[j]) - 1] = j
        gp.append(gps)
    S = int(input())
    for i in range(S):
        pontos = []
        for j in range(P):
            pontos.append(0)
        entry = input().split(' ')
        for k in range(G):
            for j in range(int(entry[0])):
                pontos[gp[k][j]] += int(entry[j+1])
        imax = 0
        for j in range(P):
            if pontos[j] > pontos[imax]:
                imax = j
        out = ''
        for j in range(P):
            if pontos[j] == pontos[imax]:
                if len(out) > 0:
                    out += ' ' + str(j+1)
                else:
                    out = str(j+1)
        print(out)

    entry = input().split(' ')
    G = int(entry[0])
    P = int(entry[1])