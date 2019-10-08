N = int(input())
while N > -1:
    entry = input().split(' ')
    cont = 0
    acu = 0
    for i in range(N):
        acu += int(entry[i])
        if acu % 100 == 0:
            acu = acu % 100
            cont += 1
    print(cont)
    N = int(input())