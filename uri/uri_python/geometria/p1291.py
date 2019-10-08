import math
coef = 1 - (math.asin(1/2) + 1/2*math.sqrt(0.75))
while True:
    try:
        r = float(input())
        c = r*r*coef
        b = r*r*(1 - math.pi/4) - 2*c
        a = r*r - 4*b - 4*c
        print('{:.3f}'.format(round(a, 3)), '{:.3f}'.format(round(b*4, 3)), '{:.3f}'.format(round(c*4, 3)))
    except EOFError:
        break