import math
entry = input().split(' ')
N = int(entry[0])
AAH = int(entry[1])
entry = input().split(' ')
xc = int(entry[0])
yc = int(entry[1])
lc = int(entry[2])
xs1 = [xc - lc/2, xc - lc/2, xc + lc/2, xc + lc/2]
ys1 = [yc - lc/2, yc + lc/2, yc - lc/2, yc + lc/2]
flag = True
for n in range(1, N):
    entry = input().split(' ')
    if (flag):
        x = int(entry[0])
        y = int(entry[1])
        l = int(entry[2])

        xs2 = [x - l/2, x - l/2, x + l/2, x + l/2]
        ys2 = [y - l/2, y + l/2, y - l/2, y + l/2]
        d = math.sqrt(pow(xs1[0] - xs2[0], 2) + pow(ys1[0] - ys2[0], 2))
        for i in range(4):
            for j in range(4):
                ds = math.sqrt(pow(xs1[i] - xs2[j], 2) + pow(ys1[i] - ys2[j], 2))
                if ds < d:
                    d = ds
        if d > AAH:
            flag = False
        xc = x
        yc = y
        lc = l
        xs1 = xs2
        ys1 = ys2
if (flag):
    print('YEAH')
else:
    print('OUCH')