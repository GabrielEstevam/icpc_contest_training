while True:
    try:
        entry = input()
        a = []
        for i in entry:
            a.append(int(i))
        b1 = 0
        b2 = 0
        for i in range(len(a)):
            b1 += (i+1)*a[i]
            b2 += (9-i)*a[i]
        b1 = (b1 % 11) % 10
        b2 = (b2 % 11) % 10
        print(str(a[0])+str(a[1])+str(a[2])+'.'+str(a[3])+str(a[4])+str(a[5])+'.'+str(a[6])+str(a[7])+str(a[8])+'-'+str(b1)+str(b2))
    except EOFError:
        break