N = int(input())
while N > 0:
    U = 0
    R = 0
    I = 0
    for j in range(N):
        entry = input().split(' ')
        u = int(entry[0])
        r = int(entry[1])
        i = int(entry[2])
        if u == 2 or u == 4 or u == 8 or u == 16:
            if u > r and u > i:
                U += 1
            U += 1
        if r == 2 or r == 4 or r == 8 or r == 16:
            if r > u and r > i:
                R += 1
            R += 1
        if i == 2 or i == 4 or i == 8 or i == 16:
            if i > u and i > r:
                I += 1
            I += 1
    if U > R and U > I:
        print('Uilton')
    elif R > U and R > I:
        print('Rita')
    elif I > U and I > R:
        print('Ingred')
    else:
        print('URI')


    N = int(input())