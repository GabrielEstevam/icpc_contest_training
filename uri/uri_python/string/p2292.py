for n in range(int(input())):
    entry = input().split(' ')
    x = int(entry[1])
    out = ""
    for i in range(len(entry[0])):
        #print('x:', x)
        if x > 0:
            if x % 2 == 1:
                if entry[0][i] == 'X':
                    outS = 'O'
                else:
                    outS = 'X'
            else:
                outS = entry[0][i]
            out += outS
            if (entry[0][i] == 'O' and outS == 'O') or (entry[0][i] == 'X' and outS == 'X'):
                x = int(x/2)
            elif entry[0][i] == 'O' and outS == 'X':
                x = int((x+1)/2)
            else:
                x = int((x-1)/2)
        else:
            out += entry[0][i]

    print(out)
    '''num = 0
    k = 1
    for i in range(len(entry[0])):
        if entry[0][i] == 'X':
            num += k
        k *= 2
    r = int(entry[1])
    print('num:', num)
    if r > num:
        r -= num
        r = r % k
        num = k
    num -= r
    out = ""
    print('num:', num)
    for i in range(len(entry[0])):
        if num % 2 == 1:
            out += 'X'
        else:
            out += 'O'
        num = int(num/2)
    print(out)'''