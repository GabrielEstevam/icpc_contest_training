import math
while True:
    try:
        entry = input().split(" ")
        r1 = int(entry[0])
        x1 = int(entry[1])
        y1 = int(entry[2])
        r2 = int(entry[3])
        x2 = int(entry[4])
        y2 = int(entry[5])
        d = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
        if d + r2 <= r1:
            print("RICO")
        else:
            print("MORTO")
    except EOFError:
        break