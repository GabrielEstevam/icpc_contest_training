entrada = input().split()
B = int(entrada[0])
N = int(entrada[1])
while B:
    Bs = []
    entrada = input().split()
    for i in range(B):
        Bs.append(int(entrada[i]))
    for i in range(N):
        entrada = input().split()
        X = int(entrada[0])
        Y = int(entrada[1])
        Z = int(entrada[2])
        Bs[X-1] -= Z
        Bs[Y-1] += Z
    flag = True
    for i in range(B):
        if Bs[i] < 0:
            flag = False
    if flag:
        print("S")
    else:
        print("N")
    entrada = input().split()
    B = int(entrada[0])
    N = int(entrada[1])