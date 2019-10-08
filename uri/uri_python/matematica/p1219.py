import math
while True:
    try:
        entry = input().split(' ')
        a = float(entry[0])
        b = float(entry[1])
        c = float(entry[2])
        p = (a+b+c)/2
        S = math.sqrt(p*(p-a)*(p-b)*(p-c))
        r = S/p
        R = (a*b*c)/(4*S)
        Ar = 3.1415926535897*r*r
        Av = S-Ar
        As = 3.1415926535897*R*R-Av-Ar
        print("{:.4f}".format(As), "{:.4f}".format(Av), "{:.4f}".format(Ar))
    except EOFError:
        break