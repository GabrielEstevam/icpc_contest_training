n = int(input())
while n != 0:
    for i in range(n):
        entry = input().split(" ")
        Q = int(entry[0])
        A = float(entry[1])
        B = float(entry[2])
        Area = (((A+B)*5)/2)*Q
        saida = "Size #"+str(i+1)+":"
        print(saida)
        print("Ice Cream Used:", "{0:.2f}".format(Area), "cm2")
    print("")
    n = int(input())