intancias = int(input())
while intancias > 0:
    primeiro = 0
    segundo = 0
    for i in range(intancias):
        entrada = input().split(" ")
        if int(entrada[0]) > int(entrada[1]):
            primeiro += 1
        elif int(entrada[0]) < int(entrada[1]):
            segundo += 1
    print("%d %d" % (primeiro, segundo))
    intancias = int(input())