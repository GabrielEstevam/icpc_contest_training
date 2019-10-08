entry = input().split(' ')
N = int(entry[0])
V = int(entry[1])
while N > 0:
    flag = False
    ks = V
    while ks > 0:
        k = ks
        cont = 0
        while k > 0:
            i = k
            while i > 0:
                cont += k
                if cont == N:
                    flag = True
                    break
                i -= 1
            if flag:
                break
            k -= 1
        if flag:
            break
        ks -= 1
    if flag:
        print('possivel')
    else:
        print('impossivel')

    entry = input().split(' ')
    N = int(entry[0])
    V = int(entry[1])