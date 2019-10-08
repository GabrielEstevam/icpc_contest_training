N = int(input())
while N != 0:
    entrada = input().split(" ")
    x = 0
    for i in range(len(entrada)):
        if int(entrada[i]) == 0:
            x +=1
    y = N - x
    print("Mary won %d times and John won %d times" % (x, y))
    N = int(input())

