for n in range(int(input())):
    entry = input().split(' ')
    n = (int(entry[3])-int(entry[1]))/(int(entry[2])-int(entry[0]))
    n = str(n)
    num = n.split('.')
    out = num[0] + ','
    if len(num[1]) > 0:
        out += num[1][0]
    else:
        out += '0'
    if len(num[1]) > 1:
        out += num[1][1]
    else:
        out += '0'
    print(out)