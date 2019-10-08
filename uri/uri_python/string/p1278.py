N = int(input())
flag = False
while N != 0:
    if flag:
        print("")
    else:
        flag = True
    v = []
    k = []
    maior = 0
    for i in range(N):
        v.append(input().split(' '))
        k.append([0, 0])
        for j in range(len(v[i])):
            if len(v[i][j]) > 0:
                k[i][0] += 1
                k[i][1] += len(v[i][j])
        maior = max([maior, k[i][0] + k[i][1]])
    for i in range(N):
        out = ""
        for j in range(0,maior - (k[i][1]+k[i][0]-1)-1):
            out += " "
        outW = ""
        for j in range(len(v[i])):
            if len(v[i][j]) > 0:
                if len(outW) > 0:
                    outW += " "
                outW += v[i][j]
        print(out+outW)
    N = int(input())