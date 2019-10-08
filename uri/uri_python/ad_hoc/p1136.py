entry = input().split(' ')
N = int(entry[0])
B = int(entry[1])
while N != 0 and B != 0:
    flag = []
    for i in range(N+1):
        flag.append(0)
    entry = input().split(' ')
    b = []
    for i in range(B):
        b.append(int(entry[i]))
    for i in range(B):
        for j in range(i, B):
            flag[abs(b[i] - b[j])] = 1

    
    verifica = True
    for i in range(N+1):
        if flag[i] == 0:
            verifica = False
            break

    if verifica:
        print('Y')
    else:
        print('N')

    entry = input().split(' ')
    N = int(entry[0])
    B = int(entry[1])