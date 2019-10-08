import math
while True:
    try:
        entry = input().split(" ")
        A = float(entry[0])
        B = float(entry[1])
        C = float(entry[2])
        h = math.tan(math.radians(A))*B+C
        print("{0:.2f}".format(5*h))
    except EOFError:
        break