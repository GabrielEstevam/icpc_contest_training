while True:
    try:
        V = float(input())
        D = float(input())
        area = 3.14 * pow(D/2, 2)
        print("ALTURA =",'{0:.2f}'.format(V/area))
        print("AREA =",'{0:.2f}'.format(area))
    except EOFError:
        break