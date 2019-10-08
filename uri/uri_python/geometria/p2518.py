import math
while True:
    try:
        N = int(input())
        entry = input().split(" ")
        H = int(entry[0])/100
        C = int(entry[1])/100
        L = int(entry[2])/100
        Area = math.sqrt(pow(H, 2) + pow(C, 2)) * L * N
        print("{0:.4f}".format(Area))
    except EOFError:
        break